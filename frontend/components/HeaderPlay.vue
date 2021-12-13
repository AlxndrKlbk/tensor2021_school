<template>
  <div class="header">
    <div class="title_scenario">
      Сценарий № 1
    </div>
    <GameListLocation/>
  </div>
</template>

<script>
import GameListLocation from "./GameListLocation.vue";
export default {
    components: { GameListLocation }
}
</script>

<style scoped>
.header {
    position: fixed;
    width: calc(100% - 300px);
    height: 100px;
    left: 300px;
    top: 0px;
    display: flex;
    background: #121212;
    justify-content: space-between;
    align-items: center;
    z-index: 99;
    padding-right: 50px;
}
.title_scenario {
  font-size: 30px;
}
</style>
