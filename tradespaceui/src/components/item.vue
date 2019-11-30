<template>
    <div id="myitem">
        <v-card
                class="mx-auto"
                max-width="344"
        >
            <v-list-item>
                <v-list-item-avatar color="grey">
                    <v-img :src="profile"></v-img>
                </v-list-item-avatar>
                <v-list-item-content>
                    <v-img :src="itemPhoto"></v-img>
                    <v-list-item-title class="headline">{{itemTitle}}</v-list-item-title>
                    <v-list-item-subtitle>by {{name}}</v-list-item-subtitle>
                </v-list-item-content>
            </v-list-item>
            <v-card-subtitle style="display: block">
                <p id="text"> {{ itemDescription }}</p>
            </v-card-subtitle>
        </v-card>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'Item',
        //DO PROP VALIDATION IF THERE IS TIME: https://vuejs.org/v2/guide/components-props.html
        props: [
            'item'
            //Item contains an array with all the different components

            //'item', 'location', 'title', 'tags', 'owner_uid', 'photo_url', 'description'

            // self.location = item['location'];
            // self.itemTitle = item['title'];
            // self.tags = item['tags'];
            // self.owner_uid = item['owner_uid'];
            // self.photo_url = item['photo_url'];
            // self.description = item['description'];
            // self.itemImage = item['photo_url'];
        ],
        data: () => ({
            itemTitle: '',
            itemDescription: '',
            itemPhoto: '',
            itemTags: '',
            itemLocation: '',
            owner_uid: '',
            name: '',
            profile: '',

        }),
        created() {
            this.itemTitle = this.item['title'];
            this.itemDescription = this.item['description'];
            this.itemPhoto = this.item['photo_url'];
            this.itemTags = this.item['tags'];
            this.itemLocation = this.item['location'];
            this.owner_uid = this.item['owner_uid'];
            let self = this;
            axios.get('/users/' + self.owner_uid, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Authorization': 'token ' + self.$store.getters.authToken
                }
            })
                .then(response => {
                    let user = response.data;
                    self.name = user['display_name'];
                    self.profile = user['photo_url'];
                })
                .catch(error => {
                    let errorCode = error.code;
                    let errorMessage = error.message;
                    alert("ERROR " + errorCode + ":" + errorMessage);
                });
        }
        // return {
        //     itemTitle: this.item['title'],
        //     itemLocation: this.location,
        //     itemTags: this.tags,
        //     itemOwner_uid: this.owner_uid,
        //     avatar: this.photo_url, //TODO: FIX OWNER AVATAR
        //     itemDescription: this.item['description'],
        //     itemImage: this.photo_url

        // }
        ,

        //TODO: MAKE A METHOD TO "GET" A USER'S PROFILE PICTURE


        // data ({
        //     return {
        //         name: '',
        //         itemTitle: '',
        //         location: 'SF',
        //         tags: [],
        //         owner_uid: '',
        //         avatar: "",
        //         description: '',
        //         itemImage: ""

        //     }
        //     // show: false,
        //     // items: [
        //     //     {src: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/22449875_913694855449733_82882405759448142_n.jpg?_nc_cat=101&_nc_oc=AQncaWWuWzFfxdVtK5P69Jl-sJRqNOoHsimpBnysDiZ4IU6CrUGl_iMle5gtvd83ylHYe0ve-pmotMRHVvP7ufkn&_nc_ht=scontent-lax3-1.xx&oh=8a7bc0b583f64c997324885cbafb92a0&oe=5E627D59'},
        //     //     {src: 'https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/22449875_913694855449733_82882405759448142_n.jpg?_nc_cat=101&_nc_oc=AQncaWWuWzFfxdVtK5P69Jl-sJRqNOoHsimpBnysDiZ4IU6CrUGl_iMle5gtvd83ylHYe0ve-pmotMRHVvP7ufkn&_nc_ht=scontent-lax3-1.xx&oh=8a7bc0b583f64c997324885cbafb92a0&oe=5E627D59'}
        //     // ]
        // }),


    }
    ;
</script>

<style scoped>
    #myitem {
        margin: 5px;
        display: inline-block;
    }

    #text {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-height: 100px;
    }
</style>