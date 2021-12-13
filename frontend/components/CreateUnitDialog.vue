<template>
  <div class="unit-form">
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

    <b-button type="is-primary" @click="onUnitSave">
      Сохранить
    </b-button>
  </div>
</template>

<script>
export default {
  data () {
    return {
      unitName: '',
      unitHealth: null,
      unitDamage: null,
      unitDifficult: null
    }
  },
  methods: {
    onUnitSave () {
      this.$emit('saveUnit', {
        unitName: this.unitName,
        unitHealth: this.unitHealth,
        unitDamage: this.unitDamage,
        unitDifficult: this.unitDifficult
      })

      this.$emit('close')
    }
  }
}
</script>

<style>
    .unit-form {
        background: white;
        padding: 50px;
        width: 600px;
        justify-content: center;
    }
</style>
