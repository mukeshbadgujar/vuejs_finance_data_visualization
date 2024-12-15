<template>
  <div>
    <h1>Logout</h1>
    <button @click="logoutUser">Logout</button>
  </div>
</template>

<script>
import store from '../store';

export default {
  methods: {
    logoutUser() {
      store.commit('logout');
      this.$router.push('/login');
    },
  },
};
</script>
