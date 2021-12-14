<template>
  <div class="create_location">
    <b-button class="button_save" type="is-success" outlined @click="createLocation">
      СОХРАНИТЬ
    </b-button>
    <div class="input_name_location">
      <input v-model="nameLocation" class="input is-medium" type="text" placeholder="Введите название локации">
    </div>
    <div class="input_article_location">
      <div class="input_article_location_title">
        ОПИСАНИЕ К ЛОКАЦИИ
      </div>
      <textarea v-model="articleLocation" class="textarea" placeholder="Введите описание локации" />
    </div>
    <div class="unit_container">
      <div class="added_unit">
        <div class="added_unit_title">
          ВРАЖЕСКИЕ ЮНИТЫ
        </div>
        <button class="added_unit_button" @click="onButtonNewRowClicked">
          +
        </button>
      </div>
      <UnitTable :unit-items="unitItems" />
    </div>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
import CreateUnitDialog from './CreateUnitDialog.vue'
import store from '~/store'
export default {
  props: ['locationProp'],
  data () {
    return {
      nameLocation: this.locationProp.nameLocation,
      articleLocation: this.locationProp.nameLocation,
      unitItems: this.locationProp.unitItems
    }
  },

  methods: {
    createLocation () {
      this.$emit('createLocation', this.location)
      this.location = {
        nameLocation: '',
        articleLocation: '',
        unitItems: []
      }
      this.$router.push('createScenario')
    },

    onButtonNewRowClicked () {
      this.$buefy.modal.open({
        parent: this,
        component: CreateUnitDialog,
        events: {
          saveUnit: (unitObject) => {
            this.saveUnit(unitObject)
          }
        }
      })
    },
    saveUnit (unitObject) {
      this.location.unitItems.push(unitObject)

      // this.$axios.$post(`...`, {
      //     headers: {

      //     },
      //     unitObject
      // });
    }
  },
}

</script>

<style>
.create_location {
  padding-left: 300px;
  padding-top: 110px;
  padding-right: 50px;
}

.input_name_location {
  margin-bottom: 15px;
}

.input_article_location {
  margin-bottom: 15px;
}

.input_article_location_title {
  color: white;
  margin-bottom: 5px;
}

.unit_container_title {
  display: flex;
}

.added_unit_title {
  color: white;
  margin-right: 15px;
}

.added_unit {
  display: flex;
}

.added_unit_button {
  cursor: pointer;
  border-radius: 15px;
}

.button_save {
  cursor: pointer;
  display: flex;
  border-radius: 3px;
  width: 150px;
  height: 45px;
  align-items: center;
  padding-left: 12px;
  margin-right: 54px;
  font-size: 15px;
}
</style>
