import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = () => Vuex.Store( {
    state: {
        nameScenario: 'asdasdasdasd',
        articleScenario: '',
        listLocation: [],
    },

    getters: {
        getNameScenario: (state) => {
            return state.nameScenario;
        }
    },

    mutations: {
        increment (state) {
            
        }
    }
})

export default store