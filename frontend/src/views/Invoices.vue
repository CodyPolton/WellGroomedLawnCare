<template>
  <v-app style="width: 100%;">
    <v-text-field 
      v-model="search" 
      append-icon="search" 
      label="Search" 
      single-line 
      hide-details></v-text-field>
    <v-data-table
      :headers="headers"
      :items="invoices"
      :search="search"
      :items-per-page="10"
      class="elevation-1"
      @click:row="handleClick"
    ></v-data-table>
  </v-app>
</template>

<script>
import axios from "axios";
// @ is an alias to /src
export default {
  name: "Invoices",
  components: {},
  data() {
    return {
      search: null,
      headers: [
        {
          text: "Invoice Name",
          align: "left",
          sortable: false,
          value: "invoice_name"
        },
        { text: "Type", value: "type" },
        { text: "Approved", value: "approved" },
        { text: "Total", value: "total_price" }
      ],
      invoices: [],
    };
  },
  created() {

      axios.get(process.env.VUE_APP_API_URL + "invoice/").then(response => {
      if (response.data) {
        response.data.forEach(item => {
          this.invoices.push(item);
        });
        console.log(this.invoices)
      }
    });
  },
  methods: {
      handleClick: function(value){
          console.log(value)
          this.$router.push('/invoice/' + value.invoiceid);

      },
  }
};
</script>