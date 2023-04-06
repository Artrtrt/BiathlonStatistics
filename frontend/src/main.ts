import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Inkline from "@inkline/inkline";
import "@inkline/inkline/dist/inkline.css";

Vue.use(Inkline);

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
