<template>
    <div class="about">
        <b-row style="text-align: center; margin: 165px 50px 0 50px">
            <div id="cover">
                <form method="get" action="">
                    <div class="tb">
                        <div class="td">
                            <input type="text" placeholder="search..." required name="search" @input="changed"
                                   v-model="searchText">
                        </div>
                        <div class="td" id="s-cover" @click="mySearch">
                            <button>
                                <div id="s-circle"></div>
                                <span></span>
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </b-row>

        <b-row style="padding: 20px 40px 0 40px" v-if="safe">
            <li v-for="item in items" v-bind:key="item.description" style="list-style-type:none;">
                <Item :item="item"></Item>
            </li>
        </b-row>

        <b-row style="padding: 20px 40px 0 40px" v-if="non">
            <b-col cols="1"></b-col>
            <b-col cols="10" style="text-align: center">
                <h1>Sorry, <p style="font-family: italic">{{searchText}}</p> is not currently a valid tag for existing items on Tradespace. Please search for items using another tag. </h1>
            </b-col>
            <b-col cols="1"></b-col>
        </b-row>

        <div class="text-center ma-2">
            <v-snackbar
                    v-model="snackbar"
            >
                {{ text }}
                <v-btn
                        color="pink"
                        text
                        @click="snackbar = false"
                >
                    Close
                </v-btn>
            </v-snackbar>
        </div>

    </div>
</template>

<script>
    import Item from '../components/item';
    import axios from "axios";
    // import qs from 'querystring';


    export default {
        name: 'About',
        components: {
            Item,
        },
        data: () => ({
            items: [],
            safe: false,
            show: true,
            searchText: "",
            non: false,
            text: '',
            snackbar: false,
        }),
        methods: {
            changed: function () {
                this.$store.commit('change', this.searchText)
            },
            mySearch: function () {
                this.safe = false;
                this.non = false;
                let self = this;
                axios.get('/search/' + this.searchText, {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Authorization': 'token ' + self.$store.getters.authToken
                    }
                })
                    .then(response => {
                        self.items = response.data.data;
                        if (self.items.length > 0) {
                            self.safe = true;
                        } else{
                            self.non = true;
                        }
                    })
                    .catch(error => {
                        let errorCode = error.code;
                        let errorMessage = error.message;
                        self.snackbar = true;
                        self.text = "ERROR " + errorCode + ":" + errorMessage;
                    });
            }
        },
        created: function () {
            this.searchText = this.$store.getters.search;
            this.mySearch();
        }
    };
</script>

<style scoped>
    .my_card {
        /*width: 1000px;*/
        height: 200px;
    }

    body {
        margin: 0;
        background-color: #ffd8d8;
    }

    .tb {
        display: table;
        width: 100%;
    }

    .td {
        display: table-cell;
        vertical-align: middle;
    }

    input, button {
        color: #fff;
        font-family: Nunito;
        padding: 0;
        margin: 0;
        border: 0;
        background-color: transparent;
    }

    #cover {
        position: absolute;
        left: 0;
        right: 0;
        width: 100%;
        padding: 5px;
        margin: -83px auto 0 auto;
        background-color: #a4a0a9;
        border-radius: 20px;
        box-shadow: 0 10px 40px #a4a0a9, 0 0 0 20px #ffffffeb;
        transform: scale(0.6);
    }

    form {
        height: 96px;
    }

    input[type="text"] {
        width: 100%;
        height: 96px;
        font-size: 60px;
        line-height: 1;
    }

    input[type="text"]::placeholder {
        color: #000000;
    }

    #s-cover {
        width: 1px;
        padding-left: 35px;
    }

    button {
        position: relative;
        display: block;
        width: 84px;
        height: 96px;
        cursor: pointer;
    }

    #s-circle {
        position: relative;
        top: -8px;
        left: 0;
        width: 43px;
        height: 43px;
        margin-top: 0;
        border-width: 15px;
        border: 15px solid #fff;
        background-color: transparent;
        border-radius: 50%;
        transition: 0.5s ease all;
    }

    button span {
        position: absolute;
        top: 68px;
        left: 43px;
        display: block;
        width: 45px;
        height: 15px;
        background-color: transparent;
        border-radius: 10px;
        transform: rotateZ(52deg);
        transition: 0.5s ease all;
    }

    button span:before, button span:after {
        content: '';
        position: absolute;
        bottom: 0;
        right: 0;
        width: 45px;
        height: 15px;
        background-color: #fff;
        border-radius: 10px;
        transform: rotateZ(0);
        transition: 0.5s ease all;
    }

    #s-cover:hover #s-circle {
        top: -1px;
        width: 67px;
        height: 15px;
        border-width: 0;
        background-color: #fff;
        border-radius: 20px;
    }

    #s-cover:hover span {
        top: 50%;
        left: 56px;
        width: 25px;
        margin-top: -9px;
        transform: rotateZ(0);
    }

    #s-cover:hover button span:before {
        bottom: 11px;
        transform: rotateZ(52deg);
    }

    #s-cover:hover button span:after {
        bottom: -11px;
        transform: rotateZ(-52deg);
    }

    #s-cover:hover button span:before, #s-cover:hover button span:after {
        right: -6px;
        width: 40px;
        background-color: #fff;
    }
</style>