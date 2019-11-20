import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        search: 'shoes',
        loggedIn: false
    },
    mutations: {
        change(state, search) {
            state.search = search
        },
        logIn(state, bool) {
            state.loggedIn = bool;
        },
    },
    getters: {
        search: state => state.search,
        loggedIn: state => state.loggedIn
    }
});