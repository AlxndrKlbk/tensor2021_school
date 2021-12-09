<template>
  <div class="header_create">
      
      <!-- <div class="button_save">
          <div class="logo_button_save">
          </div>
          <div class="text_add_scenario">
              СОХРАНИТЬ
          </div>
      </div> -->
  </div>
</template>

<script>
export default {

}
</script>

<style>
.header_create {
    position: fixed;
    width: calc(100% - 300px);
    height: 100px;
    left: 300px;
    top: 0px;
    display: flex;
    background: #121212;
    justify-content: end;
    align-items: center;
    z-index: 99;
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

.logo_button_save{
    margin-top: 8px;
}

.text_add_scenario {
    margin-left: 5px;
    align-items: center;
}
</style>