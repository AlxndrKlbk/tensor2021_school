import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const createScenario = () => new Vuex.Store({
  state: {
    nameScenario: '',
    articleScenario: '',
    listLocation: [
      {
        nameLocation: 'Локация1',
        articleLocation: 'dsiofpsdofpsdifpisdpfisdpifpsdifpsidpfisdpfisdpifpsdif',
        unitItems: [
          { unitDamage: 34, unitDifficult: 34, unitHealth: 324, unitName: 'asddfgdfgdfgfe4w' },
          { unitDamage: 32, unitDifficult: 24, unitHealth: 3166, unitName: 'asdasddfgdfg' },
          { unitDamage: 123, unitDifficult: 33, unitHealth: 32234, unitName: 'asdafdgdfgdfw' }
        ]
      }
    ]
  },

  getters: {
    getNameScenario: (state) => {
      return state.nameScenario
    }
  },

  mutations: {
    setnameScenario (state, nameScenario) {
      state.nameScenario = nameScenario
    },
    setarticleScenario (state, articleScenario) {
      state.articleScenario = articleScenario
    }
  }
})

export default createScenario
