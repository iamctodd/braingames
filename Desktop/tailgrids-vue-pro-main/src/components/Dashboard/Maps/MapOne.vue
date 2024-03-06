<script setup lang="ts">
// @ts-ignore
import jsVectorMap from 'jsvectormap'
import 'jsvectormap/dist/css/jsvectormap.min.css'
import 'jsvectormap/dist/maps/world-merc'
import { onMounted } from 'vue'

const markers = [
  { name: 'Russia', coords: [61, 105], sales: 580 },
  { name: 'Geenland', coords: [72, -42], sales: 600 },
  { name: 'Canada', coords: [56.1304, -106.3468], sales: 820 },
  { name: 'Palestine', coords: [31.5, 34.8], sales: 350 },
  { name: 'Brazil', coords: [-14.235, -51.9253], sales: 490 }
]

onMounted(() => {
  new jsVectorMap({
    map: 'world_merc',
    selector: '#mapOne',
    zoomButtons: true,

    regionStyle: {
      initial: {
        fill: '#C8D0D8'
      }
    },
    markersSelectable: true,
    markers: markers,
    markerStyle: {
      initial: {
        r: 7,
        fill: '#3056D3',
        fillOpacity: 1,
        stroke: '#FFF',
        strokeWidth: 5,
        strokeOpacity: 1
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
        class="mx-auto w-full max-w-[430px] overflow-hidden rounded-lg border border-stroke dark:border-dark-3 bg-white dark:bg-dark-2 pt-6 pb-[30px] px-[30px]"
      >
        <h4 class="mb-2 text-lg font-semibold text-dark dark:text-white">Sells by State</h4>
        <div id="mapOne" class="mapOne !h-[260px] !overflow-visible"></div>
        <p class="mt-2 text-sm text-body-color dark:text-dark-6">
          <span class="pr-1">Last updated: </span>
          <span class="text-dark dark:text-white"> 7 days </span>
          <span class="pl-1">ago</span>
        </p>
      </div>
    </div>
  </section>
  <!-- ====== Maps Section End -->
</template>
