<template>
  <div class="game_panel_unit_window">
    <div class="game_panel_unit_title">
      Панель управления юнитами
    </div>
    <div class="game_panel_unit">
      <div class="panel_enemy_unit">
        Вражеские юниты
        <GamePanelEnemyUnit />
        <GamePanelEnemyUnit />
        <GamePanelEnemyUnit />
      </div>
      <div class="panel_game_unit">
        Игровыеыва юниты
        <GamePanelGameUnit />
        <GamePanelGameUnit />
        <GamePanelGameUnit />
      </div>
    </div>
  </div>
</template>

<script>
import GamePanelEnemyUnit from './GamePanelEnemyUnit.vue'
export default {
  components: { GamePanelEnemyUnit }
}
</script>

<style>
.game_panel_unit_window {
    width: 600px;
    height: 800px;
    background: rgb(192, 192, 192);
}

.game_panel_unit_title {
    color: black;
    font-size: 20px;
    text-align: center;
    padding-top: 15px;
}

.panel_enemy_unit {
    display: flex;
    flex-direction: row;
    padding-left: 25px;
}

.panel_game_unit {
    display: flex;
    flex-direction: row;
    padding-left: 25px;
}
</style>
