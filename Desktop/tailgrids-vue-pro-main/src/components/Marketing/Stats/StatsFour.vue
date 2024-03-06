<script setup lang="ts">
import { ref } from 'vue'

const statsItems = ref([
  {
    user: '56,825',
    title: 'Clients'
  },
  {
    user: '35,574',
    title: 'Commits'
  },
  {
    user: '570+',
    title: 'Team Member'
  },
  {
    user: '50%',
    title: 'First Year of use'
  }
])
</script>

<template>
  <!-- ====== Stats Section Start -->
  <section class="bg-gray-2 dark:bg-dark py-20 lg:py-[120px]">
    <div class="px-4 mx-auto sm:container">
      <div class="-mx-4 flex flex-wrap items-center">
        <div class="w-full px-4 lg:w-7/12">
          <div class="mb-12 max-w-[560px] lg:mb-8">
            <span
              class="mb-4 inline-block rounded bg-primary py-1 px-3 text-base font-medium text-white"
            >
              Some Fun Facts
            </span>
            <h2
              class="mb-3 text-3xl leading-[1.2] font-bold text-dark dark:text-white md:text-[40px]"
            >
              Our achievements
            </h2>
            <p class="text-base text-body-color dark:text-dark-6">
              There are many variations of passages of Lorem Ipsum available but the majority have
              suffered alteration in some form.
            </p>
          </div>
        </div>

        <div class="w-full px-4 lg:w-5/12">
          <div class="-mx-3 flex flex-wrap md:-mx-4">
            <template v-for="(item, index) in statsItems" :key="index">
              <div class="w-full px-3 xs:w-1/2 md:px-4">
                <div
                  class="group mb-6 rounded-[5px] bg-white dark:bg-dark-2 py-6 px-4 text-center shadow-three hover:bg-primary md:mb-8"
                >
                  <h4
                    class="mb-1 text-2xl leading-tight font-bold text-dark dark:text-white group-hover:text-white sm:text-[28px]"
                  >
                    {{ item.user }}
                  </h4>
                  <p class="text-base text-body-color dark:text-dark-6 group-hover:text-white">
                    {{ item.title }}
                  </p>
                </div>
              </div>
            </template>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Stats Section End -->
</template>
