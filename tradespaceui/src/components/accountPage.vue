<template>
    <div id="myitem">
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
                    <v-list-item-subtitle>by Nikita</v-list-item-subtitle>
                </v-list-item-content>
            </v-list-item>
            <v-img
                    src="https://www.ft.com/__origami/service/image/v2/images/raw/http%3A%2F%2Fcom.ft.imagepublish.upp-prod-us.s3.amazonaws.com%2F4c1140ec-8826-11e8-affd-da9960227309?fit=scale-down&source=next&width=700"
                    height="200px"
            ></v-img>

<!--            <v-card-title>-->
<!--                Top western road trips-->
<!--            </v-card-title>-->

            <v-card-subtitle style="display: block">
                <p id="text">Good shoes almost new..Adidas AG is a multinational corporation, founded and headquartered in Herzogenaurach, Germany, that designs and manufactures shoes, clothing and accessories. It is the largest sportswear manufacturer in Europe, and the second largest in the world, after Nike..</p>
                <v-btn text icon color="indigo" style="margin: 0; padding: 0; display: inline-block;">
                    <v-icon>mdi-call-split</v-icon>
                </v-btn>
            </v-card-subtitle>

<!--            <v-card-actions>-->
<!--&lt;!&ndash;                <v-btn text>Share</v-btn>&ndash;&gt;-->

<!--&lt;!&ndash;                <v-btn&ndash;&gt;-->
<!--&lt;!&ndash;                        color="purple"&ndash;&gt;-->
<!--&lt;!&ndash;                        text&ndash;&gt;-->
<!--&lt;!&ndash;                >&ndash;&gt;-->
<!--&lt;!&ndash;                    Explore&ndash;&gt;-->
<!--&lt;!&ndash;                </v-btn>&ndash;&gt;-->

<!--                <v-spacer></v-spacer>-->

<!--                <v-btn-->
<!--                        icon-->
<!--                        @click="show = !show"-->
<!--                >-->
<!--                    <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>-->
<!--                </v-btn>-->
<!--            </v-card-actions>-->

<!--            <v-expand-transition>-->
<!--                <div v-show="show" style="position: fixed; background: azure">-->
<!--                    <v-divider></v-divider>-->

<!--                    <v-card-text>-->
<!--                        I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.-->
<!--                    </v-card-text>-->
<!--                </div>-->
<!--            </v-expand-transition>-->
        </v-card>
    </div>
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

    #text{
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-height: 100px;
    }
</style>