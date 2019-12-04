<template>
  <b-container fluid style="padding: 80px 40px 0 40px">
    <div style="padding-bottom: 30px">
      <div class="mt-3">
        Item Image: {{ itemImage ? itemImage.name : "" }}
      </div>
      <br />
      <b-form-file
        v-model="itemImage"
        :state="Boolean(itemImage)"
        placeholder="Choose a file or drop it here..."
        drop-placeholder="Drop file here..."
        @change="selectImage"
      ></b-form-file>
    </div>

    <b-form-input
      v-model="itemTitle"
      label="Item Title"
      placeholder="Item Title (e.g. Adidas shoes and a green dress)"
      required
    ></b-form-input>

    <b-form-input
      v-model="location"
      label="Location"
      placeholder="Location"
      style="margin-top: 10px"
      required
    ></b-form-input>

    <div style="margin-top: 10px">
      <b-form-input
        v-model="newTag"
        v-on:keyup.enter.native="addTag"
        placeholder="Enter a new tag..."
        style="margin-bottom:15px"
      ></b-form-input>

      <ul>
        <v-btn
          v-on:click="removeTag(tag)"
          style="margin-right:20px"
          v-for="tag in tags"
          v-bind:key="tag"
          >{{ tag }}</v-btn
        >
      </ul>
    </div>

    <div>
      <b-form-textarea
        id="textarea"
        v-model="description"
        placeholder="Describe your item..."
        rows="3"
        max-rows="6"
      ></b-form-textarea>
    </div>

    <div style="padding: 10px">
     
        <v-btn large color="primary" @click="editItem">Update Item</v-btn>
 
      <router-link to="/history">
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
  data: () => ({
    location: "",
    name: "Nikita",
    itemTitle: "",
    tags: [],
    itemImage: null,
    newTag: "",
    itemID: "",
    imageData: null,
    description: "",
    dialog2: false,
    snackbar: false,
    text: ''
  }),

  methods: {
    successUpdate() {
      this.$vs.notify({
        color: "success",
        title: "Upload Success",
        text: "Upload Suceeded"
      });
    },
    addTag() {
      this.tags.push(this.newTag);
      this.newTag = "";
    },
    removeTag(tagToRemove) {
      this.tags = this.tags.filter(item => item != tagToRemove);
    },
    selectImage: function(file) {
      this.itemImage = file;
    },
    editItem() {
      let self = this;
      // upload the photo and get url
      var storage_ref = firebase.storage().ref();
      var auth_token = self.$store.getters.authToken
      axios.get('/users/', {
          headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
              'Authorization': 'token ' + auth_token
          }
      })
          .then(response => {
              let userInfo = response.data;
              self.user_id = userInfo['user_id']

              var photo_url = "";
              var photo_changed = false;

              if (self.itemImage != self.old_photo_url) {
                var image_path = self.user_id + "/" + self.itemTitle
                var profile_ref = storage_ref.child(image_path)
                const profile_metadata = { contentType: self.itemImage.type }
                profile_ref.put(self.itemImage, profile_metadata);
                photo_url = "gs://tradespace-22f37.appspot.com/" + image_path;
                photo_changed = true;
                self.uploadItem(auth_token, photo_url, photo_changed);
                setTimeout(function(){ self.$router.replace('/history'); }, 11000);
              }
              else {
                photo_url = self.photo_url;
                photo_changed = false;
                self.uploadItem(auth_token, photo_url, photo_changed);
                setTimeout(function(){ self.$router.replace('/history'); }, 4000);
              }

              self.dialog2 = false;
              self.snackbar = true;
              self.text = 'Updating item information...';
          })
          .catch(error => {
              let errorCode = error.code;
              let errorMessage = error.message;
              alert("ERROR " + errorCode + ":" + errorMessage);
          });
    },
    uploadItem: function(auth_token, photo_url, photo_changed) {
      let self = this;

        axios.put('/items/' + self.itemID, qs.stringify({
            'title': self.itemTitle,
            'location': self.location,
            'description': self.description,
            'tags': self.tags,
            'photo_url': photo_url
        }), {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'token ' + auth_token
            }
        })
            .then(response => {
                if (photo_changed == true) {
                  setTimeout(function(){ alert("Successfully Updated Item: " + response['data']['title']); }, 11000);
                }
                else {
                  setTimeout(function(){ alert("Successfully Updated Item: " + response['data']['title']); }, 4000);
                }
                //Get back an Item variable. Not sure if the information is needed, but it is not used.
            })
            .catch(error => {
                let errorCode = error.code;
                let errorMessage = error.message;
                alert(errorCode + ":" + errorMessage);
                self.text = "ERROR " + errorCode + ":" + errorMessage;
            });
    }
  },

  created() {
    // alert('CHECK')
    let self = this;
    self.itemID = this.$route.params.itemID;
    axios.get('/items/' + self.itemID, {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'token ' + self.$store.getters.authToken
        }
    })
        .then(response => {
            // alert(response)
            let item = response.data;
            self.location = item['location'];
            self.itemTitle = item['title'];
            self.tags = item['tags'];
            self.owner_uid = item['owner_uid'];
            self.old_photo_url = item['photo_url'];
            self.description = item['description'];
            self.itemImage = item['photo_url'];
            axios.get('/users/' + self.owner_uid, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Authorization': 'token ' + self.$store.getters.authToken
                }
            })
                .then(response => {
                    let user = response.data;
                    self.name = user['display_name'];
                    self.email = user['email'];
                })
                .catch(error => {
                    let errorCode = error.code;
                    let errorMessage = error.message;
                    alert("ERROR " + errorCode + ":" + errorMessage);
                });

            //BELOW IS GETTING CURRENT USER. IF IT IS THE SAME USER, THEN WE WILL EDIT.
            //TODO: CHANGE THIS TO COMPARE BY ID WHEN API CHANGES!
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
.dropbox {
  outline: 2px dashed grey; /* the dash box */
  outline-offset: -10px;
  background: lightcyan;
  color: dimgray;
  padding: 10px 10px;
  min-height: 200px; /* minimum height */
  position: relative;
  cursor: pointer;
}

.input-file {
  opacity: 0; /* invisible but it's there! */
  width: 100%;
  height: 200px;
  position: absolute;
  cursor: pointer;
}

.dropbox:hover {
  background: lightblue; /* when mouse over to the drop zone, change color */
}

.dropbox p {
  font-size: 1.2em;
  text-align: center;
  padding: 50px 0;
}
</style>
