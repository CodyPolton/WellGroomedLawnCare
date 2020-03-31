<template>
  <v-container mt-5 pt-5>
    <v-layout row wrap>
      <v-flex xs8 offset-xs2 >
<v-card flat>
      <v-container pt-5>
<v-layout row wrap pa-3 ma-3>

          <v-flex xs6 offset-xs3>
              <v-card outlined tile color="green darken-2" class=" white--text headline pa-2 text-center">
                  Contact Us
              </v-card>
          </v-flex>
          <v-flex xs4></v-flex>
          <v-flex xs6 offset-xs3>
              <v-card tile raised class="pa-4" color="grey darken-3" height="300">
                  <v-layout row wrap px-5>
                      <v-flex xs12>
                          <v-card color="green">
                              <v-card-title class="white--text font-weight-light mb-2 pa-2">Phone#</v-card-title></v-card>
                      </v-flex>
                                            <v-flex xs12>
                          <v-card color="green">
                              <v-card-title class="white--text font-weight-light mb-2 pa-2">Filler</v-card-title></v-card>
                      </v-flex>
                                            <v-flex xs12>
                          <v-card color="green">
                              <v-card-title class="white--text font-weight-light mb-2 pa-2">Filler</v-card-title></v-card>
                      </v-flex>
                                            <v-flex xs12>
                          <v-card color="green">
                              <v-card-title class="white--text font-weight-light mb-2 pa-2">Filler</v-card-title></v-card>
                      </v-flex>
                                            <v-flex xs12>
                          <v-card color="green">
                              <v-card-title class="white--text font-weight-light mb-2 pa-2">Filler</v-card-title></v-card>
                      </v-flex>
                  </v-layout>
                   </v-card>
          </v-flex>
</v-layout>
  </v-container>
      </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import router from '../router';

export default {
    name: 'Contact',

  data() {
    return {
    credentials: {
      username: "TestCrewLead",
      password: "Groomed1!"
    },
    };
  },
  methods: {

  }
};
</script>