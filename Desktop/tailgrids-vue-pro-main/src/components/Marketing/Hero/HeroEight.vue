<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'

const open = ref(false)
const dropdownButtonRef = ref<HTMLButtonElement | null>(null)

const toggleNavbar = () => {
  open.value = !open.value
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
  <!-- ====== Navbar Section Start -->
  <header class="absolute top-0 left-0 z-50 w-full">
    <div class="container">
      <div class="relative flex items-center justify-between -mx-4">
        <div class="max-w-full px-4 w-60">
          <a href="javascript:void(0)" class="block w-full py-5 lg:py-3">
            <img
              src="https://cdn.tailgrids.com/2.0/image/assets/images/logo/logo-white.svg"
              alt="logo"
              class="w-full"
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
              <span class="relative my-[6px] block h-[2px] w-[30px] bg-white"></span>
              <span class="relative my-[6px] block h-[2px] w-[30px] bg-white"></span>
              <span class="relative my-[6px] block h-[2px] w-[30px] bg-white"></span>
            </button>
            <nav
              :class="{ hidden: !open }"
              id="navbarCollapse"
              class="absolute right-4 top-full w-full max-w-[250px] rounded-lg bg-white dark:bg-dark-2 py-5 px-6 shadow lg:static lg:block lg:w-full lg:max-w-full lg:bg-transparent lg:py-0 lg:shadow-none xl:ml-11 lg:dark:bg-transparent"
            >
              <ul class="block lg:flex">
                <template v-for="(item, index) in navLinkItems" :key="index">
                  <li>
                    <a
                      v-if="item.href"
                      :href="item.href"
                      class="flex border-transparent py-2 text-base font-medium text-dark dark:text-white hover:border-primary hover:text-primary lg:ml-10 lg:inline-flex lg:border-t-[3px] lg:py-6 lg:text-white"
                    >
                      {{ item.text }}
                    </a>
                  </li>
                </template>
              </ul>
            </nav>
          </div>

          <div class="justify-end hidden pr-16 sm:flex lg:pr-0">
            <form
              class="relative flex max-w-[180px] md:max-w-[230px] lg:max-w-[120px] xl:max-w-[235px]"
            >
              <input
                type="text"
                placeholder="Search here..."
                class="w-full py-2 pl-5 pr-10 bg-transparent border border-white rounded-full outline-none border-opacity-30 text-gray-7 focus:border-opacity-100 focus-visible:shadow-none"
              />
              <button class="absolute -translate-y-1/2 right-4 top-1/2">
                <svg
                  width="20"
                  height="18"
                  viewBox="0 0 20 18"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M19.4062 16.8125L13.9375 12.375C14.9375 11.0625 15.5 9.46875 15.5 7.78125C15.5 5.75 14.7187 3.875 13.2812 2.4375C10.3437 -0.5 5.5625 -0.5 2.59375 2.4375C1.1875 3.84375 0.40625 5.75 0.40625 7.75C0.40625 9.78125 1.1875 11.6562 2.625 13.0937C4.09375 14.5625 6.03125 15.3125 7.96875 15.3125C9.875 15.3125 11.75 14.5937 13.2187 13.1875L18.75 17.6562C18.8437 17.75 18.9687 17.7812 19.0937 17.7812C19.25 17.7812 19.4062 17.7187 19.5312 17.5937C19.6875 17.3437 19.6562 17 19.4062 16.8125ZM3.375 12.3437C2.15625 11.125 1.5 9.5 1.5 7.75C1.5 6 2.15625 4.40625 3.40625 3.1875C4.65625 1.9375 6.3125 1.3125 7.96875 1.3125C9.625 1.3125 11.2812 1.9375 12.5312 3.1875C13.75 4.40625 14.4375 6.03125 14.4375 7.75C14.4375 9.46875 13.7187 11.125 12.5 12.3437C10 14.8437 5.90625 14.8437 3.375 12.3437Z"
                    fill="white"
                  />
                </svg>
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </header>
  <!-- ====== Navbar Section End -->

  <!-- ====== Hero Section Start -->
  <div class="relative bg-[#090E34] pt-[120px] md:pt-[150px] lg:pt-[180px]">
    <div class="container mx-auto">
      <div class="flex flex-wrap items-center -mx-4">
        <div class="w-full px-4 lg:w-5/12">
          <div class="mb-14 lg:mb-0">
            <span class="block mb-4 text-base font-medium text-white"> We are creative team. </span>
            <h1
              class="mb-3 text-4xl font-bold !leading-[1.208] text-white md:text-5xl lg:text-[40px] xl:text-5xl"
            >
              The best way to promote business
            </h1>
            <p class="mb-9 max-w-[460px] text-base font-medium text-gray-3">
              There are many variations of passages of Lorem Ipsum available, but the majority have
              suffered.
            </p>
            <ul class="flex flex-wrap items-center gap-4">
              <li>
                <a
                  href="javascript:void(0)"
                  class="inline-flex items-center justify-center py-3 text-base font-medium text-center text-white rounded-full bg-primary px-7 hover:bg-blue-dark"
                >
                  Discover More
                </a>
              </li>
              <li>
                <a
                  href="javascript:void(0)"
                  class="inline-flex items-center px-6 py-3 text-base font-medium bg-white rounded-full text-primary hover:text-body-color shadow-1 hover:bg-gray-2"
                >
                  Explore Services
                  <span class="ml-2">
                    <svg
                      width="20"
                      height="20"
                      viewBox="0 0 20 20"
                      fill="none"
                      xmlns="http://www.w3.org/2000/svg"
                      class="fill-current"
                    >
                      <path
                        d="M18 9.5L11.5312 2.9375C11.25 2.65625 10.8125 2.65625 10.5312 2.9375C10.25 3.21875 10.25 3.65625 10.5312 3.9375L15.7812 9.28125H2.5C2.125 9.28125 1.8125 9.59375 1.8125 9.96875C1.8125 10.3437 2.125 10.6875 2.5 10.6875H15.8437L10.5312 16.0938C10.25 16.375 10.25 16.8125 10.5312 17.0938C10.6562 17.2188 10.8437 17.2813 11.0312 17.2813C11.2187 17.2813 11.4062 17.2188 11.5312 17.0625L18 10.5C18.2812 10.2187 18.2812 9.78125 18 9.5Z"
                        fill=""
                      />
                    </svg>
                  </span>
                </a>
              </li>
            </ul>
          </div>
        </div>
        <div class="w-full px-4 lg:w-7/12">
          <div class="mx-auto text-center">
            <img
              src="https://cdn.tailgrids.com/2.0/image/marketing/images/hero/hero-image-08.svg"
              alt="image"
              class="max-w-full mx-auto"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- ====== Hero Section End -->
</template>
