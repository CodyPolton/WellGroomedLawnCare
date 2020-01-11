import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authenticated: false
  },
  mutations: {
    loggedIn (state) {
      state.authenticated = true
    }
  },
  actions: {
  },
  modules: {
  }
})
