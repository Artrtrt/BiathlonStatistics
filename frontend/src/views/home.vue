<template>
  <div>
    <i-container>
      <i-collapsible v-model="active">
        <i-collapsible-item v-for="(seasonUnit, index) in model.data.app.seasonList" :key="index" :title="`${seasonUnit.title} ${seasonUnit.year}`" :id="index"></i-collapsible-item>
    </i-collapsible>
    </i-container>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import * as model from '@/module/model';
export default Vue.extend({
  name: "NetworkLan",
  data() {
    return {
      model,
      active: [],
    };
  },
});
</script>
