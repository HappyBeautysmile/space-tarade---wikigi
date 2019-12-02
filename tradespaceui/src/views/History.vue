<template>
    <b-container fluid style="padding: 80px 40px 0 40px">

        <b-row style="padding: 20px 40px 0 40px" v-if="safe">
            <li v-for="item in my_items" v-bind:key="item.description" style="list-style-type:none;">

                <!-- Removed using Item component. Can implement again if we want -->
                <!-- <router-link to="/item/12345uniqueID"> -->
                <Item :item="item"></Item>
                <!-- </router-link>  -->
                <!-- CAN USE item[''] -->
                <!-- <router-link to="/item/12345uniqueID">
                    <div id="myitem">
                        <v-card
                                class="mx-auto"
                                max-width="344"
                                hover="true"
                        >
                            <v-list-item>
                                <v-list-item-avatar color="grey">
                                    <v-img :src="avatar"></v-img>
                                </v-list-item-avatar>
                                <v-list-item-content>
                                    <v-list-item-title class="headline">{{item['title']}}</v-list-item-title>
                                    <v-list-item-subtitle>by Nikita</v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>
                            <v-img
                                    src="https://www.ft.com/__origami/service/image/v2/images/raw/http%3A%2F%2Fcom.ft.imagepublish.upp-prod-us.s3.amazonaws.com%2F4c1140ec-8826-11e8-affd-da9960227309?fit=scale-down&source=next&width=700"
                                    height="200px"
                            ></v-img>

                            <v-card-subtitle style="display: block">
                                <p id="text"> {{item['description']}}</p>
                            </v-card-subtitle>
                        </v-card>
                    </div>
                </router-link> -->
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
            my_items: [],
            safe: false
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
                    //alert(response)
                    //TODO: RESPONSE DATA IS AN ARRAY, ITERATE THROUGH AND GET THE ITEMS IN THAT WAY.
                    let items = response.data;
                    //alert(items)
                    //alert(Object.values(items));

                    self.my_items = Object.values(items);
                    self.safe = true;
                    //self.items = response.data;

                    // for(var key in items) {
                    //     var value = items[key];
                    //     alert(value);
                    // // do something with "key" and "value" variables
                    // }


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
