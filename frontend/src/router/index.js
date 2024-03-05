// src/router.js
import { createRouter, createWebHistory } from 'vue-router';
import Games from "../components/Games.vue";
import Home from "../components/Home.vue";
import Login from "../components/Login.vue";
import Register from "../components/Register.vue";

const routes = [  
  {
    path: '/games',
    name: 'Games',
    component: Games,
  },{
    path: '/',
    name: 'Home',
    component: Home,
  },{
    path: '/login',
    name: 'login',
    component: Login
  },{
    path: '/register',
    name: 'register',
    component : Register
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
