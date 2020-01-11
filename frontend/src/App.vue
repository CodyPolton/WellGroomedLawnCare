<template>
  <v-app>
    <!-- Navbar that customer will see -->
    <v-app-bar
      v-if="!authenticated"
      app
      color="primary"
      dark
      dense
    >

      <v-toolbar-title>Well Groomed Lawn Care</v-toolbar-title>

      <v-spacer />

      <v-btn
        v-if="!authenticated"
        icon
        @click="login()"

      >
        <v-icon>mdi-account</v-icon>
      </v-btn>

    </v-app-bar>

    <!-- Navbar once you are logged in for employees -->
    <v-app-bar

      color="primary"
      dark
      app
      dense
    >
      <v-app-bar-nav-icon
        v-if="!authenticated"
        @click="drawer = !drawer" />

      <v-toolbar-title>Well Groomed Lawn Care Management</v-toolbar-title>

      <v-spacer />



      <v-btn
        v-if="!authenticated"
        icon
        to="/login"
        link

      >
        <v-icon>mdi-account</v-icon>
      </v-btn>

    </v-app-bar>
    <v-navigation-drawer
      v-if="!authenticated"
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
          to="/accounts"
          link
        >
          <v-list-item-icon>
            <v-icon>
              mdi-clipboard-text
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            Accounts
            <!-- <router-link to="/invoices">
              Invoices
            </router-link> -->
          </v-list-item-content>
        </v-list-item>
        <v-list-item
          to="/crews"
          link
        >
          <v-list-item-icon>
            <v-icon>
              mdi-clipboard-text
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            Crews
            <!-- <router-link to="/invoices">
              Invoices
            </router-link> -->
          </v-list-item-content>
        </v-list-item>
        <v-list-item
          to="/schedule"
          link
        >
          <v-list-item-icon>
            <v-icon>
              mdi-clipboard-text
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            Schedule
            <!-- <router-link to="/invoices">
              Invoices
            </router-link> -->
          </v-list-item-content>
        </v-list-item>
        <v-list-item
          to="/invoices"
          link
        >
          <v-list-item-icon>
            <v-icon>
              mdi-clipboard-text
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            Invoices
            <!-- <router-link to="/invoices">
              Invoices
            </router-link> -->
          </v-list-item-content>
        </v-list-item>
        <v-list-item
          to="/configuration"
          link
        >
          <v-list-item-icon>
            <v-icon>
              mdi-tools
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            Configurations
            <!-- <router-link to="/invoices">
              Invoices
            </router-link> -->
          </v-list-item-content>
        </v-list-item>
        <!-- <v-list-item
          to="/login"
          link
        >
          <v-list-item-icon>
            <v-icon>
              mdi-clipboard-text
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            Log in
             <router-link to="/invoices">
              Invoices
            </router-link> -->
          <!-- </v-list-item-content>
        </v-list-item>

        <v-list-item
          link
          @click="logout"
        >
          <v-list-item-icon>
            <v-icon>
              mdi-clipboard-text
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            Logout
            <router-link to="/invoices">
              Invoices
            </router-link>
          </v-list-item-content>
        </v-list-item> -->
      </v-list>
    </v-navigation-drawer>
    <v-content>
      <v-container
        fluid
        class="fill-height">
        <v-btn
          v-if="authenticated"
          @click="privateMessage()">Check Private API Permissions</v-btn>

        {{ message }}
        <router-view />
        <notifications group="success" position="bottom right" :duration=1000 width='500'/>
        <notifications group="error" position="bottom right" :duration=2000 width='400'/>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Vue from 'vue'
import AuthService from './auth/AuthService'
import axios from 'axios'


const API_URL = 'http://127.0.0.1:8000/api/'
const auth = new AuthService()
export default {

  data() {
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
  mounted() {
this.checkLoggedIn();
console.log(this.$store.state.authenticated);
console.log(process.env.VUE_APP_API_URL)
  },
  methods: {

    checkLoggedIn() {
      if (this.$store.state.authenticated){
        this.authenticated = true;
      }
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

<style lang="scss" scoped>

.warn{

 &.success {
      background: #68CD86;
    }
    &.warn {
      background: #ffb648;
    }
    &.error {
      background: #E54D42;
    }
}
</style>

