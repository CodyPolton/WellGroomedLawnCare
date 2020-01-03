<template >
  <v-app style="width: 100%;">
    <v-btn @click="back">Back</v-btn>
    Accounts id = {{id}}
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="details">Details</v-tab>
      <v-tab key="expenses">Job Expenses</v-tab>
      <v-tab key="edit">Edit</v-tab>

      <v-tab-item key="details">${{total}}</v-tab-item>

      <v-tab-item key="expenses">
        <v-dialog v-model="dialog" max-width="600px">
          <template v-slot:activator="{ on }">
            <v-btn color="primary" dark v-on="on">Add Job Expense</v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">Create Expense</span>
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
                    <v-col cols="6">
                      <v-menu
                        v-model="menu2"
                        :close-on-content-click="false"
                        transition="scale-transition"
                        offset-y
                        min-width="290px"
                      >
                        <template v-slot:activator="{ on }">
                          <v-text-field
                            v-model="expense.date_purchased"
                            label="Date of Expense"
                            readonly
                            v-on="on"
                          ></v-text-field>
                        </template>
                        <v-date-picker v-model="date" @input="menu2 = false" label="Date of Expense"></v-date-picker>
                      </v-menu>
                    </v-col>
                  </v-row>
                </v-form>
              </v-container>
              <small>*indicates required field</small>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" :disabled="!valid1" text @click="addJobExpense">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>
        <v-data-table
          :headers="headers"
          :items="expenses"
          :search="search"
          :items-per-page="10"
          class="elevation-1"
          @click:row="handleClick"
        >
        </v-data-table>
      </v-tab-item>

      <v-tab-item key="edit">
        <v-form ref="form" v-model="valid1">
          <span>Edit job information:</span>
          <v-text-field v-model="job.name" focus :counter="40" :rules="rule" label="Name" required></v-text-field>
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
      total: 0,
      expense: {
        job: null,
        name: null,
        description: "",
        job_expense_type: null,
        cost: null,
        date_purchased: new Date().toISOString().substr(0, 10),
      },
      headers: [
        {
          text: "Expense Name",
          value: "name",
          align: "left"
        },
        { text: "Expense Description", align: "left", value: "description" },
        { text: "Cost" , value: "cost" }

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
      date: new Date().toISOString().substr(0, 10),
      menu: false,
      modal: false,
      menu2: false,
    };
  },
  created() {
    this.id = this.$route.params.id;
    this.expense.job = this.id;

    //get job data for this id 
    axios
      .get("http://127.0.0.1:8000/api/job/" + this.id + "/")
      .then(response => {
        console.log(response.data);
        this.job = response.data;
        console.log(this.job);
      });
    //get job types for edit
    axios.get("http://127.0.0.1:8000/api/jobtype/").then(response => {
      if (response.data) {
        response.data.forEach(item => {
          this.jobTypes.push(item);
        });
      }
    });
    //get expense type for adding new expense
    axios.get("http://127.0.0.1:8000/api/jobexpensetype/").then(response => {
      if (response.data) {
        response.data.forEach(item => {
          this.jobExpenseTypes.push(item);
        });
      }
    });
    //get each expense for this job
    axios.get("http://127.0.0.1:8000/api/expensesofjob?jobid=" + this.id).then(response => {
      console.log(response.data);
      response.data.forEach(item => {
        this.expenses.push(item);
        this.total += parseFloat(item.cost)
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
    },
    addJobExpense: function() {
      console.log(this.expense)
      axios
        .post("http://127.0.0.1:8000/api/jobexpense/", this.expense)
        .then(response => {
          this.expense = response.data;
          this.$notify({
            group: "success",
            title: "Add Job Expense Succesfully",
            type: "success"
          });
          console.log(this.expense)
          this.expenses.push(response.data);
          this.total += parseFloat(response.data.cost)
          this.dialog = false;
          this.$refs.form1.reset()
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
    }
  }
};
</script>