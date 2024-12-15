<template>
    <div>
      <h2>Signup</h2>
      <form @submit.prevent="signup">
        <input v-model="email" placeholder="Email" />
        <input v-model="username" placeholder="Username" />
        <input v-model="password" type="password" placeholder="Password" />
        <input v-model="confirmPassword" type="password" placeholder="Confirm Password" />
        <button type="submit">Signup</button>
      </form>
      <p v-if="error">{{ error }}</p>
    </div>
  </template>
  
  <script>
  import axios from '../services/axios';
  
  export default {
    data() {
      return {
        email: '',
        username: '',
        password: '',
        confirmPassword: '',
        error: null,
      };
    },
    methods: {
      async signup() {
        try {
          await axios.post('/register/', {
            email: this.email,
            username: this.username,
            password: this.password,
            confirm_password: this.confirmPassword,
          });
          this.$router.push('/login');
        } catch (err) {
          this.error = err.response?.data?.message || 'Signup failed';
        }
      },
    },
  };
  </script>
  