<template>
  <v-app style="width: 100%;">
    <v-btn @click="back">Back</v-btn>
    Yard id = {{yardid}}
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="details">Details</v-tab>
      <v-tab key="yards">Jobs</v-tab>
      <v-tab key="edit">Edit</v-tab>
      <v-tab-item key="details">hi</v-tab-item>
      <v-tab-item key="yards">
        <v-btn to="/addyard">Add Yard</v-btn>
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
        <v-form ref="form" v-model="valid">
          <span>Enter yard information:</span>
          <v-text-field
            v-model="yard.address"
            focus
            :counter="40"
            :rules="rule"
            label="Address"
            required
          ></v-text-field>
          <v-text-field
            v-model="yard.zip_code"
            :counter="5"
            :rule="[v => !!v || 'Zipcode is required']"
            type="number"
            label="Zip Code"
            required
          ></v-text-field>
          <v-text-field v-model="yard.city" :counter="40" :rules="rule" label="City" required></v-text-field>
          <v-select
            v-model="yard.state"
            :items="states"
            :rules="[v => !!v || 'State is required']"
            label="State"
            required
          ></v-select>
          <v-text-field
            v-model="yard.mow_price"
            :counter="5"
            type="number"
            label="Mow Price"
            required
          ></v-text-field>

          <v-btn :disabled="!valid" color="success" class="mr-4" @click="save">Save</v-btn>
        </v-form>
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
      accountid: null,
      yardid: null,
      yard: {},
      jobs: [],
      headers: [
        {
          text: "First Name",
          align: "left",
          sortable: false,
          value: "fname"
        },
        { text: "Last Name", align: "left", value: "lname" },
        { text: "Address", value: "address" },
        { text: "Phone Number", value: "phone" },
        { text: "Mow Cost", value: "mowcost" }
      ],
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
      valid: true,
      search: null
    };
  },
  name: "Yard",
  components: {},
  created() {
    this.yardid = this.$route.params.yardid;
    this.accountid = this.$route.params.accountid;

    axios
      .get("http://127.0.0.1:8000/api/yard/" + this.yardid + "/")
      .then(response => {
        console.log(response.data);
        this.yard = response.data;
        console.log(this.yard);
      });
  },
  methods: {
    back: function() {
      this.$router.go(-1);
    },
    handleClick: function(value) {
      this.$router.push("/yard/" + value.yardid);
    },
    save: function() {
      axios
        .put("http://127.0.0.1:8000/api/yard/" + this.yardid + "/", this.yard)
        .then(response => {
          if (response.data) {
            this.yard = response.data;
            this.$notify({
              group: "success",
              title: "Saved Yard Succesfully",
              type: "success"
            });
          }
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
                    "Error saving yard information. " +
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