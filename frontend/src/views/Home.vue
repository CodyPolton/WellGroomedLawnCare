<template>
  <v-container pt-0>
    <v-layout row wrap>
      <v-flex xs12 mb-3>
        <v-card raised color="green darken-4">
          <v-img height="350" src="../assets/grass.jpg">
            <v-container fill-height>
              <v-layout row wrap fill-height>
                <v-flex xs1></v-flex>
                <v-flex xs4 class="d-flex align-center">
                  <v-layout row wrap>
                    <v-flex xs12 class="py-3">
                      <v-card shaped color="green darken-3">
                        <v-card-title
                          class="d-flex white--text justify-center headline font-weight-light"
                        >Spring is here.</v-card-title>
                      </v-card>
                    </v-flex>
                    <v-flex xs12 class="py-3">
                      <v-card shaped color="green darken-3">
                        <v-card-title
                          class="d-flex white--text justify-center headline font-weight-light"
                        >It's time to take care of that lawn.</v-card-title>
                      </v-card>
                    </v-flex>
                    <v-flex xs12 class="py-3">
                      <v-card shaped color="white">
                        <v-card-title
                          class="d-flex primary--text justify-center headline font-weight-light"
                        >
                          Choose
                          <span class="font-weight-bold pl-1">Well-Groomed Lawn Care.</span>
                        </v-card-title>
                      </v-card>
                    </v-flex>
                  </v-layout>
                </v-flex>
                <v-flex xs1></v-flex>
                <v-flex xs6 class="d-flex align-center justify-center mb-5">
                  <v-img contain class="mb-5 pb-5" height="300" src="../assets/WellGroomedLogo.png"></v-img>
                </v-flex>
              </v-layout>
            </v-container>
          </v-img>
        </v-card>
      </v-flex>
      <v-flex xs12 mx-3 mt-1>
        <v-layout fill-height row class="d-flex justify-center">
          <v-flex xs12 mb-4>
            <v-card raised color="primary" class="services-card d-flex justify-center">
              <v-card-title class="white--text display-1 font-weight-light">Check Out Our Services!</v-card-title>
            </v-card>
          </v-flex>

          <v-flex xs4>
            <v-card hover ripple class="d-flex ml-4" link to="/landscaping">
              <v-img
                height="300"
                class="white--text d-flex align-end"
                src="https://media.istockphoto.com/photos/manicured-house-and-garden-picture-id149360161?k=6&m=149360161&s=612x612&w=0&h=6gIU-Q4S_9NPwPSUG-iYFSoJmD3UrXH66rXCE5vQqOg="
              >
                <v-card
                  tile
                  class="py-2 green--text display-1 text-center"
                  raised
                  color="white"
                >Landscaping</v-card>
              </v-img>
            </v-card>
          </v-flex>

          <v-flex xs4>
            <v-card hover ripple class="d-flex mx-4" link to="/mowing">
              <v-img
                height="300"
                class="white--text d-flex align-end"
                src="https://thumbs.dreamstime.com/b/lawn-mower-commercial-green-45847516.jpg"
              >
                <v-card
                  tile
                  class="py-2 green--text display-1 text-center"
                  raised
                  color="white"
                >Mowing</v-card>
              </v-img>
            </v-card>
          </v-flex>
          <v-flex xs4>
            <v-card hover ripple class="d-flex mr-4" link to="/yardcare">
              <v-img
                height="300"
                class="white--text d-flex align-end justify-center"
                src="https://media.wkyc.com/assets/WKYC/images/561246520/561246520_360x203.png"
              >
                <v-card
                  tile
                  class="py-2 green--text display-1 text-center"
                  raised
                  color="white"
                >Yard Care</v-card>
              </v-img>
            </v-card>
          </v-flex>
        </v-layout>
      </v-flex>
      <v-flex xs12 mx-3 mt-4>
        <v-layout fill-height row class="d-flex pb-5">
          <v-flex xs6 offset-xs3 mb-0>
            <v-card raised color="primary" class="services-card d-flex justify-center">
              <v-card-title
                class="white--text display-1 font-weight-light"
              >Meet Our Satisfied Customers!</v-card-title>
            </v-card>
          </v-flex>

          <v-flex xs6 offset-xs3 class="elevation-5">
            <v-list>
              <v-list-item v-for="item in items" :key="item.title">
                <v-list-item-avatar class="ml-5">
                  <v-img class="ml-5" :src="item.avatar"></v-img>
                </v-list-item-avatar>
                <v-list-item-icon>
                  <v-rating v-model="rating" class="px-5"></v-rating>
                </v-list-item-icon>

                <v-list-item-content class="pl-5">
                  <v-list-item-title class="pl-5" v-text="item.title"></v-list-item-title>
                  <v-list-item-subtitle class="pl-5" v-text="item.text"></v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
// @ is an alias to /src
export default {
  name: "Home",
  components: {},
  data() {
    return {
      items: [
        {
          icon: true,
          title: "Jason Oner",
          avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
          text: "Amazing service!"
        },
        {
          title: "Travis Howard",
          avatar: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
          text: "They come by every month!"
        },
        {
          title: "Ali Connors",
          avatar: "https://cdn.vuetifyjs.com/images/lists/3.jpg",
          text: "Love their work!"
        },
        {
          title: "Cindy Baker",
          avatar: "https://cdn.vuetifyjs.com/images/lists/4.jpg",
          text: "Great company!"
        }
      ],
      rating: 5
    };
  }
};
</script>
 