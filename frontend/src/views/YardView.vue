<template>
  <v-app style="width: 100%; ">
    <v-btn @click="back">Back</v-btn>
    Yard id = {{yardid}}
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="details">Details</v-tab>
      <v-tab key="yards">Jobs</v-tab>
      <v-tab key="edit">Edit</v-tab>
      <v-tab-item key="details">hi</v-tab-item>
      <v-tab-item key="yards">
        <v-dialog v-model="dialog" max-width="600px">
      <template v-slot:activator="{ on }">
        <v-btn color="primary" dark v-on="on">Add Job</v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">Create Job</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  v-model="job.name"
                  :counter="40"
                  :rules="[v => !!v || 'Name is required']"
                  label="Job Name"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-textarea
                  v-model="job.description"
                  color="teal"
                  :rules="[v => !!v || 'Description is required']"
                  label="Job Description*"
                  required
                ></v-textarea>
              </v-col>
              <v-col cols="12" sm="6">
                <v-select
                  v-model="job.job_type"
                  :items="jobTypes"
                  name="job_type"
                  item-text="job_type"
                  :rules="[v => !!v || 'Job type is required']"
                  label="Job Type*"
                  required
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" :disabled='valid'  text @click="addJob">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
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
        <v-form ref="form" v-model="valid1">
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
import addJob from '../views/AddJob.vue'
// @ is an alias to /src
export default {
  data() {
    return {
      dialog: false,
      jobtypes: {
        job_typeid: null,
        job_type: null
      },
      jobTypes: [],
      job: {
        name: null,
        description: null,
        job_type: null,
        date_completed: null,
        job_total: null,
        billed: false,
        date_created: null,
        date_updated: null
      },
      accountid: null,
      yardid: null,
      yard: {},
      jobs: [],
      headers: [
        {
          text: "Job Name",
          align: "left",
          value: "name"
        },
        { text: "Desciption", align: "middle", value: "description" },
        { text: "Job Type", value: "job_type" },
      ],
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
      valid1: true,
      valid: false,
      search: null
    };
  },
  name: "Yard",
  components: {
    addJob
  },
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

    axios
      .get("http://127.0.0.1:8000/api/job/" + this.yardid + "/")
      .then(response => {
        console.log(response.data);
        this.yard = response.data;
        console.log(this.yard);
      });

      axios.get("http://127.0.0.1:8000/api/jobtype/").then(response => {
      if (response.data) {
        response.data.forEach(item => {
          this.jobTypes.push(item);
        });
        console.log(this.jobTypes);
      }
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
    },
    addJob: function() {
      console.log(this.job);

      axios
        .post("http://127.0.0.1:8000/api/job/", this.job)
        .then(response => {
          this.$notify({
            group: "success",
            title: "Added Job Succesfully",
            type: "success"
          });
          this.dialog = false;
        })
        .catch(error => {
          if (error.response) {
            for (var prop in this.job) {
              if (
                Object.prototype.hasOwnProperty.call(error.response.data, prop)
              ) {
                this.$notify({
                  group: "error",
                  title:
                    "Error adding job. " +
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