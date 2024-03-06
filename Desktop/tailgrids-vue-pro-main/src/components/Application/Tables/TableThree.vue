<script setup lang="ts">
import { ref } from 'vue'

const users = ref([
  {
    name: 'Musharof Chowdhury',
    title: 'Multidisciplinary Web Entrepreneur',
    email: 'musharof@example.com',
    role: 'Owner'
  },
  {
    name: 'Naimur Rahman',
    title: 'Website Front-end Developer',
    email: 'naimurrahman@example.com',
    role: 'Member'
  },
  {
    name: 'Shafiq Hammad',
    title: 'Regional Paradigm Technician',
    email: 'shafiq.hd@example.com',
    role: 'Moderator'
  },
  {
    name: 'Alex Semuyel',
    title: 'Applications Engineer',
    email: 'alex.semuel@example.com',
    role: 'Admin'
  },
  {
    name: 'Sulium Keliym',
    title: 'Lead Implementation Liaison',
    email: 'suliym.info@example.com',
    role: 'Member'
  },
  {
    name: 'Devid Deekook',
    title: 'Central Security Manager',
    email: 'devid.decok@example.com',
    role: 'Moderator'
  }
])

const headers = ref([
  { name: 'Name', styles: 'min-w-[280px]' },
  { name: 'Title', styles: 'min-w-[280px]' },
  { name: 'Email', styles: 'min-w-[250px]' },
  { name: 'Role', styles: 'min-w-[140px]' },
  { name: '', styles: 'min-w-[140px]' }
])
</script>

<template>
  <section class="bg-white dark:bg-dark py-20 lg:py-[120px]">
    <div class="container mx-auto">
      <div class="flex flex-wrap -mx-4">
        <div class="w-full px-4">
          <div
            class="max-w-full overflow-x-auto bg-white dark:bg-dark-2 shadow-[0px_3px_8px_0px_rgba(0,0,0,0.08)] rounded-xl"
          >
            <table class="w-full table-auto">
              <thead>
                <tr class="text-left bg-gray dark:bg-dark-3">
                  <th
                    v-for="(header, index) in headers"
                    :key="index"
                    :class="`text-body-color dark:text-dark-7 py-4 px-4 first:pl-11 last:pr-11 text-base font-medium uppercase ${header.styles}`"
                  >
                    {{ header.name }}
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(user, index) in users" :key="index">
                  <td class="px-4 py-5 border-t border-stroke pl-11 dark:border-dark-3">
                    <h5 class="text-base text-body-color dark:text-dark-6">{{ user.name }}</h5>
                  </td>
                  <td class="px-4 py-5 border-t border-stroke dark:border-dark-3">
                    <p class="text-base text-body-color dark:text-dark-6">
                      {{ user.title }}
                    </p>
                  </td>
                  <td class="px-4 py-5 border-t border-stroke dark:border-dark-3">
                    <p class="text-base text-body-color dark:text-dark-6">{{ user.email }}</p>
                  </td>
                  <td class="px-4 py-5 border-t border-stroke dark:border-dark-3">
                    <p class="text-sm text-body-color dark:text-dark-6">{{ user.role }}</p>
                  </td>
                  <td class="px-4 py-5 text-center border-t border-stroke pr-11 dark:border-dark-3">
                    <button class="text-base font-medium text-primary">Edit</button>
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
