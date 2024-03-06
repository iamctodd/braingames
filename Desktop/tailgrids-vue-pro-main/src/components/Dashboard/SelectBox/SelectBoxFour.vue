<script setup lang="ts">
import { ref } from 'vue'

const selectListItems = ref([
  { id: 1, selected: false, title: 'List Title Here' },
  { id: 2, selected: false, title: 'List Title Here' },
  { id: 3, selected: false, title: 'List Title Here' },
  { id: 4, selected: false, title: 'List Title Here' },
  { id: 5, selected: false, title: 'List Title Here' }
])
</script>

<template>
  <!-- ====== Select List Section Start -->
  <section class="bg-gray-2 dark:bg-dark py-20 lg:py-[120px]">
    <div class="container mx-auto">
      <div>
        <h3 class="mb-6 text-lg font-semibold text-dark dark:text-white">Select List</h3>
        <div class="max-w-[270px] space-y-[10px]">
          <!-- Dynamic Select List Section -->
          <div v-for="listItem in selectListItems" :key="listItem.id">
            <input
              :type="'checkbox'"
              :name="'select-list'"
              :id="'select-list-' + listItem.id"
              class="select-list sr-only"
              v-model="listItem.selected"
            />
            <label
              :for="'select-list-' + listItem.id"
              class="select-list text-body-color dark:text-dark-6 border-stroke dark:border-dark-3 flex cursor-pointer items-center rounded-md border bg-white dark:bg-dark-2 py-3 px-5"
            >
              <span
                class="icon flex h-5 w-5 items-center justify-center rounded-full bg-secondary-color"
              >
                <svg
                  width="12"
                  height="12"
                  viewBox="0 0 12 12"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill-rule="evenodd"
                    clip-rule="evenodd"
                    d="M10.3536 2.64645C10.5488 2.84171 10.5488 3.15829 10.3536 3.35355L4.85355 8.85355C4.65829 9.04882 4.34171 9.04882 4.14645 8.85355L1.64645 6.35355C1.45118 6.15829 1.45118 5.84171 1.64645 5.64645C1.84171 5.45118 2.15829 5.45118 2.35355 5.64645L4.5 7.79289L9.64645 2.64645C9.84171 2.45118 10.1583 2.45118 10.3536 2.64645Z"
                    fill="white"
                  />
                </svg>
              </span>
              <span class="pl-[14px] text-base font-medium">{{ listItem.title }}</span>
            </label>
          </div>
          <!-- End Dynamic Select List Section -->
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Select List Section End -->
</template>
