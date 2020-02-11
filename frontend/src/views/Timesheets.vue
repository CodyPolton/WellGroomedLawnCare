<template>
  <v-app style="width: 100%; ">
    <v-btn @click="back">Back</v-btn>
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="add">Status</v-tab>
      <v-tab-item key="add">
        <v-btn v-if='timesheet.status == "No Entry"' @click="ClockIn">Clock In</v-btn>
        <v-btn v-if='timesheet.status == "Clocked In"' @click="pause">Break</v-btn>
        <v-btn v-if='timesheet.status == "Clocked In"' @click="clockout">Clock Out</v-btn>
        <v-btn v-if='timesheet.status == "Paused"' @click="ClockBackIn">Clock Back In</v-btn>
        <h2 v-if='timesheet.status == "Clocked In"'>Clocked in at : {{timesheet.start_time}}</h2>
        <h2 v-if='timesheet.status == "Clocked In"'>Hours : {{totalHours}}</h2>
      </v-tab-item>
      <v-tab key="timesheets">Timesheets</v-tab>
      
      <v-tab-item key="timesheets" >
        <v-data-table
          :loading="loading"
          :headers="headers"
          :items="timesheets"
          :search="search"
          :items-per-page="15"
          class="elevation-1"
        >
        <template slot="footer">
          <td><strong>Total Hours:</strong></td>
          <td class="text-xs-right">{{ totalHour }}</td>
          </template>
        </v-data-table>
      </v-tab-item>
      
    </v-tabs>
    
  </v-app>
</template>

<script>
import axios from "axios";
// @ is an alias to /src
export default {
  name: "Route",
  components: {},
  data() {
    return {
      timesheet: {
        timesheetid: '',
        payperiodid: '',
        dayofweek: '',
        userid: '',
        start_time: "",
        end_time: null,
        seconds_paused: null,
        pause_time: null,
        hours: null,
        status: null,
      },
      totalHour: 0,
      loading: false,
      search: null,
      timesheets: [],
      clockinStatus: null,
      payperiodid: null,
      user_id: this.$store.state.user_id,
      dayofweek: null,

      crew: null,
      item: null,
      params: null,
      headers: [
        { text: "Day of the Week",align: "left",value: "dayofweek"},
        { text: "Start Time", align: "left", value: "start_time" },
        { text: "End Time", value: "end_time" },
        { text: "Break Time(Minutes)", value: "seconds_paused" },
        { text: "Hours", value: "hours" }
      ],
    };
  },
  computed: {
    totalHours() {
      var hours = this.get_time_diff(this.timesheet.start_time,1)
      if(this.timesheet.seconds_paused){
      hours -= (this.timesheet.seconds_paused / 3600)
      }
      
      return hours.toFixed(1)
    },
  },
  created() {
    this.dayofweek = this.getDayofWeek(new Date().getDay())

    console.log(this.dayofweek)
    axios
        .get(process.env.VUE_APP_API_URL + "clockinstatus?userid=" + this.user_id)
        .then(response => {
          console.log(response.data)
          if(response.data.timesheet){
            this.timesheet = response.data.timesheet[0]
          }
          
          this.timesheet.status = response.data.status
          
          this.payperiodid = response.data.payperiod.payperiodid
          console.log(this.timesheet)
        })

    axios.post(process.env.VUE_APP_API_URL + 'gettimesheet/', {'userid': this.$store.state.user_id}).then(response=>{
        console.log(response.data.timesheet)
        response.data.timesheet.forEach(element => {
          if(element.seconds_paused){
            element.seconds_paused = element.seconds_paused /60
          }
          element.hours = Math.round(((element.hours - (element.seconds_paused/60)) + Number.EPSILON) * 100) / 100
          this.totalHour += element.hours
          console.log(this.totalHour)
          this.timesheets.push(element)
        });
        console.log(this.timesheets)
      }).catch(error => {
        console.log(error)
      });
    


    
  },
  mounted() {},
  methods: {
    back: function() {
      this.$router.go(-1);
    },
    pause :function(){
      console.log("Break")
      var d = new Date().toLocaleTimeString()
      console.log(d)
      this.timesheet.status = "Paused"
      this.timesheet.pause_time = d
      axios.put(process.env.VUE_APP_API_URL + 'timesheet/' + this.timesheet.timesheetid + "/", this.timesheet).then(response=>{
        console.log(response)

      }).catch(error => {
        console.log(error)
      });
    },
    ClockBackIn: function(){
      var seconds = this.get_time_diff(this.timesheet.pause_time, 2)
      console.log(seconds)
      this.timesheet.seconds_paused += seconds
      this.timesheet.pause_time = null
      this.timesheet.status = "Clocked In"
      axios.put(process.env.VUE_APP_API_URL + 'timesheet/' + this.timesheet.timesheetid + "/", this.timesheet).then(response=>{
        console.log(response)

      }).catch(error => {
        console.log(error)
      });
    },
    ClockIn: function(){
      var d = new Date().toLocaleTimeString()

      console.log(d)
      
      var newTimesheet = {
        payperiodid :this.payperiodid,
        dayofweek :this.dayofweek,
        userid : this.user_id,
        status : 'Clocked In',
        start_time : d
      }
      console.log(newTimesheet)
      axios.post(process.env.VUE_APP_API_URL + 'timesheet/', newTimesheet).then(response=>{
        console.log(response)
        timesheet = response.data
      }).catch(error => {
        console.log(error)
      });
      
    },
    clockout: function(){
      this.timesheet.status = "Clocked Out"
      this.timesheet.hours = this.get_time_diff(this.timesheet.start_time, 1)
      this.timesheet.end_time = new Date().toLocaleTimeString()
      console.log(this.timesheet)
      axios.put(process.env.VUE_APP_API_URL + 'timesheet/' + this.timesheet.timesheetid + "/", this.timesheet).then(response=>{
        console.log(response)
        this.timesheet = {
        timesheetid: '',
        payperiodid: '',
        dayofweek:'',
        userid:'',
        start_time: "",
        end_time: null,
        seconds_paused: null,
        pause_time: null,
        hours:null,
        status:"No entry",
      }

      }).catch(error => {
        console.log(error)
      });
    },
    get_time_diff: function( datetimeone, mode)
  {
    console.log( typeof datetimeone)
    var split = datetimeone.split(':');
    console.log(split)

    var d = new Date()

  var d1= new Date(); 
  var d2 = new Date();
  d1.setHours(split[0]);
  d1.setMinutes(split[1]);
  d2.setHours(d.getHours());
  d2.setMinutes(d.getMinutes());

    var one = new Date( d1 ).getTime();
    var two = new Date(d2).getTime();

    console.log(one)

    if( isNaN(one) )
    {
        return "";
    }

    console.log( one + " " + two);

    if (one < two) {
        var milisec_diff = two - one;
    }else{
        var milisec_diff = one - two;
    }

    if (mode == 1){
    var hours = (milisec_diff / (1000 * 60 * 60)) % 24;
    return Math.round((hours + Number.EPSILON) * 100) / 100
    }else{
      console.log("seconds")
      var seconds = (milisec_diff / 1000);
      return seconds
    }
    
  },
  getDayofWeek: function(day){
    if(day == 0){
      return 'Sunday'
    }else if(day == 1){
      return 'Monday'
    }else if(day == 2){
      return 'Tuesday'
    }else if(day == 3){
      return 'Wednesday'
    }else if(day == 4){
      return 'Thursday'
    }else if(day == 5){
      return 'Friday'
    }else if(day == 6){
      return 'Saturday'
    }
  }

  }
};
</script>