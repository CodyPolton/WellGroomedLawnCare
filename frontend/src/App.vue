<template>
  <v-app>
   <v-app-bar
      v-if="!checkLoggedIn"
      app
      color="primary"
      dark
      dense
    >

      <v-toolbar-title>Well Groomed Lawn Care</v-toolbar-title>

      <v-spacer />

      <v-btn
        v-if="!checkLoggedIn"

        link
        to="/login"
      >
        Login
      </v-btn>

    </v-app-bar>

    <!-- Navbar once you are logged in for employees -->
    <v-app-bar
        v-if="checkLoggedIn"
      color="primary"
      dark
      app
      dense
    >
      <v-app-bar-nav-icon

        @click="drawer = !drawer" />

      <v-toolbar-title>Well Groomed Lawn Care Management</v-toolbar-title>

      <v-spacer />



      <v-btn
        v-if="checkLoggedIn"

        @click="logout()"
        link

      >Logout
      </v-btn>

    </v-app-bar>
    <v-navigation-drawer
        v-if="checkLoggedIn"
      v-model="drawer"
      app
      dark
      temporary
    >
      <v-list height="64">
        <v-list-item>
          <v-list-item-content class="pa-0">
            <v-list-item-title class="title">
              {{first_name}} {{last_name}}
            </v-list-item-title>
            <v-list-item-subtitle>
              {{group_name}}
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
          to="/timesheets"
          link
        >
          <v-list-item-icon>
            <v-icon>
              mdi-clipboard-text
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            Timesheets
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
          to="/schedules"
          link
        >
          <v-list-item-icon>
            <v-icon>
              mdi-clipboard-text
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            Schedule
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
          v-if='group_level == 1'
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

        <router-view />

    </v-content>
  </v-app>
</template>

<script>
import Vue from 'vue'




export default {

  data() {

    return {
      authenticated: false,
      message: '',
      drawer: false,
      items: [
        // {
        //   action: 'mdi-leaf',
        //   title: 'Lawn Care',
        //   active: false,
        //   items: [
        //     { title: 'test item 1' },
        //     { title: 'test item 2' },
        //     { title: 'test item 3' },
        //   ],
        // },
        // {
        //   action: 'mdi-content-cut',
        //   title: 'Landscaping',
        //   items: [
        //     { title: 'test item 1' },
        //   ],
        // },
      ],

    };
  },
  computed: {
    checkLoggedIn() {
return this.$store.getters.checkAuthentication;
    },
    first_name: function () {
      return this.$store.state.first_name
    },
    last_name: function (){
      return this.$store.state.last_name
    },
    group_level: function(){
      return this.$store.state.group_level
    },
    group_name: function(){
      return this.$store.state.group_name
    },
    
  },
  mounted() {
    console.log(this.$store.state.first_name)
  },
  methods: {
    logout(){
      this.$store.commit('logout')
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

