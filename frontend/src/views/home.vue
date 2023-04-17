<template>
  <div style=" height: 100%;">
    <i-container class="_margin-top-1 _padding-top-1 _margin-bottom-1 _padding-bottom-1"  style="background-color: #c7c7c7; box-shadow: 1px 1px 3px black; height: 100%;">
      <!-- <i-input  class="_float-right _margin-bottom-1"></i-input> -->
      <div>
      <i-collapsible v-model="active">
        <i-collapsible-item v-for="(seasonUnit, index) in model.data.app.seasonList" :key="index" :title="`${seasonUnit.title} ${seasonUnit.year}`" :id="index.toString()"></i-collapsible-item>
    </i-collapsible>
  </div>
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
  methods: {
  }
});
</script>
