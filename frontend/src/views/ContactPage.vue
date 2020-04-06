<template>
  <v-container mt-5>
    <v-layout row wrap>
      <v-flex xs3>
        <v-card
          shaped
          color="primary"
          class="white--text d-flex align-center justify-center display-1 pa-5 font-weight-light mb-2"
          height="64"
        >Contact</v-card>
      </v-flex>
      <v-flex xs12>
        <v-card color="grey " class="white--text" height="600">
          <v-form ref="form" >
          <span>Any question or concerns feel free to send us a message below!</span>
          <v-textarea
            v-model="description"
            :rules="[v => !!v || 'Description is required']"
            label="Questions/conerns here"
            required
          ></v-textarea>
          
          <v-btn :disabled="!description" color="success" class="mr-4" @click="save">Send Inquiry</v-btn>
        </v-form>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: "Contact",

  data() {
    return {
      description: null
    };
  },
  methods: {
    save: function() {
      this.$notify({
            group: "success",
            title: "Inquiry has been sent",
            type: "success"
          })
        
    }
  }
};
</script>