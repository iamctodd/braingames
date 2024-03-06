<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue';

const open = ref(false);
const dropdownButtonRef = ref<HTMLButtonElement | null>(null);
const searchForm = ref(false);
const searchFormContainer = ref<HTMLElement | null>(null);

const toggleNavbar = () => {
  open.value = !open.value;
  if (searchForm.value) {
    searchForm.value = false;
  }
};

const toggleSearchForm = () => {
  searchForm.value = !searchForm.value;
};

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
    open.value = false;
  }

  if (searchFormContainer.value && !searchFormContainer.value.contains(event.target as Node)) {
    searchForm.value = false;
  }
};

onMounted(() => {
  document.addEventListener('click', handleClickOutside);
});

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
});
</script>

<template>
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

          <div class="relative justify-end hidden right-16 sm:flex lg:right-0">
            <div class="flex max-w-[200px] justify-end">
              <button
                @click="() => toggleSearchForm()"
                ref="searchFormContainer"
                class="flex items-center justify-center w-10 h-10 border rounded-full border-stroke dark:border-dark-4 dark:text-white text-dark"
              >
                <svg width="20" height="18" viewBox="0 0 20 18" class="fill-current">
                  <path
                    d="M19.4062 16.8125L13.9375 12.375C14.9375 11.0625 15.5 9.46875 15.5 7.78125C15.5 5.75 14.7187 3.875 13.2812 2.4375C10.3437 -0.5 5.5625 -0.5 2.59375 2.4375C1.1875 3.84375 0.40625 5.75 0.40625 7.75C0.40625 9.78125 1.1875 11.6562 2.625 13.0937C4.09375 14.5625 6.03125 15.3125 7.96875 15.3125C9.875 15.3125 11.75 14.5937 13.2187 13.1875L18.75 17.6562C18.8437 17.75 18.9687 17.7812 19.0937 17.7812C19.25 17.7812 19.4062 17.7187 19.5312 17.5937C19.6875 17.3437 19.6562 17 19.4062 16.8125ZM3.375 12.3437C2.15625 11.125 1.5 9.5 1.5 7.75C1.5 6 2.15625 4.40625 3.40625 3.1875C4.65625 1.9375 6.3125 1.3125 7.96875 1.3125C9.625 1.3125 11.2812 1.9375 12.5312 3.1875C13.75 4.40625 14.4375 6.03125 14.4375 7.75C14.4375 9.46875 13.7187 11.125 12.5 12.3437C10 14.8437 5.90625 14.8437 3.375 12.3437Z"
                  />
                </svg>
              </button>
            </div>
            <div
              :class="{ hidden: !searchForm }"
              
              class="absolute top-full right-0 mt-5 w-[330px] bg-white dark:bg-dark-2 rounded-md"
            >
              <form class="flex items-center justify-between">
                <input
                  type="text"
                  placeholder="Search Components or UI"
                  class="w-full py-4 pl-5 pr-8 bg-white border border-transparent rounded-md shadow-sm outline-none text-body-color dark:text-white dark:bg-dark-2 focus-visible:shadow-none"
                />
                <button class="absolute -translate-y-1/2 right-5 top-1/2 text-dark dark:text-white">
                  <svg width="20" height="18" viewBox="0 0 20 18" class="fill-current">
                    <path
                      d="M19.4062 16.8125L13.9375 12.375C14.9375 11.0625 15.5 9.46875 15.5 7.78125C15.5 5.75 14.7187 3.875 13.2812 2.4375C10.3437 -0.5 5.5625 -0.5 2.59375 2.4375C1.1875 3.84375 0.40625 5.75 0.40625 7.75C0.40625 9.78125 1.1875 11.6562 2.625 13.0937C4.09375 14.5625 6.03125 15.3125 7.96875 15.3125C9.875 15.3125 11.75 14.5937 13.2187 13.1875L18.75 17.6562C18.8437 17.75 18.9687 17.7812 19.0937 17.7812C19.25 17.7812 19.4062 17.7187 19.5312 17.5937C19.6875 17.3437 19.6562 17 19.4062 16.8125ZM3.375 12.3437C2.15625 11.125 1.5 9.5 1.5 7.75C1.5 6 2.15625 4.40625 3.40625 3.1875C4.65625 1.9375 6.3125 1.3125 7.96875 1.3125C9.625 1.3125 11.2812 1.9375 12.5312 3.1875C13.75 4.40625 14.4375 6.03125 14.4375 7.75C14.4375 9.46875 13.7187 11.125 12.5 12.3437C10 14.8437 5.90625 14.8437 3.375 12.3437Z"
                    />
                  </svg>
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>
