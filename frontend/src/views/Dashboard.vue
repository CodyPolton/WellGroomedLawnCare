<template>
  <v-container fluid class="fill-height">
    <v-layout class="align-center">
      <v-flex xs8 offset-xs2>
        <v-layout row class="d-flex">
          <v-flex xs12>
            <v-toolbar color="grey darken-3">
              <v-toolbar-title class="white--text display-1 font-weight-light">Management Dashboard</v-toolbar-title>
            </v-toolbar>
          </v-flex>
          <v-flex xs4>
            <v-btn
              v-if="group_level == 1"
              to="/accounts"
              color="primary"
              class="display-1 font-weight-light"
              link
              block
              tile
              height="200"
            >
              <v-layout row wrap class="d-flex justify-center">
                <v-flex xs2>
                  <v-icon x-large>mdi-account-multiple</v-icon>
                </v-flex>
                <v-flex xs12></v-flex>
                <v-flex xs8 pt-1>Accounts</v-flex>
              </v-layout>
            </v-btn>
          </v-flex>
          <v-flex xs4>
            <v-btn
              color="grey"
              class="display-1 font-weight-light white--text"
              to="/timesheets"
              link
              tile
              block
              height="200"
            >
              <v-layout row wrap class="d-flex justify-center">
                <v-flex xs2>
                  <v-icon x-large>mdi-clipboard-text</v-icon>
                </v-flex>
                <v-flex xs12></v-flex>
                <v-flex xs8 pt-1>Timesheets</v-flex>
              </v-layout>
            </v-btn>
          </v-flex>
          <v-flex xs4>
            <v-btn
              v-if="group_level <= 2"
              color="green darken-2"
              class="display-1 font-weight-light white--text"
              to="/crews"
              link
              tile
              block
              height="200"
            >
              <v-layout row wrap class="d-flex justify-center">
                <v-flex xs2>
                  <v-icon x-large>mdi-account-multiple</v-icon>
                </v-flex>
                <v-flex xs12></v-flex>
                <v-flex xs5 pt-1>Crews</v-flex>
              </v-layout>
            </v-btn>
          </v-flex>
          <v-flex xs4>
            <v-btn
              v-if="group_level == 1"
              color="grey darken-2"
              class="display-1 font-weight-light white--text"
              to="/schedules"
              link
              tile
              block
              height="200"
            >
              <v-layout row wrap class="d-flex justify-center">
                <v-flex xs2>
                  <v-icon x-large>mdi-calendar</v-icon>
                </v-flex>
                <v-flex xs12></v-flex>
                <v-flex xs8 pt-1>Schedules</v-flex>
              </v-layout>
            </v-btn>
          </v-flex>
          <v-flex xs4>
            <v-btn
              v-if="group_level == 1"
              color="green darken-4"
              class="display-1 font-weight-light white--text"
              to="/invoices"
              link
              tile
              block
              height="200"
            >
              <v-layout row wrap class="d-flex justify-center">
                <v-flex xs2>
                  <v-icon x-large>mdi-receipt</v-icon>
                </v-flex>
                <v-flex xs12></v-flex>
                <v-flex xs6 pt-1>Invoices</v-flex>
              </v-layout>
            </v-btn>
          </v-flex>
          <v-flex xs4>
            <v-btn
              v-if="group_level == 1"
              color="grey darken-4"
              class="display-1 font-weight-light white--text"
              to="/configuration"
              link
              tile
              block
              height="200"
            >
              <v-layout row wrap class="d-flex justify-center">
                <v-flex xs2>
                  <v-icon x-large>mdi-tools</v-icon>
                </v-flex>
                <v-flex xs12></v-flex>
                <v-flex xs10 pt-1>Configurations</v-flex>
              </v-layout>
            </v-btn>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: "Dashboard",

  data() {
    return {};
  },
  computed: {
    group_level: function() {
      return this.$store.state.group_level;
    },
    group_name: function() {
      return this.$store.state.group_name;
    }
  }
};
</script>
<style lang="stylus">
.feature-button {
  height: 100%;
}
</style>