<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'

const dropdownOpen = ref(false)
const anyInnerDropdownOpen = ref(false)
const dropdownButtonRef = ref<HTMLButtonElement | null>(null)
const dropdownContainerRef = ref<HTMLDivElement | null>(null)

// Declare innerDropdownButtonRefs array
const innerDropdownButtonRefs = ref<Array<HTMLButtonElement | null>>([])

const toggleMainDropdown = () => {
  dropdownOpen.value = !dropdownOpen.value

  if (!dropdownOpen.value) {
    anyInnerDropdownOpen.value = false
  }
}

const toggleInnerDropdown = (item: any) => {
  item.actionDropdownVisible = !item.actionDropdownVisible
  anyInnerDropdownOpen.value = item.actionDropdownVisible
}

const updateInnerDropdownButtonRef = (index: number, el: HTMLButtonElement | null) => {
  innerDropdownButtonRefs.value[index] = el
}

const handleClickOutside = (event: MouseEvent) => {
  const isOutsideDropdown =
    dropdownContainerRef.value && !dropdownContainerRef.value.contains(event.target as Node)

  const isOutsideButton =
    dropdownButtonRef.value && !dropdownButtonRef.value.contains(event.target as Node)

  const isOutsideInnerDropdowns = innerDropdownButtonRefs.value.some(
    (ref) => ref && ref.contains(event.target as Node)
  )

  if (isOutsideDropdown && isOutsideButton && !isOutsideInnerDropdowns) {
    dropdownOpen.value = false

    // Close inner dropdowns
    dropdownItems.value.forEach((item) => {
      item.actionDropdownVisible = false
    })

    anyInnerDropdownOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})

const dropdownItems = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-01.jpg',
    href: 'javascript:void(0)',
    name: 'Craig Baptista',
    text: 'Lorem ipsum has been th...',
    message: '03',
    active: true,
    actionDropdownVisible: false,
    actionItems: [
      { label: ' View Profile' },
      { label: ' Mark As Unread' },
      { label: ' Delete Message' },
      { label: ' Block Message' }
    ]
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-02.jpg',
    href: 'javascript:void(0)',
    name: 'Maren Lipshutz',
    text: 'Lorem ipsum has been th...',
    message: '01',
    active: true,
    actionDropdownVisible: false,
    actionItems: [
      { label: ' View Profile' },
      { label: ' Mark As Unread' },
      { label: ' Delete Message' },
      { label: ' Block Message' }
    ]
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-03.jpg',
    href: 'javascript:void(0)',
    name: 'Craig Baptista',
    text: 'Lorem ipsum has been th...',
    active: false,
    actionDropdownVisible: false,
    actionItems: [
      { label: ' View Profile' },
      { label: ' Mark As Unread' },
      { label: ' Delete Message' },
      { label: ' Block Message' }
    ]
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-04.jpg',
    href: 'javascript:void(0)',
    name: 'Craig Baptista',
    text: 'Lorem ipsum has been th...',
    active: true,
    actionDropdownVisible: false,
    actionItems: [
      { label: ' View Profile' },
      { label: ' Mark As Unread' },
      { label: ' Delete Message' },
      { label: ' Block Message' }
    ]
  }
])
</script>

<template>
  <!-- ====== Dropdown ======= -->
  <section class="bg-gray-2 dark:bg-dark py-20">
    <div class="container">
      <div class="flex items-center justify-center">
        <div class="relative">
          <a
            class="relative"
            href="javascriot:void(0)"
            @click.prevent="toggleMainDropdown"
            ref="dropdownButtonRef"
          >
            <span class="absolute -top-0.5 -right-0.5 z-10 h-2 w-2 rounded-full bg-red-500">
              <span
                class="absolute -z-10 inline-flex h-full w-full animate-ping rounded-full bg-red-500 opacity-75"
              ></span>
            </span>

            <svg
              class="fill-body-color dark:fill-dark-6 duration-300 ease-in-out hover:fill-primary"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M4 5C3.45228 5 3 5.45228 3 6V18C3 18.5477 3.45228 19 4 19H20C20.5477 19 21 18.5477 21 18V6C21 5.45228 20.5477 5 20 5H4ZM1 6C1 4.34772 2.34772 3 4 3H20C21.6523 3 23 4.34772 23 6V18C23 19.6523 21.6523 21 20 21H4C2.34772 21 1 19.6523 1 18V6Z"
                fill=""
              />
              <path
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M1.18085 5.42662C1.49757 4.97417 2.1211 4.86414 2.57355 5.18085L12.0001 11.7794L21.4266 5.18085C21.8791 4.86414 22.5026 4.97417 22.8193 5.42662C23.136 5.87907 23.026 6.5026 22.5735 6.81932L12.5735 13.8193C12.2292 14.0603 11.7709 14.0603 11.4266 13.8193L1.42662 6.81932C0.974174 6.5026 0.864139 5.87907 1.18085 5.42662Z"
                fill=""
              />
            </svg>
          </a>
          <!-- Dropdown Start -->
          <div
            v-show="dropdownOpen"
            ref="dropdownContainerRef"
            class="absolute -right-[120px] mt-4 flex h-[460px] w-[290px] flex-col gap-1 rounded-lg bg-white dark:bg-dark-2 shadow-card sm:-right-[34px] sm:w-[360px]"
          >
            <div class="border-b border-stroke dark:border-dark-3 py-[22px] px-6">
              <h5 class="font-semibold text-dark dark:text-white">Message (02)</h5>
            </div>

            <ul class="no-scrollbar flex h-auto flex-col gap-2 overflow-y-auto px-4 pb-20 pt-4">
              <template v-for="(item, index) in dropdownItems" :key="index">
                <li
                  class="group relative flex cursor-pointer items-center justify-between rounded-md p-3 hover:bg-gray-2 dark:hover:bg-dark-3"
                >
                  <a class="flex items-center gap-5" :href="item.href">
                    <div
                      class="relative z-10 h-9 w-9 flex-shrink-0 rounded-full border border-primary p-1 sm:h-11 sm:w-11"
                    >
                      <img
                        :src="item.image"
                        alt="User"
                        class="h-full w-full rounded-full object-cover object-center"
                      />
                      <span
                        v-if="item.active"
                        class="absolute bottom-0 right-0 z-50 h-3.5 w-3.5 rounded-full border-2 border-white dark:border-dark-2 bg-green"
                      ></span>
                      <span
                        v-if="!item.active"
                        class="absolute bottom-0 right-0 z-50 h-3.5 w-3.5 rounded-full border-2 border-white dark:border-dark-2 bg-red"
                      ></span>
                    </div>
                    <div>
                      <h6 class="font-medium text-dark dark:text-white">{{ item.name }}</h6>
                      <p class="mt-0.5 text-sm text-body-color dark:text-dark-6">{{ item.text }}</p>
                    </div>
                  </a>

                  <div class="flex items-center gap-2">
                    <span
                      v-if="item.message"
                      class="rounded-3xl bg-primary py-1 px-2 text-xs font-semibold text-white"
                      >03</span
                    >
                    <div class="relative">
                      <button
                        @click.prevent="toggleInnerDropdown(item)"
                        :ref="($el: any) => updateInnerDropdownButtonRef(index, $el)"
                        class="flex items-center justify-center text-dark dark:text-white"
                      >
                        <svg
                          class="fill-current"
                          width="14"
                          height="14"
                          viewBox="0 0 14 14"
                          fill="none"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <g clip-path="url(#clip0_4662_3241)">
                            <path
                              d="M8.75 12.25C8.75 11.2835 7.9665 10.5 7 10.5C6.0335 10.5 5.25 11.2835 5.25 12.25C5.25 13.2165 6.0335 14 7 14C7.9665 14 8.75 13.2165 8.75 12.25Z"
                              fill=""
                            />
                            <path
                              d="M8.75 7C8.75 6.0335 7.9665 5.25 7 5.25C6.0335 5.25 5.25 6.0335 5.25 7C5.25 7.9665 6.0335 8.75 7 8.75C7.9665 8.75 8.75 7.9665 8.75 7Z"
                              fill=""
                            />
                            <path
                              d="M8.75 1.75C8.75 0.783502 7.9665 1.19677e-07 7 1.61924e-07C6.0335 2.04171e-07 5.25 0.783502 5.25 1.75C5.25 2.7165 6.0335 3.5 7 3.5C7.9665 3.5 8.75 2.7165 8.75 1.75Z"
                              fill=""
                            />
                          </g>
                          <defs>
                            <clipPath id="clip0_4662_3241">
                              <rect
                                width="14"
                                height="14"
                                fill="white"
                                transform="translate(0 14) rotate(-90)"
                              />
                            </clipPath>
                          </defs>
                        </svg>
                      </button>
                      <div
                        class="absolute right-0 top-full z-[999] mt-5 w-40 space-y-1 rounded border border-stroke dark:border-dark-3 bg-white dark:bg-dark-2 p-2 shadow group-last:bottom-full group-last:top-auto group-last:mb-5"
                        v-show="item.actionDropdownVisible"
                      >
                        <template
                          v-for="(actionItem, actionIndex) in item.actionItems"
                          :key="actionIndex"
                        >
                          <button
                            class="w-full rounded py-2 px-3 text-left text-dark dark:text-white text-sm hover:bg-gray-2 dark:hover:bg-dark"
                          >
                            {{ actionItem.label }}
                          </button>
                        </template>
                      </div>
                    </div>
                  </div>
                </li>
              </template>
            </ul>
            <div
              class="absolute bottom-0 z-50 w-full rounded-b-lg border-t border-stroke dark:border-dark-3 bg-white dark:bg-dark-2 p-3"
            >
              <a
                href="javascript:void(0)"
                class="flex items-center justify-center rounded-md bg-primary p-2 font-medium text-white hover:bg-blue-dark"
              >
                View All Message
              </a>
            </div>
          </div>
          <!-- Dropdown End -->
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Dropdown ======= -->
</template>
