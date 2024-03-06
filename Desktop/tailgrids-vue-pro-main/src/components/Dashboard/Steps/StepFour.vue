<script setup lang="ts">
import { ref } from 'vue'
import VueApexCharts from 'vue3-apexcharts'

const chartData = {
  series: [72]
}

const chart = ref(null)

const apexOptions = {
  chart: {
    height: 200,
    type: 'radialBar'
  },
  plotOptions: {
    radialBar: {
      hollow: {
        size: '66%'
      },
      dataLabels: {
        name: {
          show: true,
          fontSize: '16px',
          fontFamily: '"Inter"',
          offsetY: -12
        },
        value: {
          fontSize: '28px',
          fontWeight: 'bold',
          fontFamily: 'inter',
          offsetY: 2
        },
        total: {
          show: true,
          fontFamily: 'inter',
          fontSize: '12px',
          label: 'complete',
          offsetY: -16
        }
      }
    }
  },
  dataLabels: {
    enabled: true
  },
  colors: ['#3056D3'],
  legend: {
    show: false,
    position: 'bottom'
  }
}
</script>

<template>
  <section class="min-h-screen overflow-hidden bg-white dark:bg-dark py-20 lg:py-[120px]">
    <div class="mx-auto px-4 md:container">
      <div class="flex items-center justify-center">
        <div>
          <div id="chartOne" class="-ml-5">
            <VueApexCharts
              type="radialBar"
              height="200"
              :options="apexOptions"
              :series="chartData.series"
              ref="chart"
            />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
