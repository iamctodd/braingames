<script setup lang="ts">
import { ref } from 'vue'

interface SingleStepProps {
  number: string
  name: string
  done?: boolean
  inProgress?: boolean
}

const steps = ref<SingleStepProps[]>([
  { number: 'Step 1', name: 'Credit line Assignment', done: true },
  { number: 'Step 2', name: 'Bank Acceptance', inProgress: true },
  { number: 'Step 3', name: 'Bank Acceptance' }
])
</script>

<template>
  <section class="overflow-hidden py-20 dark:bg-dark lg:py-[120px]">
    <div class="mx-auto px-4 sm:container">
      <div class="flex flex-wrap gap-[30px]">
        <template v-for="(step, index) in steps" :key="index">
          <div class="w-full max-w-[210px]">
            <div
              class="rounded-lg border p-[18px]"
              :class="{
                'border-primary bg-primary': step.done,
                'border-primary bg-gray dark:bg-primary/5': step.inProgress,
                'border-[#e7e7e7] dark:border-dark-3 ':
                  !step.done || !step.inProgress
              }"
            >
              <div
                :class="{
                  'bg-white text-primary': step.done,
                  'bg-primary text-white dark:border-primary': step.inProgress,
                  'text-body-color dark:text-dark-6': !(step.done || step.inProgress)
                }"
                class="mb-[10px] flex h-[30px] w-[30px] items-center justify-center rounded-full border"
              >
                <svg
                  width="18"
                  height="18"
                  viewBox="0 0 18 18"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                  class="fill-current"
                >
                  <path
                    d="M17.0437 3.76876C16.7906 3.51564 16.3969 3.51564 16.1437 3.76876L6.58125 13.05L1.85625 8.40939C1.60312 8.15626 1.20937 8.18439 0.956246 8.40939C0.703121 8.66251 0.731246 9.05626 0.956246 9.30939L5.93437 14.1469C6.10312 14.3156 6.32812 14.4 6.58125 14.4C6.83437 14.4 7.03125 14.3156 7.22812 14.1469L17.0437 4.61251C17.2969 4.41564 17.2969 4.02189 17.0437 3.76876Z"
                  />
                </svg>
              </div>

              <span
                :class="{
                  'text-white': step.done,
                  'text-dark dark:text-white': step.inProgress,
                  'text-body-color dark:text-dark-6': !(step.done || step.inProgress)
                }"
                class="mb-1 block text-xs uppercase"
              >
                {{ step.number }}
              </span>

              <h3
                :class="{
                  'text-white': step.done,
                  'text-dark dark:text-white': step.inProgress,
                  'text-body-color dark:text-dark-6': !(step.done || step.inProgress)
                }"
                class="mb-[10px] text-sm font-semibold"
              >
                {{ step.name }}
              </h3>

              <span
                :class="{
                  'bg-white text-primary': step.done,
                  'bg-primary text-white': step.inProgress,
                  'bg-body-color text-white dark:bg-dark-3': !(step.done || step.inProgress)
                }"
                class="inline-block rounded px-2 py-1 text-xs font-medium"
              >
                <span v-if="step.done">Completed</span>
                <span v-if="step.inProgress">InProgress</span>
                <span v-if="!(step.done || step.inProgress)">Pending</span>
              </span>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>
</template>
