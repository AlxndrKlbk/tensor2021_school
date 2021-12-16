<template>
  <div>
    <HeaderPlay :scenarioProp="scenario" />
    <PlayGame :scenarioProp="scenario" />
  </div>
</template>

<script>
import HeaderPlay from '~/components/HeaderPlay.vue'
export default {
  components: { HeaderPlay },
  layout: 'play',
  asyncData ({ store }) {
    const scenario = store.getters['createScenario/getScenario']
    return { scenario }
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
