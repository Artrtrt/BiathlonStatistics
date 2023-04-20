<template>
  <i-layout class="bg">
    <i-layout-header class="_width-100 _padding-x-0 _padding-y-0 header">
      <i-navbar :collapse="false" style="height: 100%; z-index:1">
        <i-navbar-brand class="_display-xs-none _display-sm-none _display-md-none"><img class="logo"
            src="./assets/logo.jpg" /></i-navbar-brand>
        <i-navbar-items>
          <i-nav class="_margin-right-1">
            <i-nav-item :to="{ name: 'home' }" exact-active-class="-active" class="header-element _margin-right-1">Главная
              страница</i-nav-item>
            <i-nav-item class="header-element" :to="{ name: 'calculator' }"
              exact-active-class="-active">Калькулятор</i-nav-item>
          </i-nav>
          <i-nav style="grid-gap: 10px">
            <i-button :to="{ name: 'auth' }" class="button-confirm">Войти</i-button>
            <i-button :to="{ name: 'registration' }" class="button-confirm">Зарегистрироваться</i-button>
          </i-nav>
        </i-navbar-items>
      </i-navbar>
    </i-layout-header>
    <i-layout-content class="_padding-left-0 _padding-right-lg-1 _padding-right-xl-1 _overflow-auto"
      style="height: calc(100vh - 60px)">
      <div v-if="model.data.app.seasonList.length === 0"
        style="height: 5vw; width: 5vw; position: absolute; top: 50%; left: 48%;">
        <i-loader size="auto" variant="dark" />
      </div>
      <div v-else style="height: 100%;">
        <router-view />
      </div>
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
      active: "home",
    };
  },
  methods: {
  },
  async beforeMount() {
    await model.method.app.import();
    this.$forceUpdate();
  },
});
</script>

<style>
.header {
  background-color: #6e9ccf !important;
  height: 80px;
}

.header a {
  font-size: 16px;
  color: #000000 !important;
}

.header div {
  background-color: #6e9ccf !important;
}

.header-element {
  border-radius: 15px;
}

.header-element:hover {
  background-color: #5d84b1 !important;
}

.button-confirm {
  background-color: #3d72b0 !important;
  border-color: #3d72b0 !important;
  color: #ffffff !important;
  border-radius: 10px !important;
}

.button-dunger {
  background-color: #f25f5c !important;
  border-color: #f25f5c !important;
  color: #ffffff !important;
  border-radius: 10px !important;
}

.logo {
  height: 50px;
  width: 112px;
  border-radius: 30px;
  pointer-events: none;
}

.bg {
  background: url("@/assets/bg.jpg") 0 0 / cover no-repeat fixed;
}

.text-header {
  width: 100%;
  color: #233567 !important;
  font-size: 20px;
  text-align: center;
  white-space: nowrap;
}

.content-center {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

#opacity-block {
  background-color: rgba(232, 238, 255, 0.7) !important;
  width: 600px;
  margin-right: 20px;
  margin-left: 20px;
}
</style>
