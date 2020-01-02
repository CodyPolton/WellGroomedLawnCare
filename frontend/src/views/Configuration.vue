<template>
  <v-container>
    <v-layout>
      <v-flex>
        <v-expansion-panels>
          <v-expansion-panel>
            <v-expansion-panel-header>Job Types</v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-col cols="12">
                <v-text-field
                  v-model="add.job_type"
                  :append-outer-icon="add.job_type ? 'mdi-plus-box' : ''"
                  filled
                  clear-icon="mdi-close-circle"
                  clearable
                  label="Add Job Type"
                  type="text"
                  @click:append-outer="addJobType"
                ></v-text-field>
              </v-col>
              <v-list>
                <template v-for="(item) in jobType">
                  <v-list-item :key="item.job_type">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.job_type"></v-list-item-title>
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-btn text icon color="red" @click="deleteJobType(item.job_typeid)">
                        <v-icon>mdi-delete</v-icon>
                      </v-btn>
                    </v-list-item-action>
                  </v-list-item>
                </template>
              </v-list>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
// @ is an alias to /src
export default {
  name: "Configuration",
  components: {},
  data() {
    return {
      jobType: [],
      add: {
        job_type: ""
      },
    };
  },
  created() {
    axios.get("http://127.0.0.1:8000/api/jobtype/").then(response => {
      if (response.data) {
        response.data.forEach(item => {
          this.jobType.push(item);
        });
        console.log(this.jobType);
      }
    });
  },
  methods: {
    addJobType: function() {
      console.log("hi " + this.add.job_type);
      axios
        .post("http://127.0.0.1:8000/api/jobtype/", this.add)
        .then(response => {
          this.$notify({
            group: "success",
            title: "Added Job Type Succesfully",
            type: "success"
          });
          this.add.job_type = "";
          this.jobType.push(response.data);
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
                    "Error adding job type. " +
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
    deleteJobType: function(id) {
      console.log("adf " + id);
      axios
        .delete("http://127.0.0.1:8000/api/jobtype/" + id)
        .then(response => {
          this.$notify({
            group: "success",
            title: "Deleted Job Type Succesfully",
            type: "success"
          });
          this.jobType.pop(response.data);
        })
        .catch(error => {
          if (error.response) {
            for (var prop in this.jobType) {
              if (Object.prototype.hasOwnProperty.call(error.response.data, prop)) {
                this.$notify({
                  group: "error",
                  title:
                    "Error deleting job type. " +
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