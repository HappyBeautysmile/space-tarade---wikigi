<template>

    <b-container class="myAccount">
    <b-row>
        <b-col>
            <v-card class="mx-auto" max-width="500" hover="true">
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title class="headline">Profile Picture</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-img id="accountPic"
                src=" https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/22449875_913694855449733_82882405759448142_n.jpg?_nc_cat=101&_nc_oc=AQncaWWuWzFfxdVtK5P69Jl-sJRqNOoHsimpBnysDiZ4IU6CrUGl_iMle5gtvd83ylHYe0ve-pmotMRHVvP7ufkn&_nc_ht=scontent-lax3-1.xx&oh=8a7bc0b583f64c997324885cbafb92a0&oe=5E627D59"
                height="500px"
            ></v-img>

            <v-card-subtitle style="display: block">
                <p id="text">Hi my name is Nikita and I love to trade shoes!</p>
                <v-btn text icon color="indigo" style="margin: 0; padding: 0; display: inline-block;">
                    <v-icon>mdi-call-split</v-icon>
                </v-btn>
            </v-card-subtitle>

        </v-card>
        </b-col>
        <b-col>
            <v-card class="mx-auto" max-width="500" hover="true">
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title class="headline">Profile Picture</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-img 
                src="https://www.ft.com/__origami/service/image/v2/images/raw/http%3A%2F%2Fcom.ft.imagepublish.upp-prod-us.s3.amazonaws.com%2F4c1140ec-8826-11e8-affd-da9960227309?fit=scale-down&source=next&width=700"
                height="500px"
            ></v-img>

            <v-card-subtitle style="display: block">
                <p id="text">Hi my name is Nikita and I love to trade shoes!</p>
                <v-btn text icon color="indigo" style="margin: 0; padding: 0; display: inline-block;">
                    <v-icon>mdi-call-split</v-icon>
                </v-btn>
            </v-card-subtitle>

        </v-card>
        </b-col>

        <b-col>THIRD COLUMN</b-col>
    </b-row>
    </b-container>

</template>

<script>

    export default {
        name: 'Item',
        props: ['item'],
        data: () => ({
            show: false,
        }),
    };
</script>

<style scoped>
    #myitem{
        margin: 5px;
        display: inline-block;
        /*width: 350px;*/
        /*height: 350px;*/
        /*border-radius: 3px;*/
        /*border: 1px black solid;*/
    }

    #myAccount{
        margin: 5px;
        display: inline-block;
    }

    #text{
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-height: 100px;
    }
</style>