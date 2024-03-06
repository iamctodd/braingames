<script setup lang="ts">
import { ref } from 'vue'

const brandItems = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/assets/images/brands/graygrids.svg',
    link: '#'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/assets/images/brands/lineicons.svg',
    link: '#'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/assets/images/brands/uideck.svg',
    link: '#'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/assets/images/brands/ayroui.svg',
    link: '#'
  }
])
</script>

<template>
  <!-- ====== Brands Section Start -->
  <section class="bg-white py-20 dark:bg-dark lg:py-[120px]">
    <div class="container mx-auto">
      <div class="flex flex-wrap -mx-4">
        <div class="w-full h-10 px-4">
          <div class="flex flex-wrap items-center justify-center">
            <template v-for="(item, index) in brandItems" :key="index">
              <a
                :href="item.link"
                class="flex h-20 w-[150px] items-center justify-center rounded px-4 hover:shadow-[0px_7px_25px_0px_#E3E6F0] dark:hover:shadow-[0px_7px_25px_0px_rgba(0,0,0,.5)] lg:w-[200px] 2xl:w-[180px]"
              >
                <img :src="item.image" alt="image" class="h-10 max-w-full" />
              </a>
            </template>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Brands Section End -->
</template>
