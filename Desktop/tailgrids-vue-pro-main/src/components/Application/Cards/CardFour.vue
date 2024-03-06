<script setup lang="ts">
import { ref } from 'vue'

const cardItems = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-04/image-01.jpg',
    title: 'Play – Free HTML App & SaaS Landing Page Template',
    subtitle: 'Startup Template',
    details: 'Play is free startup, saas, app landing page template.',
    titleHref: '#'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-04/image-02.jpg',
    title: 'EventGrids is HTML template for Event, Seminar',
    subtitle: 'Events Template',
    details: 'EventGrids is HTML template for Event, Seminar',
    titleHref: '#'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-04/image-01.jpg',
    title: 'Xpeedo is a high-quality landing page template',
    subtitle: 'App Landing Template',
    details: 'Xpeedo is a high-quality landing page template',
    titleHref: '#'
  }
])
</script>

<template>
  <!-- ====== Cards Section Start -->
  <section class="bg-white dark:bg-dark pt-20 pb-10 lg:pt-[120px] lg:pb-20">
    <div class="container mx-auto">
      <div class="flex flex-wrap justify-center -mx-4">
        <template v-for="(item, index) in cardItems" :key="index">
          <div class="w-full px-4 md:w-2/3 lg:w-1/2 xl:w-1/3">
            <div
              class="relative flex items-center w-full p-5 mb-10 bg-white border border-gray-3 dark:bg-dark-2 dark:border-dark-3"
            >
              <span
                class="bg-primary absolute -top-px -left-px h-[3px] w-[calc(100%+1.5px)]"
              ></span>
              <div class="w-full mr-4">
                <span class="block mb-3 text-xs font-semibold text-primary">
                  {{ item.subtitle }}
                </span>
                <h3>
                  <a
                    :href="item.titleHref"
                    class="block mb-4 text-sm font-semibold text-dark hover:text-primary dark:text-white"
                  >
                    {{ item.title }}
                  </a>
                </h3>
                <p class="text-xs text-body-color dark:text-dark-6">
                  {{ item.details }}
                </p>
              </div>
              <div class="mx-auto w-full max-w-[120px] sm:max-w-[140px]">
                <img :src="item.image" alt="image" class="w-full" />
              </div>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>
  <!-- ====== Cards Section End -->
</template>
