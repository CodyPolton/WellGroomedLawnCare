<template>
  <v-app>
    <v-btn @click='back'>Back</v-btn>
    <v-form ref="form" v-model="valid">
      <span>Enter yard information:</span>
      <v-text-field v-model="address" :counter="40" :rules="rule" label="Address" required></v-text-field>
      <v-text-field v-model="zipcode" :counter="5" :rules="zipRules" type='number' label="Zip Code" required></v-text-field>
      <v-text-field v-model="city" :counter="40" :rules="rule" label="City" required></v-text-field>
      <v-select
        v-model="state"
        :items="states"
        :rules="[v => !!v || 'State is required']"
        label="State"
        required
      ></v-select>
      <v-text-field v-model="mowprice" :counter="5" type='number' label="Mow Price" required></v-text-field>
       

      <v-btn :disabled="!valid" color="success" class="mr-4">Create Yard</v-btn>
    </v-form>
  </v-app>
</template>

<script>
// @ is an alias to /src

 

export default {
  name: "AddYard",
  data (){
      return {
        address: null,
        city: null,
        state: null,
        zipcode: null,
        mowprice: null,
        states: ['MO','AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN',
        'IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MT','NE','NV','NH',
        'NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT', 'VT', 'VA',
        'WA','WV','WI','WY'        
        ],
        rules: {
            required: value => !!value || 'Required.',
        },
        rule: [
        v => !!v || 'Required',
        v => (v && v.length <= 40) || 'Entry must be less than 40 characters',
        ],
        zipRules: [
        v => !!v || 'Required',
        v => (v && v.length == 5 ) || 'Zip code must be 5 numbers',
        ],
        valid: true

      }
    },
    components: {},
    methods: {
        back: function(){
          this.$router.go(-1)
      }
    }
};
</script>