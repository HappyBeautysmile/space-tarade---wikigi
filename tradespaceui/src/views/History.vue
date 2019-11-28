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
import axios from 'axios';

export default {
  
  name: "Account",
  components: {
    Item,
  },
  data: () => ({
    items: [
      'foo', 'bar', 'bork', 'dog', 'shoe', 'catch', 'p1', 'p2'
    ]
  }),
  created() {
    // alert('CHECK')
    let self = this;
    axios.get('/items/', {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'token ' + self.$store.getters.authToken
        }
    })
        .then(response => {
            alert(response)
            //TODO: RESPONSE DATA IS AN ARRAY, ITERATE THROUGH AND GET THE ITEMS IN THAT WAY.
            //self.items = response.data;

            // let item = response.data;
            // self.location = item['location'];
            // self.itemTitle = item['title'];
            // self.tags = item['tags'];
            // self.owner_uid = item['owner_uid'];
            // self.photo_url = item['photo_url'];
            // self.description = item['description'];
            // self.itemImage = item['photo_url'];
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
