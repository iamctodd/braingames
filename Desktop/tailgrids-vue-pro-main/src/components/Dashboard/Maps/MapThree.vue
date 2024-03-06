<script setup lang="ts">
// @ts-ignore
import jsVectorMap from 'jsvectormap'
import 'jsvectormap/dist/css/jsvectormap.min.css'
import '../../../assets/us-aea-en'
import { onMounted } from 'vue'


onMounted(() => {
  new jsVectorMap({
     map: "us_aea_en",
     selector: "#mapOne",
     zoomButtons: true,
   
     regionStyle: {
       initial: {
         fill: "#C8D0D8",
       },
       hover: {
         fillOpacity: 1,
         fill: "#3056D3",
       },
     },
     regionLabelStyle: {
       initial: {
         fontFamily: "inter",
         fontWeight: "semibold",
         fill: "#fff",
       },
       hover: {
         cursor: "pointer",
       },
     },
   
     labels: {
       regions: {
         render(code: string) {
           return code.split("-")[1];
         },
       },
     },
   });
})
</script>

<template>
  <!-- ====== Maps Section Start -->
  <section class="bg-gray-2 dark:bg-dark py-20 lg:py-[120px]">
    <div class="mx-auto px-4 md:container">
      <div
        class="mx-auto w-full max-w-[560px] overflow-hidden rounded-lg border border-stroke dark:border-dark-3 bg-white dark:bg-dark-2 py-6 px-[30px]"
      >
        <h4 class="mb-8 text-xl font-semibold text-dark dark:text-white">Region labels</h4>
        <div id="mapOne" class="mapOne mapThree !h-[260px] !overflow-visible"></div>
      </div>
    </div>
  </section>
  <!-- ====== Maps Section End -->
</template>
