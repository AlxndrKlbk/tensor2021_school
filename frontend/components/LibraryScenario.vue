<template>
  <div class="library_scenario">
    <CardScenario :scenarioProp="scenario" />
  </div>
</template>

<script>
export default {

  props: ['scenarioProp'],
  data () {
    return {
      scenario: this.scenarioProp
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
