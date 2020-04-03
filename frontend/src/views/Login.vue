<template>
  <v-container
    class="fill-height"
    fluid
  >
    <v-row
      align="center"
      justify="center"
    >
      <v-col
        cols="12"
        sm="8"
        md="4"
      >
        <v-card class="elevation-12">
          <v-toolbar
            color="primary"
            dark
            flat
          >
            <v-toolbar-title>Login</v-toolbar-title>
            <v-spacer />
          </v-toolbar>
          <v-card-text>
            <v-form
              ref="form"
              v-model="valid"
              >
              <v-container>

                <v-text-field
                  v-model="credentials.username"
                  :counter="70"
                  :rules="rules.username"
                  label="username"
                  maxlength="70"
                  required
                />

                <v-text-field
                  v-model="credentials.password"
                  :counter="20"
                  :rules="rules.password"
                  type="password"
                  label="password"
                  maxlength="20"
                  required
                />

              </v-container>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer />
            <v-btn
              color="primary"
              @click="login"
              :disabled="!valid">Login</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import router from '../router';

export default {
    name: 'Login',

  data() {
    return {
    credentials: {
      username: "admin",
      password: "Groomed1!"
    },
    valid: true,
loading:false,
        rules: {
          username: [
            v => !!v || "Username is required",
            v => (v && v.length > 0) || "A username must be more than 3 characters long",
            v => /^[A-Za-z0-9_]+$/.test(v) || "A username can only contain letters and digits"
          ],
          password: [
            v => !!v || "Password is required",
            v => (v && v.length > 7) || "The password must be longer than 7 characters"
          ]
        }
    };
  },
  methods: {
    login() {
            if (this.$refs.form.validate()) {
              this.$store.dispatch('obtainToken', this.credentials);
            }
    }
  }
};
</script>