<script setup lang="ts">
import { ref } from 'vue'

const teamMembers = ref([
  {
    id: 1,
    selected: false,
    name: 'Henry Dholi',
    role: 'Web Developer',
    imageUrl:
      'https://cdn.tailgrids.com/2.0/image/dashboard/images/box-select/box-select-01/image-01.png'
  },
  {
    id: 2,
    selected: false,
    name: 'Mariya Desoja',
    role: 'Graphics Designer',
    imageUrl:
      'https://cdn.tailgrids.com/2.0/image/dashboard/images/box-select/box-select-01/image-02.png'
  },
  {
    id: 3,
    selected: false,
    name: 'Robert Jhon',
    role: 'Ui/Ux Designer',
    imageUrl:
      'https://cdn.tailgrids.com/2.0/image/dashboard/images/box-select/box-select-01/image-03.png'
  },
  {
    id: 4,
    selected: false,
    name: 'Cody Fisher',
    role: 'Content Writer',
    imageUrl:
      'https://cdn.tailgrids.com/2.0/image/dashboard/images/box-select/box-select-01/image-04.png'
  }
])
</script>

<template>
  <!-- ====== Box Select Section Start -->
  <section class="bg-gray-2 dark:bg-dark py-20 lg:py-[120px]">
    <div class="container mx-auto">
      <div>
        <h3 class="mb-6 text-lg font-medium text-dark dark:text-white">Team Members</h3>
        <div
          class="w-full max-w-[375px] space-y-[10px] rounded-md bg-white dark:bg-dark-2 p-4 shadow-1 dark:shadow-box-dark"
        >
          <!-- Dynamic Box Select Section -->
          <div v-for="member in teamMembers" :key="member.id" class="flex items-center">
            <input
              :type="'checkbox'"
              :name="'box-select-' + member.id"
              :id="'select-' + member.id"
              class="box-select-1 sr-only"
              v-model="member.selected"
            />
            <label :for="'select-' + member.id" class="flex w-full items-center">
              <div
                class="user-box flex w-full items-center rounded-[5px] py-[10px] px-4 hover:bg-gray-2 dark:hover:bg-dark"
              >
                <div
                  class="box mr-5 flex h-5 w-full max-w-[20px] cursor-pointer items-center justify-center rounded border border-stroke dark:border-dark-3"
                >
                  <span class="icon" :class="{ 'opacity-0': !member.selected }">
                    <svg
                      width="14"
                      height="14"
                      viewBox="0 0 14 14"
                      fill="none"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        fill-rule="evenodd"
                        clip-rule="evenodd"
                        d="M12.0791 3.08687C12.307 3.31468 12.307 3.68402 12.0791 3.91183L5.66248 10.3285C5.43467 10.5563 5.06533 10.5563 4.83752 10.3285L1.92085 7.41183C1.69305 7.18402 1.69305 6.81468 1.92085 6.58687C2.14866 6.35906 2.51801 6.35906 2.74581 6.58687L5.25 9.09106L11.2542 3.08687C11.482 2.85906 11.8513 2.85906 12.0791 3.08687Z"
                        fill="white"
                      />
                    </svg>
                  </span>
                </div>
                <div class="mr-5 h-11 w-full max-w-[44px] rounded-full">
                  <img
                    :src="member.imageUrl"
                    :alt="member.name"
                    class="h-full w-full object-cover object-center"
                  />
                </div>
                <div>
                  <h4 class="text-sm font-medium text-dark dark:text-white">{{ member.name }}</h4>
                  <p class="text-xs text-body-color dark:text-dark-6">{{ member.role }}</p>
                </div>
              </div>
            </label>
          </div>
          <!-- End Dynamic Box Select Section -->
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Box Select Section End -->
</template>
