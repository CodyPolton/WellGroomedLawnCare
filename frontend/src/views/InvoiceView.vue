<template>
  <v-app style="width: 100%;">
    <v-btn @click="back">Back</v-btn>
    <v-dialog v-model="deleteDialog" max-width="400px">
                <template v-slot:activator="{ on }">
                  <v-btn color="red" dark class="mb-2" v-on="on">Delete</v-btn>
                </template>
                <v-card v-if="deleteDialog">
                  <div>
                    <v-card-title class="headline">Delete Invoice</v-card-title>
                    <v-card-text>Are you sure you want to delete this Invoice?</v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="red darken-1" text @click="deleteDialog = false">NO</v-btn>
                      <v-btn color="green darken-1" text @click="deleteInvoice">YES</v-btn>
                    </v-card-actions>
                  </div>
                </v-card>
    </v-dialog>
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="details">View Invoice</v-tab>
      <v-tab-item>
        <div class="tab-item-wrapper">
          <v-btn color='red' @click="approve" v-if='!invoice.approved'>Approve</v-btn>
          <v-btn color='green'  @click="approve" v-if='invoice.approved'>Approved</v-btn>
          <v-btn color="red" v-if='invoice.approved && !invoice.billed' dark @click="emailDialog = true" >Email Invoice</v-btn>
          <v-dialog v-model="emailDialog" max-width="400px">
                <v-card v-if="emailDialog">
                  <div>
                     <v-card-title class="headline">Email Invoice</v-card-title>
                      <v-card-text>Are you sure you want to email this invoice to the customer?</v-card-text>
                      <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="red darken-1" text @click="emailDialog = false">NO</v-btn>
                      <v-btn color="green darken-1" text @click="emailInvoice">YES</v-btn>
                    </v-card-actions>
                  </div>
                </v-card>
    </v-dialog>
          <VueDocPreview :value="docValue" :type="type" />
        </div>
      </v-tab-item>

      <v-tab key="yards">Jobs</v-tab>
      <v-tab-item>Jobs
      <v-data-table
          :headers="headers"
          :items="jobs"
          :search="search"
          item-key="jobid"
          :items-per-page="10"
          class="elevation-1"
          @click:row="handleClick"
        >
        </v-data-table>
      </v-tab-item>
      <v-tab key="upload">Upload</v-tab>
      <v-tab-item>
        <input type="file" id="file" ref="file" v-on:change="onChangeFileUpload()"/>
        <button v-on:click="submitForm()">Upload</button>
        <!-- <v-btn color="dark-green" :disabled="!file" dark @click="invoiceOveride">Replace Invoice</v-btn> -->
      </v-tab-item>
    </v-tabs>
  </v-app>
</template>

<script>
import Vue from "vue";
import VueDocPreview from "vue-doc-preview";
import axios from "axios";

// @ is an alias to /src
export default {
  name: "InvoiceView",
  components: { VueDocPreview },
  data() {
    return {
      jobs: [],
      emailDialog: null,
      file: null,
      invoice: {
        invoiceid: null,
        approved: null,
        total_price: null,
        invoice_name: null,
        paid: null,
        billed: null,
      },
      deleteDialog: false,
      publicPath: process.env.BASE_URL,
      type: "office",
      docValue: "",
      id: null,
      search: null,
      headers: [
        {
          text: "Job Name",
          align: "left",
          value: "name"
        },
        { text: "Desciption", align: "middle", value: "description" },
        { text: "Job Type", value: "job_type" }
      ],
    };
  },
  created() {
    this.id = this.$route.params.id;

    axios
      .get(process.env.VUE_APP_API_URL + "invoice/" + this.id + "/")
      .then(response => {
        this.invoice = response.data;
        console.log(this.invoice);
        this.docValue =
          process.env.VUE_APP_S3_BUCKET +
          "Invoices/" +
          this.invoice.invoice_name;
        console.log(this.docValue);
      });

    axios
      .get(process.env.VUE_APP_API_URL + "invoicejobs?invoiceid=" + this.id)
      .then(response => {
        if (response.data) {
          response.data.forEach(item => {
            this.jobs.push(item);
          });
          console.log(this.jobs)
        }
      });
  },
  methods: {
    emailInvoice: function(){
      axios
        .post(process.env.VUE_APP_API_URL + "emailinvoice/", {invoice: this.invoice.invoiceid})
        .then(response => {
          this.$notify({
            group: "success",
            title: "Emailed Invoice Succesfully",
            type: "success"
          });
          this.emailDialog = false;
        })
        .catch(error => {
          if(error.response){
            console.log(error.response)
            var message = error.response.data.message
            if(error.response.status == 500){
              message = "500 Internal Server Error. Contact Admin"
            }
            this.$notify({
              group: "error",
              title: message,
              type: "error"
            });
          }
          this.emailDialog = false;
        });
    },
    approve: function(){
      if(this.invoice.approved){
        this.invoice.approved = false
      }
      else if(!this.invoice.approved){
        this.invoice.approved = true
      }
        axios
        .put(
          process.env.VUE_APP_API_URL + "invoice/" + this.id + "/",
          this.invoice
        )
        .then(response => {
          if (response.data) {
            this.invoice = response.data;
            if(this.invoice.approved){
              this.$notify({
                group: "success",
                title: "Invoice Approved",
                type: "success"
              });
            }
            else if(!this.invoice.approved){
              this.$notify({
                group: "success",
                title: "Invoice Unapproved",
                type: "success"
              });
            }
          }
        })
        .catch(error => {
          if (error.response) {
            for (var prop in this.invoice) {
              if (
                Object.prototype.hasOwnProperty.call(error.response.data, prop)
              ) {
                this.$notify({
                  group: "error",
                  title:
                    "Error approving Invoice. " +
                    prop +
                    ": " +
                    error.response.data[prop],
                  type: "error"
                });
              }
            }
          }
        });
    },
    back: function() {
      this.$router.go(-1);
    },
    handleClick: function(value) {
      console.log(value.jobid);
      this.$router.push("/job/" + value.jobid);
    },
    invoiceOveride: function() {
      console.log(this.file)
      var formData = new FormData();
      formData.append('file',this.file)
      formData.append('file_name', this.invoice.invoice_name)
      axios.post(process.env.VUE_APP_API_URL + "overideinvoice/", formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then({

      })
    },
    submitForm(){
            let formData = new FormData();
            console.log(this.file)
            formData.append('id', this.id)
            formData.append('file', this.file);
  
            axios.post(process.env.VUE_APP_API_URL + "overideinvoice/",
                formData,
                {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
              }
            ).then(data =>{
              this.$notify({
                group: "success",
                title: "The invoice has been overrided, please refresh the page",
                type: "success"
              });
            })
            .catch(error => {
              console.log('FAILURE!!');
              this.$notify({
                  group: "error",
                  title: 'Error overriding invoice, try again later or contact System Administration',
                  type: "error"
                });
            });
    },
    onChangeFileUpload() {
    this.file = this.$refs.file.files[0];
    },
    deleteInvoice: function(){
      console.log("delete Invoice")
      console.log(this.jobs)
     this.jobs.forEach(item => {
       console.log(item)
       item.invoiceid = ''
       item.invoiced = false
       axios
        .put(process.env.VUE_APP_API_URL + "job/" + item.jobid + "/", item)
        .then(response => {
          this.$notify({
            group: "success",
            title: "Job has the invoice removed from its record",
            type: "success"
          });
        });
     })
      axios.get(process.env.VUE_APP_API_URL + "deleteinvoice?invoiceid=" + this.id).then(response => {
      this.$notify({
            group: "success",
            title: "Invoice has been deleted!",
            type: "success"
          });
      this.$router.go(-1);
          
    }).catch(error => {
      
      this.$notify({
                  group: "error",
                  title: error.response.message,
                  type: "error"
                });
          
        });
      
      this.deleteDialog = false
    }
  }
};
</script>

<style>
</style>