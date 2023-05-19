<template>
  <div style="position: fixed; z-index: 2; bottom: 2vh; right: 5vw; z-index: 2">
    <i-layout v-if="showChat" class="chat">
      <i-layout-header class="chat-header"> Общий чат </i-layout-header>
      <hr class="_margin-0" />
      <i-layout-content class="chat-content scroll">
        <div ref="chat">
          <div
            v-for="(messageUnit, index) in model.data.chat.messageList"
            :key="index"
          >
            <div
              v-if="model.data.auth.login === messageUnit.login"
              style="width: 100%; padding-left: 60px"
            >
              <div class="login">you:</div>
              <div class="your-message">
                {{ messageUnit.message }}
              </div>
            </div>
            <div v-else style="padding-right: 60px">
              <div class="login">{{ messageUnit.login }}:</div>
              <div class="message">
                {{ messageUnit.message }}
              </div>
            </div>
          </div>
        </div>
      </i-layout-content>
      <hr class="_margin-0" />
      <i-layout-footer class="chat-footer">
        <div
          v-if="model.data.auth.authorized"
          style="
            background-color: #6e9ccf;
            border-radius: 10px;
            display: flex;
            padding: 10px;
          "
        >
          <input v-model="message" @keydown.enter="sendMessage" />
          <div
            @click="sendMessage"
            style="
              height: 30px;
              width: 35px;
              background-color: #e8eeff;
              cursor: pointer;
              border-radius: 30px;
              text-align: center;
            "
          >
            <img
              style="height: 19px; width: 14px"
              src="@/assets/triangle.svg"
            />
          </div>
        </div>
        <div v-else>
          Для того чтобы отправлять сообщения в чат авторизируйтесь
        </div>
      </i-layout-footer>
    </i-layout>
    <img
      @click="showChat = !showChat"
      style="height: 60px; width: 60px; float: right; cursor: pointer"
      src="@/assets/chat.svg"
    />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import * as model from "@/module/model";
export default Vue.extend({
  name: "i-chat",
  data() {
    return {
      model,
      showChat: false,
      message: "",
    };
  },
  async mounted() {
    if (model.data.chat.messageList.length === 0) {
      await model.method.chat.import();
    }
  },
  methods: {
    async sendMessage() {
      if (this.message !== "") {
        await model.method.chat.sendMessage(this.message);
        this.message = "";
      }
    },
  },
});
</script>

<style scoped>
.message {
  word-wrap: break-word;
  background-color: #6e9ccf;
  margin-bottom: 15px;
  border-radius: 10px;
  padding: 10px;
  /* max-width: 270px; */
}

.login {
  word-wrap: break-word;
  font-size: 13px;
  font-weight: bold;
}

.your-message {
  word-wrap: break-word;
  margin-bottom: 15px;
  border-radius: 10px;
  padding: 10px;
  background-color: #e8eeff;
}

.chat {
  margin-right: 30px;
  border-radius: 20px;
  height: 600px;
  width: 300px;
  background-color: #c3d7ed;
}

.chat-header {
  font-weight: bold;
  text-align: center;
  color: #233567;
}

.chat-content {
  overflow: auto;
  padding: 15px 15px 0px 15px;
}

.chat-footer {
  border-radius: 10px;
  background-color: #c3d7ed !important;
}

.chat hr {
  background-color: #3d72b0;
}

input {
  background-color: #6e9ccf;
  width: 100%;
  height: 30px;
  padding: 15px;
  border: 0px;
  outline: none;
}
</style>
