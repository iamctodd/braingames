<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'

const open = ref(false)
const dropdownButtonRef = ref<HTMLButtonElement | null>(null)

const toggleNavbar = () => {
  open.value = !open.value
}

const toggleSubmenu = (index: number) => {
  navLinkItems.value[index].openSubmenu = !navLinkItems.value[index].openSubmenu;
}

const navLinkItems = ref([
  {
    text: 'Home',
    href: 'javascript:void(0)',
    openSubmenu: false,
    submenu: [
      { text: 'Creative Homepage', href: 'javascript:void(0)' },
      { text: 'Business Homepage', href: 'javascript:void(0)' },
      { text: 'Corporate Homepage', href: 'javascript:void(0)' },
      { text: 'Personal Homepage', href: 'javascript:void(0)' }
    ]
  },
  { text: 'Payment', href: 'javascript:void(0)' },
  { text: 'About', href: 'javascript:void(0)' },
  {
    text: 'Blog',
    href: 'javascript:void(0)',
    openSubmenu: false,
    submenu: [
      { text: 'Creative Homepage', href: 'javascript:void(0)' },
      { text: 'Business Homepage', href: 'javascript:void(0)' },
      { text: 'Corporate Homepage', href: 'javascript:void(0)' },
      { text: 'Personal Homepage', href: 'javascript:void(0)' }
    ]
  }
])

// Custom composition function to handle click outside
const handleClickOutside = (event: MouseEvent) => {

  const isOutsideDropdownButton = dropdownButtonRef.value && !dropdownButtonRef.value.contains(event.target as Node);
  const isOutsideNavbar = !document.getElementById('navbarCollapse')?.contains(event.target as Node);

  if (isOutsideNavbar && isOutsideDropdownButton) {
    open.value = false;
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
      <div class="relative -mx-4 flex items-center justify-between">
        <div class="w-60 max-w-full px-4">
          <a href="/#" class="block w-full py-5">
            <img
              src="https://cdn.tailgrids.com/2.0/image/assets/images/logo/logo.svg"
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
              class="absolute right-4 top-full w-full max-w-[250px] rounded-lg dark:bg-dark-2 bg-white py-5 shadow lg:static lg:block lg:w-full lg:max-w-full lg:py-0 lg:px-6 lg:shadow-none lg:bg-transparent lg:dark:bg-transparent"
            >
              <ul class="block lg:flex">
                <template v-for="(item, index) in navLinkItems" :key="index">
                  <li class="group relative">
                    <a
                      v-if="item.href"
                      :href="item.href"
                      @click="item.submenu && toggleSubmenu(index)"
                      class="flex px-6 py-2 text-base font-medium text-body-color hover:text-dark dark:text-dark-6 dark:hover:text-white lg:ml-12 lg:inline-flex lg:py-6"
                      :class="[
                        item.submenu ? 'relative after:absolute after:right-5 after:top-1/2 after:mt-[-2px] after:h-2 after:w-2 after:translate-y-[-50%] after:rotate-45 after:border-b-2 after:border-r-2 after:border-current group-hover:text-dark lg:after:right-0 lg:pl-0 lg:pr-4 dark:group-hover:text-white' : 'lg:px-0'
                      ]"
                    >
                      {{ item.text }}
                    </a>

                    <ul
                      v-if="item.submenu"
                      :class="[
                        !item.openSubmenu ? 'hidden lg:block' : 'block'
                      ]"
                      class="relative top-full left-0 rounded-lg bg-white px-4 transition-all group-hover:opacity-100 lg:invisible lg:absolute lg:top-[115%] lg:w-[250px] lg:p-4 lg:opacity-0 lg:shadow-lg lg:group-hover:visible lg:group-hover:top-full dark:bg-dark-2"
                    >
                      <li v-for="(submenuItem, submenuIndex) in item.submenu" :key="submenuIndex">
                        <a
                          :href="submenuItem.href"
                          class="block rounded py-[10px] px-4 text-sm font-medium text-body-color hover:bg-primary hover:text-white dark:text-dark-6"
                        >
                          {{ submenuItem.text }}
                        </a>
                      </li>
                    </ul>
                  </li>
                </template>
              </ul>
            </nav>
          </div>

          <div class="justify-end hidden pr-16 sm:flex lg:pr-0">
            <a
              href="javascript:void(0)"
              class="py-2.5 text-base font-medium px-6 dark:text-white text-dark hover:text-primary"
            >
              Login
            </a>
            <a
              href="javascript:void(0)"
              class="py-2.5 text-base font-medium text-white rounded-md bg-primary px-6 hover:bg-primary/90"
            >
              Sign Up
            </a>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>
