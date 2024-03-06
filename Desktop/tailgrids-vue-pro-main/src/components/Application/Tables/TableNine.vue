<script setup lang="ts">
import { ref, onMounted, onUnmounted  } from 'vue';
import type { Ref } from 'vue';

interface DropdownOpen {
  [key: number]: boolean;
}

const dropdownOpen: Ref<DropdownOpen> = ref({});

const toggleDropdown = (index: number) => {
  dropdownOpen.value[index] = !dropdownOpen.value[index];
};

const closeDropdown = (index: number) => {
  dropdownOpen.value[index] = false;
};

const clickHandler = ({ target }: { target: EventTarget | null }) => {
  if (!target) return;
  const dropdownButtons = document.querySelectorAll('.dropdown');
  dropdownButtons.forEach((button, index) => {
    const dropdown = button.nextElementSibling;
    if (!dropdown || (!dropdownOpen.value[index] && !dropdown.contains(target as Node))) return;
    toggleDropdown(index);
  });
};

const keyHandler = ({ keyCode }: { keyCode: number }) => {
  if (keyCode !== 27) return;
  Object.keys(dropdownOpen.value).map(Number).forEach((index) => {
    if (dropdownOpen.value[index]) {
      closeDropdown(index);
    }
  });
};

onMounted(() => {
  document.addEventListener('click', clickHandler);
  document.addEventListener('keydown', keyHandler);
});

onUnmounted(() => {
  document.removeEventListener('click', clickHandler);
  document.removeEventListener('keydown', keyHandler);
});

const users = ref([
  {
    title: 'NR',
    titleColor: 'bg-[#00BFD9]',
    name: 'Naimur Rahman',
    type: 'Annual Leave',
    period: '25 Dec 2024 - 28 Dec 2024',
    duration: '3 Days',
    status: true
  },
  {
    title: 'MC',
    titleColor: 'bg-[#FFB52B]',
    name: 'Musharof Chowdhury',
    type: 'Annual Leave',
    period: '25 Dec 2024 - 28 Dec 2024',
    duration: '3 Days',
    status: false
  },
  {
    title: 'SH',
    titleColor: 'bg-[#4926BD]',
    name: 'Shafiq Hammad',
    type: 'Annual Leave',
    period: '25 Dec 2024 - 28 Dec 2024',
    duration: '3 Days',
    status: true
  },
  {
    title: 'AS',
    titleColor: 'bg-[#132D4A]',
    name: 'Alex Semuyel',
    type: 'Annual Leave',
    period: '25 Dec 2024 - 28 Dec 2024',
    duration: '3 Days',
    status: false
  },
  {
    title: 'NR',
    titleColor: 'bg-[#00BFD9]',
    name: 'Naimur Rahman',
    type: 'Annual Leave',
    period: '25 Dec 2024 - 28 Dec 2024',
    duration: '3 Days',
    status: true
  }
])

const headers = ref([
  { name: 'Name', styles: 'min-w-[260px] text-left' },
  { name: 'Type', styles: 'min-w-[150px] text-left' },
  { name: 'Period', styles: 'min-w-[250px] text-left' },
  { name: 'Duration', styles: 'min-w-[130px] text-left' },
  { name: 'Status', styles: 'min-w-[150px] text-left' },
  { name: 'Actions', styles: 'min-w-[150px] text-right' }
])
</script>

<template>
  <section class="bg-gray-2 dark:bg-dark py-20 lg:py-[120px]">
    <div class="px-4 mx-auto lg:container">
      <div class="bg-white rounded-lg dark:bg-dark-2 shadow-card">
        <div class="max-w-full overflow-x-auto">
          <table class="w-full table-auto">
            <thead>
              <tr class="bg-[#F6F8FB] dark:bg-dark-3">
                <th
                  v-for="(header, index) in headers"
                  :key="index"
                  :class="`py-6 px-4 first:pl-10 last:pr-10 last:text-right ${header.styles}`"
                >
                  <p class="text-base font-medium text-body-color dark:text-dark-7">
                    {{ header.name }}
                  </p>
                </th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(user, index) in users"
                :key="index"
                class="border-b border-stroke dark:border-dark-3"
              >
                <td class="py-5 pl-10 pr-3">
                  <div class="flex items-center space-x-4">
                    <div
                      :class="`flex h-11 w-full max-w-[44px] items-center justify-center rounded-full text-base font-medium text-white ${user.titleColor}`"
                    >
                      {{ user.title }}
                    </div>

                    <p class="text-base text-body-color dark:text-dark-6">{{ user.name }}</p>
                  </div>
                </td>
                <td class="py-5 px-4">
                  <p class="text-base text-body-color dark:text-dark-6">{{ user.type }}</p>
                </td>
                <td class="py-5 px-4">
                  <p class="text-base text-body-color dark:text-dark-6">{{ user.period }}</p>
                </td>
                <td class="py-5 px-4">
                  <p class="text-base text-body-color dark:text-dark-6">{{ user.duration }}</p>
                </td>
                <td class="py-5 px-4">
                  <span
                    v-if="user.status"
                    class="inline-flex items-center justify-center h-8 px-5 text-base text-white rounded bg-green"
                  >
                    Approved
                  </span>
                  <span
                    v-else
                    class="inline-flex h-8 items-center justify-center rounded bg-[#F13426] px-5 text-base text-white"
                  >
                    Declined
                  </span>
                </td>
                <td class="py-5 pl-4 pr-10 text-right">
                  <div class="relative">
                    <button @click.stop="toggleDropdown(index)" class="text-body-color dark:text-dark-6 dropdown">
                      <svg
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          d="M13 12C13 11.4477 12.5523 11 12 11C11.4477 11 11 11.4477 11 12C11 12.5523 11.4477 13 12 13C12.5523 13 13 12.5523 13 12Z"
                          stroke="#637381"
                          strokeWidth="2"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                        />
                        <path
                          d="M6 12C6 11.4477 5.55228 11 5 11C4.44772 11 4 11.4477 4 12C4 12.5523 4.44772 13 5 13C5.55228 13 6 12.5523 6 12Z"
                          stroke="#637381"
                          strokeWidth="2"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                        />
                        <path
                          d="M20 12C20 11.4477 19.5523 11 19 11C18.4477 11 18 11.4477 18 12C18 12.5523 18.4477 13 19 13C19.5523 13 20 12.5523 20 12Z"
                          stroke="#637381"
                          strokeWidth="2"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                        />
                      </svg>
                    </button>

                    <div
                      v-if="dropdownOpen[index]" 
                      @click.stop="closeDropdown(index)"
                      class="absolute right-0 top-full z-40 w-[200px] space-y-1 rounded dark:bg-dark dark:border-dark-3 border-stroke border bg-white p-2 dark:shadow-card"
                    >
                      <button
                        @click.stop="closeDropdown(index)"
                        class="w-full px-3 py-2 text-sm text-left rounded text-body-color hover:bg-gray-2 dark:text-dark-6 dark:hover:bg-dark-2"
                      >
                        Edit
                      </button>
                      <button
                        @click.stop="closeDropdown(index)"
                        class="w-full px-3 py-2 text-sm text-left rounded text-body-color hover:bg-gray-2 dark:text-dark-6 dark:hover:bg-dark-2"
                      >
                        Delete
                      </button>
                    </div>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>
</template>
