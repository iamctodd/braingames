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
              class="px-6 py-8 mb-8 duration-300 bg-white rounded-lg shadow-1 hover:shadow-3 dark:bg-dark-2 sm:px-8 lg:px-6 xl:px-8 dark:shadow-card"
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
                class="group inline-flex items-center font-semibold text-primary"
              >
                {{ item.buttonText }}
                <span class="pl-2 duration-300 group-hover:translate-x-2">
                  <svg
                    width="20"
                    height="20"
                    viewBox="0 0 20 20"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M18 9.5L11.5312 2.9375C11.25 2.65625 10.8125 2.65625 10.5312 2.9375C10.25 3.21875 10.25 3.65625 10.5312 3.9375L15.7812 9.28125H2.5C2.125 9.28125 1.8125 9.59375 1.8125 9.96875C1.8125 10.3438 2.125 10.6875 2.5 10.6875H15.8437L10.5312 16.0938C10.25 16.375 10.25 16.8125 10.5312 17.0938C10.6562 17.2188 10.8437 17.2812 11.0312 17.2812C11.2187 17.2812 11.4062 17.2188 11.5312 17.0625L18 10.5C18.2812 10.2187 18.2812 9.78125 18 9.5Z"
                      fill="currentColor"
                    />
                  </svg>
                </span>
              </a>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>
  <!-- ====== Cards Section End -->
</template>
