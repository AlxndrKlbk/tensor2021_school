<template>
  <div class="game_panel_enemy_unit">
          <b-field label="Имя">
      <b-input v-model="unitName" />
    </b-field>

    <b-field label="Здоровье">
      <b-numberinput v-model="unitHealth" />
    </b-field>

    <b-field label="Урон">
      <b-numberinput v-model="unitDamage" />
    </b-field>

    <b-field label="Сложность">
      <b-numberinput v-model="unitDifficult" />
    </b-field>
      </div>
</template>

<script>
export default {

}
</script>

<style>
.game_panel_enemy_unit {
    width: 100px;
    margin-right: 50px;
}
</style>