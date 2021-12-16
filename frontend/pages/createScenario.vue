<template>
  <CreateScenario :scenarioProp="scenarios"  />
</template>

<script>

export default {
  layout: 'create',
  asyncData ({ params, store, $axios }) {
    const scenarios = {
      nameScenario: params.nameScenario,
      articleScenario: params.articleScenario,
      listLocation: store.getters['createScenario/getListLocation']
    }
    return { scenarios }
  },

  data () {
    return {
      scenarios: null
    }
  }
    // const scenarios = [];
    
    // const scenariosFromBack = await $axios.$get('http://localhost:8888/scenarios_list', {
    //   params: {},
    //   headers: {}
    // })

    // scenariosFromBack.forEach((scenarioFromBack) => {
    //   scenarios.push({
    //     id: scenarioFromBack[0],
    //     nameScenario: scenarioFromBack[1],
    //     articleScenario: scenarioFromBack[2],
    //     listLocation: scenarioFromBack[3]
    //   })
    // }) 

}

</script>

<style>

</style>
