<template>
  <div class="create_scenario">
    <b-button class="button_save" type="is-success" outlined @click="setDataScenario">
      СОХРАНИТЬ
    </b-button>
    <div class="input_name_scenario">
      <input v-model="nameScenario" class="input is-medium" type="text" placeholder="Введите название">
    </div>
    <div class="input_article_scenario">
      <div class="input_article_scenario_title">
        ОПИСАНИЕ К СЦЕНАРИЮ
      </div>
      <textarea v-model="articleScenario" class="textarea" placeholder="Введите описание сценария" />
    </div>
    <div class="location_container">
      <div class="location_container_title">
        <div class="title">
          ЛОКАЦИИ
        </div>
        <b-button class="add_location" @click="onAddLocationClick">
            +
        </b-button>
      </div>
      <div class="location_card_catalogy">
        <CardLocation v-for="locations in locationProp" :locations="locations" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import CardLocation from './CardLocation.vue'
import createScenario from '~/pages/createScenario.vue'
export default {

  components: {
    CardLocation
  },
  props: {
    scenarioProp: {
      type: Object
    }
  },
  
  data () {
    return {
      nameScenario: this.scenarioProp.nameScenario,
      articleScenario: this.scenarioProp.articleScenario,
      locationProp: this.scenarioProp.listLocation
    }
  },

  beforeMount () {},
  methods: {

    setDataScenario () {
      this.$store.commit('createScenario/setDataScenario', { nameScenario: this.nameScenario, articleScenario: this.articleScenario })
      this.$router.push('/libraryScenario')
      // this.$store.dispatch('saveScenario')
    },

    onAddLocationClick () {
      this.$router.push('/createLocation')
    }

    // createLocation (locationObject) {
    //   this.listLocation.push(locationObject)
    // }

  }
}
</script>

<style scoped>
  .create_scenario {
    padding-left: 300px;
    padding-top: 110px;
    padding-right: 50px;
  }

  .input_name_scenario {
    margin-bottom: 15px;
  }

  .input_article_scenario {
    margin-bottom: 15px;
  }

  .input_article_scenario_title {
    color: white;
    margin-bottom: 5px;
  }

  .location_container_title {
    display: flex;
  }

  .title {
    color: white;
    margin-right: 15px;
  }

  .add_location {
    color: white;
    width: 25px;
    height: 25px;
    margin-top: 7px;
    border-radius: 25px;
    background-color: #121212;
    cursor: pointer;
  }

  .location_card_catalogy {
    display: flex;
    flex-wrap: wrap;
    gap: 25px;
  }

  .button_save {
    margin-bottom: 25px;
    justify-self: end;
  }

</style>
