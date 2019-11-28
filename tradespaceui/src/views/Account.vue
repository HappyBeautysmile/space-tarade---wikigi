<template>
  <b-list-group style="padding: 80px 40px 0 40px">
    <div style="text-align:center">
      <v-list-item-avatar color="grey" size="200px">
        <v-img :src="avatarSrc"></v-img>
      </v-list-item-avatar>
      <router-link :to="display_name" class="noHyperlink">
        <v-list-item-subtitle>{{
          "Username: " + display_name
        }}</v-list-item-subtitle>
      </router-link>
      <v-list-item-subtitle>{{ "Phone Number: " + phone_number }}</v-list-item-subtitle>
      <v-list-item-subtitle>{{ "Email: " + email }}</v-list-item-subtitle>
      <v-list-item-subtitle>{{ "User ID: " + uid }}</v-list-item-subtitle>
      <v-list-item-subtitle>{{ "Location: " + location }}</v-list-item-subtitle>
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

import axios from 'axios';

export default {


  name: "Account",
  components: {},
  data: () => ({
    settings: [
      { name: "My Items", dest: "history" },
      { name: "My Trades", dest: "history" },
      { name: "Account Settings", dest: "update" }
    ],
    // display_name: "nikita123",
    // phone_number: "(555) 555-5555",
    // email: "test1234@gmail.com",
    // uid: "1",
    // avatarSrc:
    //   "https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/22449875_913694855449733_82882405759448142_n.jpg?_nc_cat=101&_nc_oc=AQncaWWuWzFfxdVtK5P69Jl-sJRqNOoHsimpBnysDiZ4IU6CrUGl_iMle5gtvd83ylHYe0ve-pmotMRHVvP7ufkn&_nc_ht=scontent-lax3-1.xx&oh=8a7bc0b583f64c997324885cbafb92a0&oe=5E627D59",
    // location: "Los Angeles, CA"
    display_name: "",
    phone_number: "",
    email: "",
    uid: "",
    avatarSrc:
      "https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/22449875_913694855449733_82882405759448142_n.jpg?_nc_cat=101&_nc_oc=AQncaWWuWzFfxdVtK5P69Jl-sJRqNOoHsimpBnysDiZ4IU6CrUGl_iMle5gtvd83ylHYe0ve-pmotMRHVvP7ufkn&_nc_ht=scontent-lax3-1.xx&oh=8a7bc0b583f64c997324885cbafb92a0&oe=5E627D59",
    location: ""
  }),

  created() {
    // alert('CHECK')
    let self = this;
    axios.get('/users/', {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'token ' + self.$store.getters.authToken
        }
    })
        .then(response => {
          // alert(response)
            let userInfo = response.data;
            self.display_name = userInfo['display_name'];
            self.phone_number = userInfo['phone_number'];
            self.email = userInfo['email'];
            self.uid = userInfo['uid'];
            //TODO: GET THE PHOTO AND LOCATION WITH GET CALL
        })
        .catch(error => {
            let errorCode = error.code;
            let errorMessage = error.message;
            alert("ERROR " + errorCode + ":" + errorMessage);
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
