<script setup lang="ts">
import { ref } from 'vue'

const cardItems = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-03/image-01.jpg',
    title: 'Top Graphic Design Courses Online',
    details:
      'Lorem ipsum dolor sitie amet, consec adipiscing elit. In pretium venenatis sed finibus orci imperdiet et.',
    date: '15 April, 2024',
    author: {
      img: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-03/author-01.png',
      name: 'Samuyl Joshi',
      role: 'Graphics Designer'
    }
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-03/image-02.jpg',
    title: 'Best Web Design Courses Online in 2021',
    details:
      'Lorem ipsum dolor sitie amet, consec adipiscing elit. In pretium venenatis sed finibus orci imperdiet et.',
    date: '15 April, 2024',
    author: {
      img: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-03/author-02.png',
      name: 'Devid Millar',
      role: 'Web Developer'
    }
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-03/image-03.jpg',
    title: 'Android App Development Courses with in 30 days',
    details:
      'Lorem ipsum dolor sitie amet, consec adipiscing elit. In pretium venenatis sed finibus orci imperdiet et.',
    date: '15 April, 2024',
    author: {
      img: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-03/author-03.png',
      name: 'Rulius Hurry',
      role: 'App Developer'
    }
  }
])
</script>

<template>
  <!-- ====== Cards Section Start -->
  <section class="bg-gray-2 dark:bg-dark pt-20 pb-10 lg:pt-[120px] lg:pb-20">
    <div class="container mx-auto">
      <div class="flex flex-wrap -mx-4">
        <template v-for="(item, index) in cardItems" :key="index">
          <div class="w-full px-4 md:w-1/2 xl:w-1/3">
            <div
              class="mb-10 overflow-hidden duration-300 bg-white rounded-lg shadow-1 dark:bg-dark-2 dark:shadow-card hover:shadow-3"
            >
              <img :src="item.image" alt="image" class="w-full" />
              <div class="px-6 py-8 sm:p-8 md:py-7 md:px-5 lg:py-8 lg:px-5 xl:py-8 xl:px-5 2xl:p-8">
                <h3>
                  <a
                    href="javascript:void(0)"
                    class="text-dark dark:text-white hover:text-primary mb-4 block text-xl font-semibold sm:text-[22px] md:text-xl lg:text-[22px] xl:text-xl 2xl:text-[22px]"
                  >
                    {{ item.title }}
                  </a>
                </h3>
                <p
                  class="mb-6 text-base leading-relaxed border-b text-body-color dark:text-dark-6 dark:border-dark-3 border-gray-3 pb-7"
                >
                  {{ item.details }}
                </p>
                <div class="flex flex-wrap items-center justify-between">
                  <div class="flex items-center w-max">
                    <div
                      class="mr-4 h-[40px] w-full max-w-[40px] overflow-hidden rounded-full md:mr-2 md:h-[35px] md:max-w-[35px] lg:mr-4 lg:h-[40px] lg:max-w-[40px]"
                    >
                      <img :src="item.author.img" alt="image" class="w-full" />
                    </div>
                    <div class="w-full">
                      <h5
                        class="text-sm font-medium text-dark dark:text-white sm:text-[15px] md:text-sm lg:text-[15px]"
                      >
                        By {{ item.author.name }}
                      </h5>
                      <p class="text-xs text-body-color dark:text-dark-6">
                        {{ item.author.role }}
                      </p>
                    </div>
                  </div>
                  <div class="w-full max-w-[100px] text-right">
                    <h5
                      class="text-sm font-medium text-dark dark:text-white sm:text-[15px] md:text-sm lg:text-[15px]"
                    >
                      Date
                    </h5>
                    <p class="text-xs text-body-color dark:text-dark-6 whitespace-nowrap">
                      {{ item.date }}
                    </p>
                  </div>
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
