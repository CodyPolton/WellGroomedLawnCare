<template>
  <v-app>
    <v-btn @click="back">Back</v-btn>
    Inovice id = {{id}}
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="details">View Invoice</v-tab>
      <v-tab-item >
        <div class="tab-item-wrapper" >
         <VueDocPreview :value='docValue' :type="type" /> 
        </div>
      </v-tab-item>
      <v-tab key="yards">Jobs</v-tab>
      

    </v-tabs>
  </v-app>
</template>

<script>
import Vue from 'vue';
import VueDocPreview from 'vue-doc-preview'

   
// @ is an alias to /src
export default {
  data() {
    return {
      publicPath: process.env.BASE_URL,
      type: 'office',
      docValue: '',
      id: null,
      mowprice: null,
      state: null,
      city: null,
      zipcode: null,
      address: null,
      
    };
  },
  name: "InvoiceView",
  components: {VueDocPreview},
  created() {
    this.id = this.$route.params.id;
    this.docValue =  'https://www.codypolton.com/InvoiceTemplate.docx'
    console.log(this.docValue)

  },
  methods: {
    back: function() {
      this.$router.go(-1);
    },
  }
};
</script>

<style>
</style>