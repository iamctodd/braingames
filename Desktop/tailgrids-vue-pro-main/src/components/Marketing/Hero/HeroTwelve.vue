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
  <header class="absolute top-0 left-0 z-50 w-full">
    <div class="container">
      <div class="relative z-40 flex items-center justify-between -mx-4">
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
              class="absolute right-4 top-full z-40 w-full max-w-[250px] rounded-lg bg-white dark:bg-dark-2 py-5 px-6 shadow lg:static lg:block lg:w-full lg:max-w-full lg:bg-transparent lg:shadow-none xl:ml-11 lg:dark:bg-transparent"
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
              class="py-3 text-base font-medium text-white rounded-md bg-dark dark:bg-dark-2 dark:hover:bg-dark-3 px-7 hover:bg-body-color"
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
  <div class="relative pt-[150px] pb-[110px] lg:pt-[170px] dark:bg-dark">
    <div class="container mx-auto">
      <div class="flex flex-wrap items-center -mx-4">
        <div class="w-full px-4 lg:w-1/2">
          <div class="mb-12 lg:mb-0">
            <h2
              class="mb-5 text-3xl font-bold leading-[1.208] text-dark dark:text-white lg:text-[38px] xl:text-[40px]"
            >
              Build beautiful website with TailGrids blocks.
            </h2>
            <p class="max-w-[485px] mb-8 text-base text-body-color dark:text-dark-6">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam at egestas tortor.
              Morbi sed odio id purus pellentesque iaculis nulla facilisi.
            </p>
            <p class="mb-5 text-base font-medium text-dark dark:text-white">
              Subscribe to get notified when we launch 🎉
            </p>
            <form class="mb-7 flex max-w-[455px] flex-wrap">
              <input
                type="email"
                class="mr-3 mb-3 h-[52px] w-full rounded-md border border-stroke dark:border-dark-3 bg-white dark:bg-dark-2 px-5 text-base text-body-color outline-none focus:border-primary focus-visible:shadow-none placeholder:text-dark-6 sm:max-w-[220px] md:max-w-[315px] lg:max-w-[250px] xl:max-w-[300px]"
                placeholder="Your work mail"
              />
              <button
                class="mb-3 h-[52px] rounded-md bg-primary px-7 text-base font-medium text-white transition hover:bg-blue-dark"
              >
                Notify Me!
              </button>
            </form>
          </div>
        </div>
        <div class="w-full px-4 lg:w-1/2">
          <div class="flex flex-wrap -mx-2 sm:-mx-4">
            <div class="w-1/2 px-2 sm:px-4">
              <div class="mb-4 h-[256px] sm:mb-8 sm:h-[442px] lg:h-[332px] xl:h-[442px]">
                <img
                  src="https://cdn.tailgrids.com/2.0/image/marketing/images/hero/hero-12/image-1.jpg"
                  alt="hero image"
                  class="object-cover object-center w-full h-full"
                />
              </div>
            </div>
            <div class="w-1/2 px-2 sm:px-4">
              <div class="mb-4 h-[120px] sm:mb-8 sm:h-[205px] lg:h-[150px] xl:h-[205px]">
                <img
                  src="https://cdn.tailgrids.com/2.0/image/marketing/images/hero/hero-12/image-2.jpg"
                  alt="hero image"
                  class="object-cover object-center w-full h-full"
                />
              </div>
              <div class="mb-4 h-[120px] sm:mb-8 sm:h-[205px] lg:h-[150px] xl:h-[205px]">
                <img
                  src="https://cdn.tailgrids.com/2.0/image/marketing/images/hero/hero-12/image-3.jpg"
                  alt="hero image"
                  class="object-cover object-center w-full h-full"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- ====== Hero Section End -->
</template>
