<script setup lang="ts">
import { ref } from 'vue'

const cardItems = ref([
  {
    title: 'Ready for SaaS Websites Crafted by TailGrids',
    details:
      'Lorem ipsum dolor sit amet, vehiculaum ero felis loreum fitiona fringilla goes scelerisque Interdum et.',
    titleHref: '#',
    author: {
      img: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-09/author-01.png',
      name: 'Naimur Rahman',
      role: 'Content Writer'
    }
  },
  {
    title: 'Ready for SaaS Websites Crafted by TailGrids',
    details:
      'Lorem ipsum dolor sit amet, vehiculaum ero felis loreum fitiona fringilla goes scelerisque Interdum et.',
    titleHref: '#',
    author: {
      img: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-09/author-02.png',
      name: 'Musharof Chy',
      role: 'Web Developer'
    }
  },
  {
    title: 'Ready for SaaS Websites Crafted by TailGrids',
    details:
      'Lorem ipsum dolor sit amet, vehiculaum ero felis loreum fitiona fringilla goes scelerisque Interdum et.',
    titleHref: '#',
    author: {
      img: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-09/author-03.png',
      name: 'Shafiq Hammad',
      role: 'Frontend Developer'
    }
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
                  :href="item.titleHref"
                  class="block mb-3 text-lg font-bold leading-tight hover:text-primary text-dark dark:text-white sm:text-xl sm:leading-tight lg:text-lg lg:leading-tight xl:text-xl xl:leading-tight"
                >
                  {{ item.title }}
                </a>
              </h3>
              <p
                class="mb-6 text-base font-medium leading-relaxed text-body-color dark:text-dark-6"
              >
                {{ item.details }}
              </p>
              <div class="flex items-center">
                <div class="mr-3 h-[40px] w-full max-w-[40px] overflow-hidden rounded-full">
                  <img :src="item.author.img" alt="image" class="w-full" />
                </div>
                <div class="w-full">
                  <h5 class="text-sm font-semibold text-dark dark:text-white sm:text-base">
                    {{ item.author.name }}
                  </h5>
                  <p class="text-xs font-medium text-body-color dark:text-dark-6">
                    {{ item.author.role }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>
  <!-- ====== Cards Section End -->
</template>
