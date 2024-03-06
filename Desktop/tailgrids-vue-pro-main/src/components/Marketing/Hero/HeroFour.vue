<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'

const open = ref(false)
const dropdownButtonRef = ref<HTMLButtonElement | null>(null)

const toggleNavbar = () => {
  open.value = !open.value
}

const navLinkItems = ref([
  { text: 'Home', href: 'javascript:void(0)' },
  { text: 'About', href: 'javascript:void(0)' },
  { text: 'Portfolio', href: 'javascript:void(0)' }
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
  <header class="absolute left-0 top-0 z-50 w-full">
    <div class="container">
      <div class="relative z-40 flex items-center justify-between -mx-4">
        <div class="w-60 max-w-full px-4">
          <a href="/#" class="block w-full py-5">
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
              class="py-3 text-base font-medium text-white px-7 hover:text-white/90"
            >
              Sign In
            </a>
            <a
              href="javascript:void(0)"
              class="py-3 text-base font-medium text-white rounded-lg bg-white/5 px-7 hover:bg-white/10"
            >
              Sign Up
            </a>
          </div>
        </div>
      </div>
    </div>
  </header>
  <!-- ====== Navbar Section End -->

  <!-- ====== Hero Section Start -->
  <div
    class="relative z-10 bg-white dark:bg-dark pt-[120px] pb-[130px] md:pt-[150px] lg:pt-[230px] lg:pb-[180px]]"
  >
    <div class="container mx-auto">
      <div class="flex flex-wrap items-center -mx-4">
        <div class="w-full px-4 lg:w-6/12 xl:w-5/12">
          <div class="hero-content">
            <h1
              class="mb-3 max-w-[480px] text-4xl font-bold leading-[1.208] text-dark dark:text-white sm:text-5xl"
            >
              Find a dream job That changes life.
            </h1>
            <p class="mb-8 max-w-[480px] text-base text-body-color dark:text-dark-6">
              With TailGrids, business and students thrive together. Business can perfectly match
              their staffing to changing demand throughout the dayed.
            </p>
            <form
              class="mb-5 w-full rounded-[10px] border border-stroke dark:border-dark-3 bg-white shadow-2 dark:bg-dark-2 px-[14px] py-[6px] md:max-w-[490px]"
            >
              <div class="flex flex-wrap -ml-2 -mr-2">
                <div class="w-full p-2 sm:w-1/2 md:w-1/3">
                  <input
                    type="text"
                    placeholder="Job Keyword"
                    class="h-[46px] w-full rounded-md border border-stroke dark:border-dark-3 bg-transparent px-4 text-sm text-body-color dark:text-dark-6 outline-none focus:bg-[#FCFDFE] dark:focus:bg-dark focus-visible:shadow-none placeholder:text-dark-7"
                  />
                </div>
                <div class="w-full p-2 sm:w-1/2 md:w-1/3">
                  <input
                    type="text"
                    placeholder="Job Location"
                    class="h-[46px] w-full rounded-md border border-stroke dark:border-dark-3 bg-transparent px-4 text-sm text-body-color dark:text-dark-6 outline-none focus:bg-[#FCFDFE] dark:focus:bg-dark focus-visible:shadow-none placeholder:text-dark-7"
                  />
                </div>
                <div class="w-full p-2 md:w-1/3">
                  <input
                    type="submit"
                    value="Search"
                    class="w-full cursor-pointer rounded-md bg-primary py-[11px] px-5 font-medium text-white transition hover:bg-blue-dark"
                  />
                </div>
              </div>
            </form>
            <p class="text-base font-medium text-body-color dark:text-dark-6">
              Try Product Designer, Software Engineer etc.
            </p>
          </div>
        </div>
        <div class="hidden px-4 lg:block xl:w-1/12"></div>
        <div class="w-full px-4 lg:w-6/12">
          <div
            class="absolute right-0 top-0 z-[-1] hidden h-full w-1/2 max-w-[720px] items-end justify-center bg-cover bg-left-top bg-no-repeat px-5 lg:flex"
            style="
              background-image: url('https://cdn.tailgrids.com/2.0/image/marketing/images/hero/hero-4-bg.svg');
            "
          >
            <div>
              <img
                src="https://cdn.tailgrids.com/2.0/image/marketing/images/hero/hero-image-04.png"
                alt="hero"
                class="max-w-full mx-auto"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- ====== Hero Section End -->
</template>
