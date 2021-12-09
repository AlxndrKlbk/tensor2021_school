<template>
    <LibraryScenario :itemsProp="items" />
</template>

<script>
import LibraryScenario from "~/components/LibraryScenario.vue";
export default {
    components: { LibraryScenario },

    async asyncData({ $axios }) {
     const result = await $axios.get(`https://frontend-test.idaproject.com/api/product`);
     
     return {
       items: result.data
     };
   },
   data () {
       return {
           items: []
       }
   }
}
</script>

<style>

</style>
