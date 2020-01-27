import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Invoices from '../views/Invoices.vue';
import Crews from '../views/Crews.vue';
import Accounts from '../views/Accounts.vue';
import AccountView from '../views/AccountView.vue';
import YardView from '../views/YardView.vue';
import InvoiceView from '../views/InvoiceView.vue';
import Schedule from '../views/Schedule.vue';
import Route from '../views/Route.vue';
import Login from '../components/Login.vue';
import Config from '../views/Configuration.vue'
import JobView from '../views/JobView.vue'
import CrewView from '../views/CrewView.vue'

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
    path: '/schedules',
    name: 'schedule',
    component: Schedule,
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
  },
  {
    path: '/configuration',
    name: 'Configuration',
    component: Config
  },
  {
    path: '/job/:id',
    name: 'JobView',
    component: JobView
  },
  {
    path: '/crew/:crewid',
    name: 'CrewView',
    component: CrewView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
