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
    first_name: 'Cody',
    last_name: null,
    group_name: null,
    group_level: null,
    user_id: null,
    endpoints: {
      obtainJWT: process.env.VUE_APP_API_URL +'token/',
      refreshJWT: process.env.VUE_APP_API_URL + 'token/refresh/'
    },
    authenticated: false
  },
  mutations: {
    loggedIn (state) {
      state.authenticated = true;
      router.push('/')
    },
    logout(state){
      this.commit('removeToken')
      state.first_name = ''
      state.last_name = ''
      state.group_level = ''
      state.group_name = ''
      state.user_id = ''
      state.jwt = ''
      state.authenticated = false;
      router.push('/')

    },
    updateToken(state, newToken){
      // axios.post(process.env.VUE_APP_API_URL + 'returnuserdetails', { token : newToken})
      //   .then((response)=>{
            // console.log(response)
            // state.first_name = response.data.first_name
            // state.last_name = response.data.last_name
            // state.group_level = response.data.group_level
            // state.group_name = response.data.group_name
            // state.user_id = response.data.user_id
            localStorage.setItem('t', newToken);
            state.jwt = newToken;
            this.commit('loggedIn');
        //   })
        // .catch((error)=>{
        //     console.log(error);
        //   })
      
  },
  removeToken(state){
    localStorage.removeItem('t');
    state.jwt = '';
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
