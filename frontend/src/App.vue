<template>
  <i-layout class="bg">
    <i-layout-header class="_padding-x-0 _padding-y-0">
      <i-navbar class="header" collapse="sm" style="height: 100%; z-index: 1">
        <i-navbar-brand
          class="_display-xs-none _display-sm-none _display-md-none"
        >
          <div @click="toHome">
            <img class="logo" src="./assets/logo.jpg" />
          </div>
        </i-navbar-brand>
        <i-navbar-items>
          <hr class="_display-md-none _display-lg-none _display-xl-none" />
          <i-nav>
            <i-nav-item
              :to="{ name: 'home' }"
              exact-active-class="-active"
              class="header-element"
              >Главная страница</i-nav-item
            >
            <i-nav-item
              class="header-element"
              :to="{ name: 'calculator' }"
              exact-active-class="-active"
              >Калькулятор</i-nav-item
            >
          </i-nav>
          <hr class="_display-md-none _display-lg-none _display-xl-none" />
          <i-nav v-if="model.data.auth.authorized">
            <a class="_padding-1"
              >{{ model.data.auth.firstName }} {{ model.data.auth.lastName }}</a
            >
            <i-nav-item>
              <i-button @click="logout" class="button-confirm">Выйти</i-button>
            </i-nav-item>
          </i-nav>
          <i-nav v-else>
            <i-nav-item class="_padding-right-0">
              <i-button :to="{ name: 'auth' }" class="button-confirm"
                >Войти</i-button
              >
            </i-nav-item>
            <i-nav-item>
              <i-button :to="{ name: 'registration' }" class="button-confirm"
                >Зарегистрироваться</i-button
              >
            </i-nav-item>
          </i-nav>
        </i-navbar-items>
      </i-navbar>
    </i-layout-header>
    <i-layout-content class="_overflow-auto">
      <div
        v-if="model.data.app.loading"
        style="height: 5vw; width: 5vw; position: absolute; top: 50%; left: 48%"
      >
        <i-loader size="auto" variant="dark" />
      </div>
      <div v-else style="height: 100%">
        <router-view />
        <Chat></Chat>
      </div>
    </i-layout-content>
  </i-layout>
</template>

<script lang="ts">
import Vue from "vue";
import * as model from "@/module/model";
import Chat from "@/components/chat.vue";

export default Vue.extend({
  name: "App",
  data() {
    return {
      model,
    };
  },
  components: {
    Chat,
  },
  methods: {
    async logout() {
      await model.method.auth.logout();
      location.reload(); // eslint-disable-line
      this.$forceUpdate();
    },
    toHome() {
      console.log("aa");
      if (this.$route.path !== "/") {
        this.$router.push("/");
      }
    },
  },
  async beforeMount() {
    await model.method.app.import();
    model.method.auth.getInfo();
    this.$forceUpdate();
  },
});
</script>

<style>
.header {
  background-color: #6e9ccf !important;
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

.button-danger {
  background-color: #ec706e !important;
  border-color: #ec706e !important;
  color: #ffffff !important;
  border-radius: 10px !important;
}

.logo {
  height: 50px;
  width: 112px;
  border-radius: 30px;
  pointer-events: none;
}

.button-icon {
  cursor: pointer;
  border-radius: 30px;
  height: 31px;
  width: 31px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.button-icon:hover {
  background-color: #c4cad8c2;
}

.bg {
  background: url("@/assets/bg.jpg") 0 0 / cover no-repeat fixed;
  height: 100vh;
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

.link {
  text-decoration: underline !important;
  cursor: pointer;
}

.color-white {
  color: #ffffff !important;
}

.bg-gold {
  background-color: #f6fab4 !important;
}

.bg-silver {
  background-color: #e6e6e6 !important;
}

.bg-bronze {
  background-color: #e6c5a3 !important;
}

::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0);
}

::-webkit-scrollbar-thumb {
  border-radius: 5px;
  background: #999;
}

::-webkit-scrollbar-corner {
  border-radius: 5px;
  background: #000;
}
</style>
