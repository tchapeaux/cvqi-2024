<script setup lang="ts">
import { computed, ref } from "vue";
import COMMUNES_DATA from "../assets/communes.json";

const emit = defineEmits(["submit"]);
const inputLocation = ref("");

const matchingCommunes = computed(() => {
  return COMMUNES_DATA.filter(
    (c) =>
      c.label.toLowerCase().includes(inputLocation.value.toLowerCase()) ||
      c.zip.includes(Number(inputLocation.value))
  );
});

function goToFirstResult() {
  if (matchingCommunes.value.length > 0) {
    handleSubmit(matchingCommunes.value[0].label);
  }
}

function handleSubmit(communeName: string)  {
  if (communeName.trim()) {
    emit("submit", communeName);
    inputLocation.value = "";
  }
};
</script>

<template>
  <input
    class="input block"
    v-model="inputLocation"
    placeholder="Commune ou code postal"
    @keyup.enter="goToFirstResult"
  />

  <p v-if="!!inputLocation && matchingCommunes.length === 0" class="block">
    Pas de communes correspondantes
  </p>
  <ul v-else-if="matchingCommunes.length < 10" class="grid block">
    <li v-for="commune of matchingCommunes" class="cell">
      <button
        class="button"
        :style="{ width: '100%' }"
        @click="() => handleSubmit(commune.label)"
      >
        {{ commune.label }}
      </button>
    </li>
  </ul>
</template>

<style scoped></style>
