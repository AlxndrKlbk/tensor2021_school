<template>
  <div class="location_card_item"  >
    <div class="location_card_cover">

    </div>
    <div class="location_card_title">
      234324234324
    </div>
    <div class="remake_location">
      <div class="remake_location_icon">
        <img src="../assets/remake.svg" alt="">
      </div>
      <div class="remake_location_title">
        Редактировать
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    listLocation: {
      type: Array,
      required: true,
    }
  }
}
</script>

<style>
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