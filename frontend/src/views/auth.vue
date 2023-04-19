<template>
  <div class="content-center">
    <i-card id="opacity-block">
      <template slot="header">
        <div class="text-header">
          <a style="color: #233567 !important; font-size: 20px;">Авторизация</a>
        </div>
      </template>
      <i-container>
        <i-row class="_margin-bottom-1 row-center">
          <i-column xs="4" md="3">
            Логин
          </i-column>
          <i-column xs="7" md="7">
            <i-input v-model="login"></i-input>
          </i-column>
        </i-row>
        <i-row class="_margin-bottom-1 row-center">
          <i-column xs="4" md="3">
            Пароль
          </i-column>
          <i-column xs="7" md="7">
            <i-input type="password" v-model="password"></i-input>
          </i-column>
        </i-row>
        <i-row class="_margin-bottom-1">
          <i-column style="display: flex; justify-content: center;">
            <i-button @click="auth" class="button-confirm">Войти</i-button>
          </i-column>
        </i-row>
        <i-row class="_margin-bottom-1">
          <i-column style="text-align: center;">
            Если у вас нет аккаунта можете <a href="/registration">зарегистрироваться</a>
          </i-column>
        </i-row>
      </i-container>
    </i-card>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import * as model from "@/module/model";

export default Vue.extend({
  name: "NetworkLan",
  data() {
    return {
      model,

      login: '',
      password: '',
    };
  },
  methods: {
    async auth() {
      await model.method.auth.login(this.login, this.password);
    }
  },
});
</script>

<style scoped>
.row-center {
  align-items: center;
  justify-content: center;
}

.link {
  color: black !important;
}
</style>