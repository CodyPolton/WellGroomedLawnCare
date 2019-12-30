<template>
  <v-app>
    <v-btn @click='back'>Back</v-btn>
    <v-form ref="form" v-model="valid">
      <span>Enter account information:</span>
      <v-text-field v-model="account.f_name" :counter="40" :rules="rule" label="First Name" required></v-text-field>
      <v-text-field v-model="account.l_name" :counter="40" :rules="rule" label="Last Name" required></v-text-field>
      <v-text-field v-model="account.address" :counter="40" :rules="rule" label="Address" required></v-text-field>
      <v-text-field v-model="account.zip_code" :counter="5" :rules="zipRules" type='number' label="Zip Code" required></v-text-field>
      <v-text-field v-model="account.city" :counter="40" :rules="rule" label="City" required></v-text-field>
      <v-select
        v-model="account.state"
        :items="states"
        :rules="[v => !!v || 'State is required']"
        label="State"
        required
      ></v-select>
      <vue-tel-input v-model="account.phone_no" placeholder='Enter phone number'></vue-tel-input>
      <v-text-field v-model="account.email" :counter="40" :rules="[]" label="Email"></v-text-field>
      <v-checkbox v-model="account.auto_invoice" color="green">
          <template v-slot:label>
                Automatic Invoices
              </template>
      </v-checkbox>
      <v-checkbox v-model="account.sameaddress" color="green">
          <template v-slot:label>
                Does the account have a yard with the same address
              </template>
      </v-checkbox>

      

      <v-btn :disabled="!valid" color="success" class="mr-4" @click='addAccount'>Create Account</v-btn>
    </v-form>
  </v-app>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import router from '../router';
 

export default {
  name: "AddAccounts",
  data (){
      return {
        account: {
          f_name: null,
          l_name: null,
          address: null,
          zip_code: null,
          city: null,
          state: null,
          phone_no: "",
          email: "",
          auto_invoice: false,
          sameaddress: null,
        },
        
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
      },
      addAccount: function(){
        axios.post('http://127.0.0.1:8000/api/account/', this.account).then((response) =>{
          console.log(response.data)
          router.replace('/accounts')
        })
      }

    }
};
</script>