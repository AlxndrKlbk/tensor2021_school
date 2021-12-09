<template>
<div class="setting_game">
  <div class="title_scenario">
      Сценарий 1
  </div>
  <div class="cart_scenario">
      <div class="cart_scenario_cover">
          <img src="../assets/oblojka.png" alt="">
      </div>
      <div class="game_panel">
        <div class="game_panel_control">
            <NuxtLink to="/playGame" class="button_play"><div class="button_play">
                Играть
            </div></NuxtLink>
            <div class="button_add_library">
                Добавить в библиотеку
            </div>
        </div>
        <div class="table_about_scenario">
            <tbody>
                <tr>
                    <th>Автор сценария</th>
                    <td>Иван Иванов</td>
                </tr>
                <tr>
                    <th>Автор публикации</th>
                    <td>Петр Петров</td>
                </tr>
                <tr>
                    <th>Дата выхода</th>
                    <td>21.21.21</td>
                </tr>
                
            </tbody>
        </div>
      </div>
  </div>
  <div class="article_scenario">
      <div class="article_scenario_title">
          Описание
      </div>
      <div class="article_scenario_container">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. A nesciunt voluptatibus dolor nisi deserunt asperiores inventore quas, commodi ipsa aliquid tempore quisquam dicta officiis quo, laborum assumenda. Voluptates, reprehenderit. Fugit, debitis nisi assumenda quo a iusto, ad ipsum consequatur perferendis corrupti, numquam saepe optio dolores incidunt ea delectus quia ab ducimus quibusdam sint. Doloremque possimus vitae repellat ut. Doloribus iure saepe placeat necessitatibus adipisci. Quo, optio magnam? Unde qui culpa ipsa tempore perferendis consequuntur vero, aperiam iusto fuga ullam eaque earum a autem esse illo?
      </div>
  </div>
  <div class="list_location_scenario">
      <div class="list_location__title">
          Локации
      </div>
      <div class="list_location_container">
          <CardLocation/>

      </div>
  </div>
</div>
</template>

<script>
import CardLocation from "./CardLocation.vue";
export default {
    components: { CardLocation }
}
</script>

<style>
.setting_game{
    padding-top: 110px;
    padding-left: 310px;
}

.title_scenario {
    width: 100%;
    margin-bottom: 15px;
    color: white;
    font-size: 25px;
}

.cart_scenario {
    display: flex;
    width: 500px;
}


.game_panel {
    margin-left: 5px;
}

.game_panel_control {
    flex-flow: column;
    align-items: center;
}

.button_play {
    background: #FFF5B5;
    border-radius: 5px;
    width: 277px;
    height: 43px;
    text-align: center;
    padding-top: 7px;
    cursor: pointer;
}

.button_add_library {
    margin-top: 10px;
    border: 2px solid white;
    border-radius: 2px;
    color: white;
    width: 277px;
    height: 38px;
    text-align: center;
    padding-top: 3px;
    cursor: pointer;
}

.table_about_scenario {
    margin-top: 15px;
    border-top: 2px thick white;
    color: rgb(218, 218, 218);
}

.article_scenario{
    position:absolute;
    top: 112px;
    left: 900px;
    color: white;
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