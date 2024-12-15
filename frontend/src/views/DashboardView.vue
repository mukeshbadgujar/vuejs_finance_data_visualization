<template>
  <div class="flex flex-col h-screen">
    <!-- Header -->
    <header class="bg-gray-800 text-white px-4 py-3 flex justify-between items-center shadow">
      <div class="flex items-center space-x-4">
        <button @click="toggleSidebar" class="text-white focus:outline-none lg:hidden">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
        <h1 class="text-xl font-bold">Dashboard</h1>
      </div>
      <button @click="logout" class="bg-red-500 hover:bg-red-600 px-4 py-2 rounded text-sm font-medium">
        Logout
      </button>
    </header>

    <div class="flex flex-1">
      <!-- Sidebar -->
      <aside
        :class="[
          'bg-gray-700 text-white w-64 lg:w-64 lg:static fixed z-20 inset-y-0 transform lg:translate-x-0 transition-transform',
          isSidebarOpen ? 'translate-x-0' : '-translate-x-full'
        ]"
        class="lg:block"
      >
        <nav class="flex flex-col h-full">
          <div class="p-4 bg-gray-800">
            <span class="text-lg font-semibold">Menu</span>
          </div>
          <ul class="flex-1 space-y-2 p-4">
            <li><a href="#" class="block px-4 py-2 rounded hover:bg-gray-600">Home</a></li>
            <li><a href="#" class="block px-4 py-2 rounded hover:bg-gray-600">Profile</a></li>
            <li><a href="#" class="block px-4 py-2 rounded hover:bg-gray-600">Settings</a></li>
          </ul>
        </nav>
      </aside>

      <!-- Main Content -->
      <main class="flex-1 overflow-y-auto bg-gray-100 p-6">
        <div class="bg-white text-gray-800 shadow rounded-lg p-6">
          <h2 class="text-xl font-semibold mb-4">Welcome to the Dashboard!</h2>
          <p class="text-gray-700">Your main content goes here.</p>
        </div>
      </main>
    </div>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white text-center py-3">
      &copy; 2024 My Dashboard. All rights reserved.
    </footer>
  </div>
</template>

<script>
import store from "../store";

export default {
  data() {
    return {
      isSidebarOpen: true, // Sidebar state
    };
  },
  methods: {
    toggleSidebar() {
      this.isSidebarOpen = !this.isSidebarOpen;
    },
    logout() {
      store.dispatch("logout");
      this.$router.replace("/login");
    },
  },
};
</script>

<style scoped>
/* Add any additional custom styles if necessary */
</style>
