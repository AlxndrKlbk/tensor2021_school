
export const state = () => ({
  nameScenario: 'adsasdasd',
  articleScenario: '',
  listLocation: [
    {
      nameLocation: 'Локация1',
      articleLocation: '1111111111111111111111111111111111111111111111111111111111111111111',
      // unitItems: [
      //   { unitDamage: 34, unitDifficult: 34, unitHealth: 324, unitName: '1', amountUnit: 5 },
      //   { unitDamage: 32, unitDifficult: 24, unitHealth: 3166, unitName: '2', amountUnit: 2 },
      //   { unitDamage: 123, unitDifficult: 33, unitHealth: 32234, unitName: '3', amountUnit: 1 }
      // ]
    },
    {
      nameLocation: 'Локация2',
      articleLocation: '22222222222222222222222222222222222222222222222222222222222222222222',
    },
    {
      nameLocation: 'Локация3',
      articleLocation: '33333333333333333333333333333333333333333333333333333333333333333333',
    },
  ]
})

export const mutations = {
  setnameScenario (state, nameScenario) {
    state.titleScenario = nameScenario
  },
  setarticleScenario (state, articleScenario) {
    state.articleScenario = articleScenario
  },

  addLocation(state, location) {
    state.listLocation.push(location)
  },


}

export const actions = {
  
}

export const getters = {
  getNameScenario: (state) => {
    return state.nameScenario
  },
  
  getListLocation: (state) => {
    return state.listLocation
  }
}
