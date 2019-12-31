<template>
  <v-app style="width: 100%;">
    <v-btn @click="back">Back</v-btn>
    <v-form ref="form" v-model="valid">
      <span>Enter job information:</span>
      <v-text-field
        v-model="job.name"
        :counter="40"
        :rules="[v => !!v || 'Name is required']"
        label="Job Name"
        required
      ></v-text-field>
      <v-col cols="12">
        <v-textarea
          v-model="job.description"
          color="teal"
          :rules="[v => !!v || 'Description is required']"
          label="Job Description"
          required
        ></v-textarea>
      </v-col>
      <v-select
        v-model="job.job_type"
        :items="jobTypes"
        name="job_type"
        item-text="job_type"
        :rules="[v => !!v || 'Job type is required']"
        label="Job Type"
        required
      ></v-select>

      <v-btn :disabled="!valid" color="success" class="mr-4" @click="addJob">Create Job</v-btn>
    </v-form>

    <v-dialog v-model="dialog"  max-width="600px">
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
                <v-text-field label="Job Name*" required></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-textarea label="Job Description*" required></v-textarea>
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
          <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click="dialog = false">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-app>
</template>

<script>
// @ is an alias to /src
import axios from "axios";

export default {
  dialog: false,
  name: "AddJob",
  data() {
    return {
      yardid: null,
      valid: null,
      jobTypes: [],
      job: {
        name: null,
        description: null,
        type: null
      }
    };
  },
  components: {},
  created() {
    this.yardid = this.$route.params.id;
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
    addJob: function() {
      console.log(this.yard);
      axios
        .post("http://127.0.0.1:8000/api/job/", this.yard)
        .then(response => {
          this.$notify({
            group: "success",
            title: "Added Yard Succesfully",
            type: "success"
          });
          this.$router.replace("/account/" + this.yard.account);
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
    }
  }
};
</script>