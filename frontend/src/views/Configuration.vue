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

          <v-expansion-panel>
            <v-expansion-panel-header>Email Templates</v-expansion-panel-header>
            <v-expansion-panel-content>
              <h2>Notes:</h2>
              <p>The Greeting and Signature is automatically taken care of</p>
              <p>There are two variables you can place in the body. If you want to use the name tied to the account put $Name.
                If you want to use the previous month type $Month. This will get filled in with the previous month.</p>
              <p>Examples: "Hi $Name" will read in the email as Hi TestName (An actual name on a real invoice)<br>
                If it is March and you type this "This invoice is for $Month" it wil; read in the email "This invoice is for Febuary"</p>
              <v-expansion-panels>
                <v-expansion-panel>
                    <v-expansion-panel-header>Mowing Invoice Template</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <v-form ref="mowingForm" v-model="mowValid">
                          <v-row>
                            <v-col cols="12">
                              <v-text-field
                                v-model="mowingTemplate.subject"
                                :counter="255"
                                :rules="[v => !!v || 'Subject is required']"
                                label="Subject*"
                                required
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12">
                              <v-textarea v-model="mowingTemplate.body" :rules="[v => !!v || 'Body is required']" label="Body*" required></v-textarea>
                            </v-col>
                          </v-row>
                          <v-layout row wrap justify-end>
                            <v-flex shrink>
                              <v-btn right color="blue darken-1" :disabled='!mowValid' text @click="testTemplate(1)">Test</v-btn>
                              <v-btn right color="blue darken-1" :disabled='!mowValid' text @click="saveTemplate(1)">Save Template</v-btn>
                            </v-flex>
                          </v-layout>
                        </v-form>
                    </v-expansion-panel-content>
                </v-expansion-panel>
                <v-expansion-panel>
                    <v-expansion-panel-header>Individual Invoice Template</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <v-form ref="indivForm" v-model="indivValid">
                          <v-row>
                            <v-col cols="12">
                              <v-text-field
                                v-model="indivTemplate.subject"
                                :counter="255"
                                :rules="[v => !!v || 'Subject is required']"
                                label="Subject*"
                                required
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12">
                              <v-textarea v-model="indivTemplate.body" :rules="[v => !!v || 'Body is required']" label="Body*" required></v-textarea>
                            </v-col>
                          </v-row>
                          
                          <v-layout row wrap justify-end>
                            <v-flex shrink>
                              <v-btn right color="blue darken-1" :disabled='!indivValid' text @click="testTemplate(2)">Test</v-btn>
                              <v-btn right color="blue darken-1" :disabled='!indivValid' text @click="saveTemplate(2)">Save Template</v-btn>
                            </v-flex>
                          </v-layout>
                        </v-form>
                    </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
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
      mowingTemplate: {
        templateid: null,
        subject: null,
        body: null
      },
      mowValid: false,
      indivTemplate: {
        templateid: null,
        subject: null,
        body: null
      },
      indivValid: false,
    };
  },
  created() {
    axios.get(process.env.VUE_APP_API_URL + "jobtype/").then(response => {
      if (response.data) {
        response.data.forEach(item => {
          this.jobType.push(item);
        });
        console.log(this.jobType);
      }
    });

    axios.get(process.env.VUE_APP_API_URL + "jobexpensetype/").then(response => {
      if (response.data) {
        response.data.forEach(item => {
          this.jobExpenseType.push(item);
        });
        console.log(this.jobExpenseType);
      }
    });

    axios.get(process.env.VUE_APP_API_URL + "emailtemplates/1").then(response => {
      if (response.data) {
        this.mowingTemplate = response.data
      }
    });
    axios.get(process.env.VUE_APP_API_URL + "emailtemplates/2").then(response => {
      if (response.data) {
        this.indivTemplate = response.data
      }
    });

  },
  methods: {
    testTemplate: function(code){
      axios
        .get(
          process.env.VUE_APP_API_URL + "testtemplate?code=" + code
        )
        .then(response => {
          if (response.data) {
            this.$notify({
              group: "success",
              title: response.data.message,
              type: "success"
            });
          }
        })
        .catch(error => {
          if (error.response) {
            for (var prop in this.indivTemplate) {
              if (
                Object.prototype.hasOwnProperty.call(error.response.data, prop)
              ) {
                this.$notify({
                  group: "error",
                  title:
                    "Error saving template. " +
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
    saveTemplate: function(code){
      var template
      if(code == 1){
        template = this.mowingTemplate
      }else if (code == 2){
        template = this.indivTemplate
      }
      axios
        .put(
          process.env.VUE_APP_API_URL + "emailtemplates/" + code + "/",
          template
        )
        .then(response => {
          if (response.data) {
            this.$notify({
              group: "success",
              title: "Template Saved",
              type: "success"
            });
          }
        })
        .catch(error => {
          if (error.response) {
            for (var prop in this.indivTemplate) {
              if (
                Object.prototype.hasOwnProperty.call(error.response.data, prop)
              ) {
                this.$notify({
                  group: "error",
                  title:
                    "Error saving template. " +
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
    addJobType: function() {
      console.log("hi " + this.add.job_type);
      axios
        .post(process.env.VUE_APP_API_URL + "jobtype/", this.add)
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
        .delete(process.env.VUE_APP_API_URL + "jobtype/" + this.jobType[index].job_typeid)
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
        .post(process.env.VUE_APP_API_URL + "jobexpensetype/", this.add)
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
        .delete(process.env.VUE_APP_API_URL + "jobexpensetype/" + this.jobExpenseType[index].job_expense_typeid)
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