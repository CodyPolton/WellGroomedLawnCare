<template>
  <v-app>
      <h1>Day 1</h1>
      <v-btn @click="route(addresses)">Route</v-btn>
      <ul id="example-1" >
        <li v-for="address in addresses">
         {{address.address}}
        </li>
    </ul>
      
  </v-app>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'ScheduleView',
  components: {
  },
  data (){
      return {
          addresses: [
              {
                address: "810 Cambridge Dr., Columbia, MO"
              },
              {
                address: "2909 Falling Leaf Ln, Columbia, MO"
              },
              {
                address: "18001 Old Hwy 63 North, Sturgeon, MO"
              }

          ]
      }
  },
  methods: {
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
          this.$router.push(url)
      }
  }
};
</script>