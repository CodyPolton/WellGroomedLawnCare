<template>
  <v-app style="width: 100%;">
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="schedule">Schedule</v-tab>
      <v-tab key="edit">Edit</v-tab>
      <v-tab-item key="schedule">
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
            </v-list-item>
          </v-list-item-group>
        </v-list>
       </v-flex>
     </v-layout>
</v-container>
</v-tab-item>
</v-tabs> 
  </v-app>
</template>

<script>
import axios from "axios";
// @ is an alias to /src
export default {
  name: 'Crewview',
  components: {
  },
  data (){
    return {
      crew: null,
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
      day12: [],
      crewid: null,
    }
  },
  created() {
    this.crewid = this.$route.params.crewid;
    this.loading = true;

    axios
      .get(process.env.VUE_APP_API_URL + "crew/" + this.crewid + "/")
      .then(response => {
        this.crew = response.data;
      });

    axios
      .get(process.env.VUE_APP_API_URL + "yard/")
      .then(response => {
        response.data.forEach(item => {
          if (item.scheduled) {
            item.scheduled = "YES";
          } else {
            item.scheduled = "NO";
          }
          console.log(item)
          console.log(this.crew)
          if(item.crew == this.crew.name){
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