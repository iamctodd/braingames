<script setup lang="ts">
// @ts-ignore
import jsVectorMap from 'jsvectormap'
import 'jsvectormap/dist/css/jsvectormap.min.css'
import { onMounted } from 'vue'
import '../../../assets/us-aea-en'

onMounted(() => {
  new jsVectorMap({
    map: 'us_aea_en',
    selector: '#mapFour',
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
    regionLabelStyle: {
      initial: {
        fontFamily: 'inter',
        fontWeight: 'semibold',
        fill: '#fff'
      },
      hover: {
        cursor: 'pointer'
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
        class="mx-auto w-full max-w-[560px] overflow-hidden rounded-lg border border-stroke dark:border-dark-3 bg-white dark:bg-dark-2 py-6 px-[30px]"
      >
        <div class="mb-8">
          <h4 class="mb-1 text-xl font-semibold text-dark dark:text-white">States statistics</h4>
          <p class="text-sm text-body-color dark:text-dark-6">
            View states statistics by hovering over the map
          </p>
        </div>
        <div id="mapFour" class="mapFour !h-[260px] !overflow-visible"></div>
      </div>
    </div>
  </section>
  <!-- ====== Maps Section End -->
</template>
