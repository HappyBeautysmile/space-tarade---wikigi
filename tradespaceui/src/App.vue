<template>
    <v-app style="margin: 0; padding: 0">
        <v-app-bar app>
            <v-toolbar-title class="headline text-uppercase">
                <router-link to="/" style="text-decoration:none;">
                    <img style="padding: 0; margin: 0" :src="require('@/assets/logo3.png')" height="48" width="50"/>
                    <span style="text-decoration:none; color: black">Trade</span>
                    <span class="font-weight-light" style="text-decoration:none; color: black">Space</span>
                </router-link>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <router-link to="/search" v-if="$store.getters.loggedIn">
                <v-btn text>
                    <span class="mr-2">Search</span>
                </v-btn>
            </router-link>
            <router-link to="/createItem" v-if="$store.getters.loggedIn">
                <v-btn text>
                    <span class="mr-2">ADD ITEM FOR TRADE</span>
                </v-btn>
            </router-link>
            <router-link to="/account" v-if="$store.getters.loggedIn">
                <v-btn text>
                    <span class="mr-2">Account</span>
                </v-btn>
            </router-link>
            <v-btn text @click="logout" v-if="$store.getters.loggedIn">
                <span class="mr-2">Log Out</span>
            </v-btn>
        </v-app-bar>
        <v-content style="margin: 0; padding: 0">
            <!--            <HelloWorld/>-->
            <router-view></router-view>
        </v-content>
    </v-app>
</template>

<script>
    import firebase from 'firebase';

    export default {
        name: "App",
        data: () => ({
            //
        }),
        methods: {
            logout: function () {
                let self = this;
                firebase.auth().signOut().then(() => {
                    self.$store.commit('logIn', false);
                    self.$router.replace('search');
                })
            }
        }
    };
</script>
