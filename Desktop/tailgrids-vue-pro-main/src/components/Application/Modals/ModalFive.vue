<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'

const modalOpen = ref(false)
const modalContainer = ref<HTMLElement | null>(null)
const trigger = ref<HTMLButtonElement | null>(null)

const setModalOpen = (value: boolean): void => {
  modalOpen.value = value
}

const handleClickOutside = (event: MouseEvent): void => {
  if (
    modalContainer.value &&
    trigger.value &&
    !modalContainer.value.contains(event.target as Node) &&
    event.target !== trigger.value
  ) {
    setModalOpen(false)
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
  <div class="container mx-auto py-20">
    <button
      ref="trigger"
      @click="setModalOpen(true)"
      class="rounded-full bg-primary px-6 py-3 text-base font-medium text-white"
    >
      Open Modal
    </button>
    <div
      class="fixed top-0 left-0 flex items-center justify-center w-full h-screen py-10 overflow-y-scroll bg-gray-2 dark:bg-dark"
      :class="{ block: modalOpen, hidden: !modalOpen }"
    >
      <div
        ref="modalContainer"
        class="mx-auto max-w-[560px] rounded-[10px] bg-white dark:bg-dark-2 p-8 shadow-1 dark:shadow-3"
      >
        <h3 class="flex mb-5 text-lg font-semibold text-dark dark:text-white sm:text-xl">
          <span class="inline-block pr-[10px]">
            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <g clip-path="url(#clip0_2095_7581)">
                <path
                  d="M12 0.674988C5.73749 0.674988 0.674988 5.73749 0.674988 12C0.674988 18.2625 5.73749 23.3625 12 23.3625C18.2625 23.3625 23.3625 18.2625 23.3625 12C23.3625 5.73749 18.2625 0.674988 12 0.674988ZM12 21.675C6.67499 21.675 2.36249 17.325 2.36249 12C2.36249 6.67499 6.67499 2.36249 12 2.36249C17.325 2.36249 21.675 6.71249 21.675 12.0375C21.675 17.325 17.325 21.675 12 21.675Z"
                  fill="#F27430"
                />
                <path
                  d="M13.5 10.2H10.5C10.05 10.2 9.63751 10.575 9.63751 11.0625V18.5625C9.63751 19.0125 10.0125 19.425 10.5 19.425H13.5C13.95 19.425 14.3625 19.05 14.3625 18.5625V11.0625C14.3625 10.575 13.95 10.2 13.5 10.2ZM12.675 17.7H11.3625V11.8875H12.675V17.7Z"
                  fill="#F27430"
                />
                <path
                  d="M12 4.61249C10.725 4.61249 9.63751 5.66249 9.63751 6.97499C9.63751 8.28749 10.6875 9.33749 12 9.33749C13.3125 9.33749 14.3625 8.28749 14.3625 6.97499C14.3625 5.66249 13.275 4.61249 12 4.61249ZM12 7.61249C11.625 7.61249 11.325 7.31249 11.325 6.93749C11.325 6.56249 11.625 6.26249 12 6.26249C12.375 6.26249 12.675 6.56249 12.675 6.93749C12.675 7.31249 12.375 7.61249 12 7.61249Z"
                  fill="#F27430"
                />
              </g>
              <defs>
                <clipPath id="clip0_2095_7581">
                  <rect width="24" height="24" fill="white" />
                </clipPath>
              </defs>
            </svg>
          </span>
          Are you sure you want to submit?
        </h3>
        <p class="text-sm mb-7 dark:text-dark-6 text-body-color">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean quis bibendum purus.
          Aliquam nec ipsum commodo ligula tristique scelerisque sed sed enim. Suspendisse varius
          libero just.
        </p>
        <div class="flex items-center justify-end space-x-1">
          <button
            @click="setModalOpen(false)"
            class="px-5 py-2 text-sm font-medium bg-white rounded-md text-dark shadow-1 dark:shadow-3 hover:text-white hover:bg-red-dark dark:text-white dark:bg-white/5"
          >
            Cancel
          </button>
          <button
            class="px-5 py-2 text-sm font-medium text-white rounded-md bg-primary hover:bg-opacity-90"
          >
            Submit
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
