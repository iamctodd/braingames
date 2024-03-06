<script setup lang="ts">
import { ref } from 'vue'

interface SingleStepProps {
  number: string
  title: string
  details: string
  done?: boolean
  ongoing?: boolean
}

const steps = ref<SingleStepProps[]>([
  {
    done: true,
    number: '1',
    title: 'Step one title',
    details:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque at sagittis sapien, eget sodales arcu. Aenean arcu velit, tincidunt ut enim vitae, scelerisque tempus lorem.'
  },
  {
    ongoing: true,
    number: '2',
    title: 'Step two title',
    details:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque at sagittis sapien, eget sodales arcu. Aenean arcu velit, tincidunt ut enim vitae, scelerisque tempus lorem.'
  },
  {
    number: '3',
    title: 'Step three title',
    details:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque at sagittis sapien, eget sodales arcu. Aenean arcu velit, tincidunt ut enim vitae, scelerisque tempus lorem.'
  }
])
</script>

<template>
  <section class="overflow-hidden py-20 dark:bg-dark lg:py-[120px]">
    <div class="mx-auto px-4 sm:container">
      <div class="mx-auto w-full max-w-[920px]">
        <template v-for="(step, index) in steps" :key="index">
          <div class="group relative flex pb-16 md:pb-[90px]">
            <span
              :style="{ height: 'calc(100% - 70px)' }"
              class="absolute left-6 top-[60px] w-[2px] border-l-2 border-dashed border-[#e7e7e7] group-last:border-none dark:border-dark-3"
              :class="{
                'border-primary dark:border-primary': step.done
              }"
            >
            </span>

            <div
              :class="{
                'border-primary bg-primary text-white dark:border-primary dark:bg-primary dark:text-white':
                  step.done,
                'border-primary text-primary dark:border-primary dark:text-primary': step.ongoing
              }"
              class="mr-4 flex h-11 w-full max-w-[44px] items-center justify-center rounded-full border border-[#e7e7e7] bg-gray text-base font-semibold text-dark dark:border-dark-3 dark:bg-dark dark:text-white md:mr-9 md:h-[50px] md:max-w-[50px] md:text-xl"
            >
              {{ step.number }}
            </div>
            <div class="w-full">
              <h3 class="mb-[10px] text-lg font-semibold text-dark dark:text-white md:text-2xl">
                {{ step.title }}
              </h3>
              <p class="text-base font-medium text-body-color dark:text-dark-6">
                {{ step.details }}
              </p>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>
</template>
