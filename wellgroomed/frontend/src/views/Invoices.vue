<template>
  <v-app>
    <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>
    <v-data-table
      :headers="headers"
      :items="invoices"
      :search="search"
      :items-per-page="10"
      class="elevation-1"
      @click:row="handleClick"
    ></v-data-table>
  </v-app>
</template>

<script>
// @ is an alias to /src
export default {
  data() {
    return {
      search: null,
      headers: [
        {
          text: "Invoice Name",
          align: "left",
          sortable: false,
          value: "iname"
        },
        { text: "Month", value: "month" },
        { text: "Type", value: "type" },
        { text: "Approved", value: "approved" },
        { text: "Total", value: "total" }
      ],
      invoices: [
        {
          iname: "First",
          month: "December",
          Type: "Mowing",
          Approved: "Yes",
          Total: "125",
          id: "1"
        }
      ]
    };
  },
  name: "Invoices",
  components: {},
  methods: {
      handleClick: function(value){
          console.log(value)
          this.$router.push('/invoice/' + value.id);
          
      },
  }
};
</script>