<script setup lang="ts">
import { ref } from "vue";

const emit = defineEmits(["submit"]);
const inputLocation = ref("");

const handleSubmit = () => {
  if (inputLocation.value.trim()) {
    emit("submit", inputLocation.value);
    inputLocation.value = "";
  }
};
</script>

<template>
  <div class="location-input columns">
    <input
      class="input column"
      v-model="inputLocation"
      @keyup.enter="handleSubmit"
      placeholder="Commune ou code postal"
    />
    <button class="button column" @click="handleSubmit">Localiser</button>
  </div>
</template>

<style scoped>
.location-input {
  margin-bottom: 20px;
}
input {
  padding: 5px;
  margin-right: 10px;
}
</style>
