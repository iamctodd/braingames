<script setup lang="ts">
import Swiper from 'swiper'
import { onMounted, onUnmounted, ref, watch  } from 'vue'

const swiper = ref<Swiper | null>(null) as { value?: Swiper };
const swiperContainer = ref<HTMLElement | null>(null);

onMounted(() => {
  initSwiper();
});

watch(swiperContainer, () => {
  initSwiper();
});


const initSwiper = () => {
  if (swiperContainer.value && !swiper.value) {
     swiper.value = new Swiper(swiperContainer.value, {
      breakpoints: {
        640: { width: 640, slidesPerView: 1 },
        768: { width: 768, slidesPerView: 2.3 },
        1024: { width: 1024, slidesPerView: 2.2 },
        1280: { width: 1280, slidesPerView: 3 },
      },
      loop: true,
      spaceBetween: 30,
    } as any);
  }
};

onUnmounted(() => {
  if (swiper.value) {
    swiper.value.destroy();
  }
});

const onPrevClick = () => {
  swiper?.value?.slidePrev();
};

const onNextClick = () => {
  swiper?.value?.slideNext();
};

interface PortfolioItem {
  image: string
  category: string
  title: string
  details: string
  buttonText: string
  buttonLink: string
}

const portfolioItems = ref<PortfolioItem[]>([
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/portfolio/portfolio-02/image-01.jpg',
    category: 'Graphic Design',
    title: 'Aura Branding Design',
    details: 'Lorem Ipsum is simply dummy text of the printing and industry.',
    buttonText: 'View Portfolio',
    buttonLink: '#'
  },
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/portfolio/portfolio-02/image-02.jpg',
    category: 'Web Design',
    title: 'Best Web Design',
    details: 'Lorem Ipsum is simply dummy text of the printing and industry.',
    buttonText: 'View Portfolio',
    buttonLink: '#'
  },
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/portfolio/portfolio-02/image-03.jpg',
    category: 'Branding',
    title: 'Branding Solutions',
    details: 'Lorem Ipsum is simply dummy text of the printing and industry.',
    buttonText: 'View Portfolio',
    buttonLink: '#'
  },
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/portfolio/portfolio-02/image-01.jpg',
    category: 'Graphic Design',
    title: 'Aura Branding Design',
    details: 'Lorem Ipsum is simply dummy text of the printing and industry.',
    buttonText: 'View Portfolio',
    buttonLink: '#'
  },
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/portfolio/portfolio-02/image-02.jpg',
    category: 'Web Design',
    title: 'Best Web Design',
    details: 'Lorem Ipsum is simply dummy text of the printing and industry.',
    buttonText: 'View Portfolio',
    buttonLink: '#'
  },
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/portfolio/portfolio-02/image-03.jpg',
    category: 'Branding',
    title: 'Branding Solutions',
    details: 'Lorem Ipsum is simply dummy text of the printing and industry.',
    buttonText: 'View Portfolio',
    buttonLink: '#'
  }
])
</script>

<template>
  <!-- ====== Portfolio Section Start -->
  <section class="pt-20 pb-12 lg:pt-[120px] lg:pb-[90px] dark:bg-dark overflow-hidden">
    <div class="container mx-auto relative overflow-hidden">
      <div class="-mx-4 flex flex-wrap">
        <div class="w-full px-4">
          <div class="mb-[60px] max-w-[510px]">
            <span class="text-primary mb-2 block text-lg font-semibold"> Our Portfolio </span>
            <h2
              class="text-dark dark:text-white text-3xl leading-[1.208] font-bold sm:text-4xl md:text-[40px]"
            >
              Our Recent Works
            </h2>
          </div>
        </div>
      </div>

      <div class="swiper-container" ref="swiperContainer">
        <div class="swiper-wrapper">
          <template v-for="(item, index) in portfolioItems" :key="index">
            <div class="swiper-slide">
              <div class="overflow-hidden rounded-xl">
                <div>
                  <img :src="item.image" alt="portfolio" class="w-full" />
                </div>

                <div class="bg-primary relative z-10 p-8 sm:p-9 lg:p-8 lg:px-6 xl:p-9">
                  <span
                    class="text-white mb-4 inline-block rounded-md bg-white/10 py-1 px-4 text-sm font-medium"
                  >
                    {{ item.category }}
                  </span>
                  <h3>
                    <a
                      :href="item.buttonLink"
                      class="mb-3 block text-2xl font-bold text-white hover:opacity-70"
                    >
                      {{ item.title }}
                    </a>
                  </h3>
                  <p class="mb-7 text-base text-white">
                    {{ item.details }}
                  </p>
                  <a
                    :href="item.buttonLink"
                    class="hover:text-primary rounded-md border border-white/30 py-[10px] px-7 text-sm font-medium text-white transition hover:border-white hover:bg-white"
                  >
                    {{ item.buttonText }}
                  </a>

                  <div class="absolute right-1 bottom-2 z-[-1]">
                    <svg
                      width="25"
                      height="60"
                      viewBox="0 0 25 60"
                      fill="none"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <ellipse cx="1.23441" cy="1.30563" rx="1.23441" ry="1.30563" fill="white" />
                      <ellipse cx="1.23441" cy="12.7953" rx="1.23441" ry="1.30563" fill="white" />
                      <ellipse cx="1.23441" cy="24.2846" rx="1.23441" ry="1.30563" fill="white" />
                      <ellipse cx="1.23441" cy="35.7743" rx="1.23441" ry="1.30563" fill="white" />
                      <ellipse cx="1.23441" cy="47.2639" rx="1.23441" ry="1.30563" fill="white" />
                      <ellipse cx="1.23441" cy="58.4922" rx="1.23441" ry="1.30563" fill="white" />
                      <ellipse cx="12.0973" cy="1.30563" rx="1.23441" ry="1.30563" fill="white" />
                      <ellipse cx="12.0973" cy="12.7953" rx="1.23441" ry="1.30563" fill="white" />
                      <ellipse cx="12.0973" cy="24.2846" rx="1.23441" ry="1.30563" fill="white" />
                      <ellipse cx="12.0973" cy="35.7743" rx="1.23441" ry="1.30563" fill="white" />
                      <ellipse cx="12.0971" cy="47.2639" rx="1.23441" ry="1.30563" fill="white" />
                      <ellipse cx="12.0971" cy="58.4922" rx="1.23441" ry="1.30563" fill="white" />
                      <ellipse cx="22.96" cy="1.30563" rx="1.23441" ry="1.30563" fill="white" />
                      <ellipse cx="22.96" cy="12.7953" rx="1.23441" ry="1.30563" fill="white" />
                      <ellipse cx="22.96" cy="24.2846" rx="1.23441" ry="1.30563" fill="white" />
                      <ellipse cx="22.96" cy="35.7743" rx="1.23441" ry="1.30563" fill="white" />
                      <ellipse cx="22.9602" cy="47.2639" rx="1.23441" ry="1.30563" fill="white" />
                      <ellipse cx="22.9602" cy="58.4922" rx="1.23441" ry="1.30563" fill="white" />
                    </svg>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </div>

        <div
          class="absolute z-50 right-0 left-0 bottom-[-62px] flex items-center justify-center lg:left-auto lg:bottom-auto lg:top-7 lg:justify-end"
        >
          <div class="prev-arrow cursor-pointer">
            <button
              @click="onPrevClick"
              class="border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 hover:border-primary hover:bg-primary mx-2 flex h-[54px] w-[54px] items-center justify-center rounded-full border bg-white dark:bg-dark-2 transition-all hover:text-white"
            >
              <svg width="10" height="21" viewBox="0 0 10 21" class="fill-current">
                <path
                  d="M9.39847 5.25871e-08C9.53382 4.07542e-08 9.70301 0.0682049 9.80453 0.170515C10.0414 0.409239 10.0414 0.784374 9.83836 1.0231L1.31122 10.1628C1.14203 10.3333 1.14203 10.6402 1.31122 10.8448L9.83837 19.9845C10.0752 20.2232 10.0414 20.5984 9.80453 20.8371C9.56766 21.0758 9.19545 21.0417 8.95858 20.803L0.431432 11.6633C-0.143812 11.0154 -0.143812 9.99226 0.431432 9.3784L8.95858 0.204619C9.09393 0.068205 9.22928 6.73781e-08 9.39847 5.25871e-08Z"
                ></path>
              </svg>
            </button>
          </div>
          <div class="next-arrow cursor-pointer">
            <button
              @click="onNextClick"
              class="border-stroke dark:border-dark-3 text-body-color dark:text-dark-6 hover:border-primary hover:bg-primary mx-2 flex h-[54px] w-[54px] items-center justify-center rounded-full border bg-white dark:bg-dark-2 transition-all hover:text-white"
            >
              <svg width="10" height="21" viewBox="0 0 10 21" class="fill-current">
                <path
                  d="M0.601526 21C0.466174 21 0.296985 20.9318 0.195471 20.8295C-0.0413943 20.5908 -0.0413938 20.2156 0.161634 19.9769L8.68878 10.8372C8.85797 10.6667 8.85797 10.3598 8.68878 10.1552L0.161634 1.01548C-0.0752317 0.77676 -0.0413943 0.401624 0.195471 0.162901C0.432336 -0.075822 0.804553 -0.0417187 1.04142 0.197004L9.56857 9.33668C10.1438 9.98464 10.1438 11.0077 9.56857 11.6216L1.04142 20.7954C0.906067 20.9318 0.770715 21 0.601526 21Z"
                ></path>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Portfolio Section End -->
</template>
