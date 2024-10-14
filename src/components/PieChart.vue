<script setup lang="ts">
import { computed } from "vue";
import { Doughnut } from "vue-chartjs";
import {
  Chart as ChartJS,
  ArcElement,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

ChartJS.register(
  ArcElement,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);

ChartJS.defaults.color = "#ccc";

const props = defineProps<{
  data: Array<object>;
}>();

const chartData = computed(() => ({
  labels: props.data.map((p) => p.name),
  datasets: [
    {
      label: "Nombre de sièges obtenus",
      data: props.data.map((p) => p.currentSeats),
      backgroundColor: props.data.map((p) => p.color),
    },
  ],
}));

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  circumference: 180,
  rotation: -90,
};
</script>

<template>
  <div class="chart-container">
    <Doughnut :data="chartData" :options="chartOptions" />
  </div>
</template>

<style scoped>
.chart-container {
  height: 400px;
}
</style>
