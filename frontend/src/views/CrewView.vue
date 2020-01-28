<template>
  <v-app style="width: 100%;">
      <v-btn @click="back">Back</v-btn>
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="schedule">Schedule</v-tab>
      <v-tab key="edit">Edit</v-tab>
      <v-tab-item key="schedule">
        <v-container>
          <v-layout class="d-flex flex-wrap">
            <v-flex xs3>
              <h2>Day 1 (Monday)</h2>
              <v-btn @click="route(day1)">Route</v-btn>
              <v-list dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day1" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-flex>
            <v-flex xs3>
              <h2>Day 2 (Tuesday)</h2>
              <v-btn @click="route(day2)">Route</v-btn>
              <v-list dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day2" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-flex>
            <v-flex xs3>
              <h2>Day 3 (Wednesday)</h2>
              <v-btn @click="route(day3)">Route</v-btn>
              <v-list dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day3" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-flex>
            <v-flex xs3>
              <h2>Day 4 (Thursday)</h2>
              <v-btn @click="route(day4)">Route</v-btn>
              <v-list dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day4" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-flex>
            <v-flex xs3>
              <h2>Day 5 (Friday)</h2>
              <v-btn @click="route(day5)">Route</v-btn>
              <v-list dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day5" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-flex>
            <v-flex xs3>
              <h2>Day 6 (Saturday)</h2>
              <v-btn @click="route(day6)">Route</v-btn>
              <v-list dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day6" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-flex>
            <v-flex xs3>
              <h2>Day 7 (Monday)</h2>
              <v-btn @click="route(day7)">Route</v-btn>
              <v-list dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day7" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-flex>
            <v-flex xs3>
              <h2>Day 8 (Tuesday)</h2>
              <v-btn @click="route(day8)">Route</v-btn>
              <v-list dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day8" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-flex>
            <v-flex xs3>
              <h2>Day 9 (Wednesday)</h2>
              <v-btn @click="route(day9)">Route</v-btn>
              <v-list dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day9" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-flex>
            <v-flex xs3>
              <h2>Day 10 (Thursday)</h2>
              <v-btn @click="route(day10)">Route</v-btn>
              <v-list dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day10" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-flex>
            <v-flex xs3>
              <h2>Day 11 (Friday)</h2>
              <v-btn @click="route(day11)">Route</v-btn>
              <v-list dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day11" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-flex>
            <v-flex xs3>
              <h2>Day 12 (Saturday)</h2>
              <v-btn @click="route(day12)">Route</v-btn>
              <v-list dense>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item disabled v-for="(item, i) in day12" :key="i">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.address"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-flex>
          </v-layout>
        </v-container>
    </v-tab-item>

    <v-tab-item key="edit">
        <v-form ref="form" v-model="valid">
          <span>Enter yard information:</span>
          <v-text-field
            v-model="saveCrew.name"
            :counter="40"
            :rules="[v => !!v || 'Crew Name is required']"
            label="Crew Name*"
            required
            ></v-text-field>

            <v-text-field
            v-model="saveCrew.crew_lead"
            :counter="40"
            label="Crew Lead Name*"
            ></v-text-field>
          

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
  name: "Crewview",
  components: {},
  data() {
    return {
      crew: null,
      saveCrew: null,
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
        this.saveCrew = this.crew
        this.crewName = this.crew.name
      

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
              this.yards.push(item)
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
    save: function(){
        axios
        .put(
          process.env.VUE_APP_API_URL + "crew/" + this.crewid + "/",
          this.saveCrew
        )
        .then(response => {
          if (response.data) {
              this.yards.forEach(yard =>{
                  if(yard.crew == this.crewName){
                      yard.crew = this.saveCrew.name
                      axios
                        .put(
                        process.env.VUE_APP_API_URL + "yard/" + yard.yardid + "/",
                        yard
                        )
                  }
                  this.crew = response.data;
              })

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
      console.log(addresses);
      var url = "/route?";
      var i = 1;
      for (var x in addresses) {
        if (i == 1) {
          var waypoint = "waypoint1=";
        } else {
          var waypoint = "&waypoint" + i + "=";
        }
        url = url + waypoint + addresses[x].address;
        i++;
      }
      console.log("The route is " + url);
      //this.$router.push(url)
    },
    back: function() {
      this.$router.go(-1);
    }
  }
};
</script>