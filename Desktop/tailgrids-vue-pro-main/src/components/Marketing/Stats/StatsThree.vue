<script setup lang="ts">
import { ref } from 'vue'

const statsItems = ref([
  {
    id: '01',
    title: 'Idea Creation',
    details: 'Lorem ipsum dolor sit amet minim consectetur adipisicing elit.'
  },
  {
    id: '02',
    title: 'Creative Design',
    details: 'Lorem ipsum dolor sit amet minim consectetur adipisicing elit.'
  },
  {
    id: '03',
    title: 'Awesome Support',
    details: 'Lorem ipsum dolor sit amet minim consectetur adipisicing elit.'
  }
])
</script>

<template>
  <!-- ====== Stats Section Start -->
  <section class="bg-white dark:bg-dark pt-20 pb-10 lg:pt-[120px] lg:pb-20">
    <div class="px-4 mx-auto sm:container">
      <div class="mx-auto mb-[70px] max-w-[570px] text-center">
        <h2 class="mb-3 text-3xl leading-[1.2] font-bold text-dark dark:text-white md:text-[40px]">
          Why Choose Us
        </h2>
        <p class="text-body-color text-base dark:text-dark-6">
          There are many variations of passages of Lorem Ipsum available but the majority have
          suffered alteration in some form.
        </p>
      </div>

      <div class="-mx-4 flex flex-wrap">
        <template v-for="(item, index) in statsItems" :key="index">
          <div class="w-full px-4 md:w-1/2 xl:w-1/3">
            <div class="mb-10 flex">
              <div class="mr-6">
                <span class="text-primary text-[40px] font-bold leading-[1.1] lg:text-[50px]">
                  {{ item.id }}
                </span>
              </div>
              <div class="w-full">
                <h3 class="mb-4 text-xl font-semibold text-dark dark:text-white sm:text-2xl">
                  {{ item.title }}
                </h3>
                <p class="text-body-color text-base dark:text-dark-6">
                  {{ item.details }}
                </p>
              </div>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>
  <!-- ====== Stats Section End -->
</template>
