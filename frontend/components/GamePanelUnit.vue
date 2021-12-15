<template>
  <section class="game_panel_unit">
    <b-button class="button_show_panel" @click="open = true">
      ≡
    </b-button>
    <b-sidebar
      v-model="open"
      type="is-light"
      :fullheight="fullheight"
      :right="right"
      class="game_panel"
    >
      <div class="p-1">
        <h1>Панель управления юнитами</h1>
        <b-menu class="panel_menu">
          <b-menu-list label="Вражеские юниты">
            <GamePanelEnemyUnit/>
          </b-menu-list>
          <b-menu-list label="Игровые юниты">
            <GamePanelAlliesUnit/>
          </b-menu-list>
        </b-menu>
      </div>
    </b-sidebar>
  </section>
</template>

<script>
import GamePanelEnemyUnit from './GamePanelEnemyUnit.vue'
import GamePanelAlliesUnit from './GamePanelAlliesUnit.vue'
export default {
  components: { GamePanelEnemyUnit, GamePanelAlliesUnit },

  data () {
    return {
      open: false,
      overlay: true,
      fullheight: true,
      right: true
    }
  }
}
</script>

<style>

.button_show_panel {
  width: 15px;
  background-color: rgb(61, 48, 19);
  border: none;
  z-index: 87;
  color: white;
  position: fixed;
  right: 0px;
  top: 100px

}
.button_show_panel span {
  font-size: 25px;
}

.game_panel {
  z-index: 70;
}

.panel_menu {
  padding-top: 25px;
}
  </style>
