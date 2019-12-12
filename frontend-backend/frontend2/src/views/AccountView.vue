<template>
  <v-app>
      <v-btn @click='back'>Back</v-btn>
    Accounts id = {{id}}
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="details">Details</v-tab>
      <v-tab key="yards">Yards</v-tab>
      <v-tab key="invoice">Invoices</v-tab>
      <v-tab key="edit">Edit</v-tab>
      <v-tab-item key="details">hi</v-tab-item>
      <v-tab-item key="yards">
        <v-btn to="/addyard">Add Yard</v-btn>
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
        <v-text-field v-model="fname" :counter="40" :rules="rule" label="First Name" required></v-text-field>
        <v-text-field v-model="lname" :counter="40" :rules="rule" label="Last Name" required></v-text-field>
        <v-text-field v-model="address" :counter="40" :rules="rule" label="Address" required></v-text-field>
        <v-text-field
          v-model="zipcode"
          :counter="5"
          :rules="zipRules"
          type="number"
          label="Zip Code"
          required
        ></v-text-field>
        <v-text-field v-model="city" :counter="40" :rules="rule" label="City" required></v-text-field>
        <v-select
          v-model="state"
          :items="states"
          :rules="[v => !!v || 'State is required']"
          label="State"
          required
        ></v-select>
        <vue-tel-input v-model="phone" placeholder="Enter phone number"></vue-tel-input>
        <v-text-field v-model="email" :counter="40" :rules="[]" label="Email"></v-text-field>
        <v-checkbox v-model="auto" color="green">
          <template v-slot:label>Automatic Invoices</template>
        </v-checkbox>
        <v-checkbox v-model="sameaddress" color="green">
          <template v-slot:label>Does the account have a yard with the same address</template>
        </v-checkbox>

        <v-btn :disabled="!valid" color="success" class="mr-4">Save</v-btn>
      </v-tab-item>
    </v-tabs>
  </v-app>
</template>

<script>
// @ is an alias to /src
export default {
  name: "AccountView",
  data() {
    return {
      id: null,
      search: null,
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
      yards: [
        {
          fname: "Cody",
          lname: "Polton",
          address: "812 Cambridge dr.",
          phone: "5734893326",
          mowcost: "25",
          id: "1"
        }
      ],
      address: "812 Cambridge Dr.",
      city: "Columbia",
      state: "MO",
      zipcode: 65203,
      phone: "5732223366",
      fname: "Test",
      lname: "Name",
      email: "test@gmail.com",
      auto: true,
      sameaddress: null,
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
  created() {
    this.id = this.$route.params.id;
  },
  components: {},
  methods: {
      handleClick: function(value){
          this.$router.push('/yard/' + value.id);
      },
      back: function(){
          this.$router.go(-1)
      }
  }
};
</script>