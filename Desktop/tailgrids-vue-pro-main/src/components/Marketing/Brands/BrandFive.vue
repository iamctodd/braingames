<script setup lang="ts">
import { ref } from 'vue'

const brandItems = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/assets/images/brands/graygrids.svg',
    link: '#'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/assets/images/brands/lineicons.svg',
    link: '#'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/assets/images/brands/ayroui.svg',
    link: '#'
  }
])
</script>

<template>
  <!-- ====== Brands Section Start -->
  <section class="bg-white py-20 dark:bg-dark lg:py-[120px]">
    <div class="container mx-auto">
      <div class="flex flex-wrap items-center -mx-4">
        <div class="w-full px-4 lg:w-1/2 xl:w-5/12">
            <div>
               <h2
                  class="text-dark dark:text-white text-3xl font-bold sm:text-4xl lg:text-3xl xl:text-[33px] 2xl:text-4xl"
                  >
                  Tailwind CSS UI Components for Modern Web Apps
               </h2>
            </div>
         </div>

        <div class="w-full px-4 lg:w-1/2 xl:w-7/12">
          <div class="flex flex-wrap items-center justify-center mt-12 lg:mt-0 xl:justify-end">
            <template v-for="(item, index) in brandItems" :key="index">
              <a
                :href="item.link"
                class="mx-4 flex min-w-[150px] max-w-[200px] items-center justify-center py-5 lg:min-w-min lg:max-w-[110px] xl:max-w-[200px]"
              >
                <img :src="item.image" alt="image" class="h-10 w-full" />
              </a>
            </template>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Brands Section End -->
</template>
