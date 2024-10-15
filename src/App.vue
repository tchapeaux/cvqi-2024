<script setup lang="ts">
import { computed, ref } from "vue";
import LocationInput from "./components/LocationInput.vue";
import WaffleChart from "./components/WaffleChart.vue";
import axios from "axios";
import COMMUNES_DATA from "./assets/communes.json";
import type { Context } from "../types/maptiler.d.ts";

const location = ref("");
const zipCode = ref("");

// Please don't steal my key
const MAPTILER_KEY = "oZEk7t5u3PrT6zsjrxlA";

const handleLocationSubmit = async (submittedLocation: string) => {
  const commune =
    COMMUNES_DATA.find(
      (c) => c.label.toLowerCase() === submittedLocation.toLowerCase()
    ) || COMMUNES_DATA.find((c) => c.zip.includes(Number(submittedLocation)));

  location.value = commune?.label || "Non trouvé";
  zipCode.value = (commune?.zip[0] && String(commune?.zip[0])) || "Non trouvé";
};

const handleAutoLocate = async () => {
  if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(
      async (position) => {
        const { accuracy, latitude, longitude } = position.coords;

        if (!latitude || !longitude || accuracy > 10000) {
          console.error("Geolocation not accurate enough", position);
          alert(
            "La localisation renvoyée par votre appareil n'est pas assez précise"
          );
          return;
        }

        // Use Axios to fetch from MapTiler
        const response = await axios.get(
          `https://api.maptiler.com/geocoding/${longitude},${latitude}.json?key=${MAPTILER_KEY}`
        );

        const allContext: Context[] = response.data.features?.[0].context;

        zipCode.value =
          allContext.find((c) => c.id.startsWith("postal_code"))?.text ||
          "Non trouvé";

        location.value =
          COMMUNES_DATA.find((c) => c.zip.includes(Number(zipCode.value)))
            ?.label || "Non trouvé";
      },
      (error) => {
        console.error("Error getting geolocation:", error);
        alert("Votre appareil n'a pas pu être localisé");
      }
    );
  }
};

function resetLocation() {
  location.value = "";
  zipCode.value = "";
}

const hasLocationData = computed(() => location.value && zipCode.value);

const currentCommune = computed(() =>
  COMMUNES_DATA.find((c) => c.zip.includes(Number(zipCode.value)))
);

const currentLocationData = computed(() =>
  currentCommune.value?.results?.parties
    .filter((p) => p.currentSeats > 0)
    .sort((p1, p2) => p2.currentSeats - p1.currentSeats)
);
</script>

<template>
  <div class="app">
    <header class="section">
      <h1 class="title is-2">Ça vote quoi ici&nbsp;?</h1>
      <p class="subtitle is-4">
        Recherche rapide des résultats des élections communales de 2024
      </p>
    </header>
    <main class="section">
      <template v-if="!hasLocationData">
        <button class="block button is-primary" @click="handleAutoLocate">
          Localisation automatique
        </button>
        <p class="block">ou</p>
        <LocationInput @submit="handleLocationSubmit" />
      </template>
      <template v-else>
        <h2 class="block title is-3">📍 {{ location }} ({{ zipCode }})</h2>
        <div class="block">
          <WaffleChart v-if="currentLocationData" :data="currentLocationData" />
        </div>
        <button class="button block" @click="resetLocation">Recommencer</button>
      </template>
    </main>
    <footer class="section">
      <p class="block">🍍Un web-gadget par tchapeaux</p>
      <p class="block">
        Données électorales récupérées le 14/10/2024 de la RTBF (<a
          href="https://www.rtbf.be/elections-2024/communales/toutes-les-communes"
          target="_blank"
          >Source</a
        >).<br />Merci le service public 🙏
      </p>
      <p class="block">
        Geo-localisation automatique par
        <a href="https://maptiler.com" target="_blank"
          ><strong>map</strong>tiler</a
        >.
      </p>
    </footer>
  </div>
</template>

<style>
.app {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}
</style>
