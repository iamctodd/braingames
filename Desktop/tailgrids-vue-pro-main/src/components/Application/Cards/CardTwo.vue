<script setup lang="ts">
import { ref } from 'vue'

const cardItems = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-02/image-01.jpg',
    title: 'Creative Website Themes & Templates in 2021',
    details: 'Lorem ipsum dolor sit amet pretium consectetur adipiscing elit.',
    buttonText: 'View Details',
    buttonLink: '#'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-02/image-02.jpg',
    title: 'Android App Development Course With In 30 Days',
    details: 'Lorem ipsum dolor sit amet pretium consectetur adipiscing elit.',
    buttonText: 'View Details',
    buttonLink: '#'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-02/image-03.jpg',
    title: 'Top 20+ Graphic Design Online Courses',
    details: 'Lorem ipsum dolor sit amet pretium consectetur adipiscing elit.',
    buttonText: 'View Details',
    buttonLink: '#'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-02/image-04.jpg',
    title: 'Best Web Design Courses Online in 2021',
    details: 'Lorem ipsum dolor sit amet pretium consectetur adipiscing elit.',
    buttonText: 'View Details',
    buttonLink: '#'
  }
])
</script>

<template>
  <!-- ====== Cards Section Start -->
  <section class="bg-white dark:bg-dark pt-20 pb-10 lg:pt-[120px] lg:pb-20">
    <div class="container mx-auto">
      <div class="flex flex-wrap -mx-4">
        <template v-for="(item, index) in cardItems" :key="index">
          <div class="w-full px-4 lg:w-1/2 xl:w-1/2">
            <div
              class="relative z-10 mb-10 block items-center overflow-hidden rounded-lg bg-[#F2F5FC] sm:flex sm:items-stretch md:items-center lg:block xl:flex xl:items-stretch dark:bg-dark-2"
            >
              <div
                class="w-full sm:max-w-[200px] md:max-w-[250px] lg:max-w-full xl:max-w-[200px] 2xl:max-w-[240px]"
              >
                <div class="h-[250px] sm:h-full lg:h-[250px] xl:h-full">
                  <img
                    :src="item.image"
                    alt="image"
                    class="object-cover object-center w-full h-full"
                  />
                </div>
              </div>
              <div class="w-full p-8 sm:p-6 md:p-8">
                <h3>
                  <a
                    :href="item.buttonLink"
                    class="block mb-3 text-xl font-semibold text-dark dark:text-white hover:text-primary"
                  >
                    {{ item.title }}
                  </a>
                </h3>
                <p class="mb-5 text-base leading-relaxed text-body-color dark:text-dark-6">
                  {{ item.details }}
                </p>
                <a
                  :href="item.buttonLink"
                  class="inline-block px-6 py-2 text-sm font-medium transition border rounded-full border-primary text-primary hover:border-primary hover:bg-primary hover:text-white"
                >
                  {{ item.buttonText }}
                </a>
              </div>
              <span class="absolute bottom-2 right-2 z-[-1]">
                <svg
                  width="22"
                  height="30"
                  viewBox="0 0 22 30"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <circle
                    cx="20.3422"
                    cy="28.6142"
                    r="1.07573"
                    transform="rotate(180 20.3422 28.6142)"
                    fill="#3056D3"
                  />
                  <circle
                    cx="20.3422"
                    cy="10.3271"
                    r="1.07573"
                    transform="rotate(180 20.3422 10.3271)"
                    fill="#3056D3"
                  />
                  <circle
                    cx="20.3383"
                    cy="19.3631"
                    r="1.07573"
                    transform="rotate(180 20.3383 19.3631)"
                    fill="#3056D3"
                  />
                  <circle
                    cx="20.3422"
                    cy="1.07564"
                    r="1.07573"
                    transform="rotate(180 20.3422 1.07564)"
                    fill="#3056D3"
                  />
                  <circle
                    cx="10.7094"
                    cy="28.6142"
                    r="1.07573"
                    transform="rotate(180 10.7094 28.6142)"
                    fill="#3056D3"
                  />
                  <circle
                    cx="10.7094"
                    cy="10.3271"
                    r="1.07573"
                    transform="rotate(180 10.7094 10.3271)"
                    fill="#3056D3"
                  />
                  <circle
                    cx="10.7094"
                    cy="19.3631"
                    r="1.07573"
                    transform="rotate(180 10.7094 19.3631)"
                    fill="#3056D3"
                  />
                  <circle
                    cx="10.7094"
                    cy="1.07564"
                    r="1.07573"
                    transform="rotate(180 10.7094 1.07564)"
                    fill="#3056D3"
                  />
                  <circle
                    cx="1.07661"
                    cy="28.6142"
                    r="1.07573"
                    transform="rotate(180 1.07661 28.6142)"
                    fill="#3056D3"
                  />
                  <circle
                    cx="1.07661"
                    cy="10.3271"
                    r="1.07573"
                    transform="rotate(180 1.07661 10.3271)"
                    fill="#3056D3"
                  />
                  <circle
                    cx="1.07661"
                    cy="19.3631"
                    r="1.07573"
                    transform="rotate(180 1.07661 19.3631)"
                    fill="#3056D3"
                  />
                  <circle
                    cx="1.07661"
                    cy="1.07564"
                    r="1.07573"
                    transform="rotate(180 1.07661 1.07564)"
                    fill="#3056D3"
                  />
                </svg>
              </span>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>
  <!-- ====== Cards Section End -->
</template>
