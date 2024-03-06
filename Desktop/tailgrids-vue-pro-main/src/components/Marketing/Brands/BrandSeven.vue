<script setup lang="ts">
import { ref } from 'vue'

const brandItems = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/assets/images/brands/graygrids-white.svg',
    link: '#'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/assets/images/brands/lineIcons-white.svg',
    link: '#'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/assets/images/brands/ayroui-white.svg',
    link: '#'
  }
])
</script>

<template>
  <!-- ====== Brands Section Start -->
  <section class="bg-primary relative z-10 py-20 lg:py-[120px]">
    <div class="container mx-auto">
      <div class="flex flex-wrap items-center -mx-4">
        <div class="w-full px-4 lg:w-1/2 xl:w-5/12">
          <div>
            <h2
              class="text-3xl font-bold text-white sm:text-4xl lg:text-3xl xl:text-[33px] 2xl:text-4xl"
            >
              Tailwind CSS UI Components for Modern Web Apps
            </h2>
          </div>
        </div>

        <div class="w-full px-4 lg:w-1/2 xl:w-7/12">
          <div class="mt-12 flex flex-wrap items-center justify-center lg:mt-0 xl:justify-end">
            <template v-for="(item, index) in brandItems" :key="index">
              <a
                :href="item.link"
                class="mx-4 flex min-w-[150px] max-w-[200px] items-center justify-center py-5 lg:min-w-min lg:max-w-[110px] xl:max-w-[200px]"
              >
                <img :src="item.image" alt="image" class="h-10 w-full" />
              </a>
            </template>
          </div>
        </div>
      </div>
    </div>

    <div>
      <span class="absolute top-4 left-4 z-[-1]">
        <svg
          width="50"
          height="49"
          viewBox="0 0 50 49"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <circle
            cx="47.7119"
            cy="46.3164"
            r="1.74121"
            transform="rotate(180 47.7119 46.3164)"
            fill="white"
          />
          <circle
            cx="47.7119"
            cy="16.7161"
            r="1.74121"
            transform="rotate(180 47.7119 16.7161)"
            fill="white"
          />
          <circle
            cx="47.7119"
            cy="31.3423"
            r="1.74121"
            transform="rotate(180 47.7119 31.3423)"
            fill="white"
          />
          <circle
            cx="47.7119"
            cy="1.74121"
            r="1.74121"
            transform="rotate(180 47.7119 1.74121)"
            fill="white"
          />
          <circle
            cx="32.3916"
            cy="46.3162"
            r="1.74121"
            transform="rotate(180 32.3916 46.3162)"
            fill="white"
          />
          <circle
            cx="32.3916"
            cy="16.7161"
            r="1.74121"
            transform="rotate(180 32.3916 16.7161)"
            fill="white"
          />
          <circle
            cx="32.3916"
            cy="31.342"
            r="1.74121"
            transform="rotate(180 32.3916 31.342)"
            fill="white"
          />
          <circle
            cx="32.3916"
            cy="1.74145"
            r="1.74121"
            transform="rotate(180 32.3916 1.74145)"
            fill="white"
          />
          <circle
            cx="17.0674"
            cy="46.3162"
            r="1.74121"
            transform="rotate(180 17.0674 46.3162)"
            fill="white"
          />
          <circle
            cx="17.0674"
            cy="16.7161"
            r="1.74121"
            transform="rotate(180 17.0674 16.7161)"
            fill="white"
          />
          <circle
            cx="17.0674"
            cy="31.342"
            r="1.74121"
            transform="rotate(180 17.0674 31.342)"
            fill="white"
          />
          <circle
            cx="17.0674"
            cy="1.74145"
            r="1.74121"
            transform="rotate(180 17.0674 1.74145)"
            fill="white"
          />
          <circle
            cx="1.74316"
            cy="46.3162"
            r="1.74121"
            transform="rotate(180 1.74316 46.3162)"
            fill="white"
          />
          <circle
            cx="1.74316"
            cy="16.7161"
            r="1.74121"
            transform="rotate(180 1.74316 16.7161)"
            fill="white"
          />
          <circle
            cx="1.74316"
            cy="31.342"
            r="1.74121"
            transform="rotate(180 1.74316 31.342)"
            fill="white"
          />
          <circle
            cx="1.74316"
            cy="1.74145"
            r="1.74121"
            transform="rotate(180 1.74316 1.74145)"
            fill="white"
          />
        </svg>
      </span>
      <span class="absolute bottom-4 right-4 z-[-1]">
        <svg
          width="50"
          height="49"
          viewBox="0 0 50 49"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <circle
            cx="47.7119"
            cy="46.3164"
            r="1.74121"
            transform="rotate(180 47.7119 46.3164)"
            fill="white"
          />
          <circle
            cx="47.7119"
            cy="16.7161"
            r="1.74121"
            transform="rotate(180 47.7119 16.7161)"
            fill="white"
          />
          <circle
            cx="47.7119"
            cy="31.3423"
            r="1.74121"
            transform="rotate(180 47.7119 31.3423)"
            fill="white"
          />
          <circle
            cx="47.7119"
            cy="1.74121"
            r="1.74121"
            transform="rotate(180 47.7119 1.74121)"
            fill="white"
          />
          <circle
            cx="32.3916"
            cy="46.3162"
            r="1.74121"
            transform="rotate(180 32.3916 46.3162)"
            fill="white"
          />
          <circle
            cx="32.3916"
            cy="16.7161"
            r="1.74121"
            transform="rotate(180 32.3916 16.7161)"
            fill="white"
          />
          <circle
            cx="32.3916"
            cy="31.342"
            r="1.74121"
            transform="rotate(180 32.3916 31.342)"
            fill="white"
          />
          <circle
            cx="32.3916"
            cy="1.74145"
            r="1.74121"
            transform="rotate(180 32.3916 1.74145)"
            fill="white"
          />
          <circle
            cx="17.0674"
            cy="46.3162"
            r="1.74121"
            transform="rotate(180 17.0674 46.3162)"
            fill="white"
          />
          <circle
            cx="17.0674"
            cy="16.7161"
            r="1.74121"
            transform="rotate(180 17.0674 16.7161)"
            fill="white"
          />
          <circle
            cx="17.0674"
            cy="31.342"
            r="1.74121"
            transform="rotate(180 17.0674 31.342)"
            fill="white"
          />
          <circle
            cx="17.0674"
            cy="1.74145"
            r="1.74121"
            transform="rotate(180 17.0674 1.74145)"
            fill="white"
          />
          <circle
            cx="1.74316"
            cy="46.3162"
            r="1.74121"
            transform="rotate(180 1.74316 46.3162)"
            fill="white"
          />
          <circle
            cx="1.74316"
            cy="16.7161"
            r="1.74121"
            transform="rotate(180 1.74316 16.7161)"
            fill="white"
          />
          <circle
            cx="1.74316"
            cy="31.342"
            r="1.74121"
            transform="rotate(180 1.74316 31.342)"
            fill="white"
          />
          <circle
            cx="1.74316"
            cy="1.74145"
            r="1.74121"
            transform="rotate(180 1.74316 1.74145)"
            fill="white"
          />
        </svg>
      </span>
    </div>
  </section>
  <!-- ====== Brands Section End -->
</template>
