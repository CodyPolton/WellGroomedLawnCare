import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Invoices from '../views/Invoices.vue';
import Crews from '../views/Crews.vue';
import Accounts from '../views/Accounts.vue';
import AddAccounts from '../views/AddAccounts.vue';
import AccountView from '../views/AccountView.vue';
import YardView from '../views/YardView.vue';
import AddYard from '../views/AddYard.vue';
import InvoiceView from '../views/InvoiceView.vue';
import ScheduleView from '../views/ScheduleView.vue';
import Route from '../views/Route.vue';
import Login from '../components/Login.vue';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/invoices',
    name: 'invoices',
    component: Invoices,
  },
  {
    path: '/crews',
    name: 'crews',
    component: Crews,
  },
  {
    path: '/accounts',
    name: 'accounts',
    component: Accounts,
  },
  {
    path: '/addaccount',
    name: 'addaccounts',
    component: AddAccounts,
  },
  {
    path: '/account/:id',
    name: 'accountview',
    component: AccountView,
  },
  {
    path: '/yard/:accountid/:yardid',
    name: 'yardview',
    component: YardView,
  },
  {
    path: '/invoice/:id',
    name: 'invoiceview',
    component: InvoiceView,
  },
  {
    path: '/addyard/:id',
    name: 'addyard',
    component: AddYard,
  },
  {
    path: '/schedule',
    name: 'scheduleview',
    component: ScheduleView,
  },
  {
    path: '/route*',
    name: 'route',
    component: Route,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
