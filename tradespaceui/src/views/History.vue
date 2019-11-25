<template>
  <b-container fluid style="padding: 80px 40px 0 40px">

    <b-row style="padding: 20px 40px 0 40px">
        <li v-for="item in items" v-bind:key="item" style="list-style-type:none;">
            <Item :item="item"></Item>
        </li>
    </b-row>

    <div style="padding: 20px">
      <router-link to="/account">
        <v-btn large color="primary"> Back to Account</v-btn>
      </router-link>
    </div>

    
  </b-container>
</template>

<script>

import Item from '../components/item';
import firebase from 'firebase';
import axios from 'axios';
import qs from 'querystring';

export default {
  
  name: "Account",
  components: {
    Item,
  },
  data: () => ({
    items: [
      'foo', 'bar', 'bork', 'dog', 'shoe', 'catch', 'p1', 'p2'
    ],
    
  }),
  methods: 
  {
    getUserItems: function () {
        //TODO: Get items from firebase


        let self = this;
        axios.post('/users/', qs.stringify({
            'email': self.email,
            'password': self.password,
            'display_name': self.name,
            'phone_number': self.phone
        }), {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        })
            .then(response => {
                alert(response);
                self.dialog2 = false;
                self.snackbar = true;
                self.text = 'Your account have been created';
                self.$router.replace('home');
                self.$store.commit('logIn', true);
                // this.$router.go(0);
            })
            .catch(error => {
                // alert(e + e.status + e.code)
                // Handle Errors here.
                let errorCode = error.code;
                let errorMessage = error.message;
                // alert("ERROR:" + errorMessage + errorCode);
                self.snackbar = true;
                self.text = "ERROR " + errorCode + ":" + errorMessage;
            });
    },
    getItems: function () {
        var self = this;
        firebase.auth().signInWithEmailAndPassword(this.email, this.password).then(
            function () {
                self.dialog1 = false;
                self.snackbar = true;
                firebase.auth().currentUser.getIdToken(/* forceRefresh */ true).then(function (idToken) {
                    alert("Token: " + idToken)
                }).catch(function (error) {
                    self.text = "ERROR:" + error;
                });
                self.text = 'Welcome back!';
                self.$router.replace('home');
                self.$store.commit('logIn', true)
                // self.$router.go(0);
            },
            function (error) {
                // Handle Errors here.
                let errorCode = error.code;
                let errorMessage = error.message;
                // alert("ERROR:" + errorMessage + errorCode);
                self.snackbar = true;
                self.text = "ERROR " + errorCode + ":" + errorMessage;
            }
        );

    },
  }
  



};
</script>

<style scoped>
.noHyperlink {
  text-decoration: none;
  color: black;
}
</style>
