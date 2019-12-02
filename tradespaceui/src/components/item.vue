<template>
    <div id="myitem">
        <div class="text-center">
            <v-dialog
                    v-model="dialog"
                    width="800"
            >
                <template v-slot:activator="{ on }">
                    <v-card
                            class="mx-auto"
                            max-width="344"
                            v-on="on"
                    >
                        <v-card-subtitle style="display: block">
                            <v-list-item-avatar color="grey" style="float: left">
                                <v-img :src="profile"></v-img>
                            </v-list-item-avatar>
                            <v-list-item-title class="headline" style="float: top">{{itemTitle}}</v-list-item-title>
                            <v-list-item-subtitle>by {{name}}</v-list-item-subtitle>
                            <v-img style="float: left" :src="itemPhoto"></v-img>
                        </v-card-subtitle>
                        <v-list-item>
                            <p id="text"> {{ itemDescription }}</p>
                        </v-list-item>
                    </v-card>
                </template>

                <v-card>
                    <v-card-title
                            class="headline grey lighten-2"
                            primary-title
                            style="display: block"
                    ><span>
                        <v-list-item-avatar color="grey" style="display: inline-block">
                            <v-img :src="profile" style="margin: 0; padding: 0"></v-img>
                        </v-list-item-avatar>
                        </span>
                        <v-list-item-title style="display: inline-block; font-size: 40px; margin-top: 15px">
                            {{itemTitle}}
                        </v-list-item-title>
                        <v-list-item-subtitle style="margin-left: 20px"> by {{name}}
                        </v-list-item-subtitle>
                        <v-list-item-subtitle style="display: inline-block; margin-left: 10px">in {{itemLocation}}
                        </v-list-item-subtitle>
                    </v-card-title>

                    <v-card-text style="padding: 10% 5% 5% 5%">
                        <b-card-img :src="itemPhoto" class="rounded-0"></b-card-img>
                        {{itemDescription}}
                    </v-card-text>

                    <v-divider></v-divider>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn text color="primary" v-if="notEditMode">Start Trade</v-btn>

                        <v-btn text color="primary" v-if="editMode">Edit Item</v-btn>
                        <v-btn
                                color="primary"
                                text
                                @click="dialog = false"
                        >
                            Back
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'Item',
        //DO PROP VALIDATION IF THERE IS TIME: https://vuejs.org/v2/guide/components-props.html
        props: [
            'item'
            //Item contains an array with all the different components
        ],
        data: () => ({
            itemTitle: '',
            itemDescription: '',
            itemPhoto: '',
            itemTags: '',
            itemLocation: '',
            owner_uid: '',
            itemID: '',
            itemOwnerID: '',
            name: '',
            profile: '',
            dialog: false,
            editMode: false,
            notEditMode: true
        }),
        methods: {
            toItem: function () {

            }
        },
        created() {
            this.itemTitle = this.item['title'];
            this.itemDescription = this.item['description'];
            this.itemPhoto = this.item['photo_url'];
            this.itemTags = this.item['tags'];
            this.itemLocation = this.item['location'];
            this.itemID = this.item['item_id'];
            this.owner_uid = this.item['owner_uid'];
            let self = this;
            if (this.owner_uid !== null || this.owner_uid !== '') {
                axios.get('/users/' + self.owner_uid, {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Authorization': 'token ' + self.$store.getters.authToken
                    }
                })
                    .then(response => {
                        let user = response.data;
                        self.name = user['display_name'];
                        self.profile = user['photo_url'];
                    })
                

                axios.get('/users/', {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Authorization': 'token ' + self.$store.getters.authToken
                    }
                })
                    .then(response => {
                        let userInfo = response.data;
                        self.curUserID = userInfo['user_id'];
                        if(self.curUserID == self.owner_uid) {
                            self.editMode = true;
                        }
                        else {
                            alert(self.curUserID);
                            alert(self.itemUserID);
                        }
                        self.notEditMode = !(self.editMode);
                    })
                    .catch(error => {
                        let errorCode = error.code;
                        let errorMessage = error.message;
                        alert("ERROR " + errorCode + ":" + errorMessage);
                    });
            }

            // .catch(error => {
            //     let errorCode = error.code;
            //     let errorMessage = error.message;
            //     // alert("ERROR " + errorCode + ":" + errorMessage);
            // });
        }

    }
    ;
</script>

<style scoped>
    #myitem {
        margin: 5px;
        display: inline-block;
    }

    #text {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-height: 100px;
    }
</style>