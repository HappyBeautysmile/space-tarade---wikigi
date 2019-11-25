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

export default {
  
  name: "Account",
  components: {
    Item,
  },
  data: () => ({
    items: [
      'foo', 'bar', 'bork', 'dog', 'shoe', 'catch', 'p1', 'p2'
    ]
  })
};
</script>

<style scoped>
.noHyperlink {
  text-decoration: none;
  color: black;
}
</style>
