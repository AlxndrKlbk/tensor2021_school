<template>
  <div class="play_game">
    <div class="article_scenario">
      <div class="article_scenario_title">
        Описание
      </div>
      <div class="article_scenario_container">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. A nesciunt voluptatibus dolor nisi deserunt asperiores inventore quas, commodi ipsa aliquid tempore quisquam dicta officiis quo, laborum assumenda. Voluptates, reprehenderit. Fugit, debitis nisi assumenda quo a iusto, ad ipsum consequatur perferendis corrupti, numquam saepe optio dolores incidunt ea delectus quia ab ducimus quibusdam sint. Doloremque possimus Lorem ipsum dolor sit amet consectetur adipisicing elit. A nesciunt voluptatibus dolor nisi deserunt asperiores inventore quas, commodi ipsa aliquid tempore quisquam dicta officiis quo, laborum assumenda. Voluptates, reprehenderit. Fugit, debitis nisi assumenda quo a iusto, ad ipsum consequatur perferendis corrupti, numquam saepe optio dolores incidunt ea delectus quia ab ducimus quibusdam sint. Doloremque possimus Lorem ipsum dolor sit amet consectetur adipisicing elit. A nesciunt voluptatibus dolor nisi deserunt asperiores inventore quas, commodi ipsa aliquid tempore quisquam dicta officiis quo, laborum assumenda. Voluptates, reprehenderit. Fugit, debitis nisi assumenda quo a iusto, ad ipsum consequatur perferendis corrupti, numquam saepe optio dolores incidunt ea delectus quia ab ducimus quibusdam sint. Doloremque possimus
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
    components: { GamePanelUnit }
}
</script>

<style scoped>
.play_game {
    padding-top: 110px;
    padding-left: 310px;
}
.article_scenario{
    position:absolute;
    top: 112px;
    left: 310px;
    color: white;
    margin-right: 50px;
}

.article_scenario_title {
    font-size: 25px;
    margin-bottom: 13px;
}

.article_scenario_container {
    margin-right: 30px;
    padding-top: 15px;
    padding-bottom: 15px;
    border-top: 1px solid white;
    border-bottom: 1px solid white;
}

.list_location_scenario {
    color: white;
    margin-top: 10px;
}

.list_location__title {
    font-size: 20px;
    margin-bottom: 15px;
}

.list_location_container {
    display: flex;
    flex-wrap: wrap;
    gap: 25px;
}
</style>
