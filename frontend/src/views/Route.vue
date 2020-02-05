<template>
  <v-app style="width: 100%; ">
    <v-btn @click="back">Back</v-btn>

    <div id="map" style="width: 100%; height: 90%; position: absolute;">
      <div id="map-canvas" />
    </div>
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
            this.makeRoute()
            console.log(response["routes"]);
            directionsRenderer.setDirections(response);
          } else {
            window.alert("Directions request failed due to " + status);
          }
        }
      );
    },
    back: function() {
      this.$router.go(-1);
    },
    makeRoute: function() {
      console.log("ok");
      response["routes"].forEach(element => {
        element.legs.forEach(element => {
          var address = element.end_address.split(",");
          console.log(address[0]);
          for (var x in this.crewYards) {
            console.log(x.address);
            if (x.address.includes(address[0])) {
              console.log("match");
              this.routeYards.push(x);
            }
          }
        });
      });
      console.log(this.routeYards);
    }
  }
};
</script>