<script setup lang="ts">
import { ref } from 'vue'

const openDropDown = ref<number | null>(null)

const navItems = ref([
  { label: 'Home' },
  { label: 'Dashboard' },
  {
    label: 'Products',
    children: [{ label: 'Dropdown One' }, { label: 'Dropdown Two' }, { label: 'Dropdown Three' }]
  },
  { label: 'Messages' },
  { label: 'Order' },
  { label: 'Calendar' },
  { label: 'Static' },
  { label: 'Documents' },
  { divider: true },
  { label: 'Chat' },
  { label: 'Settings' },
  { label: 'Log out' }
])

const toggleDropdown = (index: number | null) => {
  openDropDown.value = openDropDown.value === index ? null : index
}
</script>

<template>
  <section class="h-screen bg-gray-2 dark:bg-dark">
    <div
      class="flex h-screen w-full max-w-[300px] flex-col justify-between overflow-y-scroll bg-white dark:bg-dark-2 shadow-testimonial-6 dark:shadow-box-dark"
    >
      <div>
        <div class="px-9 pt-10 pb-9">
          <a href="javascript:void(0)">
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

        <nav>
          <ul>
            <!-- Use v-for to loop through the dynamic nav items -->
            <li v-for="(item, index) in navItems" :key="index">
              <template v-if="item.children">
                <!-- Handle dropdown click -->
                <a
                  href="javascript:void(0)"
                  @click="toggleDropdown(index)"
                  class="relative flex items-center border-r-4 py-[10px] pl-9 pr-10 text-base font-medium text-body-color dark:text-dark-6 duration-200 hover:border-primary hover:bg-primary/5"
                  :class="{
                    'border-primary bg-primary/5': openDropDown === index,
                    'border-transparent': openDropDown !== index
                  }"
                >
                  {{ item.label }}
                  <span
                    class="absolute top-1/2 right-10 -translate-y-1/2"
                    :class="{
                      'rotate-0': openDropDown !== index,
                      'rotate-180': openDropDown === index
                    }"
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
                        d="M10 14.25C9.8125 14.25 9.65625 14.1875 9.5 14.0625L2.3125 7C2.03125 6.71875 2.03125 6.28125 2.3125 6C2.59375 5.71875 3.03125 5.71875 3.3125 6L10 12.5312L16.6875 5.9375C16.9688 5.65625 17.4062 5.65625 17.6875 5.9375C17.9688 6.21875 17.9688 6.65625 17.6875 6.9375L10.5 14C10.3437 14.1562 10.1875 14.25 10 14.25Z"
                      />
                    </svg>
                  </span>
                </a>
                <!-- Display dropdown items when openDropDown is true for the current index -->
                <div v-show="openDropDown === index">
                  <ul class="py-[6px] pl-[50px] pr-10">
                    <li v-for="(childItem, childIndex) in item.children" :key="childIndex">
                      <!-- Handle dropdown item click -->
                      <a
                        href="javascript:void(0)"
                        class="flex items-center border-r-4 border-transparent py-[9px] text-base font-medium text-body-color dark:text-dark-6 duration-200 hover:text-primary"
                      >
                        {{ childItem.label }}
                      </a>
                    </li>
                  </ul>
                </div>
              </template>
              <template v-if="item.divider" >
                <div class="mx-9 my-5 h-px bg-stroke dark:bg-dark-3"></div>
              </template>
              <template v-else>
                <!-- Handle regular nav item click -->
                <a
                  href="javascript:void(0)"
                  class="relative flex items-center border-r-4 border-transparent py-[10px] pl-9 pr-10 text-base font-medium text-body-color dark:text-dark-6 duration-200 hover:border-primary hover:bg-primary/5"
                >
                  {{ item.label }}
                </a>
              </template>
            </li>
          </ul>
        </nav>
      </div>

      <div class="p-9" >
        <div class="flex items-center">
          <div class="mr-4 h-[50px] w-full max-w-[50px] rounded-full">
            <img
              src="https://cdn.tailgrids.com/2.0/image/assets/images/avatar/image-05.jpg"
              alt="profile"
              class="h-full w-full rounded-full object-cover object-center"
            />
          </div>
          <div>
            <h6 class="text-base font-medium text-dark dark:text-white">Musharof</h6>
            <p class="text-sm text-body-color dark:text-dark-6">hello@tailgrids.com</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
