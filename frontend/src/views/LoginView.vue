<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="bg-white p-6 rounded shadow-md w-96">
      <h1 class="text-xl font-bold mb-4">Login</h1>
      <form @submit.prevent="loginUser">
        <div class="mb-4">
          <label for="username" class="block text-sm font-medium text-gray-700">Username:</label>
          <input id="username" v-model="username" type="text" 
                 class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500" 
                 required />
        </div>
        <div class="mb-4">
          <label for="password" class="block text-sm font-medium text-gray-700">Password:</label>
          <input id="password" v-model="password" type="password" 
                 class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500" 
                 required />
        </div>
        <button type="submit" :disabled="loading" 
                class="w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded disabled:opacity-50">
          Login
        </button>
        <p v-if="errorMessage" class="text-red-500 mt-4 text-sm">{{ errorMessage }}</p>
      </form>
    </div>
  </div>
</template>

<script>
import axios from '../services/axios';
import store from '../store';

export default {
  data() {
    return {
      username: '',
      password: '',
      loading: false,
      errorMessage: '',
    };
  },
  methods: {
    async loginUser() {
      this.loading = true;
      this.errorMessage = '';

      try {
        const response = await axios.post('/login/', {
          username: this.username,
          password: this.password,
        });

        const { access, refresh } = response.data;
        store.dispatch('saveTokens', { access, refresh });
        this.$router.push('/dashboard');
      } catch (error) {
        this.errorMessage = error.response?.data?.detail || 'Login failed.';
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>
