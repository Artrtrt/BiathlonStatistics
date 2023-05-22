<template>
  <div class="content-center">
    <i-card id="opacity-block">
      <template slot="header">
        <div class="text-header">
          <a style="color: #233567 !important; font-size: 20px">Авторизация</a>
        </div>
      </template>
      <i-container>
        <i-form v-model="formAuth">
          <i-row class="_margin-bottom-1 row-center">
            <i-column xs="4" md="3"> Логин </i-column>
            <i-column xs="7" md="7">
              <i-form-group>
                <i-input v-model="login" :schema="formAuth.login"></i-input>
              </i-form-group>
            </i-column>
          </i-row>
          <i-row class="_margin-bottom-1 row-center">
            <i-column xs="4" md="3"> Пароль </i-column>
            <i-column xs="7" md="7">
              <i-form-group>
                <i-input
                  type="password"
                  v-model="password"
                  :schema="formAuth.password"
                ></i-input>
              </i-form-group>
            </i-column>
          </i-row>
          <i-row v-if="hasError" class="_margin-bottom-1">
            <i-column
              style="display: flex; justify-content: center; color: red"
            >
              {{ errorMessage }}
            </i-column>
          </i-row>
          <i-row class="_margin-bottom-1">
            <i-column style="display: flex; justify-content: center">
              <i-button @click="auth" class="button-confirm">Войти</i-button>
            </i-column>
          </i-row>
          <i-row class="_margin-bottom-1">
            <i-column style="text-align: center">
              Если у вас нет аккаунта можете
              <a @click="toRegistration" class="link">зарегистрироваться</a>
            </i-column>
          </i-row>
        </i-form>
      </i-container>
    </i-card>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import * as model from "@/module/model";

export default Vue.extend({
  name: "AuthPage",
  data() {
    return {
      model,

      login: "",
      password: "",

      formAuth: this.$inkline.form({
        login: {
          validators: [
            {
              rule: "minLength",
              value: 1,
              message: "Поле не должно быть пустым",
            },
          ],
        },
        password: {
          validators: [
            {
              rule: "minLength",
              value: 1,
              message: "Поле не должно быть пустым",
            },
          ],
        },
      }),

      hasError: false,
      errorMessage: "",
    };
  },
  methods: {
    toRegistration() {
      this.$router.push("/registration");
    },
    async auth() {
      this.hasError = false;
      try {
        if (this.formAuth.valid && this.isDirty) {
          await model.method.auth.login(this.login, this.password);
          this.$router.push("/");
        }
      } catch (err: any) {
        this.hasError = true;
        this.errorMessage = err.message;
      }
    },
  },
  computed: {
    isDirty(): boolean {
      return this.formAuth.login.dirty && this.formAuth.password.dirty;
    },
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
