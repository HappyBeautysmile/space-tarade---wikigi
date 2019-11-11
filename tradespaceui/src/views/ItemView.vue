<template>
    <div id="container">
        <v-card
        class="mx-auto"
        max-width="344"
        hover="true"
        >
            <v-list-item>
                <v-list-item-avatar color="grey">
                    <v-img src=" https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/22449875_913694855449733_82882405759448142_n.jpg?_nc_cat=101&_nc_oc=AQncaWWuWzFfxdVtK5P69Jl-sJRqNOoHsimpBnysDiZ4IU6CrUGl_iMle5gtvd83ylHYe0ve-pmotMRHVvP7ufkn&_nc_ht=scontent-lax3-1.xx&oh=8a7bc0b583f64c997324885cbafb92a0&oe=5E627D59"></v-img>
                </v-list-item-avatar>
                <v-list-item-content>
                    <v-list-item-title class="headline">Adidas shoes</v-list-item-title>
                    <router-link to="/nikita">
                    <v-list-item-subtitle>by Nikita</v-list-item-subtitle>
                    </router-link>
                </v-list-item-content>
            </v-list-item>
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-subtitle>Los Angeles, CA</v-list-item-subtitle>
                </v-list-item-content>
            </v-list-item>
            <v-img
                    src="https://www.ft.com/__origami/service/image/v2/images/raw/http%3A%2F%2Fcom.ft.imagepublish.upp-prod-us.s3.amazonaws.com%2F4c1140ec-8826-11e8-affd-da9960227309?fit=scale-down&source=next&width=700"
                    height="200px"
            ></v-img>

            <v-card-subtitle style="display: block">
                <p id="text">Good shoes almost new..Adidas AG is a multinational corporation, founded and headquartered in Herzogenaurach, Germany, that designs and manufactures shoes, clothing and accessories. It is the largest sportswear manufacturer in Europe, and the second largest in the world, after Nike..</p>

                <v-btn large class="item_action"> Start Trade</v-btn>
                <v-btn large class="item_action"> Hide</v-btn>
            </v-card-subtitle>
        </v-card>
    </div>
</template>

<script>

    export default {
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