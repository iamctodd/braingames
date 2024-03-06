<script setup lang="ts">
import { ref } from 'vue'

interface SingleStepProps {
  number: string
  name: string
  details: string
  done?: boolean
}

const steps = ref<SingleStepProps[]>([
  {
    done: true,
    number: 'Step 1',
    name: 'Create Account',
    details: 'Lorem ipsum dolor sit standta amet consectetur adipiscing elit.'
  },
  {
    number: 'Step 2',
    name: 'Setup Account',
    details: 'Lorem ipsum dolor sit standta amet consectetur adipiscing elit.'
  },
  {
    number: 'Step 3',
    name: 'Start Using',
    details: 'Lorem ipsum dolor sit standta amet consectetur adipiscing elit.'
  }
])
</script>

<template>
  <section class="overflow-hidden py-20 lg:py-[120px] dark:bg-dark">
    <div class="mx-auto px-4 sm:container">
      <div class="-mx-[30px] flex flex-wrap">
        <template v-for="(step, index) in steps" :key="index">
          <div class="w-full px-[30px] md:w-1/2 lg:w-1/3">
            <div class="mb-8 border-b-[3px]" :class="{'border-primary': step.done, 'border-[#E7E7E7] dark:border-dark-3': !step.done}">
              <span
                class="border-stroke dark:border-dark-3 mb-[18px] inline-block border py-1 px-4 text-sm font-medium text-dark dark:text-white"
              >
                {{ step.number }}
              </span>
              <h3 class="mb-[10px] text-xl font-medium text-primary">
                {{ step.name }}
              </h3>
              <p class="text-body-color dark:text-dark-6 mb-[22px] text-base">
                {{ step.details }}
              </p>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>
</template>
