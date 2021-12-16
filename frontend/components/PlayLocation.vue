<template>
  <div class="play_game_location">
    <div class="article_location">
      <div class="article_location_title">
        Описание
      </div>
      <div class="article_location_container">
        {{ locationProp.articlelocation }}
      </div>
      <div class="panel_unit_control">
        <GamePanelUnit/>
      </div>
    </div>
  </div>
</template>

<script>
import GamePanelUnit from "./GamePanelUnit.vue";
export default {
    components: { GamePanelUnit },
    props: ['locationProp'],

  data () {
    return {
      locationProp: this.locationProp.listLocation
    }
  }
}
</script>

<style scoped>
.play_game_location {
    padding-top: 110px;
    padding-left: 310px;
}
.article_location{
    position:absolute;
    top: 112px;
    left: 310px;
    color: white;
    margin-right: 50px;
}

.article_location_title {
    font-size: 25px;
    margin-bottom: 13px;
}

.article_location_container {
    margin-right: 30px;
    padding-top: 15px;
    padding-bottom: 15px;
    border-top: 1px solid white;
    border-bottom: 1px solid white;
}

</style>
