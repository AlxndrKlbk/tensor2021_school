<template>
  <SettingGame :scenarioProp="scenario" />
</template>

<script>
import SettingGame from '~/components/SettingGame.vue'
export default {
  components: { SettingGame },
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
