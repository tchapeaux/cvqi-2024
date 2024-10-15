s
<script setup lang="ts">
import { computed } from "vue";

import type { PartyResult } from "../../types/elections";

const props = defineProps<{
  data: Array<PartyResult>;
}>();

const seats = computed(() => {
  const _array = [];
  for (const party of props.data) {
    for (let i = 0; i < party.currentSeats; i++) {
      _array.push({
        party: party.name,
        color: party.color,
      });
    }
  }

  return _array;
});

const totalSeats = computed(() => seats.value.length);
</script>

<template>
  <p>Total: {{ totalSeats }} sièges</p>

  <ul class="square-maps">
    <li v-for="seat in seats" :style="{ '--color': seat.color }"></li>
  </ul>

  <ul class="per-group">
    <li v-for="party in props.data" :style="{ '--color': party.color }">
      {{ party.name }}: {{ party.currentSeats }} siège<span
        v-if="party.currentSeats > 1"
        >s</span
      >
    </li>
  </ul>
</template>

<style scoped>
ul.square-maps {
  --cell-size: 50px;
  list-style-type: none;
  padding: 0;
  margin: 16px 0;

  display: grid;
  grid-template-columns: repeat(auto-fill, var(--cell-size));
  gap: 4px;

  li {
    border-radius: 8px;
    width: var(--cell-size);
    height: var(--cell-size);
    background-color: var(--color);
  }
}

ul.per-group {
  list-style-type: none;
  padding: 0;

  li {
    margin-bottom: 4px;
    display: flex;
    align-items: center;

    &::before {
      content: "";
      display: inline-block;
      width: 20px;
      height: 20px;
      border-radius: 4px;
      background-color: var(--color);
      margin-right: 8px;
    }
  }
}
</style>
