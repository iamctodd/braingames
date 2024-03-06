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
      class="fixed top-0 left-0 flex items-center justify-center w-full h-full min-h-screen px-4 py-5 bg-dark/90"
      :class="{ block: modalOpen, hidden: !modalOpen }"
    >
      <div
        ref="modalContainer"
        class="w-full max-w-[570px] rounded-[20px] bg-white dark:bg-dark-2 py-12 px-8 text-center md:py-[50px] md:px-[70px]"
      >
        <div
            class="mx-auto mb-5 flex h-[60px] w-[60px] items-center justify-center rounded-full bg-red-light-5 text-red-dark"
            >
            <svg
               width="24"
               height="24"
               viewBox="0 0 24 24"
               fill="none"
               xmlns="http://www.w3.org/2000/svg"
               >
               <path
                  d="M22.6875 15.4875L14.6625 2.57498C14.025 1.71248 13.05 1.22498 12 1.22498C10.9125 1.22498 9.93753 1.71248 9.33753 2.57498L1.31253 15.4875C0.562527 16.5 0.450027 17.8125 1.01253 18.9375C1.57503 20.0625 2.70003 20.775 3.97503 20.775H20.025C21.3 20.775 22.425 20.0625 22.9875 18.9375C23.55 17.85 23.4375 16.5 22.6875 15.4875ZM21.4875 18.1875C21.1875 18.75 20.6625 19.0875 20.025 19.0875H3.97503C3.33753 19.0875 2.81253 18.75 2.51253 18.1875C2.25003 17.625 2.28753 16.9875 2.66253 16.5L10.6875 3.58748C10.9875 3.17498 11.475 2.91248 12 2.91248C12.525 2.91248 13.0125 3.13748 13.3125 3.58748L21.3375 16.5C21.7125 16.9875 21.75 17.625 21.4875 18.1875Z"
                  fill="currentColor"
                  />
               <path
                  d="M12 8.20001C11.55 8.20001 11.1375 8.57501 11.1375 9.06251V13.15C11.1375 13.6 11.5125 14.0125 12 14.0125C12.4875 14.0125 12.8625 13.6375 12.8625 13.15V9.02501C12.8625 8.57501 12.45 8.20001 12 8.20001Z"
                  fill="currentColor"
                  />
               <path
                  d="M12 15C11.55 15 11.1375 15.375 11.1375 15.8625V16.05C11.1375 16.5 11.5125 16.9125 12 16.9125C12.4875 16.9125 12.8625 16.5375 12.8625 16.05V15.825C12.8625 15.375 12.45 15 12 15Z"
                  fill="currentColor"
                  />
            </svg>
         </div>
         <h3
            class="pb-4 text-xl font-bold text-dark dark:text-white sm:text-2xl"
            >
            Deactivate Your Account
         </h3>
         <p
            class="text-base leading-relaxed mb-9 text-body-color dark:text-dark-6"
            >
            Lorem Ipsum is simply dummy text of the printing and typesetting
            industry Lorem Ipsum been.
         </p>
        <div class="-mx-3 flex flex-wrap">
          <div class="w-1/2 px-3">
            <button
              @click="setModalOpen(false)"
              class="block w-full p-3 text-base font-medium text-center transition border rounded-md border-stroke text-dark hover:border-red-dark hover:bg-red-dark hover:text-white dark:text-white"
            >
              Cancel
            </button>
          </div>
          <div class="w-1/2 px-3">
            <button
              class="block w-full p-3 text-base font-medium text-center text-white transition border rounded-md border-red-dark bg-red-dark hover:bg-red-dark/90"
            >
              <a href="/">Deactivate</a>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
