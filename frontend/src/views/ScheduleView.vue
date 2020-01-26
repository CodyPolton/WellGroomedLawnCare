<template>
  <v-app style="width: 100%;">
      <!-- <h1>Day 1</h1>
      <v-btn @click="route(addresses1)">Route</v-btn>
      <ul id="example-1" >
        <li v-for="address in addresses1">
         {{address.address}}
        </li>
    </ul> -->
    <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>
    <v-data-table
          dense
          :loading='loading'
          :headers="headers"
          :items="yards"
          :search="search"
          :items-per-page="5"
          class="elevation-1"
        >
          <template v-slot:top>
            <v-toolbar flat color="white">
              <v-toolbar-title>Yards</v-toolbar-title>
              <v-divider class="mx-4" inset vertical></v-divider>
              <v-spacer></v-spacer>
              <v-dialog v-model="dialog" max-width="300px">
                <template v-slot:activator="{ on }">
                </template>
                <v-card v-if="dialog">
                    <v-card-title>
                      <span class="headline">Which day to schedule?</span>
                    </v-card-title>

                    <v-card-text>
                      <v-container>
                        <v-btn color="blue darken-1" text @click="addToDay(1)">Day 1 (Monday)</v-btn></br>
                        <v-btn color="blue darken-1" text @click="addToDay(2)">Day 2 (Tuesday)</v-btn></br>
                        <v-btn color="blue darken-1" text @click="addToDay(3)">Day 3 (Wednesday)</v-btn></br>
                        <v-btn color="blue darken-1" text @click="addToDay(4)">Day 4 (Thursday)</v-btn></br>
                        <v-btn color="blue darken-1" text @click="addToDay(5)">Day 5 (Friday)</v-btn></br>
                        <v-btn color="blue darken-1" text @click="addToDay(6)">Day 6 (Saturday)</v-btn></br>

                        <v-btn color="blue darken-1" text @click="addToDay(7)">Day 7 (Monday)</v-btn></br>
                        <v-btn color="blue darken-1" text @click="addToDay(8)">Day 8 (Tuesday)</v-btn></br>
                        <v-btn color="blue darken-1" text @click="addToDay(9)">Day 9 (Wednesday)</v-btn></br>
                        <v-btn color="blue darken-1" text @click="addToDay(10)">Day 10 (Thursday)</v-btn></br>
                        <v-btn color="blue darken-1" text @click="addToDay(11)">Day 11 (Friday)</v-btn></br>
                        <v-btn color="blue darken-1" text @click="addToDay(12)">Day 12 (Saturday)</v-btn></br>
                      </v-container>
                    </v-card-text>
                </v-card>
              </v-dialog>
            </v-toolbar>
          </template>
          <template v-slot:item.action="{ item }">
            <v-icon :disabled='item.crew != crew'color="green" class="mr-2" @click="scheduleYard(item)">mdi-plus</v-icon>
          </template>
        </v-data-table>
        <v-container >
      <v-layout class="d-flex flex-wrap">
       <v-flex xs3 >
        <h2>Day 1 (Monday)</h2>
        <v-btn @click="route(day1)">Route</v-btn>
        <v-list dense>
          <v-list-item-group v-model="item" color="primary">
            <v-list-item
              v-for="(item, i) in day1"
              :key="i"
              
            >
              <v-list-item-content>
                <v-list-item-title v-text="item.address"></v-list-item-title>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn icon>
                  <v-icon color="red lighten-1" @click='deleteYardFromDay(1, item)'>mdi-close</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
       </v-flex>
       <v-flex xs3 >
         <h2>Day 2 (Tuesday)</h2>
         <v-btn @click="route(day2)">Route</v-btn>
        <v-list dense>
          <v-list-item-group v-model="item" color="primary">
            <v-list-item
              v-for="(item, i) in day2"
              :key="i"
            >
              <v-list-item-content>
                <v-list-item-title v-text="item.address"></v-list-item-title>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn icon>
                  <v-icon color="red lighten-1" @click='deleteYardFromDay(2, item)'>mdi-close</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
       </v-flex>
       <v-flex xs3 >
         <h2>Day 3 (Wednesday)</h2>
         <v-btn @click="route(day3)">Route</v-btn>
        <v-list dense>
          <v-list-item-group v-model="item" color="primary">
            <v-list-item
              v-for="(item, i) in day3"
              :key="i"
            >
              <v-list-item-content>
                <v-list-item-title v-text="item.address"></v-list-item-title>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn icon>
                  <v-icon color="red lighten-1" @click='deleteYardFromDay(3, item)'>mdi-close</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
       </v-flex>
       <v-flex xs3>
         <h2>Day 4 (Thursday)</h2>
         <v-btn @click="route(day4)">Route</v-btn>
        <v-list dense>
          <v-list-item-group v-model="item" color="primary">
            <v-list-item
              v-for="(item, i) in day4"
              :key="i"
            >
              <v-list-item-content>
                <v-list-item-title v-text="item.address"></v-list-item-title>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn icon>
                  <v-icon color="red lighten-1" @click='deleteYardFromDay(4, item)'>mdi-close</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
       </v-flex>
       <v-flex xs3>
         <h2>Day 5 (Friday)</h2>
         <v-btn @click="route(day5)">Route</v-btn>
        <v-list dense>
          <v-list-item-group v-model="item" color="primary">
            <v-list-item
              v-for="(item, i) in day5"
              :key="i"
            >
              <v-list-item-content>
                <v-list-item-title v-text="item.address"></v-list-item-title>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn icon>
                  <v-icon color="red lighten-1" @click='deleteYardFromDay(5, item)'>mdi-close</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
       </v-flex>
       <v-flex xs3>
         <h2>Day 6 (Saturday)</h2>
         <v-btn @click="route(day6)">Route</v-btn>
        <v-list dense>
          <v-list-item-group v-model="item" color="primary">
            <v-list-item
              v-for="(item, i) in day6"
              :key="i"
            >
              <v-list-item-content>
                <v-list-item-title v-text="item.address"></v-list-item-title>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn icon>
                  <v-icon color="red lighten-1" @click='deleteYardFromDay(6, item)'>mdi-close</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
       </v-flex>
       <v-flex xs3>
         <h2>Day 7 (Monday)</h2>
         <v-btn @click="route(day7)">Route</v-btn>
        <v-list dense>
          <v-list-item-group v-model="item" color="primary">
            <v-list-item
              v-for="(item, i) in day7"
              :key="i"
            >
              <v-list-item-content>
                <v-list-item-title v-text="item.address"></v-list-item-title>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn icon>
                  <v-icon color="red lighten-1" @click='deleteYardFromDay(7, item)'>mdi-close</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
       </v-flex>
       <v-flex xs3>
         <h2>Day 8 (Tuesday)</h2>
         <v-btn @click="route(day8)">Route</v-btn>
        <v-list dense>
          <v-list-item-group v-model="item" color="primary">
            <v-list-item
              v-for="(item, i) in day8"
              :key="i"
            >
              <v-list-item-content>
                <v-list-item-title v-text="item.address"></v-list-item-title>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn icon>
                  <v-icon color="red lighten-1" @click='deleteYardFromDay(8, item)'>mdi-close</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
       </v-flex>
       <v-flex xs3>
         <h2>Day 9 (Wednesday)</h2>
         <v-btn @click="route(day9)">Route</v-btn>
        <v-list dense>
          <v-list-item-group v-model="item" color="primary">
            <v-list-item
              v-for="(item, i) in day9"
              :key="i"
            >
              <v-list-item-content>
                <v-list-item-title v-text="item.address"></v-list-item-title>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn icon>
                  <v-icon color="red lighten-1" @click='deleteYardFromDay(9, item)'>mdi-close</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
       </v-flex>
       <v-flex xs3>
         <h2>Day 10 (Thursday)</h2>
         <v-btn @click="route(day10)">Route</v-btn>
        <v-list dense>
          <v-list-item-group v-model="item" color="primary">
            <v-list-item
              v-for="(item, i) in day10"
              :key="i"
            >
              <v-list-item-content>
                <v-list-item-title v-text="item.address"></v-list-item-title>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn icon>
                  <v-icon color="red lighten-1" @click='deleteYardFromDay(10, item)'>mdi-close</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
       </v-flex>
       <v-flex xs3>
         <h2>Day 11 (Friday)</h2>
         <v-btn @click="route(day11)">Route</v-btn>
        <v-list dense>
          <v-list-item-group v-model="item" color="primary">
            <v-list-item
              v-for="(item, i) in day11"
              :key="i"
            >
              <v-list-item-content>
                <v-list-item-title v-text="item.address"></v-list-item-title>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn icon>
                  <v-icon color="red lighten-1" @click='deleteYardFromDay(11, item)'>mdi-close</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
       </v-flex>
       <v-flex xs3>
         <h2>Day 12 (Saturday)</h2>
         <v-btn @click="route(day12)">Route</v-btn>
        <v-list dense>
          <v-list-item-group v-model="item" color="primary">
            <v-list-item
              v-for="(item, i) in day12"
              :key="i"
            >
              <v-list-item-content>
                <v-list-item-title v-text="item.address"></v-list-item-title>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn icon>
                  <v-icon color="red lighten-1" @click='deleteYardFromDay(12, item)'>mdi-close</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
       </v-flex>
     </v-layout>
</v-container>
      
  </v-app>
</template>

<script>
import axios from "axios";
// @ is an alias to /src
export default {
  name: 'ScheduleView',
  components: {
  },
  data (){
    return {
      crew: 1,
      yards: [],
      item: null,
      yard: null,
      dialog: false,
      search: null, 
      headers: [
        {text: "Address",align: "left",value: "address" },
        { text: "Scheduled", align: "left", value: "scheduled" },
        { text: "Crew", value: "crew" },
        { text: "Day(s)", value: 'days'},
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
      day12: []
    }
  },
  created() {
    this.loading = true;
    axios
      .get(process.env.VUE_APP_API_URL + "yard/")
      .then(response => {
        response.data.forEach(item => {
          if (item.scheduled) {
            item.scheduled = "YES";
          } else {
            item.scheduled = "NO";
          }
          this.yards.push(item);
          if(item.crew == this.crew){
          item.days.forEach(x => {
            if(x == 'Day1'){
              this.day1.push(item)
            }else if(x == 'Day2'){
              this.day2.push(item)
            }else if(x == 'Day3'){
              this.day3.push(item)
            }else if(x == 'Day4'){
              this.day4.push(item)
            }else if(x == 'Day5'){
              this.day5.push(item)
            }else if(x == 'Day6'){
              this.day6.push(item)
            }else if(x == 'Day7'){
              this.day7.push(item)
            }else if(x == 'Day8'){
              this.day8.push(item)
            }else if(x == 'Day9'){
              this.day9.push(item)
            }else if(x == 'Day10'){
              this.day10.push(item)
            }else if(x == 'Day11'){
              this.day11.push(item)
            }else if(x == 'Day12'){
              this.day12.push(item)
            }
          })
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
  },
  methods: {
    scheduleYard: function(item){
      this.dialog = true
      this.yard = item 
    },
    addToDay: function(day){
      if(day == 1){
        this.day1.push(this.yard)
      }else if(day ==2){
        this.day2.push(this.yard)
      }else if(day ==3){
        this.day3.push(this.yard)
      }else if(day ==4){
        this.day4.push(this.yard)
      }else if(day ==5){
        this.day5.push(this.yard)
      }else if(day ==6){
        this.day6.push(this.yard)
      }else if(day ==7){
        this.day7.push(this.yard)
      }else if(day ==8){
        this.day8.push(this.yard)
      }else if(day ==9){
        this.day9.push(this.yard)
      }else if(day ==10){
        this.day10.push(this.yard)
      }else if(day ==11){
        this.day11.push(this.yard)
      }else if(day ==12){
        this.day12.push(this.yard)
      }
      this.yard.scheduled = true
      this.yard.crew = this.crew
      this.yard.days.push('Day' + day)
      this.saveYardChange()
      this.dialog = false
    },
    deleteYardFromDay: function(day, yard){      
      if(day == 1){
        this.day1.splice(this.day1.indexOf(yard), 1);
      }else if(day ==2){
        this.day2.splice(this.day2.indexOf(yard), 1);
      }else if(day ==3){
        this.day3.splice(this.day3.indexOf(yard), 1);
      }else if(day ==4){
        this.day4.splice(this.day4.indexOf(yard), 1);
      }else if(day ==5){
        this.day5.splice(this.day5.indexOf(yard), 1);
      }else if(day ==6){
        this.day6.splice(this.day6.indexOf(yard), 1);
      }else if(day ==7){
        this.day7.splice(this.day7.indexOf(yard), 1);
      }else if(day ==8){
        this.day8.splice(this.day8.indexOf(yard), 1);
      }else if(day ==9){
        this.day9.splice(this.day9.indexOf(yard), 1);
      }else if(day ==10){
        this.day10.splice(this.day10.indexOf(yard), 1);
      }else if(day ==11){
        this.day11.splice(this.day11.indexOf(yard), 1);
      }else if(day ==12){
        this.day12.splice(this.day12.indexOf(yard), 1);
      }
      this.yard.days.splice(this.yard.days.indexOf('Day' + day), 1)
      if(!this.yard.days.length){
        this.yard.scheduled = false
      }
      this.saveYardChange()
    },
    saveYardChange: function(){
      axios
        .put(
          process.env.VUE_APP_API_URL + "yard/" + this.yard.yardid + "/",this.yard
        )
        .then(response => {
          if (response.data) {
            if (item.scheduled) {
              item.scheduled = "YES";
            } else {
              item.scheduled = "NO";
            }
            this.$notify({
              group: "success",
              title: "Change was Successful",
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
                    "Error making change " +
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
    route: function(addresses){
          console.log(addresses)
          var url = "/route?"
          var i = 1
          for(var x in addresses){
              if(i == 1){
                 var waypoint = "waypoint1="
              }else{
              var waypoint = "&waypoint" + i + "="
              }
            url = url + waypoint + addresses[x].address
            i++
          }
          console.log("The route is " + url);
          //this.$router.push(url)
    }
  }
};
</script>