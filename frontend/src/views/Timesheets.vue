<template>
  <v-app>
    <v-container>
      <v-row justify="center">
        <v-flex xs3 py-5>
          <v-card
            class="pa-4 display-2 white--text d-flex justify-center font-weight-light"
            color="primary"
          >Timesheet</v-card>
        </v-flex>
        <v-flex xs12 offset-xs0>
          <v-layout row wrap>
            <v-flex xs8 offset-xs2>
              <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
                <v-tab key="add">Status</v-tab>
                <v-tab-item class="d-flex justify-center" key="add">
                  <v-layout row wrap class="d-flex justify-center py-5">
                    <v-flex xs4>
                      <v-card
                        v-if="timesheet.status == 'Paused'"
                        class="d-flex justify-center pa-4 mb-4"
                      >Clocked in at : {{timesheet.start_time}}</v-card>
                    </v-flex>
                    <v-flex xs12></v-flex>
                    <v-flex xs4>
                      <v-card
                        class="d-flex justify-center pa-4 mb-4"
                        v-if="timesheet.status == 'Paused'"
                      >Break Started at : {{timesheet.pause_time}}</v-card>
                    </v-flex>
                    <v-flex xs12></v-flex>
                    <v-flex xs4>
                      <v-card
                        class="d-flex justify-center pa-4 mb-4"
                        v-if="timesheet.status == 'Clocked In'"
                      >Clocked in at : {{timesheet.start_time}}</v-card>
                    </v-flex>
                    <v-flex xs12></v-flex>
                    <v-flex xs4>
                      <v-card
                        class="d-flex justify-center pa-4 mb-4"
                        v-if="timesheet.status == 'Clocked In'"
                      >Hours : {{totalHours}}</v-card>
                    </v-flex>
                    <v-flex xs12></v-flex>
                    <v-flex xs4>
                      <v-btn
                        block
                        v-if="timesheet.status =='No Entry' || timesheet.status =='Clocked Out' || add"
                        @click="ClockIn"
                      >Clock In</v-btn>
                    </v-flex>
                    <v-flex xs12></v-flex>
                    <v-flex xs4>
                      <v-card
                        class="d-flex justify-center pa-4 mb-4"
                        v-if="timesheet.status == 'Paused'"
                      >Hours : {{totalHours}}</v-card>
                    </v-flex>
                    <v-flex xs12></v-flex>
                    <v-flex xs4>
                      <v-btn tile block v-if="timesheet.status == 'Clocked In'" @click="pause">Break</v-btn>
                    </v-flex>
                    <v-flex xs12></v-flex>
                    <v-flex xs4>
                      <v-btn
                        tile
                        block
                        v-if="timesheet.status == 'Clocked In'"
                        @click="clockout"
                      >Clock Out</v-btn>
                    </v-flex>
                    <v-flex xs12></v-flex>
                    <v-flex xs4>
                      <v-btn
                        block
                        tile
                        v-if="timesheet.status == 'Paused'"
                        @click="ClockBackIn"
                      >Clock Back In</v-btn>
                    </v-flex>
                  </v-layout>
                </v-tab-item>
                <v-tab key="timesheets">Timesheets</v-tab>

                <v-tab-item key="timesheets">
                  <v-toolbar color="primary">
                    <v-toolbar-title
                      class="white--text"
                    >Payperiod {{payperiodstart}} - {{payperiodend}}</v-toolbar-title>
                  </v-toolbar>
                  <v-data-table
                    :loading="loading"
                    :headers="headers"
                    :items="timesheets"
                    :search="search"
                    :items-per-page="15"
                    class="elevation-1"
                  >
                    <template slot="footer">
                      <td>
                        <strong>Total Hours:</strong>
                      </td>
                      <td class="text-xs-right">{{ totalHour }}</td>
                    </template>
                  </v-data-table>
                </v-tab-item>
              </v-tabs>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-row>
    </v-container>
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
        timesheetid: "",
        payperiodid: "",
        dayofweek: "",
        userid: "",
        start_time: "",
        end_time: null,
        seconds_paused: null,
        pause_time: null,
        hours: null,
        status: null
      },
      totalHour: 0,
      loading: false,
      search: null,
      timesheets: [],
      clockinStatus: null,
      payperiodid: null,
      user_id: this.$store.state.user_id,
      dayofweek: null,
      payperiodstart: null,
      payperiodend: null,

      crew: null,
      item: null,
      params: null,
      headers: [
        { text: "Day of the Week", align: "left", value: "dayofweek" },
        { text: "Start Time", align: "left", value: "start_time" },
        { text: "End Time", value: "end_time" },
        { text: "Break Time(Minutes)", value: "seconds_paused" },
        { text: "Hours", value: "hours" }
      ]
    };
  },
  computed: {
    totalHours() {
      var hours = this.get_time_diff(this.timesheet.start_time, 1);
      if (this.timesheet.seconds_paused) {
        hours -= this.timesheet.seconds_paused / 3600;
      }
      console.log(hours.toFixed(1))
      return hours.toFixed(1);
    }
  },
  created() {
    this.dayofweek = this.getDayofWeek(new Date().getDay());

    console.log(this.dayofweek);
    axios
      .get(process.env.VUE_APP_API_URL + "clockinstatus?userid=" + this.user_id)
      .then(response => {
        console.log(response.data);
        if (response.data.status != "Clocked Out") {
          if (response.data.timesheet) {
            this.timesheet = response.data.timesheet[0];
          }
        }
        this.timesheet.status = response.data.status;

        this.payperiodid = response.data.payperiod.payperiodid;
        this.payperiodstart = this.formatDate(
          response.data.payperiod.startDate
        );
        this.payperiodend = this.formatDate(response.data.payperiod.endDate);

        console.log(this.timesheet);
      });

    axios
      .post(process.env.VUE_APP_API_URL + "gettimesheet/", {
        userid: this.$store.state.user_id
      })
      .then(response => {
        console.log(response.data.timesheet);
        response.data.timesheet.forEach(element => {
          if (element.seconds_paused) {
            element.seconds_paused = element.seconds_paused / 60;
          }
          if (element.hours) {
            element.hours =
              Math.round(
                (element.hours - element.seconds_paused / 60 + Number.EPSILON) *
                  100
              ) / 100;
            console.log(element.hours);
            this.totalHour += element.hours;
            console.log(this.totalHour);
          }
          this.timesheets.push(element);
        });
        console.log(this.timesheets);
        this.totalHour = this.totalHour.toFixed(1);
      })
      .catch(error => {
        console.log(error);
      });
  },
  mounted() {},
  methods: {
    back: function() {
      this.$router.go(-1);
    },
    pause: function() {
      console.log("Break");
      var d = new Date().toLocaleTimeString();
      var full = d.split(" ")
      var time = full[0].split(":")
      if(full[1] == "PM" && time[0] != "12"){
        time[0] = parseInt(time[0]) + 12
        console.log("hi")
      }
      d = time[0]  + ":" + time[1] + ":" + time[2]
      console.log(d);
      this.timesheet.status = "Paused";
      this.timesheet.pause_time = d;
      axios
        .put(
          process.env.VUE_APP_API_URL +
            "timesheet/" +
            this.timesheet.timesheetid +
            "/",
          this.timesheet
        )
        .then(response => {
          console.log(response);
          this.timesheet = response.data;
          this.$notify({
            group: "success",
            title: "You are now on break",
            type: "success"
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    ClockBackIn: function() {
      var seconds = this.get_time_diff(this.timesheet.pause_time, 2);
      console.log(seconds);
      this.timesheet.seconds_paused += seconds;
      this.timesheet.pause_time = null;
      this.timesheet.status = "Clocked In";
      axios
        .put(
          process.env.VUE_APP_API_URL +
            "timesheet/" +
            this.timesheet.timesheetid +
            "/",
          this.timesheet
        )
        .then(response => {
          console.log(response);
          this.timesheet = response.data;
          this.$notify({
            group: "success",
            title: "You are now clocked back in",
            type: "success"
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    ClockIn: function() {
      var d = new Date().toLocaleTimeString();
      var full = d.split(" ")
      var time = full[0].split(":")
      if(full[1] == "PM" && time[0] != "12"){
        time[0] = parseInt(time[0]) + 12
        console.log("hi")
      }
      d = time[0]  + ":" + time[1] + ":" + time[2]
      console.log(d);

      var newTimesheet = {
        payperiodid: this.payperiodid,
        dayofweek: this.dayofweek,
        userid: this.user_id,
        status: "Clocked In",
        start_time: d,
        hours: 0
      };
      console.log(newTimesheet);
      axios
        .post(process.env.VUE_APP_API_URL + "timesheet/", newTimesheet)
        .then(response => {
          console.log(response);
          this.timesheet = response.data;
          this.$notify({
            group: "success",
            title: "You are now clocked in",
            type: "success"
          });
          console.log(this.timesheet)
        })
        .catch(error => {
          console.log(error);
        });
    },
    clockout: function() {
      this.timesheet.status = "Clocked Out";
      var d = new Date().toLocaleTimeString();
      var full = d.split(" ")
      var time = full[0].split(":")
      if(full[1] == "PM" && time[0] != "12"){
        time[0] = parseInt(time[0]) + 12
        console.log("hi")
      }
      d = time[0]  + ":" + time[1] + ":" + time[2]
      this.timesheet.hours = this.get_time_diff(this.timesheet.start_time, 1);
      this.timesheet.end_time = d
      console.log(this.timesheet);
      axios
        .put(
          process.env.VUE_APP_API_URL +
            "timesheet/" +
            this.timesheet.timesheetid +
            "/",
          this.timesheet
        )
        .then(response => {
          console.log(response);
          this.timesheet = {
            timesheetid: "",
            payperiodid: "",
            dayofweek: "",
            userid: "",
            start_time: "",
            end_time: null,
            seconds_paused: null,
            pause_time: null,
            hours: null,
            status: 'Clocked Out'
          };
          this.timesheets.push(response.data)

          this.$notify({
            group: "success",
            title: "You are now off the clock",
            type: "success"
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    get_time_diff: function(datetimeone, mode) {
      console.log("mode" + mode)
      console.log(datetimeone);
      var split = datetimeone.split(":");

      var d = new Date().toLocaleTimeString();
      var full = d.split(" ")
      var time = full[0].split(":")
      if(full[1] == "PM" && time[0] != "12"){
        time[0] = parseInt(time[0]) + 12
        console.log("bumped the time" + time[0])
      }

      var time = full[0].split(":")
      if(full[1] == "PM" && time[0] != "12"){
        time[0] = parseInt(time[0]) + 12
        console.log("bumped the time" + time[0])
      }

      var d1 = new Date();
      var d2 = new Date();
      d1.setHours(split[0]);
      d1.setMinutes(split[1]);
      d2.setHours(time[0]);
      d2.setMinutes(time[1]);

      console.log(d1 + " " + d2);

      var one = new Date(d1).getTime();
      var two = new Date(d2).getTime();

      console.log(one);

      if (isNaN(one)) {
        return "";
      }

      console.log(one + " " + two);

      if (one < two) {
        var milisec_diff = two - one;
      } else {
        var milisec_diff = one - two;
      }
      console.log(milisec_diff)
      if (mode == 1) {
        var hours = (milisec_diff / (1000 * 60 * 60)) % 24;
        return Math.round((hours + Number.EPSILON) * 100) / 100;
      } else {
        console.log("seconds");
        var seconds = milisec_diff / 1000;
        console.log(seconds)
        return seconds;
      }
    },
    getDayofWeek: function(day) {
      if (day == 0) {
        return "Sunday";
      } else if (day == 1) {
        return "Monday";
      } else if (day == 2) {
        return "Tuesday";
      } else if (day == 3) {
        return "Wednesday";
      } else if (day == 4) {
        return "Thursday";
      } else if (day == 5) {
        return "Friday";
      } else if (day == 6) {
        return "Saturday";
      }
    },
    formatDate: function(date) {
      var splitDay = date.split("-");
      return splitDay[1] + "/" + splitDay[2];
    }
  }
};
</script>