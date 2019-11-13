<template>
    
    <b-container fluid style="padding: 80px 40px 0 40px">
        <b-card class="overflow-hidden">
            <b-row>
                <b-col >
                    <b-card-img :src='itemImage' class="rounded-0"></b-card-img>
                </b-col>
                <b-col>
                    <v-list-item>
                        <v-list-item-avatar color="grey">
                            <v-img :src="avatar"></v-img>
                        </v-list-item-avatar>
                        <v-list-item-content>
                            <v-list-item-title class="headline"> {{itemTitle}} </v-list-item-title>
                            <router-link :to="name">
                            <v-list-item-subtitle>by {{name}}</v-list-item-subtitle>
                            </router-link>
                            <v-list-item-subtitle>{{location}}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>

                    <b-card-body title="">
                        <b-card-text>
                            {{description}}
                        </b-card-text>
                    </b-card-body>

                    <div style="padding: 10px">
                        <v-btn large> Start Trade</v-btn>
                        <v-btn large style="margin-left: 30px"> Hide </v-btn>
                    </div>
                </b-col>
            </b-row>
        </b-card>

    </b-container>
</template>

<script>
    export default {
        data() {
            return {
                name: 'Nikita',
                itemTitle: 'Adidas shoes',
                location: 'Los Angeles, CA',
                avatar: "https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/22449875_913694855449733_82882405759448142_n.jpg?_nc_cat=101&_nc_oc=AQncaWWuWzFfxdVtK5P69Jl-sJRqNOoHsimpBnysDiZ4IU6CrUGl_iMle5gtvd83ylHYe0ve-pmotMRHVvP7ufkn&_nc_ht=scontent-lax3-1.xx&oh=8a7bc0b583f64c997324885cbafb92a0&oe=5E627D59",
                description: 'Good shoes almost new..Adidas AG is a multinational corporation, founded and headquartered in Herzogenaurach, Germany, that designs and manufactures shoes, clothing and accessories. It is the largest sportswear manufacturer in Europe, and the second largest in the world, after Nike.',
                itemImage: "https://www.ft.com/__origami/service/image/v2/images/raw/http%3A%2F%2Fcom.ft.imagepublish.upp-prod-us.s3.amazonaws.com%2F4c1140ec-8826-11e8-affd-da9960227309?fit=scale-down&source=next&width=700"

            }
        }
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