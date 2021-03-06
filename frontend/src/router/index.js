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
import Login from '../views/Login.vue';
import Config from '../views/Configuration.vue'
import JobView from '../views/JobView.vue'
import CrewView from '../views/CrewView.vue'
import Timesheets from '../views/Timesheets.vue'
import Unauthenticated from '../components/Unauthenticated.vue'
import AboutusPage from '../views/AboutusPage.vue'
import ContactPage from '../views/ContactPage.vue'
import MowingPage from '../views/MowingPage.vue'
import YardcarePage from '../views/YardcarePage.vue'
import LandscapingPage from '../views/LandscapingPage.vue'
import Dashboard from '../views/Dashboard.vue'
import store from '../store'


Vue.use(VueRouter)

const routes = [
  {
    path: '/unauthenticated',
    name: 'unauthenticaed',
    component: Unauthenticated
  },
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/timesheets',
    name: 'timesheets',
    component: Timesheets,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/invoices',
    name: 'invoices',
    component: Invoices,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/crews',
    name: 'crews',
    component: Crews,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/accounts',
    name: 'accounts',
    component: Accounts,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/account/:id',
    name: 'accountview',
    component: AccountView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/yard/:accountid/:yardid',
    name: 'yardview',
    component: YardView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/invoice/:id',
    name: 'invoiceview',
    component: InvoiceView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/schedules',
    name: 'schedule',
    component: Schedule,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/route*',
    name: 'route',
    component: Route,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,


  },
  {
    path: '/configuration',
    name: 'Configuration',
    component: Config,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/job/:id',
    name: 'JobView',
    component: JobView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/crew/:crewid',
    name: 'CrewView',
    component: CrewView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/contact',
    name: 'Contact Us',
    component: ContactPage,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: '/landscaping',
    name: 'Landscaping',
    component: LandscapingPage,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: '/mowing',
    name: 'Mowing',
    component: MowingPage,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: '/about',
    name: 'About Us',
    component: AboutusPage,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: '/yardcare',
    name: 'Yard Care',
    component: YardcarePage,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: '/dashboard',
    name: 'Management Dashboard',
    component: Dashboard,
    meta: {
      requiresAuth: true
    }
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.checkAuthentication) {
      next()
      return
    }
    next('/login')
  } else {
    next()
  }
})
export default router
