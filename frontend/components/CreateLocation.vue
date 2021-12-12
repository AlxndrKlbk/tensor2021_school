<template>
  <div class="create_location">
    <b-button @click="createLocation" class="button_save" type="is-success" outlined>
      СОХРАНИТЬ
    </b-button>
    <div class="input_name_location">
      <input v-model="location.nameLocation" class="input is-medium" type="text" placeholder="Введите название локации">
    </div>
    <div class="input_article_location">
      <div class="input_article_location_title">
        ОПИСАНИЕ К ЛОКАЦИИ
      </div>
      <textarea v-model="location.articleLocation" class="textarea" placeholder="Введите описание локации">
        </textarea>
    </div>
    <div class="unit_container">
      <div class="added_unit">
        <div class="added_unit_title">
          ВРАЖЕСКИЕ ЮНИТЫ
        </div>
        <button @click="onButtonNewRowClicked" class="added_unit_button">
          +
        </button>
      </div>
      <UnitTable :unitItems="location.unitItems" />
    </div>
  </div>
</template>

<script>
import CreateUnitDialog from "./CreateUnitDialog.vue";
import store from "~/store/Index";
export default {
  data() {
    return {
      location: {
        nameLocation: '',
        articleLocation: '',
        unitItems: [],
      },
      
    }
  },

  methods: {
    createLocation() {
      this.location.id= Date.now();
      this.$emit('createLocation', this.location);
      this.location = {
        nameLocation: '',
        articleLocation: '',
        unitItems: [],
      }

      // this.$store.commit('addLocation', {
      //   location: this.location
      // })
      this.$router.push('createScenario')
    },

    onButtonNewRowClicked() {
      this.$buefy.modal.open({
        parent: this,
        component: CreateUnitDialog,
        events: {
          saveUnit: (unitObject) => {
            this.saveUnit(unitObject);
          }
        }
      })
    },
    saveUnit(unitObject) {
      this.location.unitItems.push(unitObject);

      // this.$axios.$post(`...`, { 
      //     headers: {

      //     }, 
      //     unitObject
      // });
    }
  }
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