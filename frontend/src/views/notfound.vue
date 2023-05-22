<template>
  <div>
    <i-container style="display: flex; flex-direction: column">
      <i-button link @click="$router.push('/')" style="color: #233567"
        >Вернуться на главную</i-button
      >
      <h1 style="text-align: center; color: #233567">Страница не найдена</h1>
      <img
        class="ne_pevezlo"
        src="@/assets/ne_povezlo.jpg"
        style="width: 100%"
      />
    </i-container>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "NotFound",
});
</script>
