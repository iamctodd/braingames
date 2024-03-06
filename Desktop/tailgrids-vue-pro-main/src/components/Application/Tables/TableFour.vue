<script setup lang="ts">
import { ref } from 'vue'

const users = ref([
  {
    name: 'Graphics Design',
    startDate: '25 Dec, 2024',
    endDate: '12 Jan, 2025'
  },
  {
    name: 'Graphics Design',
    startDate: '25 Dec, 2024',
    endDate: '12 Jan, 2025'
  },
  {
    name: 'Graphics Design',
    startDate: '25 Dec, 2024',
    endDate: '12 Jan, 2025'
  },
  {
    name: 'Graphics Design',
    startDate: '25 Dec, 2024',
    endDate: '12 Jan, 2025'
  },
  {
    name: 'Graphics Design',
    startDate: '25 Dec, 2024',
    endDate: '12 Jan, 2025'
  }
])

const headers = [
  { name: 'Project', styles: 'min-w-[280px]' },
  { name: 'Started', styles: 'min-w-[150px]' },
  { name: 'Completed', styles: 'min-w-[150px]' },
  { name: '', styles: 'min-w-[100px]' }
]
</script>

<template>
  <section class="bg-white dark:bg-dark-2 py-20 lg:py-[120px]">
    <div class="container mx-auto">
      <div class="flex flex-wrap -mx-4">
        <div class="w-full px-4">
          <div class="max-w-full overflow-x-auto rounded-xl shadow-lg">
            <table class="w-full table-auto">
              <thead>
                <tr class="bg-body-color text-left">
                  <th
                    v-for="(header, index) in headers"
                    :key="index"
                    :class="`py-4 px-4 first:pl-11 last:pr-11 text-base font-medium text-white ${header.styles}`"
                  >
                    {{ header.name }}
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr class="bg-dark" v-for="(user, index) in users" :key="index">
                  <td class="border-t border-[#47515A] py-5 px-4 pl-11">
                    <h5 class="text-base font-medium text-[#C0C3C6]">{{ user.name }}</h5>
                  </td>
                  <td class="border-t border-[#47515A] py-5 px-4">
                    <p class="text-base font-medium text-[#C0C3C6]">{{ user.startDate }}</p>
                  </td>
                  <td class="border-t border-[#47515A] py-5 px-4">
                    <p class="text-base font-medium text-[#C0C3C6]">{{ user.endDate }}</p>
                  </td>
                  <td class="border-t border-[#47515A] py-5 px-4 pr-11 text-right">
                    <button class="hover:text-primary text-base font-medium text-[#C0C3C6]">
                      Edit
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
