<template>
  <v-container>
    <v-layout>
      <v-flex>
        <v-btn @click="back">Back</v-btn>

        <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>
        <v-data-table
          :loading="loading"
          :headers="headers"
          :items="crews"
          :search="search"
          :items-per-page="15"
          class="elevation-1"
          @click:row="handleClick"
        >
          <template v-slot:top>
            <v-toolbar flat color="white">
              <v-toolbar-title>Crews</v-toolbar-title>
              <v-divider class="mx-4" inset vertical></v-divider>
              <v-spacer></v-spacer>
              <v-dialog v-model="dialog" max-width="300px">
                <template v-slot:activator="{ on }">
                  <v-btn color="blue darken-1" text @click="dialog = true">Create Crew</v-btn>
                </template>
                <v-card>
                  <v-card-title>
                    <span class="headline">Create Crew</span>
                  </v-card-title>
                  <v-card-text>
                    <small>*indicates required field</small>
                    <v-container>
                      <v-form ref="form" v-model="valid">
                        <v-row>
                          <v-col cols="12" sm="12" md="12">
                            <v-text-field
                              v-model="crew.name"
                              :counter="40"
                              :rules="[v => !!v || 'Crew Name is required']"
                              label="Crew Name*"
                              required
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-btn
                          right
                          :disabled="!valid"
                          color="success"
                          text
                          class="mr-4"
                          @click="addCrew"
                        >Create</v-btn>
                      </v-form>
                    </v-container>
                  </v-card-text>
                </v-card>
              </v-dialog>
            </v-toolbar>
          </template>
        </v-data-table>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
// @ is an alias to /src
export default {
  name: "Crews",
  components: {},
  data() {
    return {
      dialog: null,
      loading: false,
      valid: null,
      search: null,
      crews: [],
      crew: {
        name: null
      },
      headers: [
        { text: "Crew Name", align: "left", value: "name" },
        { text: "Crew Lead", align: "left", value: "crew_lead" }
      ]
    };
  },
  created() {
    this.loading = true;
    axios.get(process.env.VUE_APP_API_URL + "crew").then(response => {
      if (response.data) {
        response.data.forEach(item => {
          this.crews.push(item);
        });
        this.loading = false;
      }
    });
  },
  methods: {
    addCrew: function() {
      axios
        .post(process.env.VUE_APP_API_URL + "crew/", this.crew)
        .then(response => {
          this.$notify({
            group: "success",
            title: "Added Crew Succesfully",
            type: "success"
          });
          this.crews.unshift(response.data);
          this.dialog = false;
          this.$refs.form.reset();
        })
        .catch(error => {
          if (error.response) {
            for (var prop in this.crew) {
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
    handleClick: function(item) {
      this.$router.push("/crew/" + item.crewid);
    },
    back: function() {
      this.$router.go(-1);
    }
  }
};
</script>