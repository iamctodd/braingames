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

interface PortfolioItem {
  id: string
  image: string
  subtitle: string
  title: string
  details: string
  buttonLink: string
  buttonText: string
}

const portfolioItems = ref<PortfolioItem[]>([
  {
    id: '01',
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/portfolio/portfolio-06/portfolio-01.jpg',
    subtitle: 'Digital',
    title: 'Marketing Solutions',
    details:
      'Lorem ipsum dolor consectetur adipiscing mod tempor incididunt labore dolore magna ut veniam.',
    buttonLink: '#',
    buttonText: 'View Details'
  },
  {
    id: '02',
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/portfolio/portfolio-06/portfolio-02.jpg',
    subtitle: 'Digital',
    title: 'Marketing Solutions',
    details:
      'Lorem ipsum dolor consectetur adipiscing mod tempor incididunt labore dolore magna ut veniam.',
    buttonLink: '#',
    buttonText: 'View Details'
  },
  {
    id: '03',
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/portfolio/portfolio-06/portfolio-03.jpg',
    subtitle: 'Digital',
    title: 'Marketing Solutions',
    details:
      'Lorem ipsum dolor consectetur adipiscing mod tempor incididunt labore dolore magna ut veniam.',
    buttonLink: '#',
    buttonText: 'View Details'
  }
])
</script>

<style>
.swiper-pagination {
  bottom: -60px !important;
}
.swiper-pagination-bullet {
  margin: 0 8px !important;
  width: 10px;
  height: 10px;
  border-radius: 12px;
  background-color: #dfe4ea;
  opacity: 1;
  transition: all 0.3s ease-in-out;
}
.dark .swiper-pagination-bullet {
  background-color: #374151;
}
.swiper-pagination-bullet.swiper-pagination-bullet-active {
  width: 30px;
  background-color: #3758f9;
}
</style>

<template>
  <!-- ====== Portfolio Section Start -->
  <section class="dark:bg-dark">
    <div class="container mx-auto py-20 lg:py-[120px] overflow-hidden">
      <div class="swiper-container swiper !overflow-visible" ref="swiperContainer">
        <div class="swiper-wrapper">
          <template v-for="(item, index) in portfolioItems" :key="index">
            <div class="swiper-slide">
              <div class="-mx-4 flex flex-wrap justify-center">
                <div class="w-full px-4 lg:w-10/12 xl:w-8/12">
                  <div
                    class="relative w-full bg-cover bg-center bg-no-repeat py-12 px-10 sm:p-[60px]"
                    :style="{ backgroundImage: `url(${item.image})` }"
                  >
                    <div class="w-full">
                      <div
                        class="relative ml-auto w-full max-w-[330px] bg-white dark:bg-dark-2 py-[56px] px-8 sm:px-10"
                      >
                        <span
                          class="bg-primary absolute right-0 top-0 rounded-bl-2xl p-4 text-2xl font-semibold text-white"
                        >
                          {{ item.id }}
                        </span>
                        <span
                          class="inline-block mb-2 text-2xl font-bold sm:text-[26px] sm:leading-7 text-dark dark:text-white"
                        >
                          {{ item.subtitle }}
                        </span>
                        <h3 class="text-body-color dark:text-dark-6 mb-5 text-base font-medium">
                          {{ item.title }}
                        </h3>
                        <p class="text-body-color dark:text-dark-6 mb-9 text-sm">
                          {{ item.details }}
                        </p>
                        <a
                          :href="item.buttonLink"
                          class="text-dark dark:text-white hover:text-primary inline-flex items-center text-sm font-medium"
                        >
                          {{ item.buttonText }}
                          <span class="ml-2">
                            <svg
                              width="18"
                              height="18"
                              viewBox="0 0 18 18"
                              fill="none"
                              xmlns="http://www.w3.org/2000/svg"
                              class="fill-current"
                            >
                              <path
                                d="M16.2 8.54995L10.3781 2.6437C10.125 2.39058 9.73125 2.39058 9.47812 2.6437C9.225 2.89683 9.225 3.29058 9.47812 3.5437L14.2031 8.35308H2.25C1.9125 8.35308 1.63125 8.63433 1.63125 8.97183C1.63125 9.30933 1.9125 9.6187 2.25 9.6187H14.2594L9.47812 14.4843C9.225 14.7375 9.225 15.1312 9.47812 15.3843C9.59062 15.4968 9.75937 15.5531 9.92812 15.5531C10.0969 15.5531 10.2656 15.4968 10.3781 15.3562L16.2 9.44995C16.4531 9.19683 16.4531 8.80308 16.2 8.54995Z"
                                fill=""
                              />
                            </svg>
                          </span>
                        </a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </div>

        <div class="swiper-pagination"></div>
      </div>
    </div>
  </section>
  <!-- ====== Portfolio Section End -->
</template>
