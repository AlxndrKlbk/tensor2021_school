<template>
<div class="game_list_location">
    <GameCardLocation v-for="locations in locationProp" :locations="locations" />
</div>
  
</template>

<script>
export default {
    props: {
    scenarioProp: {
      type: Object
    }
  },

  data () {
    return {
      locationProp: this.scenarioProp.listLocation
    }
  }
}
</script>

<style>
.game_list_location {
    display: flex;
    justify-items: center;
}
</style>