<script setup lang="ts">
import { ref } from 'vue'

const cardItems = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-05/image-01.jpg',
    title: 'Mountain',
    titleHref: '#',
    details:
      'Lorem ipsum dolor sit amet, vehicula ero felis loreum fitiona fringilla scelerisque. Interdum et malesuada fames ac ante ipsum primis faucibus.',
    tags: [
      { name: '#mountain', metaHref: '#' },
      { name: '#hill', metaHref: '#' },
      { name: '#rock', metaHref: '#' }
    ]
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-05/image-02.jpg',
    title: 'Sea beach',
    titleHref: '#',
    details:
      'Lorem ipsum dolor sit amet, vehicula ero felis loreum fitiona fringilla scelerisque. Interdum et malesuada fames ac ante ipsum primis faucibus.',
    tags: [
      { name: '#sea-beach', metaHref: '#' },
      { name: '#sea', metaHref: '#' },
      { name: '#nature', metaHref: '#' }
    ]
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/cards/card-05/image-03.jpg',
    title: 'Ice land',
    titleHref: '#',
    details:
      'Lorem ipsum dolor sit amet, vehicula ero felis loreum fitiona fringilla scelerisque. Interdum et malesuada fames ac ante ipsum primis faucibus.',
    tags: [
      { name: '#ice-land', metaHref: '#' },
      { name: '#ice', metaHref: '#' }
    ]
  }
])
</script>

<template>
  <!-- ====== Cards Section Start -->
  <section class="bg-white dark:bg-dark pt-20 pb-10 lg:pt-[120px] lg:pb-20">
    <div class="container mx-auto">
      <div class="flex flex-wrap -mx-4">
        <template v-for="(item, index) in cardItems" :key="index">
          <div class="w-full px-4 md:w-1/2 xl:w-1/3">
            <div
              class="mb-10 overflow-hidden duration-300 bg-white rounded-lg shadow-1 hover:shadow-3 dark:shadow-card dark:bg-dark-2"
            >
              <img :src="item.image" alt="image" class="w-full" />
              <div class="px-6 py-8 sm:p-8">
                <h3>
                  <a
                    :href="item.titleHref"
                    class="hover:text-primary mb-4 block text-xl font-semibold text-dark dark:text-white sm:text-[22px] md:text-xl lg:text-[22px] xl:text-xl 2xl:text-[22px]"
                  >
                    {{ item.title }}
                  </a>
                </h3>
                <p
                  class="mb-5 text-base font-medium leading-relaxed text-body-color dark:text-dark-6"
                >
                  {{ item.details }}
                </p>
                <div
                  class="flex flex-wrap items-center px-2 py-1 rounded-md bg-tg-bg dark:bg-dark-3"
                >
                  <template v-for="(tag, index) in item.tags" :key="index">
                    <a
                      :href="tag.metaHref"
                      class="flex px-2 py-1 text-base font-medium text-body-color hover:text-primary dark:text-dark-6 dark:hover:text-white"
                    >
                      {{ tag.name }}
                    </a>
                  </template>
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
