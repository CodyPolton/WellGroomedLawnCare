<template>
  <v-app style="width: 100%; ">
    <v-btn @click="back">Back</v-btn>
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="details">Details</v-tab>
      <v-tab key="jobs">Jobs</v-tab>
      <v-tab key="edit">Edit</v-tab>
      <v-tab-item key="details">]
        <v-btn v-if="yard.mow_price!=null" color="primary" dark @click="yardMowed">Mowed</v-btn>
        <v-dialog v-model="confirmMowDialog" persistent max-width="400">
          <v-card>
            <v-card-title class="headline">Yard Mowed Recently</v-card-title>
            <v-card-text>This yard has already been marked as mowed today. Just want to make sure you are not marking this yard as mowed twice in on day by accident.</v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="red darken-1" text @click="confirmMowDialog = false">Did Not Mow Again</v-btn>
              <v-btn
                color="green darken-1"
                text
                @click="addMowJob(); confirmMowDialog = false"
              >Mowed Again</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-tab-item>
      <v-tab-item key="jobs">
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
              <v-btn color="blue darken-1" :disabled="valid" text @click="addJob">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>
        <v-data-table
          v-model="selected"
          :headers="headers"
          :items="jobs"
          :search="search"
          :single-select="singleSelect"
          show-select
          item-key="jobid"
          :items-per-page="10"
          class="elevation-1"
          @click:row="handleClick"
        >
          <template v-slot:top>
            <v-btn color="primary" @click="generateInvoice">Invoice Selected</v-btn>
          </template>
        </v-data-table>
      </v-tab-item>
      <v-tab-item key="edit">
        <v-form ref="form" v-model="yardEdit">
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
          >=</v-text-field>

          <v-btn :disabled="!yardEdit" color="success" class="mr-4" @click="save">Save</v-btn>
        </v-form>
      </v-tab-item>
    </v-tabs>
  </v-app>
</template>

<script>
import axios from "axios";
// @ is an alias to /src
export default {
  data() {
    return {
      selected: [],
      singleSelect: false,
      date: new Date().toJSON().slice(0, 10),
      confirmMowDialog: false,
      yardEdit: false,
      dialog: false,
      jobtypes: {
        job_typeid: null,
        job_type: null
      },
      jobTypes: [],
      job: {
        yard: null,
        name: null,
        description: null,
        job_type: null,
        date_completed: null,
        job_total: null,
        invoiced: false,
        date_created: null,
        date_updated: null,
        account: null
      },
      yardid: null,
      accountid: null,
      yard: {},
      jobs: [],
      headers: [
        {text: "Job Name",align: "left",value: "name"},
        { text: "Desciption", align: "middle", value: "description" },
        { text: "Job Type", value: "job_type" },
        {text: "Date Completed", value: 'date_completed'},
        {text: "Invoice ID", value: 'invoiceid'}
      ],
      states: [
        "MO",
        "AL",
        "AK",
        "AZ",
        "AR",
        "CA",
        "CO",
        "CT",
        "DE",
        "FL",
        "GA",
        "HI",
        "ID",
        "IL",
        "IN",
        "IA",
        "KS",
        "KY",
        "LA",
        "ME",
        "MD",
        "MA",
        "MI",
        "MN",
        "MS",
        "MT",
        "NE",
        "NV",
        "NH",
        "NJ",
        "NM",
        "NY",
        "NC",
        "ND",
        "OH",
        "OK",
        "OR",
        "PA",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VT",
        "VA",
        "WA",
        "WV",
        "WI",
        "WY"
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
  components: {},
  created() {
    this.yardid = this.$route.params.yardid;
    this.accountid = this.$route.params.accountid; 
    this.job.yard = this.yardid;
    this.job.account = this.accountid

    axios
      .get(process.env.VUE_APP_API_URL + "yard/" + this.yardid + "/")
      .then(response => {
        this.yard = response.data;
      });

    axios
      .get(process.env.VUE_APP_API_URL + "yardjobs?yardid=" + this.yardid)
      .then(response => {
        if (response.data) {
          response.data.forEach(item => {
            this.jobs.push(item);
          });
        }
      });

    axios.get(process.env.VUE_APP_API_URL + "jobtype/").then(response => {
      if (response.data) {
        response.data.forEach(item => {
          this.jobTypes.push(item);
        });
      }
    });
  },
  methods: {
    generateInvoice: function() {
      console.log(this.selected);
      var goodToInvoice = true;
      for (var job of this.selected) {
        if (job.date_completed == null) {
          this.$notify({
            group: "error",
            title:
              "Make sure all the jobs have been marked as completed \n Job: " +
              job.name +
              " has not been completed.",
            type: "error"
          });
          goodToInvoice = false
        }
        if(job.invoiceid != ''){
          this.$notify({
            group: "error",
            title:
              "The job " + job.name + " has already been put on Invoice ID = " +
              job.invoiceid,
            type: "error"
          });
          goodToInvoice = false
        }
      }
      if (goodToInvoice) {
        axios
          .post(process.env.VUE_APP_API_URL + "generateinvoice/", {
            jobs: this.selected
          })
          .then(response => {
            console.log(response.data)
            axios
              .get(process.env.VUE_APP_API_URL + "yardjobs?yardid=" + this.yardid)
              .then(response => {
                this.jobs = []
                if (response.data) {
                  response.data.forEach(item => {
                    this.jobs.push(item);
                  });
                }
            });
            this.$notify({
              group: "success",
              title: "Generated Invoice Succesfully",
              type: "success"
            });
          });
      }
    },
    back: function() {
      this.$router.go(-1);
    },
    handleClick: function(value) {
      console.log(value.jobid);
      this.$router.push("/job/" + value.jobid);
    },
    save: function() {
      axios
        .put(
          process.env.VUE_APP_API_URL + "yard/" + this.yardid + "/",
          this.yard
        )
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
        .post(process.env.VUE_APP_API_URL + "job/", this.job)
        .then(response => {
          this.$notify({
            group: "success",
            title: "Added Job Succesfully",
            type: "success"
          });
          this.jobs.push(response.data);
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
    },
    yardMowed: function() {
      axios
        .get(
          process.env.VUE_APP_API_URL + "yardmowedcheck?yardid=" + this.yardid
        )
        .then(response => {
          if (response.data.message == "Mowed today") {
            console.log(response.data.message);
            this.confirmMowDialog = true;
          } else {
            this.addMowJob();
          }
        });
    },
    addMowJob: function() {
      console.log("Mow the job");

      var mowed = {
        yard: this.yardid,
        name: "Mow(Auto)",
        description: "Mowed on " + this.date,
        job_type: "Mowing",
        date_completed: this.date,
        job_total: this.yard.mow_price,
        invoiced: false,
        date_created: null,
        date_updated: null,
        account: this.accountid
      };
      console.log(mowed);

      axios
        .post(process.env.VUE_APP_API_URL + "job/", mowed)
        .then(response => {
          this.jobs.push(response.data);
          var mowexpense = {
            job: response.data.jobid,
            name: "Mow",
            description: "",
            job_expense_type: "Mow",
            cost: this.yard.mow_price,
            date_purchased: this.date
          };
          console.log(mowexpense);
          axios
            .post(process.env.VUE_APP_API_URL + "jobexpense/", mowexpense)
            .then(response => {
              this.$notify({
                group: "success",
                title: "Yard has been mowed Succesfully",
                type: "success"
              });
            })
            .catch(error => {
              if (error.response) {
                for (var prop in mowexpense) {
                  if (
                    Object.prototype.hasOwnProperty.call(
                      error.response.data,
                      prop
                    )
                  ) {
                    this.$notify({
                      group: "error",
                      title:
                        "Error adding mow expense." +
                        prop +
                        ": " +
                        error.response.data[prop],
                      type: "error"
                    });
                  }
                }
              }
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