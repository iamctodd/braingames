<script setup lang="ts">
import type { Ref } from 'vue'
import { onMounted, onUnmounted, ref } from 'vue'

interface DropdownOpen {
  [key: number]: boolean
}

const dropdownOpen: Ref<DropdownOpen> = ref({})

const toggleDropdown = (index: number) => {
  dropdownOpen.value[index] = !dropdownOpen.value[index]
}

const closeDropdown = (index: number) => {
  dropdownOpen.value[index] = false
}

const clickHandler = ({ target }: { target: EventTarget | null }) => {
  if (!target) return
  const dropdownButtons = document.querySelectorAll('.dropdown')
  dropdownButtons.forEach((button, index) => {
    const dropdown = button.nextElementSibling
    if (!dropdown || (!dropdownOpen.value[index] && !dropdown.contains(target as Node))) return
    toggleDropdown(index)
  })
}

const keyHandler = ({ keyCode }: { keyCode: number }) => {
  if (keyCode !== 27) return
  Object.keys(dropdownOpen.value)
    .map(Number)
    .forEach((index) => {
      if (dropdownOpen.value[index]) {
        closeDropdown(index)
      }
    })
}

onMounted(() => {
  document.addEventListener('click', clickHandler)
  document.addEventListener('keydown', keyHandler)
})

onUnmounted(() => {
  document.removeEventListener('click', clickHandler)
  document.removeEventListener('keydown', keyHandler)
})

const users = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/tables/table-12/image-01.jpg',
    imageAlt: 'product',
    name: 'Apple Watch Series 7',
    category: 'Electronics',
    price: '$269',
    sold: '22',
    profit: '$45'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/tables/table-12/image-02.jpg',
    imageAlt: 'product',
    name: 'Macbook Pro M1',
    category: 'Electronics',
    price: '$546',
    sold: '34',
    profit: '$125'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/tables/table-12/image-03.jpg',
    imageAlt: 'product',
    name: 'Dell Inspiron 15',
    category: 'Electronics',
    price: '$444',
    sold: '64',
    profit: '$247'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/tables/table-12/image-04.jpg',
    imageAlt: 'product',
    name: 'HP Probook 450',
    category: 'Electronics',
    price: '$499',
    sold: '72',
    profit: '$103'
  }
])

const headers = ref([
  {
    name: 'Product Name',
    styles: 'min-w-[300px]'
  },
  {
    name: 'Category',
    styles: 'min-w-[90px]'
  },
  {
    name: 'Price',
    styles: 'min-w-[90px]'
  },
  {
    name: 'Sold',
    styles: 'min-w-[90px]'
  },
  {
    name: 'Profit',
    styles: 'min-w-[90px]'
  }
])
</script>

<template>
  <section class="bg-gray-2 dark:bg-dark py-20 lg:py-[120px]">
    <div class="px-4 mx-auto lg:container">
      <div
        class="mx-auto w-full max-w-[850px] rounded-lg border border-stroke bg-white dark:bg-dark-2 dark:border-dark-3"
      >
        <div class="max-w-full overflow-x-auto">
          <table class="w-full table-auto">
            <thead>
              <tr class="border-b border-stroke dark:border-dark-3">
                <th
                  v-for="(header, index) in headers"
                  :key="index"
                  :class="`py-5 px-4 first:pl-8 last:pr-8 ${header.styles}`"
                >
                  <p class="text-base font-medium text-left text-dark dark:text-white">
                    {{ header.name }}
                  </p>
                </th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(user, index) in users"
                :key="index"
                class="border-b border-stroke dark:border-dark-3 last-of-type:border-none"
              >
                <td class="py-[18px] pl-6 pr-3">
                  <div class="flex items-center">
                    <div class="relative">
                      <input
                        type="checkbox"
                        :id="'checkbox-' + index"
                        name="tableCheckbox"
                        class="sr-only tableCheckbox"
                      />
                      <label
                        :for="'checkbox-' + index"
                        class="flex items-center text-base cursor-pointer text-body-color dark:text-dark-6"
                      >
                        <span
                          class="icon-box mr-5 flex h-5 w-5 items-center justify-center rounded-[3px] border-[.5px] border-stroke bg-transparent text-white dark:border-dark-3"
                        >
                          <svg width="14" height="14" viewBox="0 0 10 10" class="opacity-0 icon">
                            <path
                              fill-rule="evenodd"
                              clip-rule="evenodd"
                              d="M8.62796 2.20602C8.79068 2.36874 8.79068 2.63256 8.62796 2.79528L4.04463 7.37861C3.88191 7.54133 3.61809 7.54133 3.45537 7.37861L1.37204 5.29528C1.20932 5.13256 1.20932 4.86874 1.37204 4.70602C1.53476 4.5433 1.79858 4.5433 1.96129 4.70602L3.75 6.49473L8.03871 2.20602C8.20142 2.0433 8.46524 2.0433 8.62796 2.20602Z"
                              fill="currentColor"
                            />
                          </svg>
                        </span>
                      </label>
                    </div>

                    <div class="flex items-center">
                      <img
                        :src="user.image"
                        :alt="user.imageAlt"
                        class="mr-4 h-[50px] w-[60px] rounded object-cover object-center"
                      />
                      <p class="text-base text-body-color dark:text-dark-6">{{ user.name }}</p>
                    </div>
                  </div>
                </td>
                <td class="py-[18px] px-4">
                  <p class="text-base text-body-color dark:text-dark-6">
                    {{ user.category }}
                  </p>
                </td>
                <td class="py-[18px] px-4">
                  <p class="text-base text-body-color dark:text-dark-6">
                    {{ user.price }}
                  </p>
                </td>
                <td class="py-[18px] px-4">
                  <p class="text-base text-body-color dark:text-dark-6">{{ user.sold }}</p>
                </td>
                <td class="py-[18px] px-4">
                  <p class="text-base text-body-color dark:text-dark-6">
                    {{ user.profit }}
                  </p>
                </td>
                <td class="py-[18px] pl-4 pr-6">
                  <div class="relative">
                    <button
                      @click.stop="toggleDropdown(index)"
                      class="text-body-color dark:text-dark-6 dropdown"
                    >
                      <svg
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          d="M13 12C13 11.4477 12.5523 11 12 11C11.4477 11 11 11.4477 11 12C11 12.5523 11.4477 13 12 13C12.5523 13 13 12.5523 13 12Z"
                          stroke="currentColor"
                          stroke-width="2"
                          stroke-linecap="round"
                          stroke-linejoin="round"
                        />
                        <path
                          d="M6 12C6 11.4477 5.55228 11 5 11C4.44772 11 4 11.4477 4 12C4 12.5523 4.44772 13 5 13C5.55228 13 6 12.5523 6 12Z"
                          stroke="currentColor"
                          stroke-width="2"
                          stroke-linecap="round"
                          stroke-linejoin="round"
                        />
                        <path
                          d="M20 12C20 11.4477 19.5523 11 19 11C18.4477 11 18 11.4477 18 12C18 12.5523 18.4477 13 19 13C19.5523 13 20 12.5523 20 12Z"
                          stroke="currentColor"
                          stroke-width="2"
                          stroke-linecap="round"
                          stroke-linejoin="round"
                        />
                      </svg>
                    </button>

                    <div
                      v-if="dropdownOpen[index]"
                      @click.stop="closeDropdown(index)"
                      class="absolute right-0 top-full z-40 w-[200px] space-y-1 rounded bg-white p-2 shadow-card dark:bg-dark border border-stroke dark:border-dark-3"
                    >
                      <button
                        @click.stop="closeDropdown(index)"
                        class="w-full px-3 py-2 text-sm text-left rounded text-body-color hover:bg-gray-2 dark:text-dark-6 dark:hover:bg-dark-2"
                      >
                        Edit
                      </button>
                      <button
                        @click.stop="closeDropdown(index)"
                        class="w-full px-3 py-2 text-sm text-left rounded text-body-color hover:bg-gray-2 dark:text-dark-6 dark:hover:bg-dark-2"
                      >
                        Delete
                      </button>
                    </div>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>
</template>
