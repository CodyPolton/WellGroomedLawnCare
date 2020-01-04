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
                <template v-for="(item, index) in jobType">
                  <v-list-item :key="item.job_type">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.job_type"></v-list-item-title>
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-btn text icon color="red" @click="deleteJobType(index)">
                        <v-icon>mdi-delete</v-icon>
                      </v-btn>
                    </v-list-item-action>
                  </v-list-item>
                </template>
              </v-list>
            </v-expansion-panel-content>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-header>Job Expense Types</v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-col cols="12">
                <v-text-field
                  v-model="add.job_expense_type"
                  :append-outer-icon="add.job_expense_type ? 'mdi-plus-box' : ''"
                  filled
                  clear-icon="mdi-close-circle"
                  clearable
                  label="Add Job Expense Type"
                  type="text"
                  @click:append-outer="addJobExpenseType"
                ></v-text-field>
              </v-col>
              <v-list>
                <template v-for="(item, index) in jobExpenseType">
                  <v-list-item :key="item.job_expense_type">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.job_expense_type"></v-list-item-title>
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-btn text icon color="red" @click="deleteJobExpenseType(index)">
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
      jobExpenseType: [],
      add: {
        job_type: "",
        job_expense_type: ""
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

    axios.get("http://127.0.0.1:8000/api/jobexpensetype/").then(response => {
      if (response.data) {
        response.data.forEach(item => {
          this.jobExpenseType.push(item);
        });
        console.log(this.jobExpenseType);
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
            for (var prop in this.add) {
              if (
                Object.prototype.hasOwnProperty.call(error.response.data, prop)
              ) {
                this.$notify({
                  group: "error",
                  title:
                    "Error adding job  expense type. " +
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
    deleteJobType: function(index) {
      console.log(this.jobType[index]);
      axios
        .delete("http://127.0.0.1:8000/api/jobtype/" + this.jobType[index].job_typeid)
        .then(response => {
          this.$notify({
            group: "success",
            title: "Deleted Job Type Succesfully",
            type: "success"
          });
          console.log(this.jobType.indexOf(response.data))
          this.jobType.splice(index, 1);
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
    },
    addJobExpenseType: function() {
      console.log("hi " + this.add.job_expense_type);
      axios
        .post("http://127.0.0.1:8000/api/jobexpensetype/", this.add)
        .then(response => {
          this.$notify({
            group: "success",
            title: "Added Job Expense Type Succesfully",
            type: "success"
          });
          this.add.job_expense_type = "";
          this.jobExpenseType.push(response.data);
        })
        .catch(error => {
          if (error.response) {
            for (var prop in this.add) {
              if (
                Object.prototype.hasOwnProperty.call(error.response.data, prop)
              ) {
                this.$notify({
                  group: "error",
                  title:
                    "Error adding job expense type. " +
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
    deleteJobExpenseType: function(index) {
      console.log(this.jobExpenseType[index]);
      axios
        .delete("http://127.0.0.1:8000/api/jobexpensetype/" + this.jobExpenseType[index].job_expense_typeid)
        .then(response => {
          this.$notify({
            group: "success",
            title: "Deleted Job Expense Type Succesfully",
            type: "success"
          });
          this.jobExpenseType.splice(index, 1);
        })
        .catch(error => {
          if (error.response) {
            for (var prop in this.jobExpenseType) {
              if (Object.prototype.hasOwnProperty.call(error.response.data, prop)) {
                this.$notify({
                  group: "error",
                  title:
                    "Error deleting job expense type. " +
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