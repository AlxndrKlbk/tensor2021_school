<template>
  <CreateLocation :locationProp="location" @create="createLocation" />
</template>

<script>
export default {
  layout: 'create',
  asyncData ({ params, store, $axios }) {
    const location = {
      nameLocation: params.nameLocation,
      articleLocation: params.articleLocation,
      unitItems: []
    }
    return {
      location
    }
  },
  data () {
    return {
      location: null
    }
  }
}
</script>

<style>

</style>
