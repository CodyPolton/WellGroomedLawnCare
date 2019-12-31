<template>
  <v-container>
    <v-layout>
      <v-flex>
        <v-expansion-panels>
          <v-expansion-panel>
            <v-expansion-panel-header>Job Types</v-expansion-panel-header>
            <v-expansion-panel-content> 
                <v-list>
                    <template v-for="(item) in items">
                        <v-list-item :key="item.job_type">
                            <v-icon color="yellow">
                              minus-square
                            </v-icon>
                        </v-list-item>
                    </template>
                </v-list>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
// @ is an alias to /src
export default {
  name: "Configuration",
  components: {}, 
  data() {
    return {
        jobType: [],
        
        
    }
  },
};
</script>