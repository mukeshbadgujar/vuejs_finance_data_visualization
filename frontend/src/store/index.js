import { createStore } from 'vuex';

export default createStore({
  state: {
    accessToken: null,
    refreshToken: null,
  },
  mutations: {
    setAccessToken(state, token) {
      state.accessToken = token;
      localStorage.setItem('accessToken', token);
    },
    setRefreshToken(state, token) {
      state.refreshToken = token;
      localStorage.setItem('refreshToken', token);
    },
    logout(state) {
      state.accessToken = null;
      state.refreshToken = null;
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
    },
  },
  actions: {
    initializeTokens({ commit }) {
      const accessToken = localStorage.getItem('accessToken');
      const refreshToken = localStorage.getItem('refreshToken');
      if (accessToken && refreshToken) {
        commit('setAccessToken', accessToken);
        commit('setRefreshToken', refreshToken);
      }
    },
    saveTokens({ commit }, { access, refresh }) {
      commit('setAccessToken', access);
      commit('setRefreshToken', refresh);
    },
    logout({ commit }) {
      commit('logout');
    },
  },
});
