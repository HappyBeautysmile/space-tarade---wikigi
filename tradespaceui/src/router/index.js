import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
// import firebase from "firebase";
Vue.use(VueRouter);

const routes = [
  {
    path: "*",
    name: "home",
    component: Home
  },
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  {
    path: "/search",
    name: "search",
    // meta: {
    //   requiresAuth: true
    // },
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Search.vue")
  },
  {
    path: "/item/12345uniqueID",
    name: "item/12345uniqueID",
    // meta: {
    //   requiresAuth: true
    // },
    component: () => import("../views/ItemView.vue")
  },
  {
    path: "/account",
    name: "account",
    // meta: {
    //   requiresAuth: true
    // },
    component: () => import("../views/Account.vue")
  },

  {
    path: "/createItem",
    name: "createItem",
    component: () => import("../views/CreateItem.vue"),
    // meta: {
    //   requiresAuth: true
    // }
  },

  {
    path: "/email",
    name: "email",
    // meta: {
    //   requiresAuth: true
    // },
    component: () => import("../views/Email.vue")
  },

  {
    path: "/payment",
    name: "payment",
    meta: {
      requiresAuth: true
    },
    component: () => import("../views/Payment.vue")
  },

  {
    path: "/history",
    name: "history",
    // meta: {
    //   requiresAuth: true
    // },
    component: () => import("../views/History.vue")
  }
];



const router = new VueRouter({
  routes
});

// router.beforeEach((to, from,next) =>{
//   const currentUser = firebase.auth().currentUser;
//   const requireAuth = to.matched.some(record => record.meta.requiresAuth);
//
//   if (requireAuth && !currentUser) next('home');
//   else if (!requireAuth && currentUser) next('home');
//   else next();
// });

export default router;
