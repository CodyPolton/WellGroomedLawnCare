<template>
  <v-app style="width: 100%;">
    <v-btn @click="generateMowInvoices" color='primary'>Generate Mowing Invoices</v-btn>
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
          if(item.paid == false) 
            item.paid = "No"
          else item.paid = 'Yes'
          if(item.billed == false) 
            item.billed = "No"
          else item.billed = 'Yes'
          if(item.approved == false) 
            item.approved = "No"
          else item.approved = 'Yes'
          
          this.invoices.push(item);
        });
        console.log(this.invoices)
      }
    });
  },
  methods: {
      handleClick: function(value){
        this.$router.push('/invoice/' + value.invoiceid);

      },
      generateMowInvoices: function(){
        var date = new Date
        var month = date.getMonth()
        // Add this back in once developed
        // if(month == '0' ){
        //   month = '12'
        // } 
        month++
        console.log(month)
        
      }
  }
};
</script>