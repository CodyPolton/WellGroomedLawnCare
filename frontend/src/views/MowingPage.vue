<template>
  <v-container mt-5>
    <v-layout row wrap>
      <v-flex xs3>
        <v-card
          shaped
          color="primary"
          class="white--text d-flex align-center justify-center display-1 pa-5 font-weight-light mb-2"
          height="64"
        >Mowing</v-card>
      </v-flex>
      <v-flex xs9></v-flex>
      <v-flex xs8>

          <v-layout row wrap class="px-3">
            <v-card color="grey" class="pa-5">
            <v-flex xs3>
<v-card class="headline px-2 green darken-2 white--text">Lawn Mowing</v-card>
            </v-flex>

            <v-flex xs12>
              <v-card class="px-4 py-2 mt-4">
         Looking to maximize your lawn’s potential? Well Groomed Lawncare teams maintain turf ranging all sizes. We serve small homes in the city to some of Columbia’s largest, most-demanding commercial properties. We utilize industry-leading technology to back up our highly trained crews. The brand was built in lawn mowing and we are proud of our ability to consistently exceed our customers’ expectations in lawn care. Our crews are outfitted with late-model equipment specific to maintaining any type of lawn, no matter how large or small. If your yard is doomed call Well Groomed!
</v-card>
            </v-flex>
            </v-card>
          </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: "Mowing",

  data() {
    return {};
  }
};
</script>