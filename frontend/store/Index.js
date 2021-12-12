import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


const store = () => Vuex.Store({
  state: {
    nameScenario: '',
    articleScenario: '',
    listLocation: [],
  },

  getters: {
    getNameScenario: (state) => {
      return state.nameScenario;
    }
  },

  mutations: {
    increment(state, objectData) {
      state.nameScenario = objectData.nameScenario
    },

    addLocation(state, objectData) {
        state.listLocation.push(objectData.location)
    }
  }
})

export default store