<template>
  <v-app>
    <v-btn @click="back">Back</v-btn>
    Inovice id = {{id}}
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="details">View Invoice</v-tab>
      <v-tab-item>view</v-tab-item>
      <v-tab key="yards">Jobs</v-tab>
      

    </v-tabs>
  </v-app>
</template>

<script>
// @ is an alias to /src
export default {
  data() {
    return {
      id: null,
      mowprice: null,
      state: null,
      city: null,
      zipcode: null,
      address: null,
      
    };
  },
  name: "Crews",
  components: {},
  created() {
    this.id = this.$route.params.id;
  },
  methods: {
    back: function() {
      this.$router.go(-1);
    }
  }
};
</script>