import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Inkline from "@inkline/inkline";
import "@inkline/inkline/dist/inkline.css";
import VueYandexMetrika from "vue-yandex-metrika-ts";

Vue.use(VueYandexMetrika, {
  id: 93817424,
  env: process.env.NODE_ENV,
});

Vue.use(Inkline);

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
