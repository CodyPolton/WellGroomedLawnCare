<template>
  <v-container mt-5>
    <v-layout row wrap>
      <v-flex xs3>
        <v-card
          shaped
          color="primary"
          class="white--text d-flex align-center justify-center display-1 pa-5 font-weight-light mb-2"
          height="64"
        >About Us</v-card>
      </v-flex>
      <v-flex xs9></v-flex>
      <v-flex xs8>

          <v-layout row wrap class="px-3">
            <v-card color="grey" class="pa-5">
            <v-flex xs2>
<v-card class="headline green darken-2 white--text text-center">About Us</v-card>
            </v-flex>

            <v-flex xs12>
              <v-card class="px-4 py-2 mt-4">
          This bussiness started 5 years ago with a high school student named Landon Wisswal. Started off in his backyard and as he grew he recruited some friends to help him and now he is working all over town taking care of anything and everything lawncare related.
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
  name: "About",

  data() {
    return {};
  }
};
</script>