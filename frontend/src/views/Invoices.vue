<template>
  <v-app style="width: 100%;">
    <loading :active.sync="mowloading" 
        :is-full-page="fullPage"></loading>
    <v-btn @click="confirmMowDialog = true" color='primary'>Generate Mowing Invoices</v-btn>
        <v-dialog v-model="confirmMowDialog"  max-width="400">
          <v-card>
            <v-card-title class="headline">Monthly Invoice Generater</v-card-title>
            <v-card-text>Are you sure you want to generate last month's invoices? This can not be undone! You will have to manually delete all of the generated invoices if this is a mistake.</v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="red darken-1" text @click="confirmMowDialog = false">No</v-btn>
              <v-btn
                color="green darken-1"
                text
                @click="generateMowInvoices(); confirmMowDialog = false"
              >Generate Invoices</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
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
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';
export default {
  name: "Invoices",
  components: {
    Loading
  },
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
      confirmMowDialog: false,
      mowloading: false,
      fullPage: true,
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
        this.mowloading = true
        var date = new Date
        var month = date.getMonth()
        if(month == '0' ){
          //month = '12'
        } 
        month++
        console.log(month)

        axios
        .get(
          process.env.VUE_APP_API_URL + "mowinginvoices?month=" + month
        )
        .then(response => {
          if (response.data) {
            this.yard = response.data;
            this.$notify({
              group: "success",
              title: "Finished Generating Invoices",
              type: "success"
            });
            this.mowloading = false;
          }
        })
        .catch(error => {
          if (error.response) {
            console.log(error.response)
            this.$notify({
              group: "error",
              title: error.response.data.message,
              type: "error"
            });
            this.mowloading = false;
          }
        });
        
      }
  }
};
</script>