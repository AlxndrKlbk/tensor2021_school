<template>
  <div class="sidebar">
    <div class="sidebar_item_user">
      <div class="sidebar_item_user_icon">
        <img height="50px" width="50px" src="../assets/logo_user.svg" alt="">
      </div>
      <div class="sidebar_item_user_name">
        Username
      </div>
    </div>
    <div class="sideber_list">
      <div class="sideber_list_item">
        <div class="sideber_list_item_icon">
          <img src="../assets/home.svg" alt="">
        </div>
        <div class="sideber_list_item_title">
          Домой
        </div>
      </div>
      <div class="sideber_list_item">
        <div class="sideber_list_item_icon">
          <img src="../assets/magazin.svg" alt="">
        </div>
        <div class="sideber_list_item_title">
          Магазин
        </div>
      </div>
      <div class="sideber_list_item active">
        <div class="sideber_list_item_icon">
          <img src="../assets/labrary.svg" alt="">
        </div>
        <NuxtLink to="/libraryScenario">
          <div class="sideber_list_item_title">
            Библиотека
          </div>
        </NuxtLink>
      </div>
      <div class="sideber_list_item_setting">
        <div class="sideber_list_item_setting_icon">
          <img src="../assets/setting.png" alt="Setting">
        </div>
        <div class="sideber_list_item_setting_title">
          Настройки
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
.sidebar {
    position: fixed;
    background: #121212;
    width: 300px;
    height: 100%;
    padding-left: 70px;
    z-index: 99;
}

.sidebar_item_user {
    align-items: center;
    display: flex;
    margin-top: 20px;
    margin-bottom: 100px;
}

.sidebar_item_user_name {
    margin-left: 15px;
    color: white;
}

.sideber_list_item {
    cursor: pointer;
    display: flex;
    align-items: center;
    margin-top: 80px;
}

.sideber_list_item.active {
    color: white;
}

.sideber_list_item_title {
    font-size: 18px;
    margin-left: 15px;
}

.sideber_list_item_title:hover {
    color: white;
}

.sideber_list_item_setting {
    cursor: pointer;
    display: flex;
    margin-top: 80px;
}

.sideber_list_item_setting_title {
    font-size: 18px;
    margin-left: 15px;
}

.sideber_list_item_setting_title:hover {
    color: white;
}
</style>
