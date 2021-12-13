<template>
  <b-table :data="data" :columns="columns" />
</template>

<script>
export default {
  props: {
    unitItems: {
      type: Array,
      default: () => []
    }
  },
  data () {
    return {
      data: this.unitItems,
      columns: [
        {
          field: 'unitName',
          label: 'Имя вражеского юнита'
        },
        {
          field: 'unitHealth',
          label: 'Здоровье'
        },
        {
          field: 'unitDamage',
          label: 'Урон'
        },
        {
          field: 'unitDifficult',
          label: 'Уровень сложности'
        }
      ]
    }
  }
}
</script>
