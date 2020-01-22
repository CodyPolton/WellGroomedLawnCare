<template>
  <v-container>
    <v-layout>
      <v-flex>
        <v-btn @click="back">Back</v-btn>
        <v-dialog v-model="dialog" max-width="600px">
          <template v-slot:activator="{ on }">
            <v-btn color="primary" dark v-on="on">Add Account</v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">Create Account</span>
            </v-card-title>
            <v-card-text>
              <small>*indicates required field</small>
              <v-container>
                <v-form ref="form" v-model="valid">
                  <v-row>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field
                        v-model="account.f_name"
                        :counter="40"
                        :rules="rule"
                        label="First Name*"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field
                        v-model="account.l_name"
                        :counter="40"
                        :rules="rule"
                        label="Last Name*"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="7" md="8">
                      <v-text-field
                        v-model="account.address"
                        :counter="40"
                        :rules="rule"
                        label="Address*"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="5" md="4">
                      <v-text-field
                        v-model="account.zip_code"
                        :counter="5"
                        :rules="zipRules"
                        type="number"
                        label="Zipcode*"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="7" md="8">
                      <v-text-field
                        v-model="account.city"
                        :counter="40"
                        :rules="rule"
                        label="City*"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="5" md="4">
                      <v-select
                        v-model="account.state"
                        :items="states"
                        :rules="[v => !!v || 'State is required']"
                        label="State*"
                        required
                      ></v-select>
                    </v-col>
                    <v-col cols="12">
                      <vue-tel-input v-model="account.phone_no" placeholder="Enter phone number"></vue-tel-input>
                    </v-col>
                    <v-col cols="12">
                      <v-text-field v-model="account.email" :counter="40" :rules="[]" label="Email"></v-text-field>
                    </v-col>
                    <v-col cols="12">
                      <v-checkbox v-model="account.auto_invoice" color="green">
                        <template v-slot:label>Automatic Invoices</template>
                      </v-checkbox>
                    </v-col>
                    <v-col cols="12">
                      <v-checkbox v-model="account.sameaddress" color="green">
                        <template v-slot:label>Does the account have a yard with the same address</template>
                      </v-checkbox>
                    </v-col>
                  </v-row>
                </v-form>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                :disabled="!valid"
                text
                @click="addAccount"
              >Create Account</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>
        <v-data-table
          :loading="loading"
          :headers="headers"
          :items="accounts"
          :search="search"
          :items-per-page="15"
          class="elevation-1"
          @click:row="handleClick"
        >
          <template
            v-slot:accounts.auto_invoice="{ item }"
          >{{ accounts.auto_invoice? 'true' : 'false' }}</template>
        </v-data-table>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";

// @ is an alias to /src
export default {
  data() {
    return {
      loading: false,
      dialog: null,
      account: {
        f_name: null,
        l_name: null,
        address: null,
        zip_code: null,
        city: null,
        state: null,
        phone_no: "",
        email: "",
        auto_invoice: false,
        sameaddress: null
      },
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
      valid: true,

      search: "",
      headers: [
        {
          text: "First Name",
          align: "left",
          value: "f_name"
        },
        { text: "Last Name", align: "left", value: "l_name" },
        { text: "Email", value: "email" },
        { text: "Phone Number", value: "phone_no" },
        { text: "Auto Invoices", value: "auto_invoice" }
      ],
      accounts: []
    };
  },
  created() {
    this.loading = true;
    console.log(process.env.VUE_APP_API_URL)
    axios
      .get(process.env.VUE_APP_API_URL + "account/")
      .then(response => {
        response.data.forEach(item => {
          if (item.auto_invoice) {
            item.auto_invoice = "YES";
          } else {
            item.auto_invoice = "NO";
          }
          this.accounts.push(item);
        });
        this.loading = false;
      })
      .catch(error => {
          this.$notify({
            group: "error",
            title: "Backend is down please contact your System adminstartor.",
            type: "error"
          });
      });
  },
  methods: {
    handleClick: function(value) {
      this.$router.push("/account/" + value.accountid);
    },
    back: function() {
      this.$router.go(-1);
    },
    addAccount: function() {
      var yard = {
        account: null,
        address: null,
        city: null,
        state: null,
        zip_code: null,
        mow_price: null
      };
      axios
        .post(process.env.VUE_APP_API_URL + "account/", this.account)
        .then(response => {
          this.$notify({
            group: "success",
            title: "Added Account Succesfully",
            type: "success"
          });
          if (response.data.auto_invoice) {
            response.data.auto_invoice = "YES";
          } else {
            response.data.auto_invoice = "NO";
          }
          yard.account = response.data.accountid;
          this.accounts.push(response.data);
          this.dialog = false;

          console.log(this.account);
          if (this.account.sameaddress) {
            console.log("same address");
            yard.address = this.account.address;
            yard.city = this.account.city;
            yard.state = this.account.state;
            yard.zip_code = this.account.zip_code;
            console.log(yard);
            axios
              .post(process.env.VUE_APP_API_URL + "yard/", yard)
              .then(response => {
                this.$notify({
                  group: "success",
                  title: "Added Yard Succesfully",
                  type: "success"
                });
              })
              .catch(error => {
                if (error.response) {
                  for (var prop in yard) {
                    if (
                      Object.prototype.hasOwnProperty.call(
                        error.response.data,
                        prop
                      )
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
            this.$refs.form.reset();
          }
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
                    "Error adding account. " +
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