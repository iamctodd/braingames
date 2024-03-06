<script setup lang="ts">
import { ref } from 'vue'

const avatarItems = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-01.jpg',
    size: '24px',
    bulletSize: '7px',
    bulletPosition: '-2px'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-02.jpg',
    size: '38px',
    bulletSize: '12px',
    bulletPosition: '-4px'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-03.jpg',
    size: '42px',
    bulletSize: '13px',
    bulletPosition: '-6px'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-04.jpg',
    size: '52px',
    bulletSize: '15px',
    bulletPosition: '-6px'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/dashboard/images/avatar/image-05.jpg',
    size: '80px',
    bulletSize: '18px',
    bulletPosition: '-8px'
  }
])
</script>

<template>
  <!-- ====== Avatars Section Start -->
  <section class="bg-white dark:bg-dark py-[75px]">
    <div class="mx-auto px-4 sm:container">
      <div class="flex items-end justify-center space-x-2 sm:space-x-5">
        <template v-for="(item, index) in avatarItems" :key="index">
          <div class="relative rounded-[15px]" :class="{'rounded-lg' : index === 0}" :style="{ width: item.size, height: item.size }">
            <img
              :src="item.image"
              alt="avatar"
              class="h-full w-full rounded-[15px] object-cover object-center"
              :class="{'rounded-lg' : index === 0}"
            />
            <span
               class="absolute block rounded-full border-[2.7px] border-white dark:border-dark bg-[#219653]"
               :style="{ width: item.bulletSize, height: item.bulletSize, top: item.bulletPosition, right: item.bulletPosition }"
               ></span>
          </div>
        </template>
      </div>
    </div>
  </section>
  <!-- ====== Avatars Section End -->
</template>
