<template>
  <div class="create_scenario">
    <b-button @click="setnameScenariotoStore" class="button_save" type="is-success" outlined>
      СОХРАНИТЬ
    </b-button>
    <div class="input_name_scenario">
      <input v-model="nameScenario" class="input is-medium" type="text" placeholder="Введите название" />
    </div>
    <div class="input_article_scenario">
      <div class="input_article_scenario_title">ОПИСАНИЕ К СЦЕНАРИЮ</div>
      <textarea v-model="articleScenario" class="textarea" placeholder="Введите описание сценария"></textarea>
    </div>
    <div class="location_container">
      <div class="location_container_title">
        <div class="title">
          ЛОКАЦИИ
        </div>
        <button class="add_location">
          <NuxtLink to="/createLocation">+</NuxtLink>
        </button>
      </div>
      <div class="location_card_catalogy">
        <ListLocation :listLocation="listLocation" />
      </div>
    </div>
  </div>
</template>

<script>
  import store from '~/store/Index';
import ListLocation from './ListLocation.vue';
  export default {
    

    components: {
    ListLocation
},

    beforeMount() {
      
    },

    data() {
      return {
        nameScenario: '',
        articleScenario: '',
        listLocation: [],
      }
    },

    methods: {
      setnameScenariotoStore() {
        this.$store.commit('increment', {
          nameScenario: this.nameScenario
        })
      }
    }
  };

</script>

<style>
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
    border-radius: 15px;
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
