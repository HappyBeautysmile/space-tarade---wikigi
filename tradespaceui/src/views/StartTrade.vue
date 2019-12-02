<template>
    <div id="starttrade">
        <b-row style="margin-top: 60px">
            <b-col cols="6" style="padding: 2%">
                <h1>You want {{itemTitle}} </h1>
                <b-container fluid style="margin-top: 50px">
                    <b-card class="overflow-hidden">
                        <b-row>
                            <b-col>
                                <v-list-item>
                                    <v-list-item-avatar color="grey">
                                        <v-img :src="profilePhoto"></v-img>
                                    </v-list-item-avatar>
                                    <v-list-item-content>
                                        <v-list-item-title class="headline">{{itemTitle}}</v-list-item-title>
                                        <router-link :to="name">
                                            <v-list-item-subtitle>by {{name}}</v-list-item-subtitle>
                                        </router-link>
                                        <v-list-item-subtitle>{{location}}</v-list-item-subtitle>
                                    </v-list-item-content>
                                </v-list-item>
                                <b-col>
                                    <b-card-img :src="itemPhoto" class="rounded-0"></b-card-img>
                                </b-col>
                                <b-card-body title>
                                    <b-card-text>{{itemDescription}}</b-card-text>
                                </b-card-body>
                            </b-col>
                        </b-row>
                    </b-card>

                </b-container>
            </b-col>
            <b-col cols="6" style="border-left: black solid 1px; padding: 2%">
                <h1>and have to offer in return:</h1>
                <h3 style="margin-top: 20px">Cash:</h3>
                <v-text-field
                        label="Offer any amount of~$"
                        v-model="myCash"></v-text-field>
                <h3 style="margin-top: 20px">and/or one of your own items you think {{name}} will be interested in:</h3>
                <b-row style="" v-if="safe">
                    <li v-for="item in my_items" v-bind:key="item.description" style="list-style-type:none;">
                        <Item :item="item"></Item>
                    </li>
                </b-row>
                <v-btn style="margin-top: 40px"
                       large
                       @click="makeOffer"
                >Make Offer</v-btn>
            </b-col>
        </b-row>
    </div>
</template>
<script>
    import Item from '../components/specialItem';
    import axios from "axios";
    import firebase from "firebase";


    export default {
        name: 'StartTrade',
        components: {
            Item,
        },
        data: () => ({
            safe: false,
            my_items: [],
            item: {},
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
            myCash: 0
        }),
        methods: {
            makeOffer: function () {
                //all data
            alert('Item: '+ this.itemID + 'on cash: ' + this.myCash + 'and item id' + this.$store.getters.selected);
            }
        },
        created() {
            let self = this;
            axios.get('/items/' + this.$store.getters.item, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Authorization': 'token ' + self.$store.getters.authToken
                }
            }).then(response => {
                // alert(response)
                this.item = response.data;
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
                            self.profilePhoto = user['photo_url'];

                            if (self.profilePhoto) {
                                self.photo_path = self.profilePhoto.split('appspot.com/')[1];
                                var storage = firebase.storage();
                                var storageRef = storage.ref();
                                storageRef.child(self.photo_path).getDownloadURL().then(function (url) {
                                    self.profile_photo = url;
                                });
                            }
                        });

                    if (self.itemPhoto) {
                        self.photo_path = self.itemPhoto.split('appspot.com/')[1];
                        var storage = firebase.storage();
                        var storageRef = storage.ref();
                        storageRef.child(self.photo_path).getDownloadURL().then(function (url) {
                            self.item_photo = url;
                        });
                    }
                }
            })
            //     .catch(error => {
            //     let errorCode = error.code;
            //     let errorMessage = error.message;
            //     alert("ERROR " + errorCode + ":" + errorMessage);
            axios.get('/items/', {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Authorization': 'token ' + self.$store.getters.authToken
                }
            })
                .then(response => {
                    //alert(response)
                    //TODO: RESPONSE DATA IS AN ARRAY, ITERATE THROUGH AND GET THE ITEMS IN THAT WAY.
                    let items = response.data;
                    self.my_items = Object.values(items);
                    self.safe = true;
                })
                .catch(error => {
                    let errorCode = error.code;
                    let errorMessage = error.message;
                    alert("ERROR " + errorCode + ":" + errorMessage);
                });
        }
    };
</script>

<style scoped>

</style>