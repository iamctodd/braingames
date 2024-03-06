<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'

const open = ref(false)
const dropdownButtonRef = ref<HTMLButtonElement | null>(null)

const toggleNavbar = () => {
  open.value = !open.value
}

const navLinkItems = ref([
  { text: 'Home', href: 'javascript:void(0)' },
  { text: 'Payment', href: 'javascript:void(0)' },
  { text: 'Features', href: 'javascript:void(0)' }
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
  <header class="flex items-center w-full bg-white dark:bg-dark">
    <div class="container">
      <div class="relative flex items-center justify-between -mx-4">
        <div class="order-last px-4 lg:order-first lg:w-6/12 xl:w-5/12 2xl:w-4/12">
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
            class="dark:bg-dark-2 absolute right-4 top-full w-full max-w-[250px] rounded-lg bg-white py-5 px-6 shadow lg:static lg:block lg:w-full lg:max-w-full lg:shadow-none lg:dark:bg-transparent"
          >
            <ul class="block lg:flex">
              <template v-for="(item, index) in navLinkItems" :key="index">
                <li>
                  <a
                    v-if="item.href"
                    :href="item.href"
                    class="flex py-2 text-base font-medium text-body-color dark:text-dark-6 hover:text-dark lg:ml-12 lg:inline-flex dark:hover:text-white"
                  >
                    {{ item.text }}
                  </a>
                </li>
              </template>
            </ul>
          </nav>
        </div>

        <div class="px-4 lg:w-3/12 xl:w-3/12 2xl:w-4/12">
          <a href="javascript:void(0)" class="block w-[150px] max-w-full py-5 lg:mx-auto">
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

        <div class="w-full px-4 lg:w-3/12 xl:w-4/12 2xl:w-4/12">
          <div class="justify-end hidden pr-16 sm:flex lg:pr-0">
            <a
              href="javascript:void(0)"
              class="py-2.5 text-base font-medium px-6 text-dark dark:text-white hover:text-primary"
            >
              Login
            </a>
            <a
              href="javascript:void(0)"
              class="py-2.5 text-base font-medium text-white rounded-md whitespace-nowrap bg-dark dark:bg-white dark:text-dark px-6 hover:bg-opacity-90"
            >
              Sign Up
            </a>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>
