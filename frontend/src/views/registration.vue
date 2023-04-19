<template>
  <div class="content-center">
    <i-card id="opacity-block">
      <template slot="header">
        <div class="text-header">
          <a style="color: #233567 !important; font-size: 20px;">Регистрация</a>
        </div>
      </template>
      <i-container>
        <i-form v-model="formRegistration">
          <i-row class="_margin-bottom-1 row-center">
            <i-column xs="4" md="3">
              Имя
            </i-column>
            <i-column xs="7" md="7">
              <i-form-group>
                <i-input v-model="firstname" :schema="formRegistration.firstname"/>
              </i-form-group>
            </i-column>
          </i-row>
          <i-row class="_margin-bottom-1 row-center">
            <i-column xs="4" md="3">
              Фамилия
            </i-column>
            <i-column xs="7" md="7">
              <i-form-group>
                <i-input v-model="lastname" :schema="formRegistration.lastname"/>
              </i-form-group>
            </i-column>
          </i-row>
          <i-row class="_margin-bottom-1 row-center">
            <i-column xs="4" md="3">
              Логин
            </i-column>
            <i-column xs="7" md="7">
              <i-form-group>
                <i-input v-model="login" :schema="formRegistration.login"/>
              </i-form-group>
            </i-column>
          </i-row>
          <i-row class="_margin-bottom-1 row-center">
            <i-column xs="4" md="3">
              Пароль
            </i-column>
            <i-column xs="7" md="7">
              <i-form-group>
                <i-input type="password" v-model="password" :schema="formRegistration.password"/>
              </i-form-group>
            </i-column>
          </i-row>
        <i-row class="_margin-bottom-1">
          <i-column style="display: flex; justify-content: center;">
            <i-form-group>
            <i-button type="submit" @click="registration" class="button-confirm">Зарегистрироваться</i-button>
          </i-form-group>
          </i-column>
        </i-row>
      </i-form>
        <i-row class="_margin-bottom-1">
          <i-column style="text-align: center;">
            Если у вас есть аккаунта можете <a href="/auth">войти</a>
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

      firstname: '',
      lastname: '',
      login: '',
      password: '',

      formRegistration: this.$inkline.form({
        firstname: {
          validators: [
            { rule: 'minLength', value: 1, message: "Поле не должно быть пустым" },
            { rule: 'custom', validator: (v: any) => /^[а-яА-Яa-zA-Z]*$/.test(v), message: "Вводите только буквы" }
          ]
        },
        lastname: {
          validators: [
          { rule: 'minLength', value: 1, message: "Поле не должно быть пустым" },
            { rule: 'custom', validator: (v: any) => /^[а-яА-Яa-zA-Z]*$/.test(v), message: "Вводите только буквы" }
          ]
        },
        login: {
          validators: [
            { rule: 'minLength', value: 3, message: "Длина должна быть больше 2 символов" },
            { rule: 'custom', validator: (v: any) => /^\w*$/.test(v), message: "Вводите только буквы и цифры" }
          ]
        },
        password: {
          validators: [
            { rule: 'minLength', value: 6, message: "Длина должна быть больше 5 символов" }
          ]
        },
      })
    };
  },
  methods: {
    async registration() {
      if (this.formRegistration.valid && this.formRegistration.dirty) {
        await model.method.auth.registration(this.firstname, this.lastname, this.login, this.password);
      }
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