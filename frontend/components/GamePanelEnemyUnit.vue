<template>
  <div class="game_panel_enemy_unit">
    <b-field label="Враг №1">
      <div class="game_panel_enemy_unit_container">
        <div class="game_panel_form_item">
          <div class="title_counter_health">
            Здоровье
          </div>
          <b-numberinput type="is-dark" size="is-small" />
        </div>
        <div class="game_panel_form_item">
          <div class="title_counter_damage">
            Урон
          </div>
          <b-numberinput type="is-dark" size="is-small" />
        </div>
      </div>
    </b-field>
  </div>
</template>

<script>
export default {
}
</script>

<style>
.game_panel_enemy_unit {
  margin-top: 25px;
}

.game_panel_form_item {
  display: flex;
  flex-direction: column;
  text-align: center;
}

.game_panel_enemy_unit_container {
  display: flex;
  flex-direction: column;
}
</style>
