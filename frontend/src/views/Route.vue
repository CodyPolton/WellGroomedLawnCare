<template>
  <v-app style="width: 100%; ">
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>

      <v-tab key="map">Map</v-tab>
      <v-tab key="route">Route</v-tab>
      <v-tab-item key="map">
        <div style="width: 100%; height: 1000px;">
          <div id="map" style="width: 100%; height: 90%; position: absolute;">
            <div id="map-canvas" />
          </div>
        </div>
      </v-tab-item>
      <v-tab-item key="route">
        <v-continer>
          <v-layout row class="d-flex justify-center">
<v-flex xs3 py-5>
          <v-card
            class="pa-4 display-2 white--text d-flex justify-center font-weight-light"
            color="primary"
          >Route</v-card>
        </v-flex>
            <v-flex xs12 class="px-5 mx-5">
              <v-row justify="center">
                <v-flex xs6>
<v-list tile dense color="grey">
          <v-list-item-group v-model="item" color="primary">
            <v-list-item v-for="(item, i) in routeYards" :key="i" @click="goToYard(item)">
              <v-list-item-content>
                <v-list-item-title class="white--text subtitle-1 pl-5 ml-5" v-text="item.address"></v-list-item-title>
              </v-list-item-content>
              <v-list-item-action class="mr-5 pr-5">
                <v-btn icon @click="individualRoute(item)">
                  <v-icon color="white">mdi-google-maps</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
                </v-flex>
              </v-row>

            </v-flex>
          </v-layout>
        </v-continer>

      </v-tab-item>
    </v-tabs>
  </v-app>
</template>

<script>
import GoogleMapsLoader from "google-maps";
import axios from "axios";
// @ is an alias to /src
export default {
  name: "Route",
  components: {},
  data() {
    return {
      crew: null,
      item: null,
      params: null,
      crewYards: [],
      routeYards: [],
      origin: "721 North Denninghoff Rd, Columbia, MO"
    };
  },
  created() {
    this.params = this.$route.query;
    this.crew = this.params.crewid;

    axios
      .get(process.env.VUE_APP_API_URL + "yardforcrew?crew=" + this.crew)
      .then(response => {
        response.data.forEach(item => {
          this.crewYards.push(item);
        });
        this.initMap();
      });
  },
  mounted() {},
  methods: {
    initMap: function() {
      var self = this;
      GoogleMapsLoader.KEY = "AIzaSyAKCyU_Na3n2DiQ7Z5aJ2OQaET2QHRZw2s";
      GoogleMapsLoader.load(function(google) {
        var directionsService = new google.maps.DirectionsService();
        var directionsRenderer = new google.maps.DirectionsRenderer();
        var map = new google.maps.Map(document.getElementById("map"), {
          zoom: 10,
          center: { lat: 38.9517, lng: -92.3341 }
        });
        directionsRenderer.setMap(map);
        self.calculateAndDisplayRoute(directionsService, directionsRenderer);
      });
    },
    calculateAndDisplayRoute: function(directionsService, directionsRenderer) {
      var waypts = [];
      var yards = this.crewYards;
      var route = this.routeYards;
      for (var x in this.params) {
        if (x != "crewid") {
          var address = { location: this.params[x] };
          waypts.push(address);
        }
      }
      directionsService.route(
        {
          origin: { query: this.origin },
          destination: { query: this.origin },
          waypoints: waypts,
          optimizeWaypoints: true,
          travelMode: "DRIVING"
        },
        function(response, status) {
          if (status === "OK") {
            response["routes"].forEach(element => {
              element.legs.forEach(element => {
                var matched = false;
                var address = element.end_address.split(",");
                yards.forEach(x => {
                  if (!matched && x.address.includes(address[0])) {
                    route.push(x);
                    matched = true;
                  }
                });
                if (!matched) {
                  var add2 = element.end_address.split(" ");
                  yards.forEach(x => {
                    if (
                      !matched &&
                      x.address.includes(add2[0]) &&
                      x.address.includes(add2[1])
                    ) {
                      route.push(x);
                      matched = true;
                    }
                  });
                }
              });
            });
            console.log(response["routes"]);
            directionsRenderer.setDirections(response);
          } else {
            window.alert("Directions request failed due to " + status);
          }
        }
      );
      // this.routeYards = route
      console.log(this.routeYards);
    },
    back: function() {
      this.$router.go(-1);
    },
    route: function() {
      console.log(this.routeYards);
    },
    goToYard: function(value) {
      this.$router.push("/yard/" + value.account + "/" + value.yardid);
    },
    individualRoute: function(yard) {
      var address = yard.address + ", " + yard.city + ", " + yard.zip_code;
      window.open("https://google.com/maps/dir//" + address, "_blank");
    }
  }
};
</script>