import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import Vuex from 'vuex';
import {store} from './store/store'

Vue.use(Vuex);
Vue.config.productionTip = false;
Vue.use(BootstrapVue);

new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount('#app');
