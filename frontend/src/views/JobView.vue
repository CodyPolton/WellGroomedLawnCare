<template>
  <v-app style="width: 100%; ">
    <v-btn @click="back">Back</v-btn>
    Yard id = {{yardid}}
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="details">Details</v-tab>
      <v-tab key="costs">Job Costs</v-tab>
      <v-tab key="edit">Edit</v-tab>
      <v-tab-item key="details">hi</v-tab-item>
      <v-tab-item key="costs">
        job costs
        <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>
        <v-data-table
          :headers="headers"
          :items="jobs"
          :search="search"
          :items-per-page="10"
          class="elevation-1"
          @click:row="handleClick"
        ></v-data-table>
      </v-tab-item>
      <v-tab-item key="edit">
        edit
      </v-tab-item>
    </v-tabs>
  </v-app>
</template>

<script>
import axios from "axios";
// @ is an alias to /src
export default {
  data() {
    return {
        
    }
  },
  methods: {
    back: function() {
      this.$router.go(-1);
    },
    handleClick: function(){

    }
  },
  created(){

  },
}
