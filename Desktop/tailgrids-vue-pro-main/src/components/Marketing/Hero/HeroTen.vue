<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'

const open = ref(false)
const dropdownButtonRef = ref<HTMLButtonElement | null>(null)

const toggleNavbar = () => {
  open.value = !open.value
}

const navLinkItems = ref([
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
  <!-- ====== Navbar Section Start -->
  <header class="absolute top-0 left-0 z-20 w-full">
    <div class="container">
      <div class="relative z-10 flex items-center justify-between -mx-4">
        <div class="max-w-full px-4 w-60">
          <a href="javascript:void(0)" class="block w-full py-5">
            <img
              src="https://cdn.tailgrids.com/2.0/image/assets/images/logo/logo.svg"
              alt="logo"
              class="block w-full dark:hidden"
            />
            <img
              src="https://cdn.tailgrids.com/2.0/image/assets/images/logo/logo-white.svg"
              alt="logo"
              class="hidden w-full dark:block"
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
              class="absolute right-4 top-full z-10 w-full max-w-[250px] rounded-lg bg-white dark:bg-dark-2 py-5 px-6 shadow lg:static lg:block lg:w-full lg:max-w-full lg:bg-transparent lg:shadow-none xl:ml-11 lg:dark:bg-transparent"
            >
              <ul class="block lg:flex">
                <template v-for="(item, index) in navLinkItems" :key="index">
                  <li>
                    <a
                      v-if="item.href"
                      :href="item.href"
                      class="flex py-2 text-base font-medium text-dark dark:text-white hover:text-primary lg:ml-10 lg:inline-flex"
                    >
                      {{ item.text }}
                    </a>
                  </li>
                </template>
              </ul>
            </nav>
          </div>

          <div class="justify-end hidden pr-16 sm:flex lg:pr-0">
            <a
              href="javascript:void(0)"
              class="py-3 text-base font-medium text-white rounded-md bg-primary px-7 hover:bg-blue-dark"
            >
              Get Started
            </a>
          </div>
        </div>
      </div>
    </div>
  </header>
  <!-- ====== Navbar Section End -->

  <!-- ====== Hero Section Start -->
  <div
    class="relative z-10 overflow-hidden bg-white dark:bg-dark pt-[120px] pb-[110px] md:pt-[150px] lg:pt-[180px]"
  >
    <div class="container mx-auto">
      <div class="flex flex-wrap -mx-4">
        <div class="w-full px-4 lg:w-6/12 xl:w-5/12">
          <div class="hero-content max-w-[575px]">
            <h1
              class="mb-4 text-4xl font-bold capitalize !leading-[1.208] text-dark dark:text-white sm:text-[42px] lg:text-[40px] xl:text-5xl"
            >
              <span>Business site templates Crafted with</span>
              <span class="pl-0.5 text-primary">TailGrids.</span>
            </h1>
            <p class="mb-9 max-w-[477px] text-base text-body-color dark:text-dark-6">
              With TailGrids, business and students thrive together. Business can perfectly match
              their staffing to changing demand throughout the dayed.
            </p>
            <ul class="flex flex-wrap items-center gap-4">
              <li>
                <a
                  href="javascript:void(0)"
                  class="inline-flex items-center justify-center py-3 text-base font-medium text-center text-white border border-transparent rounded-md bg-primary px-7 hover:bg-blue-dark"
                >
                  Know More
                </a>
              </li>
              <li>
                <a
                  href="javascript:void(0)"
                  class="inline-flex items-center justify-center py-3 text-base font-medium text-center transition border rounded-md border-dark dark:border-white px-7 text-dark dark:text-white hover:bg-dark hover:text-white dark:hover:bg-white dark:hover:text-dark"
                >
                  Contact Us
                </a>
              </li>
            </ul>
          </div>
        </div>
        <div class="w-full px-4 lg:w-6/12 xl:w-7/12">
          <div class="lg:ml-auto lg:text-right">
            <div class="absolute right-0 top-0 z-[-1] hidden h-full lg:inline-block">
              <img
                src="https://cdn.tailgrids.com/2.0/image/marketing/images/hero/hero-image-10.png"
                alt="hero"
                class="h-full max-w-full lg:ml-auto"
              />
              <span class="absolute top-0 right-3 z-[-2] h-full w-[105%] xl:right-8 xl:w-full">
                <svg viewBox="0 0 743 710" fill="none" class="w-full max-h-full">
                  <path
                    opacity="0.2"
                    d="M170.825 0H908V753H186.118C61.1679 753 -27.8471 631.69 9.64041 512.496L170.825 0Z"
                    fill="url(#paint0_linear_1414_931)"
                  />
                  <defs>
                    <linearGradient
                      id="paint0_linear_1414_931"
                      x1="421"
                      y1="0"
                      x2="421"
                      y2="753"
                      gradientUnits="userSpaceOnUse"
                    >
                      <stop stop-color="#3056D3" />
                      <stop offset="1" stop-color="#3056D3" stop-opacity="0" />
                    </linearGradient>
                  </defs>
                </svg>
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- ====== Hero Section End -->
</template>
