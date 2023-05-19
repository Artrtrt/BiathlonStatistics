<template>
  <div v-if="showConfirm">
    <div
      @click="confirm()"
      style="float: left"
      class="button-icon _margin-right-1"
    >
      <img src="@/assets/checkmark.svg" />
    </div>
    <div @click="cancel()" style="float: left" class="button-icon">
      <img src="@/assets/cross.svg" />
    </div>
  </div>
  <div v-else>
    <div style="float: left" class="button-icon">
      <i-button :disabled="disabled" @click="primary()" link
        ><img src="@/assets/pen.svg"
      /></i-button>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "i-confirm-button",
  props: {
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      showConfirm: false,
    };
  },
  methods: {
    async primary() {
      this.$emit("primary");
      this.showConfirm = true;
    },
    confirm() {
      this.showConfirm = false;
      this.$emit("confirm");
    },
    cancel() {
      this.showConfirm = false;
      this.$emit("cancel");
    },
  },
});
</script>
