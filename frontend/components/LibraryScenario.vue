<template>
  <div class="library_scenario">
    <CardScenario v-for="scenario in scenarioProp" :scenarioProp="scenarios" />
  </div>
</template>

<script>
export default {

  props: ['scenarioProp'],
  data () {
    return {
      scenarios: this.scenarioProp
    }
  }
}
</script>

<style>
.library_scenario {
    padding-left: 350px;
    padding-top: 110px;
    padding-right: 50px;
    display: flex;
    flex-wrap: wrap;
}
</style>
