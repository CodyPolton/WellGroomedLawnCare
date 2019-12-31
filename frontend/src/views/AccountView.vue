<template >
  <v-app style="width: 100%;">
    <v-btn @click="back">Back</v-btn>
    Accounts id = {{id}}
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="details">Details</v-tab>
      <v-tab key="yards">Yards</v-tab>
      <v-tab key="invoice">Invoices</v-tab>
      <v-tab key="edit">Edit</v-tab>

      <v-tab-item key="details">hi</v-tab-item>

      <v-tab-item key="yards">
        <v-btn @click="addYard">Add Yard</v-btn>
        <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>
        <v-data-table
          :headers="headers"
          :items="yards"
          :search="search"
          :items-per-page="10"
          class="elevation-1"
          @click:row="handleClick"
        ></v-data-table>
      </v-tab-item>

      <v-tab-item key="invoices">Invoices</v-tab-item>

      <v-tab-item key="edit">
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
          :rules="zipRules"
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
      false: false,
      id: null,
      search: null,
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
      yards: [],
      account: {},
      states: [
        "MO",        "AL",        "AK",        "AZ",        "AR",        "CA",        "CO",        "CT",
        "DE",        "FL",        "GA",        "HI",        "ID",        "IL",        "IN",        "IA",
        "KS",        "KY",        "LA",        "ME",        "MD",        "MA",        "MI",        "MN",
        "MS",        "MT",        "NE",        "NV",        "NH",        "NJ",        "NM",        "NY",
        "NC",        "ND",        "OH",        "OK",        "OR",        "PA",        "RI",        "SC",
        "SD",        "TN",        "TX",        "UT",        "VT",        "VA",        "WA",        "WV",
        "WI",        "WY"
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
  created() {
    this.id = this.$route.params.id;
    axios
      .get("http://127.0.0.1:8000/api/account/" + this.id + "/")
      .then(response => {
        console.log(response.data);
        this.account = response.data;
        console.log(this.account);
      });

    axios
      .get("http://127.0.0.1:8000/api/accountsyards?id=" + this.id)
      .then(response => {
        console.log(response.data);
        response.data.forEach(item => {
          this.yards.push(item);
        });
      });
  },
  mounted() {},
  components: {},
  methods: {
    handleClick: function(value) {
      this.$router.push("/yard/" + this.id + "/" + value.yardid);
    },
    back: function() {
      this.$router.go(-1);
    },
    addYard: function() {
      this.$router.replace("/addyard/" + this.id);
    },
    save: function() {
      axios
        .put("http://127.0.0.1:8000/api/account/" + this.id + "/", this.account)
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