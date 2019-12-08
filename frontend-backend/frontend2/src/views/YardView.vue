<template>
  <v-container>
    <v-layout>
        <v-btn @click='back'>Back</v-btn>
      <v-flex>Yard id = {{id}}</v-flex>
    </v-layout>
  </v-container>
</template>

<script>
// @ is an alias to /src
export default {
  data() {
    return {
      id: null
    };
  },
  name: "Crews",
  components: {},
  created() {
    this.id = this.$route.params.id;
  },
  methods: {
      back: function(){
          this.$router.go(-1)
      }
  }
};
</script>