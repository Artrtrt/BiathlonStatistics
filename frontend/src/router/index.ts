import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";

import Home from "@/views/home.vue";
import Сalculator from "@/views/сalculator.vue";
import Competition from "@/views/competition.vue";

import Auth from "@/views/auth.vue";
import Registration from "@/views/registration.vue";
import Notfound from "@/views/notfound.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    name: "home",
    component: Home,
    meta: {
      title: "Главная",
    },
  },
  {
    path: "/calculator",
    name: "calculator",
    component: Сalculator,
    meta: {
      title: "Калькулятор медалей",
    },
  },
  {
    path: "/competiton/:index?",
    name: "competition",
    component: Competition,
    meta: {
      title: "Соревнование",
    },
  },
  {
    path: "/auth",
    name: "auth",
    component: Auth,
    meta: {
      title: "Авторизация",
    },
  },
  {
    path: "/registration",
    name: "registration",
    component: Registration,
    meta: {
      title: "Регистрация",
    },
  },
  {
    path: "*",
    name: "notfound",
    component: Notfound,
    meta: {
      title: "Not found",
    },
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
