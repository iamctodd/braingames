<script setup lang="ts">
import { ref } from 'vue'
import VueApexCharts from 'vue3-apexcharts'

const chartData = {
  series: [85]
}

const chart = ref(null)

const apexOptions = {
  chart: {
    fontFamily: 'Inter, sans-serif',
    height: 150,
    type: 'radialBar'
  },

  plotOptions: {
    radialBar: {
      hollow: {
        size: '50%'
      },
      dataLabels: {
        name: {
          show: false
        },
        value: {
          fontSize: '16px',
          offsetY: 8
        },
        total: {
          show: false
        }
      }
    }
  },
  dataLabels: {
    enabled: true
  },
  colors: ['#3758F9'],
  legend: {
    show: false
  }
}
</script>

<template>
  <!-- ====== Chart Section Start -->
  <section class="bg-gray-2 dark:bg-dark py-20 lg:py-[120px]">
    <div class="mx-auto px-4 md:container">
      <div
        class="relative mx-auto w-full max-w-[350px] rounded-lg border border-stroke dark:border-dark-3 bg-white dark:bg-dark-2 px-5 py-6 sm:px-[30px]"
      >
        <button
          class="absolute -right-[22px] top-[41%] -rotate-90 rounded-t-md bg-secondary py-1 px-4 text-sm font-medium text-white"
        >
          Clean
        </button>

        <div class="flex items-center">
          <div class="w-full">
            <div id="chartOne" class="-ml-5">
              <VueApexCharts
                type="radialBar"
                height="150"
                :options="apexOptions"
                :series="chartData.series"
                ref="chart"
              />
            </div>
          </div>
          <div class="w-full">
            <p class="mb-2 text-xl font-semibold leading-none text-dark dark:text-white">
              Available Storage
            </p>
            <p class="text-sm font-medium text-dark dark:text-white">
              <span>150</span> <span class="text-xs text-body-color dark:text-dark-6"> GB </span>
              <span>/ 512</span>
              <span class="text-xs text-body-color dark:text-dark-6"> GB </span>
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Chart Section End -->
</template>
