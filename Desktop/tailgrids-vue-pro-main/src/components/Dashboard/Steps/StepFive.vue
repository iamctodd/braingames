<script setup lang="ts">
import { ref } from 'vue'

interface SingleStepProps {
  number: string
  name: string
  done?: boolean
  inProgress?: boolean
}

const steps = ref<SingleStepProps[]>([
  { number: 'Step 1', name: 'Create Account', done: true },
  { number: 'Step 2', name: 'Login', inProgress: true },
  { number: 'Step 3', name: 'Payment' },
  { number: 'Step 4', name: 'Confirm' }
])
</script>

<template>
  <section class="overflow-hidden py-20 lg:py-[120px] dark:bg-dark">
    <div class="mx-auto px-4 sm:container">
      <div class="mx-auto w-max">
        <template v-for="(step, index) in steps" :key="index">
          <div class="group relative z-10 flex items-center justify-end pb-[62px]">
            <span
              :class="{
                'bg-primary dark:bg-primary': step.done,
                'bg-gradient-to-b from-primary via-[#3056d37f] to-[#3056d300]': step.inProgress
              }"
              class="absolute right-[18px] top-4 -z-10 h-full w-1 bg-gray group-last:hidden dark:bg-dark-2"
            ></span>
            <div class="mr-8 text-right">
              <span class="text-sm text-body-color dark:text-dark-6 sm:text-base">
                {{ step.number }}
              </span>
              <h3 class="text-base font-medium text-dark dark:text-white sm:text-lg">
                {{ step.name }}
              </h3>
            </div>

            <div>
              <div
                :class="{
                  'bg-primary dark:bg-primary': step.done || step.inProgress,
                  'bg-gray dark:bg-dark-2': !(step.done || step.inProgress)
                }"
                class="flex h-10 w-10 items-center justify-center rounded-full"
              >
                <span
                  :class="{
                    'bg-primary dark:bg-primary': step.done || step.inProgress,
                    'bg-white dark:bg-dark-5': !(step.done || step.inProgress)
                  }"
                  class="flex h-6 w-6 items-center justify-center rounded-full"
                >
                  <svg
                    v-if="step.done || step.inProgress"
                    width="16"
                    height="12"
                    viewBox="0 0 16 12"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      fill-rule="evenodd"
                      clip-rule="evenodd"
                      d="M15.671 0.491162L15.6941 0.521153C16.1124 1.06264 16.1273 1.9008 15.5768 2.45815L7.29232 11.3732C6.92972 11.7721 6.43864 12 5.89584 12C5.38903 12 4.87105 11.7821 4.49894 11.3727L0.376545 6.92507C-0.125563 6.36795 -0.125491 5.51224 0.376618 4.95512C0.931025 4.33998 1.8678 4.33778 2.42493 4.94855L5.91939 8.71874L13.5978 0.455859C14.155 -0.154327 15.0914 -0.151944 15.6456 0.46301L15.671 0.491162Z"
                      fill="white"
                    />
                  </svg>
                </span>
              </div>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>
</template>
