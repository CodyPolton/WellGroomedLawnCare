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
      <v-flex xs12>
        <v-card color="grey " class="white--text" height="600">
          <h1>About Us</h1>
          This bussiness started 5 years ago with a high school student named Landon Wisswal. Started off in his backyard and as he grew he recruited some friends to help him and now he is working all over town taking care of anything and everything lawncare related.
        </v-card>
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