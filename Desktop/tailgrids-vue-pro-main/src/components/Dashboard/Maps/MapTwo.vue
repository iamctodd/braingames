<script setup lang="ts">
// @ts-ignore
import jsVectorMap from 'jsvectormap'
import 'jsvectormap/dist/css/jsvectormap.min.css'
import 'jsvectormap/dist/maps/world'
import { onMounted, ref } from 'vue'

const countries = ref([
  {
    name: 'United States',
    flag: 'https://cdn.tailgrids.com/2.0/image/assets/images/countries/usa.svg',
    percentage: 35
  },
  {
    name: 'Canada',
    flag: 'https://cdn.tailgrids.com/2.0/image/assets/images/countries/canada.svg',
    percentage: 26
  },
  {
    name: 'France',
    flag: 'https://cdn.tailgrids.com/2.0/image/assets/images/countries/france.svg',
    percentage: 18
  },
  {
    name: 'Italy',
    flag: 'https://cdn.tailgrids.com/2.0/image/assets/images/countries/italy.svg',
    percentage: 14
  },
  {
    name: 'Australia',
    flag: 'https://cdn.tailgrids.com/2.0/image/assets/images/countries/australia.svg',
    percentage: 10
  },
  {
    name: 'India',
    flag: 'https://cdn.tailgrids.com/2.0/image/assets/images/countries/india.svg',
    percentage: 7
  }
])

onMounted(() => {
  new jsVectorMap({
    map: 'world',
    selector: '#mapTwo',
    zoomButtons: true,

    regionStyle: {
      initial: {
        fill: '#A9BDFF'
      },
      hover: {
        fillOpacity: 1,
        fill: '#3056D3'
      }
    },

    onRegionTooltipShow: function (tooltip: { selector: any, text: () => any }, code: string) {
      if (code === 'EG') {
        tooltip.selector.innerHTML = tooltip.text() + ' <b>(Hello Russia)</b>'
      }
    }
  })
})
</script>

<template>
  <!-- ====== Maps Section Start -->
  <section class="bg-gray-2 dark:bg-dark py-20 lg:py-[120px]">
    <div class="mx-auto px-4 md:container">
      <div
        class="mx-auto w-full max-w-[770px] overflow-hidden rounded-lg border border-stroke dark:border-dark-3 bg-white dark:bg-dark-2"
      >
        <div class="p-[30px]">
          <div class="justify-between sm:flex mb-10">
            <div class="mb-2">
              <h3
                class="text-lg font-semibold leading-none text-dark dark:text-white sm:text-xl mb-1"
              >
                Sessions by country
              </h3>
              <p class="text-sm font-medium text-body-color dark:text-dark-6">
                View website visitors by hovering over the map
              </p>
            </div>
            <div class="mb-2">
              <div class="relative z-20 inline-block">
                <select
                  name=""
                  id=""
                  class="relative z-20 inline-flex appearance-none rounded-md border border-stroke dark:border-dark-3 bg-transparent py-[9px] pl-3 pr-10 text-sm text-body-color dark:text-dark-6 outline-none"
                >
                  <option value="" class="dark:bg-dark-2">Last 7 days</option>
                  <option value="" class="dark:bg-dark-2">Last 15 days</option>
                </select>
                <span
                  class="absolute top-1/2 right-3 z-10 -translate-y-1/2 text-body-color dark:text-dark-6"
                >
                  <svg
                    width="18"
                    height="18"
                    viewBox="0 0 18 18"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                    class="fill-current"
                  >
                    <path
                      d="M9.00001 12.8251C8.83126 12.8251 8.69064 12.7689 8.55001 12.6564L2.08126 6.30015C1.82814 6.04702 1.82814 5.65327 2.08126 5.40015C2.33439 5.14702 2.72814 5.14702 2.98126 5.40015L9.00001 11.2783L15.0188 5.3439C15.2719 5.09077 15.6656 5.09077 15.9188 5.3439C16.1719 5.59702 16.1719 5.99077 15.9188 6.2439L9.45001 12.6001C9.30939 12.7408 9.16876 12.8251 9.00001 12.8251Z"
                    />
                  </svg>
                </span>
              </div>
            </div>
          </div>
          <div id="mapTwo" class="mapTwo !h-[260px]"></div>
        </div>
        <div class="space-y-[14px] border-t border-stroke dark:border-dark-3 p-[30px]">
          <template v-for="(country, index) in countries" :key="index">
            <div class="items-center sm:flex">
              <div class="flex w-full max-w-[170px] items-center">
                <img :src="country.flag" :alt="country.name" class="mr-[14px] h-[14px]" />
                <p class="text-base font-medium text-dark dark:text-white">{{ country.name }}</p>
              </div>
              <div class="relative block h-[18px] w-full rounded bg-[#E5E7EB] dark:bg-dark-3">
                <div
                  :style="{ width: `${country.percentage}%` }"
                  class="absolute left-0 top-0 flex h-full items-center justify-center rounded bg-primary text-xs font-medium text-white"
                >
                  {{ country.percentage }}%
                </div>
              </div>
            </div>
          </template>
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Maps Section End -->
</template>
