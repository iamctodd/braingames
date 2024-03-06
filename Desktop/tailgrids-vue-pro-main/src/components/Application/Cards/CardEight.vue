<script setup lang="ts">
import { ref } from 'vue'

const cardItems = ref([
  {
    title: 'Ready for SaaS Websites Crafted by TailGrids',
    details:
      'Lorem ipsum dolor sit amet, vehiculaum ero felis loreum fitiona fringilla goes scelerisque Interdum et.',
    buttonText: 'Learn More',
    buttonLink: '#'
  },
  {
    title: 'Ready for SaaS Websites Crafted by TailGrids',
    details:
      'Lorem ipsum dolor sit amet, vehiculaum ero felis loreum fitiona fringilla goes scelerisque Interdum et.',
    buttonText: 'Learn More',
    buttonLink: '#'
  },
  {
    title: 'Ready for SaaS Websites Crafted by TailGrids',
    details:
      'Lorem ipsum dolor sit amet, vehiculaum ero felis loreum fitiona fringilla goes scelerisque Interdum et.',
    buttonText: 'Learn More',
    buttonLink: '#'
  }
])
</script>

<template>
  <!-- ====== Cards Section Start -->
  <section class="bg-gray-1 dark:bg-dark pt-20 pb-10 lg:pt-[120px] lg:pb-20">
    <div class="container mx-auto">
      <div class="flex flex-wrap justify-center -mx-4">
        <template v-for="(item, index) in cardItems" :key="index">
          <div class="w-full px-4 md:w-1/2 lg:w-1/3">
            <div
              class="px-6 py-8 mb-8 duration-300 bg-white rounded-lg shadow-1 dark:shadow-card hover:shadow-3 dark:bg-dark-2 sm:px-8 lg:px-6 xl:px-8"
            >
              <h3>
                <a
                  :href="item.buttonLink"
                  class="block mb-3 text-lg font-bold leading-tight hover:text-primary text-dark dark:text-white sm:text-xl sm:leading-tight lg:text-lg lg:leading-tight xl:text-xl xl:leading-tight"
                >
                  {{ item.title }}
                </a>
              </h3>
              <p
                class="mb-5 text-base font-medium leading-relaxed text-body-color dark:text-dark-6"
              >
                {{ item.details }}
              </p>
              <a
                :href="item.buttonLink"
                class="inline-flex items-center px-4 py-2 font-semibold text-white rounded bg-primary hover:bg-opacity-90"
              >
                {{ item.buttonText }}
              </a>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>
  <!-- ====== Cards Section End -->
</template>
