<template>
  <div class="header">
      <div class="title_scenario">
          Сценарий № 1
      </div>
      <div class="list_location">
        <CardLocation/>
        <CardLocation/>
        <CardLocation/>
      </div>
        
  </div>
</template>

<script>
import CardLocation from "./CardLocation.vue";
export default {
    
}
</script>

<style>
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
}



</style>