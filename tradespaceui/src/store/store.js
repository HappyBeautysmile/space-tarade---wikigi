import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        search: 'shoes',
        loggedIn: false,
        authToken: ''
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
    },
    getters: {
        search: state => state.search,
        loggedIn: state => state.loggedIn,
        authToken: state => state.authToken
    }
});