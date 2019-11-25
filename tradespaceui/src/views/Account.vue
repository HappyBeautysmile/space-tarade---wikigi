<template>
  <b-list-group style="padding: 80px 40px 0 40px">
    <div style="text-align:center">
      <v-list-item-avatar color="grey" size="200px">
        <v-img :src="currentUser.avatarSrc"></v-img>
      </v-list-item-avatar>
      <router-link :to="currentUser.display_name" class="noHyperlink">
        <v-list-item-subtitle>{{
          "Username: " + currentUser.display_name
        }}</v-list-item-subtitle>
      </router-link>
      <v-list-item-subtitle>{{ "Phone Number: " + currentUser.phone_number }}</v-list-item-subtitle>
      <v-list-item-subtitle>{{ "Email: " + currentUser.email }}</v-list-item-subtitle>
      <v-list-item-subtitle>{{ "User ID: " + currentUser.uid }}</v-list-item-subtitle>
      <v-list-item-subtitle>{{ "Location: " + currentUser.location }}</v-list-item-subtitle>
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
export default {
  name: "Account",
  components: {},
  data: () => ({
    settings: [
      { name: "My Items", dest: "history" },
      { name: "My Trades", dest: "history" },
      { name: "Account Settings", dest: "email" }
    ],
    currentUser: {
      display_name: "nikita123",
      phone_number: "(555) 555-5555",
      email: "test1234@gmail.com",
      uid: "1",
      avatarSrc:
        "https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/22449875_913694855449733_82882405759448142_n.jpg?_nc_cat=101&_nc_oc=AQncaWWuWzFfxdVtK5P69Jl-sJRqNOoHsimpBnysDiZ4IU6CrUGl_iMle5gtvd83ylHYe0ve-pmotMRHVvP7ufkn&_nc_ht=scontent-lax3-1.xx&oh=8a7bc0b583f64c997324885cbafb92a0&oe=5E627D59",
      location: "Los Angeles, CA"
    }
    
  })
};
</script>

<style scoped>
.noHyperlink {
  text-decoration: none;
  color: black;
}
</style>
