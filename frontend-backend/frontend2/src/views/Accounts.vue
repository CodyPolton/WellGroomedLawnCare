<template>
  <v-container>
    <v-layout>
      <v-flex>
        <v-btn @click='back'>Back</v-btn>
        <v-btn to="/addaccount">Add Account</v-btn>
              <v-spacer></v-spacer>

        <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>
        <v-data-table :headers="headers" :items="accounts" :search="search" :items-per-page="10" 
                class="elevation-1" @click:row="handleClick">
            
        </v-data-table>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
// @ is an alias to /src
export default {
  data() {
    return {
      search: '',
      headers: [
        {
          text: "First Name",
          align: "left",
          sortable: false,
          value: "fname"
        },
        { text: "Last Name", align: "left", value: "lname" },
        { text: "Email", value: "email" },
        { text: "Phone Number", value: "phone" },
        { text: "Auto Invoices", value: "auto" },
      ],
      accounts: [
        {
          fname: "Cody",
          lname: "Polton",
          email: "test@gmail.com",
          phone: "573 489-3326",
          auto: "Yes",
          id: "1"
        },
        {
          fname: "Cody2",
          lname: "Polton",
          email: "test@gmail.com",
          phone: "573 489-3326",
          auto: "No",
          id: "2"
        },
      ]
    };
  }, 
  methods: {
      handleClick: function(value){
          console.log(value)
          this.$router.push('/account/' + value.id);
          
      },
      back: function(){
          this.$router.go(-1)
      }
  }
};
</script>