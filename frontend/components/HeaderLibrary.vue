<template>
  <div class="header">
      <div class="sort">
          <div class="sort_title">
              Сортировать по:
          </div>
          <div class="sort_selected" @click="sortActive = !sortActive">
              <div class="sort_selected_text" ref="selectedText">
                  Недавние
              </div>
              <div class="sort_selected_icon">
                  <svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M0.353516 0.646409L4.35352 4.64641M9.35352 0.353516L4.35352 5.35352" stroke="white"/>
</svg>

              </div>
          </div>
          <div class="sort_list" :class="{ active: sortActive }">
              <div class="sort_list_item" @click="sortItems('time')">
                  Недавно сыгранные
              </div>
              <div class="sort_list_item" @click="sortItems('popular')">
                  По популярности
              </div>
          </div>
      </div>
      <NuxtLink to="/createScenario">
      <div class="button_add_scenario">
          <div class="logo_button_add_scenario">
              <svg width="30" height="30" viewBox="0 0 32 38" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M0 3C0 1.34314 1.34315 0 3 0H16.1111C19.9771 0 23.1111 3.13401 23.1111 7V30.2222H3C1.34315 30.2222 0 28.8791 0 27.2222V3Z" fill="#333333"/>
<path d="M1.77783 3.77783C1.77783 2.67326 2.67326 1.77783 3.77783 1.77783H9.66672C10.219 1.77783 10.6667 2.22555 10.6667 2.77783V28.4445H3.77783C2.67326 28.4445 1.77783 27.5491 1.77783 26.4445V3.77783Z" fill="#6E6E6E"/>
<path d="M10.6665 8.88892H18.5554C19.1077 8.88892 19.5554 9.33663 19.5554 9.88892V28.4445H10.6665V8.88892Z" fill="#6E6E6E"/>
<path d="M10.6665 7.11108H12.4443V8.88886H10.6665V7.11108Z" fill="#6E6E6E"/>
<path d="M10.6665 3.55566H15.9998V8.889H11.6665C11.1142 8.889 10.6665 8.44128 10.6665 7.889V3.55566Z" fill="#333333"/>
<circle cx="22.2221" cy="27.5556" r="9.02778" fill="#333333" stroke="#6E6E6E" stroke-width="1.5"/>
<rect x="21.3335" y="23.1111" width="1.77778" height="8.88889" fill="#6E6E6E"/>
<rect x="26.6665" y="26.6667" width="1.77778" height="8.88889" transform="rotate(90 26.6665 26.6667)" fill="#6E6E6E"/>
</svg>
          </div>
          <div class="text_add_scenario">
              Добавить новый сценарий
          </div>
      </div>
      </NuxtLink>
  </div>
</template>

<script>
export default {
    data: function() {
        return {
            sortActive: false
        };
    },

    methods: {
        sortItems(e) {
            if(e ==='time' ) {
                this.$refs.selectedText.textContent = `дате игры`
            }

            if(e ==='popular') {
                this.$refs.selectedText.textContent = `популярности`
            }

            this.sortActive = !this.sortActive
        }
    },
}
</script>

<style>
.header {
    position: fixed;
    width: calc(100% - 300px);
    height: 100px;
    left: 300px;
    top: 0px;
    display: flex;
    background: #121212;
    justify-content: space-between;
    align-items: center;
    z-index: 99;
}

.sort {
    margin-left: 54px;
    display: flex;
    color: white;
    font-size: 18px;

}

.sort_selected {
    position: relative;
    display: flex;

}


.sort_selected_text {
    margin-left: 5px;
    color: #797979;
    cursor: pointer;
}

.sort_selected_icon {
    cursor: pointer;
    align-items: center;
    margin-left: 5px;
}

.sort_list {
    display: none;
    position: absolute;
    background: #313131;
    top: 75px;
    left: 50px;
    right: 0px;
    width: 250px;

}

.sort_list.active {
    display: block;
}

.sort_list_item {
    padding: 8px 0 8px 10px;
    cursor: pointer;
    width: 100%;
    color: #797979;
}

.sort_list_item:hover {
    color: white;
    background: #3d3d3d;
}


.button_add_scenario {
    cursor: pointer;
    display: flex;
    background: #C4C4C4;
    border-radius: 3px;
    width: 250px;
    height: 45px;
    align-items: center;
    padding-left: 12px;
    margin-right: 54px;
    font-size: 15px;
}

.logo_button_add_scenario{
    margin-top: 8px;
}

.text_add_scenario {
    margin-left: 5px;
    align-items: center;
}

</style>