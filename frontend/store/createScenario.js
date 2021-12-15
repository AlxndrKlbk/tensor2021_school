
export const state = () => ({
  nameScenario: '',
  articleScenario: '',
  listLocation: []
})

export const mutations = {
  setDataScenario (state, { nameScenario, articleScenario }) {
    state.nameScenario = nameScenario,
    state.articleScenario = articleScenario
  },

  setLocation (state, objectLocation) {
    state.listLocation.push( objectLocation )
  }


}

export const actions = {
  
}

export const getters = {
  getNameScenario: (state) => {
    return state.nameScenario
  },
  getListLocation: (state) => {
    return state.listLocation
  },
  getScenario: (state) => {
    return state
  }
}
