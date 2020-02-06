<template>
  <v-app style="width: 100%; ">
    <v-btn @click="back">Back</v-btn>
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="timesheets">Timesheets</v-tab>
      <v-tab key="add">Add Time</v-tab>
      <v-tab-item key="timesheets" >
        
      </v-tab-item>
      <v-tab-item key="add">
        
      </v-tab-item>
    </v-tabs>
    
  </v-app>
</template>

<script>
import axios from "axios";
// @ is an alias to /src
export default {
  name: "Route",
  components: {},
  data() {
    return {
      crew: null,
      item: null,
      params: null,
      crewYards: [],
      routeYards: [],
      origin: "721 North Denninghoff Rd, Columbia, MO"
    };
  },
  created() {
    

    
  },
  mounted() {},
  methods: {
    back: function() {
      this.$router.go(-1);
    },

  }
};
</script>