<template>
  <b-container fluid style="padding: 5% 0% 0 0%">
    <h1 class="mytradestitle">
      <router-link to="/account">
        <div
          style="position: absolute; padding-left:5%; color:black; font-size:large; margin-top:1%"
        >&lt; BACK</div>
      </router-link>MY TRADES
    </h1>
    <b-card
      no-body
      style="margin-top: 2%; height: 50%; width:100%; margin-right: 2%; display:inline-block;"
      v-for="transaction in trade_list"
      v-bind:key="transaction.trade_id"
    >
      <b-row>
        <v-card-title style="padding-left:5%;">
          <div style="white-space:nowrap">Trade with {{ transaction.other_user.display_name }}</div>
        </v-card-title>
        <b-button
          v-if="transaction.status == 0 || transaction.status == 1"
          class="pushRight"
          variant="danger"
          v-on:click= "() => cancel(transaction.trade_id)"
        >Cancel</b-button>
      </b-row>
      <b-row style="display: flex; flex-direction: row; flex-wrap: nowrap; ">
        <b-col
          style="display: flex; flex-direction: column; align-items: center; flex: 1 1 auto; max-width: 26%"
        >
          <img
            v-if="transaction.other_user.photo_url != null"
            :src="transaction.other_user.photo_url"
            style="width: 70%; height: auto; position:relative; border-radius:50%"
          />
          <img
            v-else
            src="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/320/google/80/black-question-mark-ornament_2753.png"
            style="width: 70%; height: auto; position:relative; border-radius:50%"
          />
          <b-card-body style="text-align: center;">
            <v-list-item-title>
              {{
              transaction.other_user.phone_number
              }}
            </v-list-item-title>
            <v-list-item-title>
              {{
              transaction.other_user.email
              }}
            </v-list-item-title>
          </b-card-body>
        </b-col>
        <b-col style="flex: 1 1 auto; max-width: 26%">
          <b-card no-body style="height:100%">
            <b-card-title style="padding:5%">Your Item</b-card-title>
            <div
              style="
                  display: flex;
                  flex-direction: column;
                  justify-content: center;
                  align-items: center;
                  "
            >
              <b-img v-if="transaction.your_item == null && transaction.your_price == null" contain color="grey" src="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/320/google/80/black-question-mark-ornament_2753.png" class="imageCard"></b-img>
              <b-img v-else-if="transaction.your_item != null" contain color="grey" :src="transaction.your_item.photo_url" class="imageCard"></b-img>
              <b-img v-else-if="transaction.your_price != null" contain color="grey" src="http://clipart-library.com/data_images/539708.png" class="imageCard"></b-img>

              <b-card-body>
                <v-list-item-title style="text-align: center">
                  <div v-if="transaction.your_item == null && transaction.your_price == null" style="white-space:normal;"> N/A </div>
                  <div v-else-if="transaction.your_item != null && transaction.your_price != null" style="white-space:normal;">{{ transaction.your_item.title }} + ${{ transaction.your_price }}</div>
                  <div v-else-if="transaction.your_price != null" style="white-space:normal;">${{ transaction.your_price }}</div>
                  <div v-else-if="transaction.your_item != null" style="white-space:normal;">{{ transaction.your_item.title }}</div>
                </v-list-item-title>
              </b-card-body>
            </div>
          </b-card>
        </b-col>
        <b-col style="flex: 1 1 auto; max-width: 26%">
          <b-card no-body style="height:100%">
            <b-card-title style="padding:5%">Their Item</b-card-title>
            <div
              style="
                  display: flex;
                  flex-direction: column;
                  justify-content: center;
                  align-items: center;
                  "
            >
              <b-img v-if="transaction.their_item == null && transaction.their_price == null" contain color="grey" src="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/320/google/80/black-question-mark-ornament_2753.png" class="imageCard"></b-img>
              <b-img v-else-if="transaction.their_item != null" contain color="grey" :src="transaction.their_item.photo_url" class="imageCard"></b-img>
              <b-img v-else-if="transaction.their_price != null" contain color="grey" src="http://clipart-library.com/data_images/539708.png" class="imageCard"></b-img>

              <b-card-body>
                <v-list-item-title style="text-align: center">
                  <div v-if="transaction.their_item == null && transaction.their_price == null" style="white-space:normal;"> N/A </div>
                  <div v-else-if="transaction.their_item != null && transaction.their_price != null" style="white-space:normal;">{{ transaction.their_item.title }} + ${{ transaction.their_price }}</div>
                  <div v-else-if="transaction.their_price != null" style="white-space:normal;">${{ transaction.their_price }}</div>
                  <div v-else-if="transaction.their_item != null" style="white-space:normal;">{{ transaction.their_item.title }}</div>
                </v-list-item-title>
              </b-card-body>
            </div>
          </b-card>
        </b-col>
        <b-col style="flex: 1 1 auto; max-width:22%">
          <b-card-body style="height:100%">
            <div class="pushHalfway">
              <b-card-title>STATUS:</b-card-title>
              <v-list-item-title v-if="transaction.status == 0">Waiting for seller</v-list-item-title>
              <v-list-item-title v-else-if="transaction.status == 1">Waiting for action</v-list-item-title>
              <v-list-item-title v-else-if="transaction.status == 2">In the works</v-list-item-title>
              <v-list-item-title v-else-if="transaction.status == 3">Complete</v-list-item-title>
              <v-list-item-title v-else-if="transaction.status == 4">Cancelled</v-list-item-title>
              <v-list-item-title v-else>Error</v-list-item-title>
            </div>

            <b-button class="pushDown" v-if="transaction.status == 1" @click="$router.push({path: `/sellerItemSelect/${transaction.trade_id}`})">Select an Item from Other User</b-button>
            <b-button class="pushDown" v-else-if="transaction.status == 2" v-on:click= "() => markComplete(transaction.trade_id)">Mark Trade as Complete</b-button>
          </b-card-body>
        </b-col>
      </b-row>
    </b-card>
  </b-container>
</template>

<script>

import firebase from 'firebase';
import axios from 'axios';
import qs from 'qs';

export default {
  name: "MyTrades",
  components: {},
  data: () => ({
    trade_list: [],
    dummy_text: ''
  }),
  methods: {
    updateUserProfile: function(trade) {
        var storage = firebase.storage();
        var storageRef = storage.ref();

        if (trade.other_user.photo_url) {
          let photo_path = trade.other_user.photo_url.split('appspot.com/')[1];
          storageRef.child(photo_path).getDownloadURL().then(function(url) {
            trade.other_user.photo_url = url;
          });
        }

        if (trade.their_item) {
          if (trade.their_item.photo_url != "") {
            let photo_path = trade.their_item.photo_url.split('appspot.com/')[1];
            storageRef.child(photo_path).getDownloadURL().then(function(url) {
              trade.their_item.photo_url = url;
            });
          }
        }

        if (trade.your_item) {
          if (trade.your_item.photo_url != "") {
            let photo_path = trade.your_item.photo_url.split('appspot.com/')[1];
            storageRef.child(photo_path).getDownloadURL().then(function(url) {
              trade.your_item.photo_url = url;
            });
          }
        }
    },

    cancel: function(trade_id) {
      let self = this;

      axios.post('/trades/' + trade_id + '/remove', qs.stringify({
        'tradeID': trade_id
      }), {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Authorization': 'token ' + self.$store.getters.authToken
        }
      })
      .then(response => {
        self.dummy_text = response;
        alert("Successfully Cancelled Trade");
        setTimeout(function(){ self.$router.replace('/account'); }, 500);
      })
      .catch(error => {
        let errorCode = error.code;
        let errorMessage = error.message;
        self.snackbar = true;
        self.text = "ERROR " + errorCode + ":" + errorMessage;
      });
    },

    markComplete: function(trade_id) {
      let self = this;

      axios.post('/trades/' + trade_id + '/complete', qs.stringify({
        'tradeID': trade_id
      }), {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Authorization': 'token ' + self.$store.getters.authToken
        }
      })
      .then(response => {
        self.dummy_text = response;
        alert("Successfully Marked Trade as Complete");
        setTimeout(function(){ self.$router.replace('/account'); }, 500);
      })
      .catch(error => {
        let errorCode = error.code;
        let errorMessage = error.message;
        self.snackbar = true;
        self.text = "ERROR " + errorCode + ":" + errorMessage;
      });
    }

  },
  created() {
    let self = this;
    axios.get('/trades/', {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'token ' + self.$store.getters.authToken
      }
    })
      .then(response => {
        let responseData = response.data;
        self.trade_list = responseData['trades'];
        var index;
        for (index = 0; index < self.trade_list.length; index++) { 
          self.updateUserProfile(self.trade_list[index]);
        } 
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
.noHyperlink {
  text-decoration: none;
  color: black;
}

.imageSize {
  width: 100%;
  height: 20vw;
  object-fit: cover;
}

.imageCard {
  width: 150px;
  height: 150px;
}

.pushRight {
  margin-left: auto;
  margin-right: 1%;
}

.pushDown {
  position: absolute;
  bottom: 10%;
}

.pushHalfway {
  position: absolute;
  bottom: 50%;
}

.card {
  overflow-wrap: break-word;
  word-wrap: break-word;
  hyphens: auto;
}

.mytradestitle {
  width: 100%;
  margin-top: 2%;
  text-align: center;
}
</style>
