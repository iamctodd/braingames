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
      class="fixed top-0 left-0 w-full h-screen py-10 overflow-y-scroll bg-white dark:bg-dark"
      :class="{ block: modalOpen, hidden: !modalOpen }"
    >
      <div
        ref="modalContainer"
        class="mx-auto max-w-[465px] rounded-[10px] bg-white dark:bg-dark-2 p-8 shadow-1 dark:shadow-three"
      >
        <div class="overflow-hidden border rounded-md mb-9 border-stroke dark:border-dark-3">
          <img
            src="https://cdn.tailgrids.com/2.0/image/application/images/modals/image-01.svg"
            alt="modal image"
            class="w-full"
          />
        </div>

        <div class="text-center">
          <h3 class="mb-2.5 text-2xl font-semibold text-dark dark:text-white sm:text-[28px]">
            Access has been requested
          </h3>
          <p class="mb-6 text-base text-body-color dark:text-dark-6">
            Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum
            been.
          </p>
          <div class="mb-9 flex items-center justify-center space-x-[14px]">
            <span
              class="block w-3 h-3 rounded-full cursor-pointer bg-primary hover:bg-primary"
            ></span>
            <span
              class="block h-3 w-3 cursor-pointer rounded-full bg-[#DAE6FF] hover:bg-primary"
            ></span>
            <span
              class="block h-3 w-3 cursor-pointer rounded-full bg-[#DAE6FF] hover:bg-primary"
            ></span>
          </div>
          <div class="flex items-center space-x-4">
            <button
              @click="setModalOpen(false)"
              class="w-full h-12 text-base font-medium text-center bg-white rounded-md text-body-color shadow-1 hover:bg-gray-2 dark:shadow-3 dark:bg-white/5 dark:text-white dark:hover:bg-white/10"
            >
              Skip
            </button>
            <button
              class="w-full h-12 text-base font-medium text-center text-white rounded-md bg-primary hover:bg-opacity-90"
            >
              Next
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
