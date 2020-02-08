<template >
  <v-app style="width: 100%;">
    <v-btn @click="back">Back</v-btn>
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="details">Details</v-tab>
      <v-tab key="expenses">Job Expenses</v-tab>
      <v-tab key="edit">Edit</v-tab>

      <v-tab-item key="details">
        ${{total}}
        <v-btn
          color="blue darken-1"
          text
          :disabled="completed"
          @click="completeJob"
        >Job Completed</v-btn>
        <v-dialog v-model="deleteDialog" max-width="400px">
                <template v-slot:activator="{ on }">
                  <v-btn color="red" dark class="mb-2" v-on="on">Delete</v-btn>
                </template>
                <v-card v-if="deleteDialog">
                  <div>
                    <v-card-text>
                      <span class="headline">Are you sure you want to delete this job?</span>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="red darken-1" text @click="deleteDialog = false">NO</v-btn>
                      <v-btn color="green darken-1" text @click="deleteJob">YES</v-btn>
                    </v-card-actions>
                  </div>
                </v-card>
              </v-dialog>
      </v-tab-item>

      <v-tab-item key="expenses">
        <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>
        <v-data-table
          :headers="headers"
          :items="expenses"
          :search="search"
          :items-per-page="10"
          class="elevation-1"
        >
          <template v-slot:top>
            <v-toolbar flat color="white">
              <v-toolbar-title>Expenses</v-toolbar-title>
              <v-divider class="mx-4" inset vertical></v-divider>
              <v-spacer></v-spacer>
              <v-dialog v-model="dialog" max-width="600px">
                <template v-slot:activator="{ on }">
                  <v-btn color="primary" dark class="mb-2" v-on="on">New Expense</v-btn>
                </template>
                <v-card v-if="dialog">
                  <div v-click-outside="close">
                    <v-card-title>
                      <span class="headline">{{ formTitle }}</span>
                    </v-card-title>

                    <v-card-text>
                      <v-container>
                        <v-form ref="form1" v-model="valid1">
                          <v-row>
                            <v-col cols="12">
                              <v-text-field
                                v-model="expense.name"
                                :counter="40"
                                :rules="[v => !!v || 'Name is required']"
                                label="Expense Name*"
                                required
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12">
                              <v-textarea v-model="expense.description" label="Expense Description"></v-textarea>
                            </v-col>
                            <v-col cols="12" sm="6">
                              <v-select
                                v-model="expense.job_expense_type"
                                :items="jobExpenseTypes"
                                name="job_expense_type"
                                item-text="job_expense_type"
                                :rules="[v => !!v || 'Expense type is required']"
                                label="Expense Type*"
                                required
                              ></v-select>
                            </v-col>
                            <v-col cols="12" sm="6">
                              <v-text-field
                                v-model="expense.cost"
                                type="number"
                                label="Expense Total*"
                                :rules="[v => !!v || 'Total is required']"
                              ></v-text-field>
                            </v-col>
                          </v-row>
                        </v-form>
                      </v-container>
                    </v-card-text>

                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="blue darken-1" text @click="saveExpense">{{formButton}}</v-btn>
                    </v-card-actions>
                  </div>
                </v-card>
              </v-dialog>
            </v-toolbar>
          </template>
          <template v-slot:item.action="{ item }">
            <v-icon color="blue" class="mr-2" @click="editExpense(item)">mdi-pen</v-icon>
            <v-icon color="red" @click="deleteExpense(item)">mdi-delete</v-icon>
          </template>
        </v-data-table>
      </v-tab-item>

      <v-tab-item key="edit">
        <v-form ref="form" v-model="jobEditValid">
          <span>Edit job information:</span>
          <v-text-field v-model="job.name" focus :counter="40" :rules="rule" label="Name" required></v-text-field>
          <v-textarea
            v-model="job.description"
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
          <v-btn :disabled="!jobEditValid" color="success" class="mr-4" @click="save">Save</v-btn>
        </v-form>
      </v-tab-item>
    </v-tabs>
  </v-app>
</template>

<script>
import axios from "axios";
import ClickOutside from "vue-click-outside";
// @ is an alias to /src
export default {
  name: "JobView",
  data() {
    return {
      completed: true,
      deleteDialog: false,
      dialog: false,
      id: null,
      search: null,
      total: 0,
      tempExpense: {},
      expense: {
        job: null,
        name: null,
        description: "",
        job_expense_type: null,
        cost: null
      },
      headers: [
        {
          text: "Expense Name",
          value: "name",
          align: "left"
        },
        { text: "Expense Description", align: "left", value: "description" },
        { text: "Cost", value: "cost" },
        { text: "Actions", align: "right", value: "action", sortable: false }
      ],
      valid1: null,
      expenses: [],
      job: {},
      jobTypes: [],
      jobExpenseTypes: [],
      rule: [
        v => !!v || "Required",
        v => (v && v.length <= 40) || "Entry must be less than 40 characters"
      ],
      valid: false,
      valid1: false,
      jobEditValid: false,
      editdialog: true,
      editedIndex: -1,
      closeCounter: 0
    };
  },
  created() {
    this.id = this.$route.params.id;
    this.expense.job = this.id;

    //get job data for this id
    axios
      .get(process.env.VUE_APP_API_URL + "job/" + this.id + "/")
      .then(response => {
        this.job = response.data;
        if (this.job.date_completed == null) {
          this.completed = false;
        }
      });
    //get job types for edit
    axios.get(process.env.VUE_APP_API_URL + "jobtype/").then(response => {
      if (response.data) {
        response.data.forEach(item => {
          this.jobTypes.push(item);
        });
      }
    });
    //get expense type for adding new expense
    axios
      .get(process.env.VUE_APP_API_URL + "jobexpensetype/")
      .then(response => {
        if (response.data) {
          response.data.forEach(item => {
            this.jobExpenseTypes.push(item);
          });
        }
      });
    //get each expense for this job
    axios
      .get(process.env.VUE_APP_API_URL + "expensesofjob?jobid=" + this.id)
      .then(response => {
        response.data.forEach(item => {
          this.expenses.push(item);
          this.total += parseFloat(item.cost);
        });
      });
    console.log(this.expenses);
  },
  mounted() {},
  directives: {
    ClickOutside
  },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Expense" : "Edit Expense";
    },
    formButton() {
      return this.editedIndex === -1 ? "Create Expense" : "Save";
    }
  },
  components: {},
  methods: {
    handleClick: function(value) {
      this.$router.push("/yard/" + this.id + "/" + value.yardid);
    },
    back: function() {
      this.$router.go(-1);
    },
    completeJob: function() {
      this.job.date_completed = new Date().toJSON().slice(0, 10);
      this.job.job_total = this.total;
      console.log(this.job);
      axios
        .put(process.env.VUE_APP_API_URL + "job/" + this.id + "/", this.job)
        .then(response => {
          this.job = response.data;
          console.log(this.job)
          this.$notify({
            group: "success",
            title: "Job has been marked as COMPLETED",
            type: "success"
          });
          if (this.job.date_completed != null) {
            this.completed = true;
          }
        });
    },
    deleteJob: function(){
        console.log(this.job)
        var yard = this.job.yard
        axios
        .delete(
          process.env.VUE_APP_API_URL + "job/" + this.id
        )
        .then(response => {
          this.$notify({
            group: "success",
            title: "Deleted Job Succesfully",
            type: "success"
          });
           this.$router.push("/yard/" + yard);
        })
        .catch(error => {
          if (error.response) {
            for (var prop in this.expense) {
              if (
                Object.prototype.hasOwnProperty.call(error.response.data, prop)
              ) {
                this.$notify({
                  group: "error",
                  title:
                    "Error deleting expense. " +
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
    //saving the job information
    save: function() {
      axios
        .put(process.env.VUE_APP_API_URL + "api/job/" + this.id + "/", this.job)
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
    },
    //this will create a new expense if index =-1, otherwise it will save the edited job expense
    saveExpense: function() {
      if (this.editedIndex === -1) {
        axios
          .post(process.env.VUE_APP_API_URL + "jobexpense/", this.expense)
          .then(response => {
            this.expenses.unshift(response.data);
            this.total += parseFloat(response.data.cost);
            this.dialog = false;
            this.$refs.form1.reset();
            console.log(this.expense);
            this.$notify({
              group: "success",
              title: "Add Job Expense Succesfully",
              type: "success"
            });
          })
          .catch(error => {
            if (error.response) {
              for (var prop in this.expense) {
                if (
                  Object.prototype.hasOwnProperty.call(
                    error.response.data,
                    prop
                  )
                ) {
                  this.$notify({
                    group: "error",
                    title:
                      "Error adding job expense." +
                      prop +
                      ": " +
                      error.response.data[prop],
                    type: "error"
                  });
                }
              }
            }
          });
          this.closeCounter++
      } else {
        axios
          .patch(
            process.env.VUE_APP_API_URL +
              "jobexpense/" +
              this.expense.job_expenseid +
              "/",
            this.expense
          )
          .then(response => {
            this.$notify({
              group: "success",
              title: "Saved Expense Information Succesfully",
              type: "success"
            });
            //if cost  changed fix total
            if (this.tempExpense.cost != response.data.cost) {
              this.total -= parseFloat(this.tempExpense.cost);
              this.total += parseFloat(response.data.cost);
            }
            this.expenses.splice(this.editedIndex, 1, response.data);
            this.$refs.form1.reset();
            this.dialog = false;
            this.editedIndex = -1;
            this.closeCounter++;
          })
          .catch(error => {
            if (error.response) {
              for (var prop in this.expense) {
                if (
                  Object.prototype.hasOwnProperty.call(
                    error.response.data,
                    prop
                  )
                ) {
                  this.$notify({
                    group: "error",
                    title:
                      "Error Saving Expense Information. " +
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
    },
    editExpense: function(item) {
      this.editedIndex = this.expenses.indexOf(item);
      this.tempExpense = this.expenses[this.editedIndex];
      this.expense.name = item.name;
      this.expense.description = item.description;
      this.expense.job_expense_type = item.job_expense_type;
      this.expense.cost = item.cost;
      this.expense.job_expenseid = item.job_expenseid;
      this.dialog = true;
    },
    deleteExpense: function(item) {
      axios
        .delete(
          process.env.VUE_APP_API_URL + "jobexpense/" + item.job_expenseid
        )
        .then(response => {
          this.$notify({
            group: "success",
            title: "Deleted Expense Succesfully",
            type: "success"
          });
          this.total -= item.cost;
          this.expenses.splice(this.expenses.indexOf(item), 1);
        })
        .catch(error => {
          if (error.response) {
            for (var prop in this.expense) {
              if (
                Object.prototype.hasOwnProperty.call(error.response.data, prop)
              ) {
                this.$notify({
                  group: "error",
                  title:
                    "Error deleting expense. " +
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
    close: function() {
      if (this.closeCounter % 2 == 1) {
        this.editedIndex = -1;
        this.$refs.form1.reset();
      }
      this.closeCounter++;
    }
  }
};
</script>