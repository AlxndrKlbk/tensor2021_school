<template>
  <div  class="location_card_item">
    <div class="location_card_cover" />
    <div class="location_card_title">
      {{ locations.nameLocation }}
    </div>
    <div class="remake_location">
      <div class="remake_location_icon">
        <img src="../assets/remake.svg" alt="">
      </div>
      <div class="remake_location_title" @click="onEditLocation">
        Редактировать
      </div>
    </div>
  </div>
</template>

<script>
import { mapMutations, mapState } from 'vuex'
export default {
  props: ['locations'],

  methods: {
    onEditLocation (_event, location) {
      this.$router.push({
        name: 'createLocation',
        params: {
          nameLocation: /* location.nameLocation */'Драсте 1',
          articleLocation: 'Драсте дратсе',
          unitItems: []
        }
      }).catch(() => {})
    },
  }
}

</script>

<style scoped>
.location_card_item {

}

.location_card_cover {
    width: 100px;
    height: 100px;
    background-color: white;
    border-radius: 50px;
}

.location_card_title {
    color: white;
}

.remake_location {
    margin-top: 5px;
    display: flex;
    cursor: pointer;
}

.remake_location_title {
    margin-left: 5px;
    color: white;
    font-size: 13px;
}

.remake_location_title:hover {
    color: fuchsia;
}
</style>
