<template>
  <b-container fluid style="padding: 80px 40px 0 40px">
    <b-card class="overflow-hidden">
      <b-row>
        <b-col>
          <b-card-img :src="itemImage" class="rounded-0"></b-card-img>
        </b-col>
        <b-col>
          <v-list-item>
            <v-list-item-avatar color="grey">
              <v-img :src="avatar"></v-img>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title class="headline">{{itemTitle}}</v-list-item-title>
              <router-link :to="name">
                <v-list-item-subtitle>by {{name}}</v-list-item-subtitle>
              </router-link>
              <v-list-item-subtitle>{{location}}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <b-card-body title>
            <b-card-text>{{description}}</b-card-text>
          </b-card-body>

                    <div style="padding: 10px">
                        <v-btn large>Start Trade</v-btn>
                        <v-btn large style="margin-left: 30px" @click="$router.go(-1)"> Hide</v-btn>
                    </div>
                </b-col>
            </b-row>
        </b-card>

    </b-container>
</template>

<script>
    import axios from 'axios';
    // import router from "../router";
    // import qs from 'querystring';

    export default {
        data() {
            return {
                name: '',
                itemTitle: '',
                location: 'SF',
                tags: [],
                owner_uid: '',
                avatar: "",
                description: '',
                itemImage: ""

            }
        },
        methods: {
            back: function () {
                this.$router.replace('search');
            }
        },
        created() {
            // alert('CHECK')
            let self = this;
            axios.get('/items/' + 'zXyO8kIkustrX3CU8EVt', {
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
                    self.photo_url = item['photo_url'];
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
                        })
                        .catch(error => {
                            let errorCode = error.code;
                            let errorMessage = error.message;
                            alert("ERROR " + errorCode + ":" + errorMessage);
                        });
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
#container {
  grid-area: main;
  align-self: center;
  justify-self: center;
  margin-top: 10%;
  margin-left: 5%;
  float: left;
}

.item_action {
  margin: 10px;
}
</style>