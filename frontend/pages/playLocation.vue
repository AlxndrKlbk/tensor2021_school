<template>
  <div>
      <HeaderPlayLocation :scenarioProp="scenario" />
      <PlayLocation :locationProp="scenario" />
  </div>
</template>

<script>
import HeaderPlayLocation from "~/components/HeaderPlayLocation.vue"
export default {
    layout: "play",
    asyncData({ store }) {
        const scenario = store.getters["createScenario/getScenario"];
        return { scenario };
    },
    data() {
        return {
            scenario: null
        };
    },
    components: { HeaderPlayLocation }
}
</script>

<style>

</style>