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

const avatars = ref([
  {
    img: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-05.jpg',
    name: 'Devid Milinear',
  },
  {
    img: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-05.jpg',
    name: 'Devid Milinear',
    arrow: true
  },
  {
    img: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-05.jpg',
    arrow: true
  }
])
</script>

<template>
  <section class="bg-white dark:bg-dark py-[75px]">
    <div class="mx-auto px-4 sm:container">
      <div class="-mx-4 flex flex-wrap justify-center">
        <template v-for="(avatar, index) in avatars" :key="index">
          <div class="mb-8 w-full px-4 md:w-1/2 lg:w-1/3">
            <div class="relative inline-block">
              <button @click.stop="toggleDropdown(index)" class="flex items-center text-left">
                <div class="relative mr-4 h-[42px] w-[42px] rounded-full">
                  <img
                    :src="avatar.img"
                    alt="avatar"
                    class="h-full w-full rounded-full object-cover object-center"
                  />
                  <span
                    class="absolute -top-0.5 -right-0.5 block h-[14px] w-[14px] rounded-full border-[2.3px] border-white dark:border-dark bg-[#219653]"
                  ></span>
                </div>
                <span v-if="avatar.name" class="text-base font-medium text-dark dark:text-white">
                  {{ avatar.name }}
                </span>
                <span v-if="avatar.arrow" class="pl-[10px] text-dark dark:text-white">
                  <svg
                    width="20"
                    height="20"
                    viewBox="0 0 20 20"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                    class="fill-current"
                  >
                    <path
                      d="M10 14.25C9.8125 14.25 9.65625 14.1875 9.5 14.0625L2.3125 7C2.03125 6.71875 2.03125 6.28125 2.3125 6C2.59375 5.71875 3.03125 5.71875 3.3125 6L10 12.5312L16.6875 5.9375C16.9688 5.65625 17.4062 5.65625 17.6875 5.9375C17.9688 6.21875 17.9688 6.65625 17.6875 6.9375L10.5 14C10.3437 14.1562 10.1875 14.25 10 14.25Z"
                    />
                  </svg>
                </span>
              </button>
              <div
                v-if="dropdownOpen[index]"
                @click.stop="closeDropdown(index)"
                class="shadow-card dark:shadow-box-dark absolute right-0 top-full z-40 w-[200px] space-y-1 rounded bg-white dark:bg-dark-2 p-2"
              >
                <a
                  href="javascript:void(0)"
                  class="text-body-color dark:text-dark-6 hover:bg-gray-2 dark:hover:bg-dark-3 block w-full rounded py-2 px-3 text-left text-sm"
                  >Profile</a
                >
                <a
                  href="javascript:void(0)"
                  class="text-body-color dark:text-dark-6 hover:bg-gray-2 dark:hover:bg-dark-3 block w-full rounded py-2 px-3 text-left text-sm"
                  >Settings</a
                >
                <a
                  href="javascript:void(0)"
                  class="text-body-color dark:text-dark-6 hover:bg-gray-2 dark:hover:bg-dark-3 block w-full rounded py-2 px-3 text-left text-sm"
                  >Sign Out</a
                >
              </div>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>
</template>
