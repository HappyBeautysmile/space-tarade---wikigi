<template>
    <div style="margin: 0; padding: 0">
        <b-row style="margin: 60px 0 0 0; padding: 0">
            <!--            <b-col col="1"></b-col>-->
            <b-col cols="12" style="text-align: center; padding: 20px 20% 0 20%">
                <img style="padding: 0; margin: 0" :src="require('@/assets/logo3.png')" height="240" width="250"/>
                <div style="font-size: 50px">
                    <span>Trade</span>
                    <span class="font-weight-light">Space</span>
                </div>
                <div v-if="!$store.getters.loggedIn" style="padding: 10px">
                    <v-dialog v-model="dialog1" persistent max-width="600px">
                        <template v-slot:activator="{ on }">
                            <v-btn large style="margin-left: 30px" v-on="on">Sign In</v-btn>
                        </template>
                        <v-card>
                            <v-card-title>
                                <span class="headline">User Information:</span>
                            </v-card-title>
                            <v-card-text>
                                <v-container>
                                    <v-row>
                                        <v-col cols="12">
                                            <v-text-field label="Email*" required v-model="email"></v-text-field>
                                        </v-col>
                                        <v-col cols="12">
                                            <v-text-field label="Password*" type="password" required
                                                          v-model="password"></v-text-field>
                                        </v-col>
                                    </v-row>
                                </v-container>
                                <small>Dont have an account, sign up:
                                    <v-btn color="blue darken-1" text @click="dialog1 = false, dialog2 = true">Sign Up
                                    </v-btn>
                                </small>
                            </v-card-text>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="blue darken-1" text @click="dialog1 = false">Close</v-btn>
                                <v-btn color="blue darken-1" text @click="signIn">Log In</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                    <v-dialog v-model="dialog2" persistent max-width="600px">
                        <template v-slot:activator="{ on }">
                            <v-btn large style="margin-left: 30px" v-on="on">Sign Up</v-btn>
                        </template>
                        <v-card>
                            <v-card-title>
                                <span class="headline">User Profile:</span>
                            </v-card-title>
                            <v-card-text>
                                <v-container>
                                    <v-row>
                                        <v-col cols="12" sm="8" md="6">
                                            <v-text-field label="Full Name*" required
                                                          v-model="display_name"></v-text-field>
                                        </v-col>
                                        <v-col cols="12" sm="8" md="6">
                                            <v-text-field label="Phone Number*" required
                                                          v-model="phone_number"></v-text-field>
                                            <small>Add +1 to the number!</small>
                                        </v-col>
                                        <v-col cols="12">
                                            <v-text-field label="Email*" required v-model="email"></v-text-field>
                                        </v-col>
                                        <v-col cols="12">
                                            <v-text-field label="Password*" type="password" required
                                                          v-model="password"></v-text-field>
                                        </v-col>
                                        <v-col cols="12">
                                            <v-file-input id="prof-picture" label="Profile Picture*" ref="profile_pic" required
                                                          v-model="profile" @change="selectImage"></v-file-input>
                                        </v-col>
                                    </v-row>
                                </v-container>
                                <small>* indicates required field<br></small>
                                <small>Have an account already, sign in:
                                    <v-btn color="blue darken-1" text @click="dialog2 = false, dialog1 = true">Sign In
                                    </v-btn>
                                </small>
                            </v-card-text>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="blue darken-1" text @click="dialog2 = false">Close</v-btn>
                                <v-btn color="blue darken-1" text @click="signUp">Register</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                </div>
                <div style="font-size: 20px; padding: 0; margin: 0;">
                    <p>What is Tradespace ?</p>
                    <span class="font-weight-light">
                        TradeSpace is an online platform where you can swap unwanted items like clothing,
                        furniture, etc. with other users. Every time you buy something, there's a chance you won't
                        be able to return it. And if you use it for a while and want to sell it later on, resale value is
                        significantly lower than purchase value. Or you might even have items like furniture that you
                        don't know what to do with when you move. Why deal with this hassle when you can just trade your
                        unwanted items to other people for mutual benefit?
                    </span>
                </div>
            </b-col>
        </b-row>
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
        data: () => ({
            user_id: "",
            display_name: "",
            phone_number: "",
            email: "",
            password: "",
            photo_url: "",
            image: "",
            dialog1: false,
            dialog2: false,
            user_data: {},
            dummy_data: {},
            text: '',
            snackbar: false,
            selectedFile: null
        }),
        methods: {
            selectImage: function(file) {
                this.image = file;
            },

            signUp: function () {
                let self = this;

                axios.post('/users/', qs.stringify({
                    'email': self.email,
                    'password': self.password,
                    'display_name': self.display_name,
                    'phone_number': self.phone_number,
                    'photo_url': 'gs://tradespace-22f37.appspot.com/temp_profile.jpg'
                }), {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }
                })
                    .then(response => {
                        self.user_data = response.data;
                        self.initialSignIn();
                        self.dialog2 = false;
                        self.snackbar = true;
                        self.text = 'Your account has been created';
                        self.$router.replace('home');
                        self.$store.commit('logIn', true);
                    })
                    .catch(error => {
                        let errorCode = error.code;
                        let errorMessage = error.message;
                        self.snackbar = true;
                        self.text = "ERROR " + errorCode + ": " + errorMessage;
                    });
            },

            signIn: function () {
                let self = this;

                firebase.auth().signInWithEmailAndPassword(this.email, this.password).then(
                    function () {
                        self.dialog1 = false;
                        self.snackbar = true;
                        firebase.auth().currentUser.getIdToken(/* forceRefresh */ true).then(function (idToken) {
                            self.$store.commit('setToken', idToken)
                        }).catch(function (error) {
                            self.text = "ERROR:" + error.message;
                        });
                        self.text = 'Welcome back!';
                        self.$router.replace('home');
                        self.$store.commit('logIn', true)
                    },
                    function (error) {
                        let errorCode = error.code;
                        let errorMessage = error.message;
                        self.snackbar = true;
                        self.text = "ERROR " + errorCode + ":" + errorMessage;
                    }
                );
            },

            initialSignIn: function () {
                let self = this;
                
                firebase.auth().signInWithEmailAndPassword(this.email, this.password).then(
                    function () {
                        firebase.auth().currentUser.getIdToken(/* forceRefresh */ true).then(function (idToken) {
                            self.$store.commit('setToken', idToken);
                            self.updateInfo();
                        }).catch(function (error) {
                            self.text = "ERROR:" + error.message;
                        }); 
                        self.$router.replace('home');
                        self.$store.commit('logIn', true)
                    },
                    function (error) {
                        let errorCode = error.code;
                        let errorMessage = error.message;
                        self.snackbar = true;
                        self.text = "ERROR " + errorCode + ":" + errorMessage;
                    }
                );
            },

            updateInfo: function () {
                let self = this;

                var storage_ref = firebase.storage().ref();
                var profile_ref = storage_ref.child(self.user_data.user_id + '/profile.jpg');
                const profile_metadata = { contentType: self.image.type };
                profile_ref.put(self.image, profile_metadata);

                axios.post('/users/update/', qs.stringify({
                    'email': self.email,
                    'display_name': self.display_name,
                    'phone_number': self.phone_number,
                    'photo_url': 'gs://tradespace-22f37.appspot.com/' + self.user_data.user_id + '/profile.jpg'
                }), {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Authorization': 'token ' + self.$store.getters.authToken
                    }
                })
                    .then(response => {
                        self.dummy_data = response;
                    })
                    .catch(error => {
                        let errorCode = error.code;
                        let errorMessage = error.message;
                        self.snackbar = true;
                        self.text = "ERROR " + errorCode + ":" + errorMessage;
                    });
            }
        },
    };
</script>