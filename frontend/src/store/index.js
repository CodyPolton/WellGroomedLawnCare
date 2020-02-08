import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'
import createPersistedState from "vuex-persistedstate";
import * as Cookie from 'js-cookie'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    jwt: localStorage.getItem('t'),
    endpoints: {
      obtainJWT: 'http://127.0.0.1:8000/api/token/',
      refreshJWT: 'http://127.0.0.1:8000/api/refresh_token/'
    },
    authenticated: false
  },
  mutations: {
    loggedIn (state) {
      state.authenticated = true;
      router.push('home')
    },
    logout(state){
      state.authenticated = false;
      router.push('home')

    },
    updateToken(state, newToken){
      localStorage.setItem('t', newToken);
      state.jwt = newToken;
      this.commit('loggedIn');
  },
  removeToken(state){
    localStorage.removeItem('t');
    state.jwt = null;
  }
},
  actions: {
    obtainToken(context, loginInfo){
      const payload = {
        username: loginInfo.username,
        password: loginInfo.password
      }
      axios.post(this.state.endpoints.obtainJWT, payload)
        .then((response)=>{
            this.commit('updateToken', response.data.token);
          })
        .catch((error)=>{
            console.log(error);
          })
    },
    refreshToken(){
      const payload = {
        token: this.state.jwt
      }
      axios.post(this.state.endpoints.refreshJWT, payload)
        .then((response)=>{
            this.commit('updateToken', response.data.token)
          })
        .catch((error)=>{
            console.log(error)
          })
    },
    inspectToken(){
      const token = this.state.jwt;
      if(token){
        const decoded = jwt_decode(token);
        const exp = decoded.exp
        const orig_iat = decode.orig_iat
        if(exp - (Date.now()/1000) < 1800 && (Date.now()/1000) - orig_iat < 628200){
          this.dispatch('refreshToken')
        } else if (exp -(Date.now()/1000) < 1800){
          // DO NOTHING, DO NOT REFRESH
        } else {
          // PROMPT USER TO RE-LOGIN, THIS ELSE CLAUSE COVERS THE CONDITION WHERE A TOKEN IS EXPIRED AS WELL
        }
      }
    }
  },
  getters: {
    checkAuthentication: state => {
      return state.authenticated;
    }
  },
  modules: {
  },
  plugins: [
    createPersistedState({
        getState: (key) => Cookie.getJSON(key),
        setState: (key, state) => Cookie.set(key, state, { expires: 1, secure: false })
    })
 ]
})
