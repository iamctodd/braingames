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
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/assets/images/brands/plainadmin.svg',
    link: '#'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/assets/images/brands/ecom.svg',
    link: '#'
  }
])
</script>

<template>
  <!-- ====== Brands Section Start -->
  <section class="bg-white py-20 dark:bg-dark lg:py-[120px]">
    <div class="container mx-auto">
      <div class="flex flex-wrap -mx-4">
        <div class="w-full px-4">
          <div class="mx-auto flex max-w-[570px] flex-wrap items-center justify-center">
            <template v-for="(item, index) in brandItems" :key="index">
              <a
                :href="item.link"
                class="border-stroke flex h-[110px] max-w-[188px] items-center justify-center border px-7 hover:bg-primary/10 dark:border-primary/20"
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
