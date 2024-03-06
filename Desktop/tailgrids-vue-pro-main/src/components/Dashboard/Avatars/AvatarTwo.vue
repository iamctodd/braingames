<script setup lang="ts">
import { ref } from 'vue'

const avatarItems = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-01.jpg',
    size: '24px'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-02.jpg',
    size: '38px'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-03.jpg',
    size: '42px'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-04.jpg',
    size: '52px'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-05.jpg',
    size: '80px'
  }
])
</script>

<template>
  <!-- ====== Avatars Section Start -->
  <section class="bg-white dark:bg-dark py-[75px]">
    <div class="mx-auto px-4 sm:container">
      <div class="flex items-end justify-center space-x-2 sm:space-x-5">
        <template v-for="(item, index) in avatarItems" :key="index">
          <div :style="{ width: item.size, height: item.size }">
            <img
              :src="item.image"
              alt="avatar"
              class="h-full w-full object-cover object-center"
            />
          </div>
        </template>
      </div>
    </div>
  </section>
  <!-- ====== Avatars Section End -->
</template>
