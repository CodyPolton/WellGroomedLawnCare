<template >
  <v-app>

    <v-tabs  background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="details" name='Details'>Details</v-tab>
      <v-tab key="yards" name='Yards'>Yards</v-tab>
      <v-tab key="invoice" name='Invoices'>Invoices</v-tab>
      <v-tab key="edit" name='Edit'>Edit</v-tab>

      <v-tab-item key="details">

        <v-layout row wrap class="d-flex align-center my-5 py-5">
          <v-flex xs6 offset-xs4 >
                        <v-layout row wrap>


                <v-flex xs4 offset-xs2 class="text-center headline">
                  <v-card class="pa-5">
Balance: ${{account.balance}}
                  </v-card>

                </v-flex>
                <v-flex xs12 class="mt-5"></v-flex>
                <v-flex xs4 offset-xs2 class="d-flex justify-center">
<v-dialog v-model="dialog1" max-width="400px">
          <template v-slot:activator="{ on }">
            <v-btn color="blue" dark v-on="on">Make Payment</v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">Payment amount</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-form ref="form1" v-model="valid2">
                  <v-row>
                    <v-col cols="12" sm="5" md="8">
                      <v-text-field
                        v-model="payment"
                        :rules="rule"
                        type="number"
                        label="Payment Amount"
                        required
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-form>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" :disabled='!valid2' text @click="makePayment">Make Payment</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
                </v-flex>



                          </v-layout>
          </v-flex>
        </v-layout>


      </v-tab-item>

      <v-tab-item key="yards">
        <v-layout row wrap>
          <v-flex xs10 offset-xs1 class="mt-5">
<v-dialog v-model="dialog" max-width="600px">
          <template v-slot:activator="{ on }">
            <v-btn color="primary" dark v-on="on">Add Yard</v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">Yard Information</span>
            </v-card-title>
            <v-card-text>
              <small>*indicates required field</small>
              <v-container>
                <v-form ref="form1" v-model="valid1">
                  <v-row>
                    <v-col cols="12" sm="7" md="8">
                      <v-text-field
                        v-model="yard.address"
                        :counter="40"
                        :rules="rule"
                        label="Address*"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="5" md="4">
                      <v-text-field
                        v-model="yard.zip_code"
                        :counter="5"
                        :rules="zipRules"
                        type="number"
                        label="Zipcode*"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="7" md="8">
                      <v-text-field v-model="yard.city" :counter="40" :rules="rule" label="City*"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="5" md="4">
                      <v-select
                        v-model="yard.state"
                        :items="states"
                        :rules="[v => !!v || 'State is required']"
                        label="State*"
                        required
                      ></v-select>
                    </v-col>
                    <v-col cols="12" sm="5" md="4">
                      <v-text-field
                        v-model="yard.mow_price"
                        :counter="6"
                        type="number"
                        label="Mow Price"
                        required
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-form>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" :disabled='!valid1' text @click="addYard">Add Yard</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-text-field filled v-model="search" append-icon="mdi-magnify" label="Search" single-line class="mt-5" hide-details></v-text-field>
        <v-data-table
          :loading="loading"
          :headers="headers"
          :items="yards"
          :search="search"
          :items-per-page="10"
          class="elevation-1"
          @click:row="handleClick"
        ></v-data-table>
          </v-flex>
        </v-layout>

      </v-tab-item>

      <v-tab-item key="invoices">
                <v-layout row wrap mt-5 pt-5>
          <v-flex xs10 offset-xs1>
<v-data-table
      :headers="invoiceheaders"
      :items="invoices"
      :search="invoicesearch"
      :items-per-page="10"
      class="elevation-1"
      @click:row="handleInvoiceClick"
    ></v-data-table>
          </v-flex>
        </v-layout>
      </v-tab-item>

      <v-tab-item key="edit">
<v-layout row wrap mt-5 pt-5>
<v-flex xs10 offset-xs1>
<v-form ref="form" v-model="valid">
          <v-text-field
            v-model="account.f_name"
            ref="name"
            :counter="40"
            :rules="rule"
            autofocus
            label="First Name"
            required
          ></v-text-field>
          <v-text-field
            v-model="account.l_name"
            :counter="40"
            :rules="rule"
            label="Last Name"
            required
          ></v-text-field>
          <v-text-field
            v-model="account.address"
            :counter="40"
            :rules="rule"
            label="Address"
            required
          ></v-text-field>
          <v-text-field
            v-model="account.zip_code"
            :counter="5"
            :rules="[v => !!v || 'Zipcode is required']"
            type="number"
            label="Zip Code"
            required
          ></v-text-field>
          <v-text-field v-model="account.city" :counter="40" :rules="rule" label="City" required></v-text-field>
          <v-select
            v-model="account.state"
            :items="states"
            :rules="[v => !!v || 'State is required']"
            label="State"
            required
          ></v-select>
          <vue-tel-input v-model="account.phone_no" placeholder="Enter phone number"></vue-tel-input>
          <v-text-field v-model="account.email" :counter="40" :rules="[]" label="Email"></v-text-field>
          <v-checkbox v-model="account.auto_invoice" color="green">
            <template v-slot:label>Automatic Invoices</template>
          </v-checkbox>
          <v-btn :disabled="!valid" color="success" class="mr-4" @click="save">Save</v-btn>
          <v-btn  color="red" class="mr-4" @click="deleteAccount">Delete Account</v-btn>
        </v-form>
</v-flex>
</v-layout>

      </v-tab-item>
    </v-tabs>
  </v-app>
</template>

<script>
import axios from "axios";
// @ is an alias to /src
export default {
  name: "AccountView",
  data() {
    return {
      invoicesearch: null,
      invoices: [],
      loading: false,
      dialog: false,
      dialog1: false,
      id: null,
      search: null,
      payment: null,
      headers: [
        {
          text: "Address",
          value: "address",
          align: "left"
        },
        { text: "City", align: "left", value: "city" },
        { text: "Zip Code", value: "zip_code" },
        { text: "State", value: "state" },
        { text: "Mow Price", value: "mow_price" }
      ],
      invoiceheaders: [
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
      yardtemp: {
        account: '',
        address: '',
        city: '',
        state: '',
        zip_code: '',
        mow_price: ''
      },
      yard: {
        account: null,
        address: null,
        city: null,
        state: null,
        zip_code: null,
        mow_price: null,
        days: ['None']
      },
      valid1: null,
      valid2: null,
      yards: [],
      account: {},
      states: [
        "MO",
        "AL",
        "AK",
        "AZ",
        "AR",
        "CA",
        "CO",
        "CT",
        "DE",
        "FL",
        "GA",
        "HI",
        "ID",
        "IL",
        "IN",
        "IA",
        "KS",
        "KY",
        "LA",
        "ME",
        "MD",
        "MA",
        "MI",
        "MN",
        "MS",
        "MT",
        "NE",
        "NV",
        "NH",
        "NJ",
        "NM",
        "NY",
        "NC",
        "ND",
        "OH",
        "OK",
        "OR",
        "PA",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VT",
        "VA",
        "WA",
        "WV",
        "WI",
        "WY"
      ],
      rules: {
        required: value => !!value || "Required."
      },
      rule: [
        v => !!v || "Required",
        v => (v && v.length <= 40) || "Entry must be less than 40 characters"
      ],
      zipRules: [
        v => !!v || "Required",
        v => (v && v.length == 5) || "Zip code must be 5 numbers"
      ],
      valid: true
    };
  },
  computed: {

  },
  created() {
    this.id = this.$route.params.id;
    this.yard.account = this.id;
    this.loading = true;
    axios
      .get(process.env.VUE_APP_API_URL + "account/" + this.id + "/")
      .then(response => {
        console.log(response.data);
        this.account = response.data;
        console.log(this.account);
      });

    axios
      .get(process.env.VUE_APP_API_URL + "accountsyards?id=" + this.id)
      .then(response => {
        console.log(response.data);
        response.data.forEach(item => {
          this.yards.push(item);
        });
      });

    axios.get(process.env.VUE_APP_API_URL + "accountinvoices?id=" + this.id).then(response => {
      if (response.data) {

        response.data.forEach(item => {
          console.log(item)
          this.invoices.push(item);
        });
        console.log(this.invoices)
      }
    });
    this.loading = false
  },
  mounted() {},
  components: {},
  methods: {
    handleClick: function(value) {
      this.$router.push("/yard/" + this.id + '/' + value.yardid);
    },
    handleInvoiceClick: function(value){
      this.$router.push('/invoice/' + value.invoiceid)
    },
    makePayment: function(){
      this.account.balance = parseInt(this.account.balance) + this.payment
        axios
        .put(process.env.VUE_APP_API_URL + "account/" + this.id + "/", this.account)
        .then(response => {
          this.account = response.data;
          this.$notify({
            group: "success",
            title: "Payment Accounted for Succesfully",
            type: "success"
          });
          this.dialog1 = false
          this.payment = null
        })
        .catch(error => {
          if (error.response) {
            for (var prop in this.account) {
              if (
                Object.prototype.hasOwnProperty.call(error.response.data, prop)
              ) {
                this.$notify({
                  group: "error",
                  title:
                    "Error Making Payment. " +
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
    addYard: function() {
      console.log(this.yard);
      axios
        .post(process.env.VUE_APP_API_URL + "yard/", this.yard)
        .then(response => {
          this.$notify({
            group: "success",
            title: "Added Yard Succesfully",
            type: "success"
          });
          this.yards.unshift(response.data);
          this.dialog = false;
          this.$refs.form1.reset()
        })
        .catch(error => {
          if (error.response) {
            for (var prop in this.yard) {
              if (
                Object.prototype.hasOwnProperty.call(error.response.data, prop)
              ) {
                this.$notify({
                  group: "error",
                  title:
                    "Error adding yard. " +
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
    deleteAccount: function() {
        axios
        .delete(
          process.env.VUE_APP_API_URL + "account/" + this.id
        )
        .then(response => {
          this.$notify({
            group: "success",
            title: "Deleted Account Succesfully",
            type: "success"
          });
           this.$router.push("/accounts/");
        })
        .catch(error => {
          if (error.response) {
            for (var prop in this.expense) {
              if (
                Object.prototype.hasOwnProperty.call(error.response.data, prop)
              ) {
                this.$notify({
                  group: "error",
                  title:
                    "Error deleting account. " +
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
    save: function() {
      axios
        .put(process.env.VUE_APP_API_URL + "account/" + this.id + "/", this.account)
        .then(response => {
          this.account = response.data;
          this.$notify({
            group: "success",
            title: "Saved Account Information Succesfully",
            type: "success"
          });
        })
        .catch(error => {
          if (error.response) {
            for (var prop in this.account) {
              if (
                Object.prototype.hasOwnProperty.call(error.response.data, prop)
              ) {
                this.$notify({
                  group: "error",
                  title:
                    "Error Saving Account Information. " +
                    prop +
                    ": " +
                    error.response.data[prop],
                  type: "error"
                });
              }
            }
          }
        });
    }
  }
};
</script>