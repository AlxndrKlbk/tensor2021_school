<template>
  <div class="library_scenario">
    <CardScenario v-for="item in items" :key="item.id" :item="item" />
  </div>
</template>

<script>
export default {

  props: {
    itemsProp: {
      type: Array,
      default: () => []
    }
  },
  data () {
    return {
      items: this.itemsProp
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
