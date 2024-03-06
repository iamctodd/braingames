<script setup lang="ts">
import { ref } from 'vue'

const statsItems = ref([
  {
    user: '220',
    title: 'Projects'
  },
  {
    user: '150K',
    title: 'Earned'
  },
  {
    user: '24/7',
    title: 'Delivery'
  },
  {
    user: '99%',
    title: 'Success'
  }
])
</script>

<template>
  <!-- ====== Stats Section Start -->
  <section class="bg-white dark:bg-dark pb-20 lg:pb-[120px]">
    <div class="bg-primary pt-20 pb-[140px] lg:pt-[120px]">
      <div class="mx-auto px-4 sm:container">
        <div class="mx-auto max-w-[570px] text-center">
          <span class="mb-2 block text-lg font-semibold text-white"> Some Fun Facts </span>
          <h2 class="mb-3 text-3xl leading-[1.2] font-bold text-white md:text-[40px]">
            Our achievements
          </h2>
          <p class="text-base text-gray-7">
            There are many variations of passages of Lorem Ipsum available but the majority have
            suffered alteration in some form.
          </p>
        </div>
      </div>
    </div>

    <div class="-mt-[100px]">
      <div class="px-4 mx-auto sm:container">
        <div
          class="shadow-2 dark:shadow-box-dark mx-auto flex max-w-[970px] flex-wrap items-center justify-center rounded-xl bg-white dark:bg-dark-2 py-[65px] px-10"
        >
          <template v-for="(item, index) in statsItems" :key="index">
            <div class="w-1/2 md:w-1/4">
              <div class="mb-10 text-center md:mb-0">
                <p class="text-body-color dark:text-dark-6 mb-1">{{ item.title }}</p>
                <span
                  class="block text-4xl leading-[1.2] font-bold text-dark dark:text-white sm:text-[40px]"
                >
                  {{ item.user }}
                </span>
              </div>
            </div>
          </template>
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Stats Section End -->
</template>
