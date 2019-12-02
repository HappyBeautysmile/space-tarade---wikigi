<template>
    <div id="starttrade">
        <b-row style="margin-top: 60px">
            <b-col cols="6" style="padding: 2%">
                <h1>{{name}} wants </h1>
                <b-container fluid style="margin-top: 50px">
                    <b-card class="overflow-hidden">
                        <b-row>
                            <b-col>
                                <v-list-item>
                                    <v-list-item-content>
                                        <v-list-item-title class="headline" style="float: top">{{itemTitle}}</v-list-item-title>
                                        <v-list-item-subtitle>in {{itemLocation}}</v-list-item-subtitle>
                                    </v-list-item-content>
                                </v-list-item>
                                <b-col>
                                    <b-card-img :src="itemPhoto" class="rounded-0" style="width:300px; height:300px"></b-card-img>
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
                <h1>In return, you want</h1>
                <h3 style="margin-top: 70px">Cash ($):</h3>
                <v-text-field
                    v-model="myCash"></v-text-field>
                <h3 style="margin-top: 20px">and/or one of the other user's items:</h3>
                <b-row style="" v-if="safe">
                    <li v-for="item in my_items" v-bind:key="item.description" style="list-style-type:none;">
                        <Item :item="item" :tradeId="tradeID"></Item>
                    </li>
                </b-row>
                <v-btn style="margin-top: 80px"
                       large
                       @click="makeOffer"
                >Make Offer</v-btn>
                <router-link to="/trades">
                    <v-btn large style="margin-left: 30px; margin-top: 80px" color="secondary"> Cancel </v-btn>
                </router-link>   
            </b-col>
        </b-row>
    </div>
</template>
<script>

    import Item from '../components/specialItem';
    import axios from "axios";
    import firebase from "firebase";
    import qs from 'querystring';

    export default {
        name: 'StartTrade',
        components: {
            Item,
        },
        data: () => ({
            safe: false,
            tradeID: '',
            my_items: [],
            item: {},
            itemTitle: '',
            itemDescription: '',
            itemPhoto: '',
            itemLocation: '',
            owner_uid: '',
            itemID: '',
            itemOwnerID: '',
            name: '',
            other_id: '',
            profilePhoto: '',
            dialog: false,
            editMode: false,
            notEditMode: true,
            myCash: 0,
            text1: ''
        }),
        methods: {
            makeOffer: function () {
                //alert('Item: '+ this.itemID + 'on cash: ' + this.myCash + 'and item id ' + this.$store.getters.selected);

                let self = this;
                let path = '/trades/' + self.tradeID + '/barter';
                let val = self.$store.getters.selected;
                let tok = self.$store.getters.authToken;
                axios.put(path, qs.stringify({
                    'buyer_item': val
                }), {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Authorization': 'token ' + tok
                    }
                })
                    .then(response => {
                        self.text1 = response;
                        self.$router.replace('/trades');
                    })
                    .catch(error => {
                        let errorCode = error.code;
                        let errorMessage = error.message;
                        alert("ERROR " + errorCode + ":" + errorMessage);
                    });
            },

            getOtherData: function () {
                let self = this;
                axios.get('/items/other_user/' + self.other_id, {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Authorization': 'token ' + self.$store.getters.authToken
                    }
                })
                    .then(response => {
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
        },
        created() {
            let self = this;
            self.tradeID = this.$route.params.tradeID;

            axios.get('/trades/' + self.tradeID, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Authorization': 'token ' + self.$store.getters.authToken
                }
            })
                .then(response => {
                    let responseData = response.data;
                    
                    self.name = responseData.other_user.display_name;
                    self.other_id = responseData.other_user.user_id;

                    self.itemTitle = responseData.your_item.title;
                    self.itemDescription = responseData.your_item.description;
                    self.itemLocation = responseData.your_item.location;
                    self.itemPhoto = responseData.your_item.photo_url;

                    self.photo_path = self.itemPhoto.split('appspot.com/')[1];
                    var storage = firebase.storage();
                    var storageRef = storage.ref();
                    storageRef.child(self.photo_path).getDownloadURL().then(function(url) {
                        self.itemPhoto = url;
                    });

                    self.getOtherData();
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