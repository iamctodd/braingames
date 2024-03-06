<script setup lang="ts">
import { ref } from 'vue'

const currentPage = ref<number>(1)
const totalPages = ref<number>(4)

const pages = ref<number[]>([])

// Populate pages array with total page count
for (let i = 1; i <= totalPages.value; i++) {
  pages.value.push(i)
}

const navigatePage = (direction: number) => {
  currentPage.value += direction
  updatePages()
}

const goToPage = (page: number) => {
  currentPage.value = page
  updatePages()
}

const updatePages = () => {
  if (currentPage.value < 1) {
    currentPage.value = 1
  } else if (currentPage.value > totalPages.value) {
    currentPage.value = totalPages.value
  }
}
</script>

<template>
  <div class="text-center">
    <div class="inline-flex p-3 mb-12 bg-white rounded dark:bg-dark-2 shadow-1 dark:shadow-3">
      <ul class="-mx-[6px] flex items-center">
        <li class="px-[6px]">
          <a
            href="javascript:void(0)"
            @click="navigatePage(-1)"
            class="text-dark dark:text-white dark:hover:bg-white/5 flex h-6 items-center justify-center rounded px-3 text-xs hover:bg-[#EDEFF1]"
          >
            <span class="mr-1">
              <svg
                width="12"
                height="13"
                viewBox="0 0 12 13"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M10.5 6.0875H2.49375L5.68125 2.84375C5.85 2.675 5.85 2.4125 5.68125 2.24375C5.5125 2.075 5.25 2.075 5.08125 2.24375L1.2 6.18125C1.03125 6.35 1.03125 6.6125 1.2 6.78125L5.08125 10.7188C5.15625 10.7937 5.26875 10.85 5.38125 10.85C5.49375 10.85 5.5875 10.8125 5.68125 10.7375C5.85 10.5687 5.85 10.3063 5.68125 10.1375L2.5125 6.93125H10.5C10.725 6.93125 10.9125 6.74375 10.9125 6.51875C10.9125 6.275 10.725 6.0875 10.5 6.0875Z"
                  fill="currentColor"
                />
              </svg>
            </span>
            Previous
          </a>
        </li>
        <li v-for="page in pages" :key="page" class="px-[6px]">
          <a
            href="javascript:void(0)"
            @click="goToPage(page)"
            class="min-w-[24px] flex h-6 px-1 items-center justify-center rounded text-base text-body-color dark:hover:bg-white/5 hover:bg-[#EDEFF1] dark:hover:text-white"
            >{{ page }}</a
          >
        </li>
        <li class="px-[6px]">
          <a
            href="javascript:void(0)"
            @click="navigatePage(1)"
            class="text-dark dark:text-white dark:hover:bg-white/5 flex h-6 items-center justify-center rounded px-3 text-xs hover:bg-[#EDEFF1]"
          >
            Next
            <span class="ml-1">
              <svg
                width="12"
                height="13"
                viewBox="0 0 12 13"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M10.8 6.2L6.91875 2.2625C6.75 2.09375 6.4875 2.09375 6.31875 2.2625C6.15 2.43125 6.15 2.69375 6.31875 2.8625L9.46875 6.06875H1.5C1.275 6.06875 1.0875 6.25625 1.0875 6.48125C1.0875 6.70625 1.275 6.9125 1.5 6.9125H9.50625L6.31875 10.1563C6.15 10.325 6.15 10.5875 6.31875 10.7563C6.39375 10.8313 6.50625 10.8688 6.61875 10.8688C6.73125 10.8688 6.84375 10.8313 6.91875 10.7375L10.8 6.8C10.9688 6.63125 10.9688 6.36875 10.8 6.2Z"
                  fill="currentColor"
                />
              </svg>
            </span>
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>
