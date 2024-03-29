<template>
  <div class="content-center">
    <i-card id="opacity-block">
      <template slot="header">
        <div class="text-header">
          <a style="color: #233567 !important; font-size: 20px">Регистрация</a>
        </div>
      </template>
      <i-container>
        <i-form v-model="formRegistration">
          <i-row class="_margin-bottom-1 row-center">
            <i-column xs="4" md="3"> Имя </i-column>
            <i-column xs="7" md="7">
              <i-form-group>
                <i-input
                  v-model="firstname"
                  :schema="formRegistration.firstname"
                />
              </i-form-group>
            </i-column>
          </i-row>
          <i-row class="_margin-bottom-1 row-center">
            <i-column xs="4" md="3"> Фамилия </i-column>
            <i-column xs="7" md="7">
              <i-form-group>
                <i-input
                  v-model="lastname"
                  :schema="formRegistration.lastname"
                />
              </i-form-group>
            </i-column>
          </i-row>
          <i-row class="_margin-bottom-1 row-center">
            <i-column xs="4" md="3"> Логин </i-column>
            <i-column xs="7" md="7">
              <i-form-group>
                <i-input v-model="login" :schema="formRegistration.login" />
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
                  :schema="formRegistration.password"
                />
              </i-form-group>
            </i-column>
          </i-row>
          <i-row class="_margin-bottom-1 row-center">
            <i-column xs="4" md="3"> Подтвердите пароль </i-column>
            <i-column xs="7" md="7">
              <i-form-group>
                <i-input
                  type="password"
                  :schema="formRegistration.passwordConfirmation"
                />
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
              <i-form-group>
                <i-button
                  type="submit"
                  @click="registration"
                  class="button-confirm"
                  >Зарегистрироваться</i-button
                >
              </i-form-group>
            </i-column>
          </i-row>
        </i-form>
        <i-row class="_margin-bottom-1">
          <i-column style="text-align: center">
            Если у вас есть аккаунт можете
            <a @click="toAuth" class="link">войти</a>
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
  name: "RegistrationPage",
  data() {
    return {
      model,

      firstname: "",
      lastname: "",
      login: "",
      password: "",

      hasError: false,
      errorMessage: "",

      formRegistration: this.$inkline.form({
        firstname: {
          validators: [
            {
              rule: "minLength",
              value: 1,
              message: "Поле не должно быть пустым",
            },
            {
              rule: "custom",
              validator: (v: any) => /^[а-яёА-ЯЁa-zA-Z]*$/.test(v),
              message: "Вводите только буквы",
            },
          ],
        },
        lastname: {
          validators: [
            {
              rule: "minLength",
              value: 1,
              message: "Поле не должно быть пустым",
            },
            {
              rule: "custom",
              validator: (v: any) => /^[а-яёА-ЯЁa-zA-Z]*$/.test(v),
              message: "Вводите только буквы",
            },
          ],
        },
        login: {
          validators: [
            {
              rule: "minLength",
              value: 3,
              message: "Длина должна быть больше 2 символов",
            },
            {
              rule: "custom",
              validator: (v: any) => /^\w*$/.test(v),
              message: "Вводите только латинские буквы или цифры",
            },
          ],
        },
        password: {
          validators: [
            {
              rule: "minLength",
              value: 6,
              message: "Длина должна быть больше 5 символов",
            },
          ],
        },
        passwordConfirmation: {
          validators: [
            {
              rule: "sameAs",
              target: "password",
              message: "Пароли не совпадают",
            },
          ],
        },
      }),
    };
  },
  methods: {
    toAuth() {
      this.$router.push("/auth");
    },
    async registration() {
      this.hasError = false;
      this.errorMessage = "";
      if (this.formRegistration.valid && this.isDirty) {
        try {
          await model.method.auth.registration(
            this.firstname,
            this.lastname,
            this.login,
            this.password
          );
          this.$router.push("/");
        } catch (err: any) {
          this.hasError = true;
          this.errorMessage = err.message;
        }
      }
    },
  },
  computed: {
    isDirty(): boolean {
      return (
        this.formRegistration.firstname.dirty &&
        this.formRegistration.lastname.dirty &&
        this.formRegistration.login.dirty &&
        this.formRegistration.password.dirty &&
        this.formRegistration.passwordConfirmation.dirty
      );
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
