import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        search: 'shoes',
        loggedIn: false,
        authToken: '',
        item: '',
        selected: '',
    },
    mutations: {
        change(state, search) {
            state.search = search
        },
        logIn(state, bool) {
            state.loggedIn = bool;
            state.authToken = '';
        },
        setToken(state, token) {
            state.authToken = token;
        },
        startTrade(state, item2) {
            state.item = item2;
        },
        selectItem(state, item1) {
            state.selected = item1;
        },
    },
    getters: {
        search: state => state.search,
        loggedIn: state => state.loggedIn,
        authToken: state => state.authToken,
        item: state => state.item,
        selected: state => state.selected,
    }
});