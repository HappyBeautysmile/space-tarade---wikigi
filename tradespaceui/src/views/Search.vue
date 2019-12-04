<template>
    <div>
        <b-row style="text-align: center; margin: 180px 50px 0 50px">
            <div id="cover">
                <form method="get" action="">
                    <div class="tb">
                        <div class="td">
                            <input type="text" placeholder="search..." required name="search" @input="changed"
                                   v-model="searchText">
                        </div>
                        <router-link to="/about">
                            <div class="td" id="s-cover">
                                <button>
                                    <div id="s-circle"></div>
                                    <span></span>
                                </button>
                            </div>
                        </router-link>

                    </div>
                </form>
            </div>
        </b-row>
    </div>
</template>

<script>
    export default {
        name: "Search",
        data: () => ({
            show: true,
            searchText: ""
        }),
        methods: {
            changed: function () {
                this.$store.commit('change', this.searchText)
            },
        }
    }
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