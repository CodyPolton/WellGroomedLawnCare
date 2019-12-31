<template>
  <v-container>
    <v-layout>
      <v-flex>
        <v-btn @click='back'>Back</v-btn>
        <v-btn to="/addaccount">Add Account</v-btn>
              <v-spacer></v-spacer>

        <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>
        <v-data-table :headers="headers" :items="accounts" :search="search" :items-per-page="15" 
                class="elevation-1" @click:row="handleClick">
            <template v-slot:accounts.auto_invoice="{ item }">
              {{ accounts.auto_invoice? 'true' : 'false' }}
            </template>
        </v-data-table>
        
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'

// @ is an alias to /src
export default {
  data() {
    return {
      search: '',
      headers: [
        {
          text: "First Name",
          align: "left",
          value: "f_name"
        },
        { text: "Last Name", align: "left", value: "l_name" },
        { text: "Email", value: "email" },
        { text: "Phone Number", value: "phone_no" },
        { text: "Auto Invoices", value: "auto_invoice" },
      ],
      accounts: [
      ],
    };
  }, 
  created() {
      this.isLoading = true
      axios.get('http://127.0.0.1:8000/api/account/').then((response)=> {
        console.log(response.data)
        response.data.forEach((item)=> {
          if(item.auto_invoice){
            item.auto_invoice = "YES"
          }else{
            item.auto_invoice = "NO"
          }
          this.accounts.push(item)
        })        
      })
      this.isLoading = false
  },
  methods: {
      handleClick: function(value){
          console.log(value)
          this.$router.push('/account/' + value.accountid);
          
      },
      back: function(){
          this.$router.go(-1)
      }
  }
};
</script>