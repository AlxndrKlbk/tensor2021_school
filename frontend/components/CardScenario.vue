<template>
  <div class="card_scenario">
    <div class="card_scenario_cover">
      <!-- <img :src="`https://frontend-test.idaproject.com${$props.item.photo}`" :alt="$props.item.name"> -->
    </div>
    <div class="card_scenario_title">
      {{ scenarioProp.nameScenario }}
    </div>
    <div class="card_scenario_control_panel">
      <div class="play_scenario">
        <div class="play_scenario_icon">
          <img src="../assets/play.svg" alt="">
        </div>
        <div class="play_scenario_title">
          <NuxtLink to="/settingGame" class="play_scenario_title">
            Запустить
          </NuxtLink>
        </div>
      </div>
      <div class="remake_scenario">
        <div class="remake_scenario_icon">
          <img src="../assets/remake.svg" alt="">
        </div>
        <div class="remake_scenario_title" @click="onEditScenario">
          Редактировать
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['scenarioProp'],

  methods: {
    onEditScenario (_event, scenario) {
      this.$router.push({
        name: 'createScenario',
        params: {
          nameScenario: 'Ебучий сценарий',
          articleScenario: 'Ебучее описание сценария',
          listLocation: []
        }
      }).catch(() => {})
    }
  }

}

</script>

<style>
 .card_scenario {
   height: 400px;
   width: 220px;
   margin: 8px
 }

 .card_scenario_cover {
   height: 250px;
   background: lawngreen;
 }

 .card_scenario_title {
   font-size: 20px;
   margin-top: 5px;
   margin-left: 5px;
   color: white;
 }

 .card_scenario_control_panel {
   margin-left: 5px;
 }

 .play_scenario {
   margin-top: 5px;
   cursor: pointer;
   display: flex;

 }

 .play_scenario_title {
   margin-left: 5px;
   color: white;
 }

 .play_scenario_title:hover {
   color: greenyellow;
 }

 .remake_scenario {
   margin-top: 5px;
   display: flex;
   cursor: pointer;
 }

 .remake_scenario_title {
   margin-left: 5px;
   color: white;
 }

 .remake_scenario_title:hover {
   color: fuchsia;
 }
</style>
