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
      <div class="flex flex-wrap items-center -mx-4">
        <div class="w-full px-4 lg:w-6/12 xl:w-5/12">
            <div class="mb-12 lg:mb-0">
               <h2
                  class="text-dark dark:text-white mb-5 text-3xl font-bold sm:text-4xl lg:text-[34px] 2xl:text-[38px]"
                  >
                  Used by the world's most popular companies
               </h2>
               <p
                  class="mb-10 text-base leading-relaxed text-body-color dark:text-dark-6"
                  >
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                  Pellentesque lobortis lectus ut dui dapibus vestibulum. Aenean
                  efficitur fermentum vestibulum.
               </p>
               <div class="flex flex-wrap">
                  <a
                     href="javascript:void(0)"
                     class="block py-3 mb-3 mr-3 text-base font-medium text-white transition border border-transparent rounded-md bg-primary px-7 hover:bg-opacity-90"
                     >
                  Know More
                  </a>
                  <a
                     href="javascript:void(0)"
                     class="block py-3 mb-3 text-base font-medium transition bg-transparent border rounded-md border-primary text-primary hover:bg-primary px-7 hover:text-white"
                     >
                  Contact Us
                  </a>
               </div>
            </div>
        </div>

        <div class="w-full px-4 lg:w-6/12 xl:w-7/12">
          <div class="flex flex-wrap items-center justify-center">
            <template v-for="(item, index) in brandItems" :key="index">
              <a
                :href="item.link"
                class="border-stroke dark:border-primary/10 flex h-[110px] max-w-[188px] items-center justify-center border px-7 hover:bg-primary/10 dark:hover:bg-primary/5"
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
