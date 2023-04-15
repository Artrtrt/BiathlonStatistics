<template>
  <i-layout>
    <i-layout-header class="_width-100 _padding-x-0 _padding-y-0">
      <i-navbar class="header" :collapse="false">
        <i-navbar-brand
          ><img class="logo" src="./assets/logo.png"
        /></i-navbar-brand>
        <i-navbar-items>
          <i-nav>
            <i-nav-item :to="{ name: 'home' }">Главная</i-nav-item>
            <i-nav-item :to="{ name: 'calculator' }">Калькулятор</i-nav-item>
          </i-nav>
        </i-navbar-items>
      </i-navbar>
    </i-layout-header>
    <i-layout-content
      class="_padding-top-1 _padding-left-0 _padding-right-lg-1 _padding-right-xl-1 _overflow-auto"
      style="height: calc(100vh - 72px); background-color: #c7c7c7;"
    >
      <router-view />
    </i-layout-content>
  </i-layout>
</template>

<script lang="ts">
import Vue from "vue";
import * as model from "@/module/model";

export default Vue.extend({
  name: "NetworkLan",
  data() {
    return {
      model,
    };
  },
  async beforeMount() {
    await model.method.app.import();
    this.$forceUpdate();
    // console.log(model.data.app.seasonList);
  },
});
</script>

<style>
.header {
  background-color: #dbe9fc !important;
}

.header a {
  font-size: 20px;
}

.logo {
  height: 40px;
  width: 40px;
  border-radius: 40px;
  pointer-events: none;
}
</style>
