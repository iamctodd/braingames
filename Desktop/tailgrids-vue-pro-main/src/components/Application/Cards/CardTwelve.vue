<script setup lang="ts">
import { ref } from 'vue'

const cardItems = ref([
  {
    title: 'Card Title here',
    details:
      'Lorem ipsum dolor sit amet, vehiculaum ero felis loreum fitiona fringilla goes scelerisque Interdum et.',
    titleHref: '#'
  },
  {
    title: 'Card Title here',
    details:
      'Lorem ipsum dolor sit amet, vehiculaum ero felis loreum fitiona fringilla goes scelerisque Interdum et.',
    titleHref: '#'
  },
  {
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
            <div class="mb-10 bg-white border border-stroke dark:bg-dark-2 dark:border-dark-3">
              <div class="py-5 border-b border-stroke px-7 dark:border-dark-3">
                <h3>
                  <a
                    :href="item.titleHref"
                    class="inline-block text-lg font-semibold hover:text-primary text-dark dark:text-white sm:text-xl lg:text-lg xl:text-xl"
                  >
                    {{ item.title }}
                  </a>
                </h3>
              </div>

              <div class="pt-6 px-7 pb-9">
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
