<script setup lang="ts">
import { ref } from 'vue'

const avatarItems = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-01.jpg'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-02.jpg'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-03.jpg'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-04.jpg'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-05.jpg'
  }
])
</script>

<template>
  <!-- ====== Avatars Section Start -->
  <section class="bg-white dark:bg-dark py-[75px]">
    <div class="mx-auto px-4 sm:container">
      <div class="flex items-end justify-center">
        <template v-for="(item, index) in avatarItems" :key="index">
          <div class="-ml-4 h-[50px] w-[50px] rounded-full border-4 border-white dark:border-dark-3">
            <img
              :src="item.image"
              alt="avatar"
              class="h-full w-full rounded-full object-cover object-center"
            />
          </div>
        </template>
      </div>
    </div>
  </section>
  <!-- ====== Avatars Section End -->
</template>
