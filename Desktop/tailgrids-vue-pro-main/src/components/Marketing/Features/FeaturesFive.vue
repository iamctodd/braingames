<script setup lang="ts">
import { ref } from 'vue'

const featuresItems = ref([
  {
    id: '1',
    title: `RESEARCH`,
    details: 'Lorem ipsum dolor amet adipiscing eiusmod.'
  },
  {
    id: '2',
    title: `SKETCHES`,
    details: 'Lorem ipsum dolor amet adipiscing eiusmod.'
  },
  {
    id: '3',
    title: `CONCEPT`,
    details: 'Lorem ipsum dolor amet adipiscing eiusmod.'
  },
  {
    id: '4',
    title: `PRESENTATION`,
    details: 'Lorem ipsum dolor amet adipiscing eiusmod.'
  }
])
</script>

<template>
  <!-- ====== Services Section Start -->
  <section class="bg-gray-2 dark:bg-dark pt-20 pb-12 lg:pt-[120px] lg:pb-[90px]">
    <div class="container mx-auto">
      <div class="-mx-4 flex flex-wrap">
        <div class="w-full px-4">
          <div class="mx-auto mb-[60px] max-w-[510px] text-center lg:mb-[70px]">
            <span class="text-primary mb-2 block text-lg font-semibold"> Project Planing </span>
            <h2
              class="text-dark dark:text-white mb-3 text-3xl leading-[1.2] font-bold sm:text-4xl md:text-[40px]"
            >
              What we do for you?
            </h2>
            <p class="text-body-color text-base dark:text-dark-6">
              There are many variations of passages of Lorem Ipsum available but the majority have
              suffered alteration in some form.
            </p>
          </div>
        </div>
      </div>

      <div class="-mx-4 flex flex-wrap justify-center">
        <template v-for="(item, index) in featuresItems" :key="index">
          <div class="w-full px-4 md:w-1/2 xl:w-1/4">
            <div
              class="group relative mb-10 overflow-hidden rounded-[10px] border border-stroke dark:border-dark-3 bg-white dark:bg-dark-2 py-11 px-6 text-center duration-200 hover:-translate-y-2 hover:shadow-feature hover:border-transparent"
            >
              <div
                class="text-dark dark:text-white group-hover:border-primary group-hover:bg-primary mx-auto mb-9 flex h-20 w-20 items-center justify-center rounded-full border border-stroke dark:border-dark-3 text-3xl font-semibold drop-shadow-feature group-hover:text-white"
              >
                {{ item.id }}
              </div>
              <h4 class="text-primary mb-[14px] text-lg font-semibold uppercase">
                {{ item.title }}
              </h4>
              <p class="text-body-color dark:text-dark-6 text-base">
                {{ item.details }}
              </p>
              <span
                class="bg-primary absolute bottom-0 left-0 block h-2 w-0 duration-200 group-hover:w-full"
              ></span>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>
  <!-- ====== Services Section End -->
</template>
