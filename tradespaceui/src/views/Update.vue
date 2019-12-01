<template>
  <b-container style="padding: 80px 40px 0 40px">

    <h1 class="mytradestitle" style="text-align:center">
      UPDATE ACCOUNT
    </h1>

    <div style="padding-bottom: 30px">
      Name:
      <b-form-input
        v-model="display_name"
        label="Name"
        placeholder="Name"
        style="margin-top: 10px"
        required
      ></b-form-input>
    </div>

    <div style="padding-bottom: 30px">
      Phone Number:
      <b-form-input
        v-model="phone_number"
        label="Phone Number"
        placeholder="Phone Number"
        style="margin-top: 10px"
        required
      ></b-form-input>
    </div>

    <div style="padding-bottom: 30px">
      Email:
      <b-form-input
        v-model="email"
        label="Email"
        placeholder="Email"
        style="margin-top: 10px"
        required
      ></b-form-input>
    </div>

    <div style="padding-bottom: 30px">
      Profile Picture:
      <v-file-input 
        id="prof-picture" 
        label="Update profile picture" 
        ref="profile_pic"
        v-model="profile" 
        @change="selectImage"
      ></v-file-input>
    </div>

    <div style="padding: 30px">
      <v-btn large color="primary" @click="updateImage"> Submit </v-btn>
      <router-link to="/account">
        <v-btn large style="margin-left: 30px" color="secondary"> Cancel </v-btn>
      </router-link>    
    </div>

    <div class="text-center ma-2">
      <v-snackbar 
        v-model="snackbar"
      >
        {{ text }}
      </v-snackbar>
    </div>

  </b-container>
</template>

<script>

import firebase from 'firebase';
import axios from 'axios';
import qs from 'querystring';

export default {

  name: "Account",
  components: {},
  data: () => ({
    user_id: "",
    display_name: "",
    phone_number: "",
    email: "",
    photo_url: "",
    image: "",
    itemImage: null,
    text1: "",
    dialog2: false,
    snackbar: false,
    text: ''
  }),
  methods: {
    selectImage: function(file) {
      this.image = file;
    },

    updateUser: function () {
      let self = this;

      axios.post('/users/update/', qs.stringify({
        'email': self.email,
        'display_name': self.display_name,
        'phone_number': self.phone_number,
        'photo_url': self.photo_url
      }), {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Authorization': 'token ' + self.$store.getters.authToken
        }
      })
      .then(response => {
        self.text1 = response;
        self.$router.replace('account');
      })
      .catch(error => {
        let errorCode = error.code;
        let errorMessage = error.message;
        self.snackbar = true;
        self.text = "ERROR " + errorCode + ":" + errorMessage;
      });
    },

    updateImage: function  () {
      let self = this;

      self.dialog2 = false;
      self.snackbar = true;
      self.text = 'Updating account information...';

      if (self.image != "") {
        var storage_ref = firebase.storage().ref();
        var profile_ref = storage_ref.child(self.user_id + '/profile.jpg');
        const profile_metadata = { contentType: self.image.type };
        profile_ref.put(self.image, profile_metadata);
        setTimeout(function(){ self.updateUser(); }, 8000);
      }
      else {
        setTimeout(function(){ self.updateUser(); }, 1000);
      }
      
    }
  },
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
            self.user_id = userInfo['user_id'];
            self.display_name = userInfo['display_name'];
            self.phone_number = userInfo['phone_number'];
            self.email = userInfo['email'];
            self.photo_url = userInfo['photo_url'];
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
