
export const state = () => ({
  nameScenario: '',
  articleScenario: '',
  listLocation: [ 
    { nameLocation: 'Локация 1', articleLocation: 'Описание крутой локации №1', unitItems: [] },
    { nameLocation: 'Локация 2', articleLocation: 'Описание крутой локации №2', unitItems: [] },
    { nameLocation: 'Локация 3', articleLocation: 'Описание крутой локации №3', unitItems: [] }
  ]
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

// export const actions = {
//   async saveScenario ({ store, $axios }) {
//     listLocation.map((location) => {
//       const enemies = {};

//       location.unitItems.forEach((unit) => {
//         enemies[unit.unitName] = 1;
//       })

//       return {
//         nameLocation: location.nameLocation,
//         articleLocation: location.articleLocation,
//         enemies: enemies
//       } 
//     })
    
//     await $axios.$post('http://localhost:8888/save_scenario', {
//       nameScenario: state.nameScenario,
//       articleScenario: state.articleScenario,
//       listLocation: state.listLocation,
//       unitItems: state.listLocation[0].unitItems
//     })
//   }
// }

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
