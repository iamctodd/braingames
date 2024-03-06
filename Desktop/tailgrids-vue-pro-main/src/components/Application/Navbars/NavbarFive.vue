<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'

const open = ref(false)
const dropdownButtonRef = ref<HTMLButtonElement | null>(null)
const alert = ref(false)

const toggleNavbar = () => {
  open.value = !open.value
}

const closeAlert = () => {
  alert.value = !alert.value
}

const navLinkItems = ref([
  { text: 'Home', href: 'javascript:void(0)' },
  { text: 'About Us', href: 'javascript:void(0)' },
  { text: 'Services', href: 'javascript:void(0)' },
  { text: 'Blog', href: 'javascript:void(0)' },
  { text: 'Contact', href: 'javascript:void(0)' }
])

// Custom composition function to handle click outside
const handleClickOutside = (event: MouseEvent) => {
  if (dropdownButtonRef.value && !dropdownButtonRef.value.contains(event.target as Node)) {
    open.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<template>
  <div :class="{ hidden: alert }" class="w-full py-3 bg-gradient-to-r from-primary to-secondary">
    <div class="container mx-auto">
      <div class="relative w-full">
        <p class="text-sm font-medium text-center text-white">
          50% Flat Discount on TailGrids UI - Grab it Now!
        </p>
        <button @click="closeAlert" class="absolute right-0 -translate-y-1/2 top-1/2">
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g opacity="0.8">
              <path
                d="M17 7L7 17"
                stroke="white"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path fill-rule="evenodd" clip-rule="evenodd" d="M7 7L17 17L7 7Z" fill="white" />
              <path
                d="M7 7L17 17"
                stroke="white"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </g>
          </svg>
        </button>
      </div>
    </div>
  </div>

  <header class="flex items-center w-full bg-white dark:bg-dark">
    <div class="container">
      <div class="relative flex items-center justify-between -mx-4">
        <div class="max-w-full px-4 w-60">
          <a href="/#" class="block w-full py-5 lg:py-3">
            <img
              src="https://cdn.tailgrids.com/2.0/image/assets/images/logo/logo-primary.svg"
              alt="logo"
              class="dark:hidden"
            />
            <img
              src="https://cdn.tailgrids.com/2.0/image/assets/images/logo/logo-white.svg"
              alt="logo"
              class="hidden dark:block"
            />
          </a>
        </div>

        <div class="flex w-full items-center justify-between px-4">
          <div>
            <button
              @click="toggleNavbar"
              ref="dropdownButtonRef"
              id="navbarToggler"
              class="absolute right-4 top-1/2 block -translate-y-1/2 rounded-lg px-3 py-[6px] ring-primary focus:ring-2 lg:hidden"
            >
              <span
                class="relative my-[6px] block h-[2px] w-[30px] bg-body-color dark:bg-white"
              ></span>
              <span
                class="relative my-[6px] block h-[2px] w-[30px] bg-body-color dark:bg-white"
              ></span>
              <span
                class="relative my-[6px] block h-[2px] w-[30px] bg-body-color dark:bg-white"
              ></span>
            </button>
            <nav
              :class="{ hidden: !open }"
              id="navbarCollapse"
              class="absolute right-4 top-full w-full max-w-[250px] justify-center rounded-lg bg-white py-5 px-6 shadow lg:static lg:flex lg:w-full lg:max-w-full lg:bg-transparent lg:py-0 lg:shadow-none dark:bg-dark-2 lg:dark:bg-transparent"
            >
              <ul class="block lg:flex">
                <template v-for="(item, index) in navLinkItems" :key="index">
                  <li>
                    <a
                      v-if="item.href"
                      :href="item.href"
                      class="flex py-2 text-base font-medium text-body-color hover:text-dark dark:text-dark-6 dark:hover:text-white lg:mx-6 lg:inline-flex lg:py-6"
                    >
                      {{ item.text }}
                    </a>
                  </li>
                </template>
              </ul>
            </nav>
          </div>

          <div class="justify-end hidden pr-16 sm:flex lg:pr-0">
            <div class="flex justify-end">
              <a
                href="javascript:void(0)"
                class="inline-block py-3 text-base font-medium transition border rounded-md px-7 whitespace-nowrap border-secondary text-secondary hover:bg-secondary hover:text-white"
              >
                Sign In
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>
