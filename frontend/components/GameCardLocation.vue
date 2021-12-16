<template>
  <div class="location_card_item">
    <a @click="nextLocation">
      <div class="location_card_cover" alt="nameLocation"></div>
    </a>
    
    </div>
  </div>
</template>

<script>
export default {
  props: ['locations'],


  data () {
    return {
      nameLocation: this.locations.nameLocation
    }
  },

  methods: {
    nextLocation() {
      this.$router.push({
        name: 'playLocation',
        params: {
          idLocation: 1
        }
      })
    }
  }
}
</script>

<style>
.location_card_cover {
    width: 50px;
    height: 50px;
    background-color: white;
    border-radius: 25px;
    margin-right: 25px;
}
</style>