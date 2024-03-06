<script setup lang="ts">
import Swiper from 'swiper/bundle'
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
      slidesPerView: 1,
      pagination: {
        el: '.swiper-pagination',
        clickable: true
      }
    } as any)
  }
}

onUnmounted(() => {
  if (swiper.value) {
    swiper.value.destroy()
  }
})

interface TestimonialItem {
  image: string
  name: string
  position: string
  details: string
}

const testimonialItems = ref<TestimonialItem[]>([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/marketing/images/testimonials/testimonial-03/image-02.png',
    name: 'Healther Bennit',
    position: 'Founder - Dailousm',
    details: `Lorem Ipsum available, but the majority have suffered alteration in some form, injected humour, or randomised words which don't look slightly believable, If you are to passage.`
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/marketing/images/testimonials/testimonial-03/image-01.png',
    name: 'Kamala Harish',
    position: 'Founder - ProductHunt',
    details: `Lorem Ipsum available, but the majority have suffered alteration in some form, injected humour, or randomised words which don't look slightly believable, If you are to passage.`
  }
])
</script>

<style>
.swiper-pagination {
  bottom: -5px !important;
}
.swiper-pagination-bullet {
  margin: 0 16px !important;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: #d0d4e1;
  opacity: 1;
  transition: all 0.3s ease-in-out;
}
.swiper-pagination-bullet:hover {
  background-color: #13c296;
}
.swiper-pagination-bullet.swiper-pagination-bullet-active {
  background-color: #13c296;
}
</style>

<template>
  <!-- ====== Testimonials Section Start -->
  <section class="pb-20 pt-20 dark:bg-dark lg:pb-[120px] lg:pt-[120px]">
    <div class="container mx-auto">
      <div class="-mx-4 flex flex-wrap justify-center">
        <div class="w-full px-4">
          <div class="mx-auto mb-[60px] max-w-[510px] text-center lg:mb-20">
            <span class="text-primary mb-2 block text-lg font-semibold"> What People Says </span>
            <h2
              class="text-dark dark:text-white mb-3 text-3xl leading-[1.2] font-bold sm:text-4xl md:text-[40px]"
            >
              Client Testimonials
            </h2>
            <p class="text-body-color text-base dark:text-dark-6">
              There are many variations of passages of Lorem Ipsum available but the majority have
              suffered alteration in some form.
            </p>
          </div>
        </div>
      </div>

      <div class="-mx-4 flex flex-wrap justify-center">
        <div class="w-full px-4 lg:w-10/12 xl:w-8/12 2xl:w-7/12">
          <div class="swiper-container swiper !pb-8" ref="swiperContainer">
            <div class="swiper-wrapper">
              <template v-for="(item, index) in testimonialItems" :key="index">
                <div class="swiper-slide py-7 px-5">
                  <div
                    class="relative items-center rounded-lg bg-[#F8F9FF] dark:bg-dark-2 py-10 px-10 md:flex lg:px-[70px]"
                  >
                    <div
                      class="relative z-10 mb-12 h-[165px] w-full max-w-[165px] rounded-full md:mb-0"
                    >
                      <img :src="item.image" alt="image" class="w-full rounded-full" />
                      <div class="absolute left-0 top-0 z-[-1]">
                        <svg
                          width="160"
                          height="160"
                          viewBox="0 0 160 160"
                          fill="none"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <rect
                            x="-6.88525"
                            y="18.9728"
                            width="36.731"
                            height="209.602"
                            rx="18.3655"
                            transform="rotate(-45 -6.88525 18.9728)"
                            fill="#13C296"
                          />
                        </svg>
                      </div>
                      <div class="absolute -left-2 top-5 z-[-2]">
                        <svg
                          width="152"
                          height="152"
                          viewBox="0 0 152 152"
                          fill="none"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <rect
                            x="-5"
                            y="12.5433"
                            width="24.9386"
                            height="204.237"
                            rx="12.4693"
                            transform="rotate(-45 -5 12.5433)"
                            fill="#3758F9"
                          />
                        </svg>
                      </div>
                    </div>
                    <div class="w-full pl-0 md:pl-14">
                      <p class="text-body-color dark:text-dark-6 mb-6 text-base">
                        {{ item.details }}
                      </p>
                      <h4 class="text-primary mb-1 text-lg font-semibold"> {{ item.name }}</h4>
                      <h6 class="text-body-color dark:text-dark-6 text-sm font-normal italic">
                        {{ item.position }}
                      </h6>
                    </div>
                    <div>
                      <span class="absolute -left-5 -bottom-5 z-[-1]">
                        <svg
                          width="77"
                          height="77"
                          viewBox="0 0 77 77"
                          fill="none"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <circle
                            cx="1.66343"
                            cy="74.5221"
                            r="1.66343"
                            transform="rotate(-90 1.66343 74.5221)"
                            fill="#13C296"
                          />
                          <circle
                            cx="1.66343"
                            cy="30.94"
                            r="1.66343"
                            transform="rotate(-90 1.66343 30.94)"
                            fill="#13C296"
                          />
                          <circle
                            cx="16.3016"
                            cy="74.5221"
                            r="1.66343"
                            transform="rotate(-90 16.3016 74.5221)"
                            fill="#13C296"
                          />
                          <circle
                            cx="16.3016"
                            cy="30.94"
                            r="1.66343"
                            transform="rotate(-90 16.3016 30.94)"
                            fill="#13C296"
                          />
                          <circle
                            cx="30.9398"
                            cy="74.5221"
                            r="1.66343"
                            transform="rotate(-90 30.9398 74.5221)"
                            fill="#13C296"
                          />
                          <circle
                            cx="30.9398"
                            cy="30.94"
                            r="1.66343"
                            transform="rotate(-90 30.9398 30.94)"
                            fill="#13C296"
                          />
                          <circle
                            cx="45.578"
                            cy="74.5221"
                            r="1.66343"
                            transform="rotate(-90 45.578 74.5221)"
                            fill="#13C296"
                          />
                          <circle
                            cx="45.578"
                            cy="30.94"
                            r="1.66343"
                            transform="rotate(-90 45.578 30.94)"
                            fill="#13C296"
                          />
                          <circle
                            cx="60.2162"
                            cy="74.5216"
                            r="1.66343"
                            transform="rotate(-90 60.2162 74.5216)"
                            fill="#13C296"
                          />
                          <circle
                            cx="74.6634"
                            cy="74.5216"
                            r="1.66343"
                            transform="rotate(-90 74.6634 74.5216)"
                            fill="#13C296"
                          />
                          <circle
                            cx="60.2162"
                            cy="30.9398"
                            r="1.66343"
                            transform="rotate(-90 60.2162 30.9398)"
                            fill="#13C296"
                          />
                          <circle
                            cx="74.6634"
                            cy="30.9398"
                            r="1.66343"
                            transform="rotate(-90 74.6634 30.9398)"
                            fill="#13C296"
                          />
                          <circle
                            cx="1.66343"
                            cy="59.8839"
                            r="1.66343"
                            transform="rotate(-90 1.66343 59.8839)"
                            fill="#13C296"
                          />
                          <circle
                            cx="1.66343"
                            cy="16.3017"
                            r="1.66343"
                            transform="rotate(-90 1.66343 16.3017)"
                            fill="#13C296"
                          />
                          <circle
                            cx="16.3016"
                            cy="59.8839"
                            r="1.66343"
                            transform="rotate(-90 16.3016 59.8839)"
                            fill="#13C296"
                          />
                          <circle
                            cx="16.3016"
                            cy="16.3018"
                            r="1.66343"
                            transform="rotate(-90 16.3016 16.3018)"
                            fill="#13C296"
                          />
                          <circle
                            cx="30.9398"
                            cy="59.8839"
                            r="1.66343"
                            transform="rotate(-90 30.9398 59.8839)"
                            fill="#13C296"
                          />
                          <circle
                            cx="30.9398"
                            cy="16.3018"
                            r="1.66343"
                            transform="rotate(-90 30.9398 16.3018)"
                            fill="#13C296"
                          />
                          <circle
                            cx="45.578"
                            cy="59.8839"
                            r="1.66343"
                            transform="rotate(-90 45.578 59.8839)"
                            fill="#13C296"
                          />
                          <circle
                            cx="45.578"
                            cy="16.3018"
                            r="1.66343"
                            transform="rotate(-90 45.578 16.3018)"
                            fill="#13C296"
                          />
                          <circle
                            cx="60.2162"
                            cy="59.8839"
                            r="1.66343"
                            transform="rotate(-90 60.2162 59.8839)"
                            fill="#13C296"
                          />
                          <circle
                            cx="74.6634"
                            cy="59.8839"
                            r="1.66343"
                            transform="rotate(-90 74.6634 59.8839)"
                            fill="#13C296"
                          />
                          <circle
                            cx="60.2162"
                            cy="16.3017"
                            r="1.66343"
                            transform="rotate(-90 60.2162 16.3017)"
                            fill="#13C296"
                          />
                          <circle
                            cx="74.6634"
                            cy="16.3017"
                            r="1.66343"
                            transform="rotate(-90 74.6634 16.3017)"
                            fill="#13C296"
                          />
                          <circle
                            cx="1.66343"
                            cy="45.2455"
                            r="1.66343"
                            transform="rotate(-90 1.66343 45.2455)"
                            fill="#13C296"
                          />
                          <circle
                            cx="1.66343"
                            cy="1.66347"
                            r="1.66343"
                            transform="rotate(-90 1.66343 1.66347)"
                            fill="#13C296"
                          />
                          <circle
                            cx="16.3016"
                            cy="45.2455"
                            r="1.66343"
                            transform="rotate(-90 16.3016 45.2455)"
                            fill="#13C296"
                          />
                          <circle
                            cx="16.3016"
                            cy="1.66347"
                            r="1.66343"
                            transform="rotate(-90 16.3016 1.66347)"
                            fill="#13C296"
                          />
                          <circle
                            cx="30.9398"
                            cy="45.2455"
                            r="1.66343"
                            transform="rotate(-90 30.9398 45.2455)"
                            fill="#13C296"
                          />
                          <circle
                            cx="30.9398"
                            cy="1.66347"
                            r="1.66343"
                            transform="rotate(-90 30.9398 1.66347)"
                            fill="#13C296"
                          />
                          <circle
                            cx="45.578"
                            cy="45.2455"
                            r="1.66343"
                            transform="rotate(-90 45.578 45.2455)"
                            fill="#13C296"
                          />
                          <circle
                            cx="45.578"
                            cy="1.66347"
                            r="1.66343"
                            transform="rotate(-90 45.578 1.66347)"
                            fill="#13C296"
                          />
                          <circle
                            cx="60.2162"
                            cy="45.2457"
                            r="1.66343"
                            transform="rotate(-90 60.2162 45.2457)"
                            fill="#13C296"
                          />
                          <circle
                            cx="74.6634"
                            cy="45.2457"
                            r="1.66343"
                            transform="rotate(-90 74.6634 45.2457)"
                            fill="#13C296"
                          />
                          <circle
                            cx="60.2162"
                            cy="1.66371"
                            r="1.66343"
                            transform="rotate(-90 60.2162 1.66371)"
                            fill="#13C296"
                          />
                          <circle
                            cx="74.6634"
                            cy="1.66371"
                            r="1.66343"
                            transform="rotate(-90 74.6634 1.66371)"
                            fill="#13C296"
                          />
                        </svg>
                      </span>
                      <span class="absolute -top-7 -right-4">
                        <svg
                          width="58"
                          height="60"
                          viewBox="0 0 58 60"
                          fill="none"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <path
                            fill-rule="evenodd"
                            clip-rule="evenodd"
                            d="M23 59.2671C23 44.8581 23 33.1774 23 33.1774C39.0163 33.1774 52 44.8581 52 59.2671C52 59.2671 52 59.2671 23 59.2671Z"
                            fill="#13C296"
                          />
                          <path
                            fill-rule="evenodd"
                            clip-rule="evenodd"
                            d="M57 49.7009C57 22.8041 57 1 57 1C26.0721 1 1 22.8041 1 49.7009C1 49.7009 1 49.7009 57 49.7009Z"
                            stroke="#3758F9"
                            stroke-width="1.5"
                          />
                        </svg>
                      </span>
                    </div>
                  </div>
                </div>
              </template>
            </div>

            <div class="swiper-pagination"></div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Testimonials Section End -->
</template>
