import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = () => new Vuex.Store({
  state: {
    nameScenario: '',
    articleScenario: '',
    listLocation: [
      { nameLocation: 'Локация1' }
    ]
  },

  getters: {
    getNameScenario: (state) => {
      return state.nameScenario
    }
  },

  mutations: {
    increment (state, objectData) {
      state.nameScenario = objectData.nameScenario
    },

    addLocation (state, objectData) {
      state.listLocation.push(objectData.location)
    }
  },

  modules: {

  }
})

export default store
