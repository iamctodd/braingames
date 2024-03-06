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

  const isDropdownButton = (target as HTMLElement).closest('.dropdown-button')
  const isDropdownContent = (target as HTMLElement).closest('.dropdown-content')

  if (!isDropdownButton && !isDropdownContent) {
    Object.keys(dropdownOpen.value).forEach((index) => {
      closeDropdown(parseInt(index))
    })
  }
}

onMounted(() => {
  document.addEventListener('click', clickHandler)
})

onUnmounted(() => {
  document.removeEventListener('click', clickHandler)
})

const userItems = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/users-list/image-01.png',
    name: 'Devid Wilium',
    position: 'Digital marketer'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/users-list/image-02.png',
    name: 'Deniyal Shifer',
    position: 'Graphics designe'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/users-list/image-03.png',
    name: 'Philifs Geno',
    position: 'Content creator'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/users-list/image-04.png',
    name: 'Marko Diyan',
    position: 'Web developer'
  }
])
</script>

<template>
  <!-- ====== Users List Start -->
  <section class="relative z-10 overflow-hidden bg-white dark:bg-dark py-20 lg:py-[100px]">
    <div class="container mx-auto">
      <div>
        <h3 class="mb-8 text-2xl font-medium text-dark dark:text-white sm:text-[28px]">
          Users List
        </h3>
        <div
          class="border-stroke dark:border-dark-3 max-w-[370px] border bg-white dark:bg-dark-2 py-[10px]"
        >
          <template v-for="(item, index) in userItems" :key="index">
            <div
              class="flex items-center justify-between p-[18px] hover:bg-gray-1 dark:hover:bg-dark-3"
            >
              <div class="flex items-center">
                <div class="mr-4 h-[50px] w-full max-w-[50px] overflow-hidden rounded-full">
                  <img
                    :src="item.image"
                    alt="user"
                    class="rounded-full object-cover object-center"
                  />
                </div>
                <div>
                  <h4 class="text-base font-medium text-dark dark:text-white">{{ item.name }}</h4>
                  <p class="text-body-color text-sm dark:text-dark-6">{{ item.position }}</p>
                </div>
              </div>
              <div>
                <div x-data="{openDropDown: false}" class="relative">
                  <button
                    @click.stop="toggleDropdown(index)"
                    class="text-body-color dark:text-dark-6"
                  >
                    <svg
                      width="20"
                      height="20"
                      viewBox="0 0 20 20"
                      fill="none"
                      xmlns="http://www.w3.org/2000/svg"
                      class="fill-current"
                    >
                      <path
                        d="M11.6667 15.8333C11.6667 14.9129 10.9205 14.1667 9.99999 14.1667C9.07952 14.1667 8.33333 14.9129 8.33333 15.8333C8.33333 16.7538 9.07952 17.5 9.99999 17.5C10.9205 17.5 11.6667 16.7538 11.6667 15.8333Z"
                      />
                      <path
                        d="M11.6667 9.99996C11.6667 9.07949 10.9205 8.33329 9.99999 8.33329C9.07952 8.33329 8.33333 9.07949 8.33333 9.99996C8.33333 10.9204 9.07952 11.6666 9.99999 11.6666C10.9205 11.6666 11.6667 10.9204 11.6667 9.99996Z"
                      />
                      <path
                        d="M11.6667 4.16671C11.6667 3.24623 10.9205 2.50004 9.99999 2.50004C9.07952 2.50004 8.33333 3.24623 8.33333 4.16671C8.33333 5.08718 9.07952 5.83337 9.99999 5.83337C10.9205 5.83337 11.6667 5.08718 11.6667 4.16671Z"
                      />
                    </svg>
                  </button>
                  <div
                    v-if="dropdownOpen[index]"
                    @click.stop="closeDropdown(index)"
                    class="shadow-card absolute right-0 top-full z-40 w-[150px] space-y-1 rounded bg-white dark:bg-dark p-2"
                  >
                    <button
                      class="text-body-color dark:text-dark-6 hover:bg-gray-2 dark:hover:bg-dark-2 w-full rounded py-1.5 px-3 text-left text-sm"
                    >
                      Edit
                    </button>
                    <button
                      class="text-body-color dark:text-dark-6 hover:bg-gray-2 dark:hover:bg-dark-2 w-full rounded py-1.5 px-3 text-left text-sm"
                    >
                      Delete
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Users List End -->
</template>
