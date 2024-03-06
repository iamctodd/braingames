<script setup lang="ts">
import { ref } from 'vue'

const cardItems = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-06/image-01.jpg',
    title: 'Mountain',
    details:
      'Lorem ipsum dolor sit amet, vehicula ero felis loreum fitiona fringilla scelerisque. Interdum et malesuada fames ac ante ipsum primis faucibus.',
    titleHref: '#',
    author: {
      img: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-06/author-01.png',
      name: 'Naimur Rahman',
      role: 'Content Writer'
    }
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-06/image-02.jpg',
    title: 'Sea beach',
    details:
      'Lorem ipsum dolor sit amet, vehicula ero felis loreum fitiona fringilla scelerisque. Interdum et malesuada fames ac ante ipsum primis faucibus.',
    titleHref: '#',
    author: {
      img: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-06/author-02.png',
      name: 'Musharof Chy',
      role: 'Web Developer'
    }
  }
])
</script>

<template>
  <!-- ====== Cards Section Start -->
  <section class="bg-white dark:bg-dark pt-20 pb-10 lg:pt-[120px] lg:pb-20">
    <div class="container mx-auto">
      <div class="flex flex-wrap justify-center -mx-4">
        <template v-for="(item, index) in cardItems" :key="index">
          <div class="w-full px-4 lg:w-10/12 xl:w-8/12 2xl:w-7/12">
            <div
              class="relative z-10 items-center block mb-10 overflow-hidden duration-300 rounded-lg shadow-1 dark:shadow-card hover:shadow-3 dark:bg-dark-2 sm:items-stretch md:flex md:items-center xl:items-stretch"
            >
              <div class="h-[250px] w-full md:h-full md:max-w-[320px] lg:max-w-[335px]">
                <img
                  :src="item.image"
                  alt="image"
                  class="object-cover object-center w-full h-full"
                />
              </div>
              <div class="w-full px-6 py-8 sm:px-8 md:py-6 lg:py-8">
                <div class="flex items-center mb-5">
                  <div class="mr-3 h-[40px] w-full max-w-[40px] overflow-hidden rounded-full">
                    <img :src="item.author.img" alt="image" class="w-full" />
                  </div>
                  <div class="w-full">
                    <h5 class="text-sm font-semibold text-dark sm:text-base dark:text-white">
                      {{ item.author.name }}
                    </h5>
                    <p class="text-xs font-medium text-body-color dark:text-dark-6">
                      {{ item.author.role }}
                    </p>
                  </div>
                </div>
                <h3>
                  <a
                    :href="item.titleHref"
                    class="block mb-3 text-xl font-semibold hover:text-primary text-dark dark:text-white sm:text-2xl md:text-xl lg:text-2xl"
                  >
                    {{ item.title }}
                  </a>
                </h3>
                <p class="text-base leading-relaxed text-body-color dark:text-dark-6">
                  {{ item.details }}
                </p>
              </div>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>
  <!-- ====== Cards Section End -->
</template>
