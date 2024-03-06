<script setup lang="ts">
import { ref } from 'vue'

interface SingleStepProps {
  number: string
  name: string
  done?: boolean
  ongoing?: boolean
}

const steps = ref<SingleStepProps[]>([
  { number: '1', name: 'Step 1', done: true },
  { number: '2', name: 'Step 2', ongoing: true },
  { number: '3', name: 'Step 3' },
  { number: '4', name: 'Step 4' },
  { number: '5', name: 'Step 5' }
])
</script>

<template>
  <section class="overflow-hidden py-20 dark:bg-dark lg:py-[120px]">
    <div class="mx-auto px-4 sm:container">
      <div class="-mx-3 flex items-center justify-center sm:-mx-7 md:-mx-10 lg:-mx-[50px]">
        <template v-for="(step, index) in steps" :key="index">
          <div class="group relative px-3 text-center sm:px-7 md:px-10 lg:px-[50px]">
            <span
              :class="{
                'bg-primary dark:bg-primary': step.done
              }"
              class="absolute -right-[45px] top-[17px] block h-[2px] w-[80px] bg-gray group-last:hidden dark:bg-dark-2 sm:-right-[60px] sm:top-[25px] sm:w-[120px]"
            ></span>
            <span
              :class="{
                'border-primary bg-primary text-white dark:border-primary dark:bg-primary':
                  step.done,
                'border-primary text-primary dark:border-primary dark:text-primary': step.ongoing
              }"
              class="border-stroke dark:border-dark-3 bg-gray-1 dark:bg-dark-4 relative z-10 mx-auto mb-[10px] flex h-9 w-9 items-center justify-center rounded-full border-2 text-base font-medium text-dark dark:text-white sm:h-[50px] sm:w-[50px] sm:text-xl"
            >
              {{ step.number }}
            </span>
            <span class="text-[10px] font-medium text-dark dark:text-white sm:text-base md:text-xl">
              {{ step.name }}
            </span>
          </div>
        </template>
      </div>
    </div>
  </section>
</template>
