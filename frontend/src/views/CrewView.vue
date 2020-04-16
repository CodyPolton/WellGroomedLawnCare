<template>
  <v-app style="width: 100%;">
    <v-container>
<v-row justify="center">
        <v-flex xs4 pt-5 my-5>
        <v-card
          class="pa-4 display-2 white--text d-flex justify-center font-weight-light"
          color="primary"
        >Crew Schedule</v-card>
      </v-flex>
  <v-flex xs12>
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="schedule">Schedule</v-tab>
      <v-tab key="edit">Edit</v-tab>
      <v-tab-item key="schedule">
        <v-container>
          <v-layout class="d-flex flex-wrap">
            <v-flex xs3 class="px-3">
                <v-toolbar color="grey darken-1" class="white--text font-weight-light" dense>
                  <v-toolbar-title>Day 1 (Monday)</v-toolbar-title>
                </v-toolbar>
                <v-card tile color="grey" class="white--text">
              <v-btn tile block color="green" class="white--text title" @click="route(day1)">Route</v-btn>
              <v-list tile dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day1" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
                </v-card>
            </v-flex>
            <v-flex xs3 class="px-3">
                             <v-toolbar color="grey darken-1" class="white--text font-weight-light" dense>
                  <v-toolbar-title>Day 2 (Tuesday)</v-toolbar-title>
                </v-toolbar>
                              <v-card tile color="grey" class="white--text">
              <v-btn tile block color="green" class="white--text title" @click="route(day2)">Route</v-btn>
              <v-list tile dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day2" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
                              </v-card>
            </v-flex>
            <v-flex xs3 class="px-3">
                              <v-toolbar color="grey darken-1" class="white--text font-weight-light" dense>
                  <v-toolbar-title>Day 3 (Wednesday)</v-toolbar-title>
                </v-toolbar>
                                            <v-card tile color="grey" class="white--text">
              <v-btn tile block color="green" class="white--text title" @click="route(day3)">Route</v-btn>
              <v-list tile  dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day3" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
                                            </v-card>
            </v-flex>
            <v-flex xs3 class="px-3">
                             <v-toolbar color="grey darken-1" class="white--text font-weight-light" dense>
                  <v-toolbar-title>Day 4 (Thursday)</v-toolbar-title>
                </v-toolbar>
                                            <v-card tile color="grey" class="white--text">
              <v-btn tile block color="green" class="white--text title" @click="route(day4)">Route</v-btn>
              <v-list  tile dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day4" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
                                            </v-card>
            </v-flex>
            <v-flex xs3 class="px-3">
                <v-toolbar color="grey darken-1" class="white--text font-weight-light" dense>
                  <v-toolbar-title>Day 5 (Friday)</v-toolbar-title>
                </v-toolbar>
                                            <v-card tile color="grey" class="white--text">
              <v-btn tile block color="green" class="white--text title" @click="route(day5)">Route</v-btn>
              <v-list tile  dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day5" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
                                            </v-card>
            </v-flex>
            <v-flex xs3 class="px-3">
                <v-toolbar color="grey darken-1" class="white--text font-weight-light" dense>
                  <v-toolbar-title>Day 6 (Saturday)</v-toolbar-title>
                </v-toolbar>
                                            <v-card tile color="grey" class="white--text">
              <v-btn tile block color="green" class="white--text title" @click="route(day6)">Route</v-btn>
              <v-list tile  dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day6" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
                                            </v-card>
            </v-flex>
            <v-flex xs3 class="px-3">
                              <v-toolbar color="grey darken-1" class="white--text font-weight-light" dense>
                  <v-toolbar-title>Day 7 (Monday)</v-toolbar-title>
                </v-toolbar>
                                            <v-card tile color="grey" class="white--text">
              <v-btn tile block color="green" class="white--text title" @click="route(day7)">Route</v-btn>
              <v-list tile  dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day7" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
                                            </v-card>
            </v-flex>
            <v-flex xs3 class="px-3">
                              <v-toolbar color="grey darken-1" class="white--text font-weight-light" dense>
                  <v-toolbar-title>Day 8 (Tuesday)</v-toolbar-title>
                </v-toolbar>
                                            <v-card tile color="grey" class="white--text">
              <v-btn tile block color="green" class="white--text title" @click="route(day8)">Route</v-btn>
              <v-list tile  dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day8" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
                                            </v-card>
            </v-flex>
            <v-flex xs3 class="px-3">
                              <v-toolbar color="grey darken-1" class="white--text font-weight-light" dense>
                  <v-toolbar-title>Day 9 (Wednesday)</v-toolbar-title>
                </v-toolbar>
                                            <v-card tile color="grey" class="white--text">
              <v-btn tile block color="green" class="white--text title" @click="route(day9)">Route</v-btn>
              <v-list tile  dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day9" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
                                            </v-card>
            </v-flex>
            <v-flex xs3 class="px-3">
                             <v-toolbar color="grey darken-1" class="white--text font-weight-light" dense>
                  <v-toolbar-title>Day 10 (Thursday)</v-toolbar-title>
                </v-toolbar>
                                            <v-card tile color="grey" class="white--text">
              <v-btn tile block color="green" class="white--text title" @click="route(day10)">Route</v-btn>
              <v-list tile  dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day10" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
                                            </v-card>
            </v-flex>
            <v-flex xs3 class="px-3">
                             <v-toolbar color="grey darken-1" class="white--text font-weight-light" dense>
                  <v-toolbar-title>Day 11 (Friday)</v-toolbar-title>
                </v-toolbar>
                                            <v-card tile color="grey" class="white--text">
              <v-btn tile block color="green" class="white--text title" @click="route(day11)">Route</v-btn>
              <v-list tile  dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day11" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
                                            </v-card>
            </v-flex>
            <v-flex xs3 class="px-3">
                              <v-toolbar color="grey darken-1" class="white--text font-weight-light" dense>
                  <v-toolbar-title>Day 12 (Saturday)</v-toolbar-title>
                </v-toolbar>
                                            <v-card tile color="grey" class="white--text">
              <v-btn tile block color="green" class="white--text title" @click="route(day12)">Route</v-btn>
              <v-list tile  dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day12" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
                                            </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-tab-item>

      <v-tab-item key="edit">
        <v-container>
          <v-layout>
            <v-flex xs10 offset-xs1>
        <v-form ref="form" v-model="valid">
          <span>Enter yard information:</span>
          <v-text-field
            v-model="crew.name"
            :counter="40"
            :rules="[v => !!v || 'Crew Name is required']"
            label="Crew Name*"
            required
          ></v-text-field>

          <v-text-field v-model="crew.crew_lead" :counter="40" label="Crew Lead Name*"></v-text-field>

          <v-btn :disabled="!valid" color="success" class="mr-4" @click="save">Save</v-btn>
        </v-form>
        </v-flex>
        </v-layout>
        </v-container>
      </v-tab-item>
    </v-tabs>
</v-flex>
</v-row>


    </v-container>
  </v-app>
</template>

<script>
import axios from "axios";
// @ is an alias to /src
export default {
  name: "Crewview",
  components: {},
  data() {
    return {
      crew: {
        name: "",
        crew_lead: ""
      },
      crewName: null,
      yards: [],
      item: null,
      valid: false,
      yard: null,
      dialog: false,
      search: null,
      headers: [
        { text: "Address", align: "left", value: "address" },
        { text: "Scheduled", align: "left", value: "scheduled" },
        { text: "Crew", value: "crew" },
        { text: "Day(s)", value: "days" },
        { text: "Actions", align: "right", value: "action", sortable: false }
      ],
      day1: [],
      day2: [],
      day3: [],
      day4: [],
      day5: [],
      day6: [],
      day7: [],
      day8: [],
      day9: [],
      day10: [],
      day11: [],
      day12: [],
      crewid: null
    };
  },
  created() {
    this.crewid = this.$route.params.crewid;
    this.loading = true;

    axios
      .get(process.env.VUE_APP_API_URL + "crew/" + this.crewid + "/")
      .then(response => {
        this.crew = response.data;
        this.crewName = this.crew.name;

        axios
          .get(process.env.VUE_APP_API_URL + "yard/")
          .then(response => {
            response.data.forEach(item => {
              if (item.scheduled) {
                item.scheduled = "YES";
              } else {
                item.scheduled = "NO";
              }
              if (item.crew == this.crew.name) {
                item.days.forEach(x => {
                  if (x == "Day1") {
                    this.day1.push(item);
                  } else if (x == "Day2") {
                    this.day2.push(item);
                  } else if (x == "Day3") {
                    this.day3.push(item);
                  } else if (x == "Day4") {
                    this.day4.push(item);
                  } else if (x == "Day5") {
                    this.day5.push(item);
                  } else if (x == "Day6") {
                    this.day6.push(item);
                  } else if (x == "Day7") {
                    this.day7.push(item);
                  } else if (x == "Day8") {
                    this.day8.push(item);
                  } else if (x == "Day9") {
                    this.day9.push(item);
                  } else if (x == "Day10") {
                    this.day10.push(item);
                  } else if (x == "Day11") {
                    this.day11.push(item);
                  } else if (x == "Day12") {
                    this.day12.push(item);
                  }
                  this.yards.push(item);
                });
              }
            });
            this.loading = false;
          })
          .catch(error => {
            this.$notify({
              group: "error",
              title: "Backend is down please contact your System adminstartor.",
              type: "error"
            });
          });
      });
  },
  methods: {
    save: function() {
      axios
        .put(
          process.env.VUE_APP_API_URL + "crew/" + this.crewid + "/",
          this.crew
        )
        .then(response => {
          if (response.data) {
            this.yards.forEach(yard => {
              if (yard.crew == this.crewName) {
                yard.crew = this.crew.name;
                axios.put(
                  process.env.VUE_APP_API_URL + "yard/" + yard.yardid + "/",
                  yard
                );
              }
              this.crew = response.data;
            });

            this.$notify({
              group: "success",
              title: "Saved Crew Succesfully",
              type: "success"
            });
            this.crew = response.data;
          }
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
                    "Error saving crew information. " +
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
    route: function(addresses) {
      if (addresses.length == 0) {
        this.$notify({
          group: "error",
          title: "There are no yards to generate a route",
          type: "error"
        });
        return;
      } else {
        console.log(addresses);

        var url = "/route?crewid=" + this.crew.name;
        var i = 1;
        for (var x in addresses) {
          if (i == 1) {
            var waypoint = "&waypoint1=";
          } else {
            var waypoint = "&waypoint" + i + "=";
          }
          url = url + waypoint + addresses[x].address + ", " + addresses[x].city + ", " + addresses[x].state + " " + addresses[x].zip_code;
          i++;
        }
        console.log("The route is " + url);
        this.$router.push(url)
      }
    },
    back: function() {
      this.$router.go(-1);
    }
  }
};
</script>