<template>
  <v-app style="width: 100%; ">
    <v-btn @click="back">Back</v-btn>
    <v-tabs background-color="grey accent-4" centered class="elevation-2" dark>
      <v-tab key="map">Map</v-tab>
      <v-tab key="route">Route</v-tab>
      <v-tab-item key="map" >
        <div style="width: 100%; height: 500px;">
          <div id="map" style="width: 100%; height: 90%; position: absolute;">
            <div id="map-canvas" />
          </div>
        </div>
      </v-tab-item>
      <v-tab-item key="route">
        <v-btn @click="route">route</v-btn>
        <v-list dense>
            <v-list-item-group v-model="item" color="primary">
              <v-list-item v-for="(item, i) in routeYards" :key="i" @click='goToYard(item)'>
                <v-list-item-content>
                  <v-list-item-title v-text="item.address"></v-list-item-title>
                </v-list-item-content>
                <v-list-item-action>
                  <v-btn icon>
                    <v-icon color="red lighten-1" >mdi-close</v-icon>
                  </v-btn>
                </v-list-item-action>
              </v-list-item>
            </v-list-item-group>
          </v-list>
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
    console.log(this.crew);

    axios
      .get(process.env.VUE_APP_API_URL + "yardforcrew?crew=" + this.crew)
      .then(response => {
        console.log(response);
        response.data.forEach(item => {
          this.crewYards.push(item);
        });
        console.log(this.crewYards);
        this.initMap();
      });
  },
  mounted() {},
  methods: {
    initMap: function() {
      var self = this;
      GoogleMapsLoader.KEY = "AIzaSyAKCyU_Na3n2DiQ7Z5aJ2OQaET2QHRZw2s";
      GoogleMapsLoader.load(function(google) {
        console.log("1");
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
      var yards = this.crewYards
      var route = this.routeYards;
      for (var x in this.params) {
        if (x != "crewid") {
          var address = { location: this.params[x] };
          waypts.push(address);
        }
      }
      console.log(waypts);
      console.log("3");
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
            console.log(response);
            console.log("ok");
            console.log(yards)
      response["routes"].forEach(element => {
        element.legs.forEach(element => {
          console.log(element.end_address)
          var matched = false
          var address = element.end_address.split(",");
          yards.forEach(x =>{
            if (!matched && x.address.includes(address[0])) {
              console.log(address[0]);
              console.log("match");
              console.log(x);
              route.push(x);
              matched = true
            }
          })
          if(!matched){
            var add2 = element.end_address.split(" ");
            yards.forEach(x =>{
            if (!matched && x.address.includes(add2[0]) && x.address.includes(add2[1])) {
              console.log("match 2");
              console.log(x);
              route.push(x);
              matched = true
            }
            })
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
      console.log(this.routeYards)
    },
    back: function() {
      this.$router.go(-1);
    },
    route: function() {
      
      console.log(this.routeYards);
    },
    goToYard: function(value){
      console.log(value)
      this.$router.push("/yard/" + value.account + "/" + value.yardid);
    }

  }
};
</script>