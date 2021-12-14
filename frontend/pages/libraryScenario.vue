<template>
  <LibraryScenario :scenarioProp="scenario" />
</template>

<script>
import LibraryScenario from '~/components/LibraryScenario.vue'

export default {
  components: { LibraryScenario },

  asyncData ({ store }) {
    const scenario = {
      nameScenario: store.getters['createScenario/getNameScenario']
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
