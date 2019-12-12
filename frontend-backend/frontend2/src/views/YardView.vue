<template>
  <v-app>
    <v-btn @click="back">Back</v-btn>
    Yard id = {{id}}
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
          :items="yards"
          :search="search"
          :items-per-page="10"
          class="elevation-1"
          @click:row="handleClick"
        ></v-data-table>
      </v-tab-item>
      <v-tab-item key="edit">
        <v-form ref="form" v-model="valid">
          <span>Enter yard information:</span>
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
          <v-text-field v-model="mowprice" :counter="5" type="number" label="Mow Price" required></v-text-field>

          <v-btn :disabled="!valid" color="success" class="mr-4">Save</v-btn>
        </v-form>
      </v-tab-item>
    </v-tabs>
  </v-app>
</template>

<script>
// @ is an alias to /src
export default {
  data() {
    return {
      id: null,
      mowprice: null,
      state: null,
      city: null,
      zipcode: null,
      address: null,
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
    };
  },
  name: "Crews",
  components: {},
  created() {
    this.id = this.$route.params.id;
  },
  methods: {
    back: function() {
      this.$router.go(-1);
    }
  }
};
</script>