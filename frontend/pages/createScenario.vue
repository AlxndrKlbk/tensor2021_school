<template>
  <CreateScenario :scenarioProp="scenario"  />
</template>

<script>

export default {
  layout: 'create',
  asyncData ({ params, store, $axios }) {
    const scenario = {
      nameScenario: params.nameScenario,
      articleScenario: params.articleScenario,
      listLocation: store.getters['createScenario/getListLocation']
    }
    return {
      scenario
    }
  },
  data () {
    return {
      scenario: null
    }
  }
}
</script>

<style>

</style>
