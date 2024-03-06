<script setup lang="ts">
// Import necessary functions from Vue
import { ref } from 'vue'

// Define the data for the Checkbox List
const checkboxItems = ref([
  {
    id: 1,
    checked: false,
    initials: 'MC',
    name: 'Musharof Chowdhury',
    role: 'Founder & CEO',
    color: '#FFB52B'
  },
  {
    id: 2,
    checked: false,
    initials: 'NR',
    name: 'Naimur Rahman',
    role: 'Product Designer',
    color: '#00BFD9'
  },
  {
    id: 3,
    checked: false,
    initials: 'SH',
    name: 'Shafiq Hammad',
    role: 'Frontend Developer',
    color: '#4926BD'
  },
  {
    id: 4,
    checked: false,
    initials: 'MH',
    name: 'Mahbub Hasan',
    role: 'Backend Developer',
    color: '#094285'
  }
])
</script>

<template>
  <!-- ====== Checkbox List Start -->
  <section class="relative z-10 overflow-hidden bg-white dark:bg-dark py-20 lg:py-[100px]">
    <div class="mx-auto px-4 lg:container">
      <div
        class="mx-auto mb-8 w-full max-w-[770px] overflow-hidden rounded-[10px] border border-stroke dark:border-dark-3 bg-white dark:bg-dark-2"
      >
        <div class="w-full border-b border-stroke dark:border-dark-3 py-6 px-6">
          <h3 class="leading-[40px] text-[28px] font-semibold text-dark dark:text-white">
            Checkbox List
          </h3>
        </div>
        <div>
          <!-- Dynamic Checkbox List -->
          <div
            v-for="item in checkboxItems"
            :key="item.id"
            class="flex items-center border-b border-stroke dark:border-dark-3 py-5 px-6 hover:bg-gray-1 dark:hover:bg-dark"
          >
            <div class="mr-[22px]">
              <input
                type="checkbox"
                :id="'checkbox-' + item.id"
                class="checkbox-list sr-only"
                v-model="item.checked"
              />
              <label
                :for="'checkbox-' + item.id"
                class="flex h-5 w-5 cursor-pointer items-center justify-center rounded border border-stroke dark:border-dark-3"
              >
                <span class="icon" :class="{ 'opacity-0': !item.checked }">
                  <svg
                    width="11"
                    height="8"
                    viewBox="0 0 11 8"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M10.0915 0.951972L10.0867 0.946075L10.0813 0.940568C9.90076 0.753564 9.61034 0.753146 9.42927 0.939309L4.16201 6.22962L1.58507 3.63469C1.40401 3.44841 1.11351 3.44879 0.932892 3.63584C0.755703 3.81933 0.755703 4.10875 0.932892 4.29224L0.932878 4.29225L0.934851 4.29424L3.58046 6.95832C3.73676 7.11955 3.94983 7.2 4.1473 7.2C4.36196 7.2 4.55963 7.11773 4.71406 6.9584L10.0468 1.60234C10.2436 1.4199 10.2421 1.1339 10.0915 0.951972ZM4.2327 6.30081L4.2317 6.2998C4.23206 6.30015 4.23237 6.30049 4.23269 6.30082L4.2327 6.30081Z"
                      fill="white"
                      stroke="white"
                      stroke-width="0.4"
                    />
                  </svg>
                </span>
              </label>
            </div>
            <div class="flex w-full items-center">
              <div
                class="mr-[14px] flex h-11 w-full max-w-[44px] items-center justify-center rounded-full text-base font-medium uppercase text-white"
                :style="{ backgroundColor: item.color }"
              >
                {{ item.initials }}
              </div>
              <div class="w-full sm:flex">
                <h4 class="text-base font-medium text-dark dark:text-white sm:min-w-[220px]">
                  {{ item.name }}
                </h4>
                <p class="text-base text-body-color dark:text-dark-6">{{ item.role }}</p>
              </div>
            </div>
          </div>
          <!-- End Dynamic Checkbox List -->
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Checkbox List End -->
</template>
