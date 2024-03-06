<script setup lang="ts">
import Swiper from 'swiper'
import { onMounted, onUnmounted, ref, watch } from 'vue'

const swiper = ref<Swiper | null>(null) as { value?: Swiper }
const swiperContainer = ref<HTMLElement | null>(null)

onMounted(() => {
  initSwiper()
})

watch(swiperContainer, () => {
  initSwiper()
})

const initSwiper = () => {
  if (swiperContainer.value && !swiper.value) {
    swiper.value = new Swiper(swiperContainer.value, {
      breakpoints: {
        640: { width: 640, slidesPerView: 1 },
        768: { width: 768, slidesPerView: 2.2 },
        1024: { width: 1024, slidesPerView: 2.2 },
        1280: { width: 1280, slidesPerView: 3 }
      },
      loop: true,
      spaceBetween: 30
    } as any)
  }
}

onUnmounted(() => {
  if (swiper.value) {
    swiper.value.destroy()
  }
})

const onPrevClick = () => {
  swiper?.value?.slidePrev()
}

const onNextClick = () => {
  swiper?.value?.slideNext()
}

interface TestimonialItem {
  image: string
  name: string
  position: string
  details: string
}

const testimonialItems = ref<TestimonialItem[]>([
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/testimonials/testimonial-04/image-01.png',
    name: 'Sabo Masties',
    position: 'Founder @ Rolex',
    details: `Our members are so impressed. It's intuitive. It's clean. It's distraction free. If you're building a community.`
  },
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/testimonials/testimonial-04/image-02.png',
    name: 'Musharof Chowdhury',
    position: 'Founder @ Ayro UI',
    details: `Our members are so impressed. It's intuitive. It's clean. It's distraction free. If you're building a community.`
  },
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/testimonials/testimonial-04/image-03.png',
    name: 'William Smith',
    position: 'Founder @ Trorex',
    details: `Our members are so impressed. It's intuitive. It's clean. It's distraction free. If you're building a community.`
  },
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/testimonials/testimonial-04/image-01.png',
    name: 'Sabo Masties',
    position: 'Founder @ Rolex',
    details: `Our members are so impressed. It's intuitive. It's clean. It's distraction free. If you're building a community.`
  },
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/testimonials/testimonial-04/image-02.png',
    name: 'Musharof Chowdhury',
    position: 'Founder @ Ayro UI',
    details: `Our members are so impressed. It's intuitive. It's clean. It's distraction free. If you're building a community.`
  },
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/testimonials/testimonial-04/image-03.png',
    name: 'William Smith',
    position: 'Founder @ Trorex',
    details: `Our members are so impressed. It's intuitive. It's clean. It's distraction free. If you're building a community.`
  }
])
</script>

<template>
  <!-- ====== Testimonials Section Start -->
  <section class="pt-20 pb-10 lg:pt-[120px] lg:pb-20 dark:bg-dark">
    <div class="container mx-auto relative overflow-hidden">
      <div class="flex flex-wrap justify-center -mx-4">
        <div class="w-full px-4">
          <div class="mx-auto mb-[60px] max-w-[510px] text-center">
            <span class="block mb-2 text-lg font-semibold text-primary"> Testimonials </span>
            <h2
              class="text-dark dark:text-white mb-3 text-3xl leading-[1.2] font-bold sm:text-4xl md:text-[40px]"
            >
              What our Clients Says
            </h2>
            <p class="text-base text-body-color dark:text-dark-6">
              There are many variations of passages of Lorem Ipsum available but the majority have
              suffered alteration in some form.
            </p>
          </div>
        </div>
      </div>

      <div class="swiper-container" ref="swiperContainer">
        <div class="swiper-wrapper">
          <template v-for="(item, index) in testimonialItems" :key="index">
            <div class="swiper-slide">
              <div class="relative flex justify-center">
                <div class="relative w-full pb-16">
                  <div
                    class="mb-10 bg-white p-8 shadow-testimonial-5 dark:bg-dark-2 dark:shadow-box-dark lg:px-6 lg:py-8 xl:p-8"
                  >
                    <div class="mb-5 flex items-center gap-1">
                      <span v-for="index in 5" :key="index">
                        <svg
                          width="18"
                          height="16"
                          viewBox="0 0 18 16"
                          fill="none"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <path
                            d="M9.09815 0.360596L11.1054 6.06493H17.601L12.3459 9.5904L14.3532 15.2947L9.09815 11.7693L3.84309 15.2947L5.85035 9.5904L0.595291 6.06493H7.0909L9.09815 0.360596Z"
                            fill="#FBB040"
                          />
                        </svg>
                      </span>
                    </div>

                    <p class="mb-6 text-base text-body-color dark:text-dark-6">
                      {{ item.details }}
                    </p>

                    <div class="flex items-center">
                      <div class="mr-4 h-[50px] w-full max-w-[50px]">
                        <img :src="item.image" alt="testimonial" class="w-full" />
                      </div>

                      <div class="w-full">
                        <h5 class="mb-0.5 text-sm font-semibold text-dark dark:text-white">
                          {{ item.name }}
                        </h5>
                        <p class="text-xs text-secondary-color dark:text-dark-6">
                          {{ item.position }}
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </div>

        <div class="absolute z-10 bottom-0 left-0 right-0 flex items-center justify-center gap-3">
          <div class="prev-arrow cursor-pointer">
            <button
              @click="onPrevClick"
              class="flex h-12 w-12 items-center justify-center bg-white text-dark shadow-btn-3 transition-all hover:bg-primary hover:text-white dark:bg-dark-2 dark:text-white dark:shadow-none"
            >
              <svg
                width="22"
                height="22"
                viewBox="0 0 22 22"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
                class="fill-current"
              >
                <path
                  d="M19.25 10.2437H4.57187L10.4156 4.29687C10.725 3.9875 10.725 3.50625 10.4156 3.19687C10.1062 2.8875 9.625 2.8875 9.31562 3.19687L2.2 10.4156C1.89062 10.725 1.89062 11.2063 2.2 11.5156L9.31562 18.7344C9.45312 18.8719 9.65937 18.975 9.86562 18.975C10.0719 18.975 10.2437 18.9062 10.4156 18.7687C10.725 18.4594 10.725 17.9781 10.4156 17.6688L4.60625 11.7906H19.25C19.6625 11.7906 20.0063 11.4469 20.0063 11.0344C20.0063 10.5875 19.6625 10.2437 19.25 10.2437Z"
                  fill=""
                />
              </svg>
            </button>
          </div>
          <div class="next-arrow cursor-pointer">
            <button
              @click="onNextClick"
              class="flex h-12 w-12 items-center justify-center bg-white text-dark shadow-btn-3 transition-all hover:bg-primary hover:text-white dark:bg-dark-2 dark:text-white dark:shadow-none"
            >
              <svg
                width="22"
                height="22"
                viewBox="0 0 22 22"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
                class="fill-current"
              >
                <path
                  d="M19.8 10.45L12.6844 3.23124C12.375 2.92186 11.8938 2.92186 11.5844 3.23124C11.275 3.54061 11.275 4.02186 11.5844 4.33124L17.3594 10.2094H2.75C2.3375 10.2094 1.99375 10.5531 1.99375 10.9656C1.99375 11.3781 2.3375 11.7562 2.75 11.7562H17.4281L11.5844 17.7031C11.275 18.0125 11.275 18.4937 11.5844 18.8031C11.7219 18.9406 11.9281 19.0094 12.1344 19.0094C12.3406 19.0094 12.5469 18.9406 12.6844 18.7687L19.8 11.55C20.1094 11.2406 20.1094 10.7594 19.8 10.45Z"
                  fill="white"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Testimonials Section End -->
</template>
