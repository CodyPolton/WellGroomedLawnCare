<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <v-app-bar-nav-icon @click="drawer = !drawer" />

      <v-toolbar-title>Well Groomed Lawn Care</v-toolbar-title>

      <v-spacer />



          <v-btn
            icon
            v-if="!authenticated"
      @click="login()"

          >
            <v-icon>mdi-account</v-icon>
          </v-btn>

    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      app
      dark
      temporary
    >
      <v-list height="64">
        <v-list-item>
          <v-list-item-content class="pa-0">
            <v-list-item-title class="title">
              User Name Placeholder
            </v-list-item-title>
            <v-list-item-subtitle>
              Admin/Employee/Customer
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-divider />
      <v-list>
        <v-list-item
          link
        >
          <v-list-item-icon>
            <v-icon>
              mdi-home
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>
              Home
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-group
          v-for="item in items"
          :key="item.title"
          v-model="item.active"
          :prepend-icon="item.action"
          no-action
        >
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title v-text="item.title" />
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="subItem in item.items"
            :key="subItem.title"
          >
            <v-list-item-content>
              <v-list-item-title v-text="subItem.title" />
            </v-list-item-content>
          </v-list-item>
        </v-list-group>
        <v-list-item
          link
        >
          <v-list-item-icon>
            <v-icon>
              mdi-navigation
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>
              Routing
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item
          link
        >
          <v-list-item-icon>
            <v-icon>
              mdi-clipboard-text
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <router-link to="/invoices">
              Invoices
            </router-link>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-content>
      <v-container fluid>
        <v-btn
        v-if="authenticated"
        @click="privateMessage()">Check Private API Permissions</v-btn>
                <v-btn
        v-if="authenticated"
       @click="logout()">Log Out</v-btn>
       {{ message }}
        <router-view />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import AuthService from './auth/AuthService'
import axios from 'axios'

const API_URL = 'http://localhost:8000'
const auth = new AuthService()
export default {

  data() {
    this.handleAuthentication()
    this.authenticated = false

    auth.authNotifier.on('authChange', authState => {
      this.authenticated = authState.authenticated
    })
    return {
      authenticated: false,
      message: '',
      drawer: false,
      items: [
        {
          action: 'mdi-leaf',
          title: 'Lawn Care',
          active: false,
          items: [
            { title: 'test item 1' },
            { title: 'test item 2' },
            { title: 'test item 3' },
          ],
        },
        {
          action: 'mdi-content-cut',
          title: 'Landscaping',
          items: [
            { title: 'test item 1' },
          ],
        },
      ],

    };
  },
  methods: {
    // this method calls the AuthService login() method
    login () {
      auth.login()
    },
    handleAuthentication () {
      auth.handleAuthentication()
    },
    logout () {
      auth.logout()
    },
    privateMessage () {
      const url = `${API_URL}/api/private/`
      return axios.get(url, {headers: {Authorization: `Bearer ${auth.getAuthToken()}`}}).then((response) => {
        console.log(response.data)
        this.message = response.data || ''
      })
    }
  }
};
</script>