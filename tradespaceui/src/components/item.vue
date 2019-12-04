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
                            <v-list-item-avatar color="grey" style="float: left" size="70px">
                                <v-img v-bind:src="profile_photo"></v-img>
                            </v-list-item-avatar>
                            <v-list-item-title class="headline" style="float: top">{{itemTitle}}</v-list-item-title>
                            <v-list-item-subtitle>by {{name}}</v-list-item-subtitle>
                            <v-img style="float: left" v-bind:src="item_photo"></v-img>
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
                    >
                        <v-row>
                            <v-list-item-avatar color="grey" style="display: inline-block" size="150px">
                                <v-img v-bind:src="profile_photo" style="margin: 0; padding: 0"></v-img>
                            </v-list-item-avatar>
                            <v-col>
                                <v-list-item-title style="display: inline-block; font-size: 40px; margin-top:20px; margin-left: 10px">
                                    {{itemTitle}}
                                </v-list-item-title>
                                <v-list-item-subtitle style="margin-left: 15px"> by {{name}}
                                </v-list-item-subtitle>
                                <v-list-item-subtitle style="display: inline-block; margin-left: 15px">in {{itemLocation}}
                                </v-list-item-subtitle>
                            </v-col>
                        </v-row>
                    </v-card-title>

                    <v-card-text style="padding: 1% 5% 1% 5%">
                        <v-row>
                            <v-col>
                                <b-card-img v-bind:src="item_photo" class="rounded-0" style="width:350px; height:350px"></b-card-img>
                            </v-col>
                            <v-col>
                                {{itemDescription}}
                            </v-col>
                        </v-row>
                    </v-card-text>

                    <v-divider></v-divider>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn text color="primary" v-if="notEditMode" @click="startTrade">Start Trade</v-btn>

                        <v-btn text color="primary" v-if="editMode" @click="$router.push({path: `/editItem/${itemID}`})">Edit Item</v-btn>
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
        <div class="text-center ma-2">
            <v-snackbar
                    v-model="snackbar"
            >
                {{ text }}
                <v-btn
                        color="pink"
                        text
                        @click="snackbar = false"
                >
                    Close
                </v-btn>
            </v-snackbar>
        </div>
    </div>
</template>

<script>

    import firebase from 'firebase';
    import axios from 'axios';
    import qs from 'querystring';

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
            profilePhoto: '',
            dialog: false,
            editMode: false,
            notEditMode: true,
            text: '',
            snackbar: false
        }),
        methods: {
            startTrade: function () {
                let self = this;
                axios.post('/trades/request_new', qs.stringify({
                    'item_id': self.itemID
                }), {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Authorization': 'token ' + self.$store.getters.authToken
                    }
                })
                    .then(response => {
                        self.dummy_data = response;
                        self.$router.push({path: '/trades'})
                    })
                    .catch(error => {
                        let errorCode = error.code;
                        let errorMessage = error.message;
                        self.snackbar = true;
                        self.text = "ERROR " + errorCode + ":" + errorMessage;
                    });
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
            this.profilePhoto = "gs://tradespace-22f37.appspot.com/" + this.owner_uid + "/profile.jpg";
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
                    });

                var storage = firebase.storage();
                var storageRef = storage.ref();

                if (self.itemPhoto) {
                    self.photo_path = self.itemPhoto.split('appspot.com/')[1];
                    storageRef.child(self.photo_path).getDownloadURL().then(function(url) {
                        self.item_photo = url;
                    });
                }

                if (self.profilePhoto) {
                    self.photo_path = self.profilePhoto.split('appspot.com/')[1];
                    storageRef.child(self.photo_path).getDownloadURL().then(function(url) {
                        self.profile_photo = url;
                    });
                }

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
                        self.notEditMode = !(self.editMode);
                    })
                    .catch(error => {
                        let errorCode = error.code;
                        let errorMessage = error.message;
                        self.snackbar = true;
                        self.text = "ERROR " + errorCode + ":" + errorMessage;
                    });
            }
        }

    };
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
