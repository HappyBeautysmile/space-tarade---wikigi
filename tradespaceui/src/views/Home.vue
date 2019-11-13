<template>
    <div style="margin: 0; padding: 0">
        <b-row style="margin: 60px 0 0 0; padding: 0">
            <!--            <b-col col="1"></b-col>-->
            <b-col col="10" style="text-align: center; padding: 20px 20% 0 20%">
                <img style="padding: 0; margin: 0" :src="require('@/assets/logo3.png')" height="240" width="250"/>
                <div style="font-size: 50px">
                    <span>Trade</span>
                    <span class="font-weight-light">Space</span>
                </div>
                <div style="padding: 10px">
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
                                <v-btn color="blue darken-1" text @click="dialog1 = false">Log In</v-btn>
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
                                        <v-col cols="12" sm="6" md="4">
                                            <v-text-field label="Legal first name*" required
                                                          v-model="first"></v-text-field>
                                        </v-col>
                                        <v-col cols="12" sm="6" md="4">
                                            <v-text-field label="Legal middle name" v-model="midle"></v-text-field>
                                        </v-col>
                                        <v-col cols="12" sm="6" md="4">
                                            <v-text-field
                                                    label="Legal last name*"
                                                    required
                                                    v-model="last"
                                            ></v-text-field>
                                        </v-col>
                                        <v-col cols="12">
                                            <v-text-field label="Email*" required v-model="email"></v-text-field>
                                        </v-col>
                                        <v-col cols="12">
                                            <v-text-field label="Password*" type="password" required
                                                          v-model="password"></v-text-field>
                                        </v-col>
                                    </v-row>
                                </v-container>
                                <small>*indicates required field</small>
                            </v-card-text>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="blue darken-1" text @click="dialog2 = false">Close</v-btn>
                                <v-btn color="blue darken-1" text @click="dialog2 = false">Register</v-btn>
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
    </div>
</template>

<script>
    export default {
        data: () => ({
            name: "",
            first: "",
            last: "",
            email: "",
            password: "",
            dialog1: false,
            dialog2: false,
        }),
    };
</script>
