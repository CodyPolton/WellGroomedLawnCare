<template>
  <v-app style="width: 100%; heigth: 30px;">
    

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
          <v-btn color="blue darken-1"  text @click="addJob">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-app>
</template>

<script>
// @ is an alias to /src
import axios from "axios";

export default {
  name: "AddJob",
  data() {
    return {
        dialog: false,
      yardid: null,
      valid: null,
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
      }
    };
  },
  components: {},
  created() {
    this.yardid = this.$route.params.id;
    console.log(this.yardid)
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
    typeCallback: function(val) {
      console.log("hi");
      this.job.job_type = val;
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