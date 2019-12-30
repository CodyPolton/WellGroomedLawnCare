import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import VueTelInput from 'vue-tel-input';
import VueSession from 'vue-session';
import Axios from 'axios';
import Vuex from 'vuex';
import Notifications from 'vue-notification'




Vue.prototype.$http = Axios;

const token = localStorage.getItem('user-token')
if (token) {
  Vue.prototype.$http.defaults.headers.common['Authorization'] = token
}

Vue.use(Notifications)
Vue.use(VueTelInput)
Vue.use(VueSession)
Vue.use(Vuex);

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
