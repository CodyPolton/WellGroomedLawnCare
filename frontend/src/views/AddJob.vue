<template>
  <v-app style="width: 100%;">
    <v-btn @click='back'>Back</v-btn>
    <v-form ref="form" v-model="valid">
      <span>Enter job information:</span>
      <v-text-field v-model="job.name" :counter="40" :rules="[v => !!v || 'Name is required']" label="Job Name" required></v-text-field>
      <v-col cols="12">
            <v-textarea
              v-model="job.description"
              color="teal"
              :rules="[v => !!v || 'Description is required']" label="Job Description" required
            >
            </v-textarea>
          </v-col>
      <v-select
        v-model="job.job_type"
        :items="types"
        :rules="[v => !!v || 'Job type is required']"
        label="Job Type"
        required
      ></v-select>
       

      <v-btn :disabled="!valid" color="success" class="mr-4" @click="addJob">Create Job</v-btn>
    </v-form>
  </v-app>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: "AddJob",
  data (){
      return {
          yardid: null,
          valid: null,
          types: [],
          job: {
              name: null,
              description: null,
              type: null
          }
      }
  },
  components: {},
    created() {
    this.yardid = this.$route.params.id;
    },
    methods: {
      back: function(){
        this.$router.go(-1)
      },
      addJob: function(){
        console.log(this.yard)
        axios.post('http://127.0.0.1:8000/api/job/', this.yard).then((response) =>{
        this.$notify({
              group: "success",
              title: "Added Yard Succesfully",
              type: "success"
            });
        this.$router.replace('/account/' + this.yard.account)
        }).catch(error => {
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
}

</script>