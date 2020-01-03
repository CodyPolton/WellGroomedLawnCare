<template >
  <v-app style="width: 100%;">
    <v-btn @click="back">Back</v-btn>
    Accounts id = {{id}}
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="details">Details</v-tab>
      <v-tab key="costs">Job Costs</v-tab>
      <v-tab key="edit">Edit</v-tab>

      <v-tab-item key="details">hi</v-tab-item>

      <v-tab-item key="costs">
        
        <v-dialog v-model="dialog" max-width="600px">
          <template v-slot:activator="{ on }">
            <v-btn color="primary" dark v-on="on">Add Job Cost</v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">Create Expense</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="expense.name"
                      :counter="40"
                      :rules="[v => !!v || 'Name is required']"
                      label="Expense Name*"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <v-textarea
                      v-model="expense.description"
                      label="Job Description"
                    ></v-textarea>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-select
                      v-model="expense.job_type"
                      :items="jobTypes"
                      name="job_type"
                      item-text="job_type"
                      :rules="[v => !!v || 'Job type is required']"
                      label="Job Type*"
                      required
                    ></v-select>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field
            v-model="expense.cost"
            type="number"
            label="Expense Total*"
            required
          ></v-text-field>
                  </v-col>

                </v-row>
              </v-container>
              <small>*indicates required field</small>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" :disabled="valid" text @click="addJobCost">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>
        <v-data-table
          :headers="headers"
          :items="jobCosts"
          :search="search"
          :items-per-page="10"
          class="elevation-1"
          @click:row="handleClick"
        ></v-data-table>
      </v-tab-item>

      <v-tab-item key="edit">
        <v-form ref="form" v-model="valid1">
          <span>Edit job information:</span>
          <v-text-field
            v-model="job.name"
            focus
            :counter="40"
            :rules="rule"
            label="Name"
            required
          ></v-text-field>
          <v-textarea
                      v-model="job.description"
                      color="teal"
                      :rules="[v => !!v || 'Description is required']"
                      label="Job Description*"
                      required
                    ></v-textarea>
          <v-select
                      v-model="job.job_type"
                      :items="jobTypes"
                      name="job_type"
                      item-text="job_type"
                      :rules="[v => !!v || 'Job type is required']"
                      label="Job Type*"
                      required
                    ></v-select>
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
  name: "JobView",
  data() {
    return {
      dialog: false,
      id: null,
      search: null,
      expense: {
        name: null,
        description: null,
        
      },
      headers: [
        {
          text: "Expense Name",
          value: "address",
          align: "left"
        },
        { text: "Expense Description", align: "left", value: "city" },
        { text: "Cost", value: "zip_code" },
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
        mow_price: null
      },
      valid1: null,
      jobCosts: [],
      job: {},
      jobTypes: [],
      rule: [
        v => !!v || "Required",
        v => (v && v.length <= 40) || "Entry must be less than 40 characters"
      ],      
      valid: true
    };
  },
  created() {
    this.id = this.$route.params.id;
    this.yard.account = this.id;
    axios
      .get("http://127.0.0.1:8000/api/job/" + this.id + "/")
      .then(response => {
        console.log(response.data);
        this.job = response.data;
        console.log(this.job);
      });

    axios.get("http://127.0.0.1:8000/api/jobtype/").then(response => {
      if (response.data) {
        response.data.forEach(item => {
          this.jobTypes.push(item);
        });
      }
    });

    axios
      .get("http://127.0.0.1:8000/api/job/" + this.id)
      .then(response => {
        console.log(response.data);
        response.data.forEach(item => {
          this.jobCosts.push(item);
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
    save: function() {
      axios
        .put("http://127.0.0.1:8000/api/job/" + this.id + "/", this.job)
        .then(response => {
          this.job = response.data;
          this.$notify({
            group: "success",
            title: "Saved Job Information Succesfully",
            type: "success"
          });
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
                    "Error Saving Job Information. " +
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