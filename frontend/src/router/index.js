import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Invoices from '../views/Invoices.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/invoices',
    name: 'invoices',
    component: Invoices,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
