<template>
  <b-list-group style="padding: 80px 40px 0 40px">
    <div style="text-align:center">
      <v-list-item-avatar color="grey" size="200px">
        <v-img v-bind:src="profile_photo"></v-img>
      </v-list-item-avatar>
      <v-list-item-subtitle>{{ display_name }}</v-list-item-subtitle>
      <v-list-item-subtitle>{{ "Phone Number: " + phone_number }}</v-list-item-subtitle>
      <v-list-item-subtitle>{{ "Email: " + email }}</v-list-item-subtitle>
    </div>
    <router-link
      :to="`/${setting.dest}`"
      class="noHyperlink"
      v-for="setting in settings"
      v-bind:key="setting.name"
    >
      <b-list-group-item variant="primary" button>{{
        setting.name
      }}</b-list-group-item>
    </router-link>
  </b-list-group>
</template>

<script>

import firebase from 'firebase';
import axios from 'axios';

export default {

  name: "Account",
  components: {},
  data: () => ({
    settings: [
      { name: "My Items", dest: "history" },
      { name: "My Trades", dest: "trades" },
      { name: "My Account", dest: "update" }
    ],
    display_name: "",
    phone_number: "",
    email: "",
    photo_url: "",
    profile_photo: ""
  }),

  created() {
    let self = this;
    axios.get('/users/', {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'token ' + self.$store.getters.authToken
        }
    })
        .then(response => {
            let userInfo = response.data;
            self.display_name = userInfo['display_name'];
            self.phone_number = userInfo['phone_number'];
            self.email = userInfo['email'];
            self.photo_url = userInfo['photo_url'];

            if (self.photo_url) {
              self.photo_path = self.photo_url.split('appspot.com/')[1];
              var storage = firebase.storage();
              var storageRef = storage.ref();
              storageRef.child(self.photo_path).getDownloadURL().then(function(url) {
                  self.profile_photo = url;
              });
            }
        })
        .catch(error => {
            let errorCode = error.code;
            let errorMessage = error.message;
            self.snackbar = true;
            self.text = "ERROR " + errorCode + ": " + errorMessage;
        });

  },
};

</script>

<style scoped>
.noHyperlink {
  text-decoration: none;
  color: black;
}
</style>
