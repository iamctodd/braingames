<script setup lang="ts">
import { ref } from 'vue'

const cardItems = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-10/image-01.jpg',
    title: 'Card Title here',
    details:
      'Lorem ipsum dolor sit amet, vehiculaum ero felis loreum fitiona fringilla goes scelerisque Interdum et.',
    titleHref: '#'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-10/image-02.jpg',
    title: 'Card Title here',
    details:
      'Lorem ipsum dolor sit amet, vehiculaum ero felis loreum fitiona fringilla goes scelerisque Interdum et.',
    titleHref: '#'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-10/image-03.jpg',
    title: 'Card Title here',
    details:
      'Lorem ipsum dolor sit amet, vehiculaum ero felis loreum fitiona fringilla goes scelerisque Interdum et.',
    titleHref: '#'
  }
])
</script>

<template>
  <!-- ====== Cards Section Start -->
  <section class="bg-gray-2 dark:bg-dark pt-20 pb-10 lg:pt-[120px] lg:pb-20">
    <div class="container mx-auto">
      <div class="flex flex-wrap justify-center -mx-4">
        <template v-for="(item, index) in cardItems" :key="index">
          <div class="w-full px-4 md:w-1/2 lg:w-1/3">
            <div
              class="p-4 pb-6 mb-10 duration-300 bg-white rounded-lg shadow-1 dark:shadow-card hover:shadow-3 dark:bg-dark-2"
            >
              <div class="w-full mb-6 overflow-hidden rounded-md">
                <img
                  :src="item.image"
                  alt="card image"
                  class="object-cover object-center w-full h-full"
                />
              </div>

              <div class="px-[10px]">
                <h3>
                  <a
                    :href="item.titleHref"
                    class="inline-block mb-3 text-lg font-semibold hover:text-primary text-dark dark:text-white sm:text-xl lg:text-lg xl:text-xl"
                  >
                    {{ item.title }}
                  </a>
                </h3>
                <p class="text-base text-body-color dark:text-dark-6">
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
