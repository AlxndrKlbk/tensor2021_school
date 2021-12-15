<template>
  <CreateScenario :scenarioProp="scenario"  />
</template>

<script>

export default {
  layout: 'create',
  asyncData ({ params, store, $axios }) {
    // const scenario = {
    //   nameScenario: params.nameScenario,
    //   articleScenario: params.articleScenario,
    //   listLocation: store.getters['createScenario/getListLocation']
    // }
    const scenario = $axios.$get('http://127.0.0.1:8888/scenarios_list')
    return scenario
  },
}

</script>

<style>

</style>
