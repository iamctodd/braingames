<script setup lang="ts">
import { ref } from 'vue'

interface PortfolioItem {
  image: string
  subtitle: string
  title: string
  link: string
}

const portfolioItems = ref<PortfolioItem[]>([
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/portfolio/portfolio-05/image-01.jpg',
    subtitle: 'INVITATION',
    title: 'Branding Design',
    link: '#'
  },
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/portfolio/portfolio-05/image-02.jpg',
    subtitle: 'STATIONARY',
    title: 'Best Marketing tips',
    link: '#'
  },
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/portfolio/portfolio-05/image-03.jpg',
    subtitle: 'INVITATION',
    title: 'Web Design Trend',
    link: '#'
  },
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/marketing/images/portfolio/portfolio-05/image-04.jpg',
    subtitle: 'PRODUCT',
    title: 'Business Card Design',
    link: '#'
  }
])
</script>

<template>
  <!-- ====== Portfolio Section Start -->
  <section class="pt-20 pb-5 lg:pt-[120px] lg:pb-[60px] dark:bg-dark">
    <div class="container mx-auto">
      <div class="-mx-4 flex flex-wrap">
        <div class="w-full px-4 lg:w-1/2">
          <div class="mb-[60px] max-w-[510px]">
            <span class="text-primary mb-2 block text-lg font-semibold"> Portfolio </span>
            <h2
              class="text-dark dark:text-white mb-3 text-3xl leading-[1.208] font-bold sm:text-4xl md:text-[40px]"
            >
              Check out some of our recent projects below.
            </h2>
            <p class="text-body-color dark:text-dark-6 text-base">
              There are many variations of passages of Lorem Ipsum available but the majority have
              suffered alteration in some form.
            </p>
          </div>

          <template v-for="(item, index) in portfolioItems" :key="index">
            <div v-if="index % 2 !== 0">
              <div class="mb-[60px] mr-0 lg:mr-4">
                <div class="mb-9 overflow-hidden rounded-xl">
                  <img :src="item.image" alt="image" class="w-full" />
                </div>
                <div class="content">
                  <div class="mb-4 flex items-center">
                    <span class="bg-primary mr-3 inline-block h-px w-6"></span>
                    <span class="text-primary text-sm font-semibold uppercase"> {{ item.subtitle }} </span>
                  </div>
                  <h3>
                    <a
                      :href="item.link"
                      class="text-dark dark:text-white hover:text-primary inline-block text-xl font-bold sm:text-2xl"
                    >
                      {{ item.title }}
                    </a>
                  </h3>
                </div>
              </div>
            </div>
          </template>
        </div>

        <div class="w-full px-4 lg:w-1/2">
          <template v-for="(item, index) in portfolioItems" :key="index">
            <div v-if="index % 2 === 0">
              <div class="mb-[60px] mr-0 lg:mr-4">
                <div class="mb-9 overflow-hidden rounded-xl">
                  <img :src="item.image" alt="image" class="w-full" />
                </div>
                <div class="content">
                  <div class="mb-4 flex items-center">
                    <span class="bg-primary mr-3 inline-block h-px w-6"></span>
                    <span class="text-primary text-sm font-semibold uppercase"> {{ item.subtitle }} </span>
                  </div>
                  <h3>
                    <a
                      :href="item.link"
                      class="text-dark dark:text-white hover:text-primary inline-block text-xl font-bold sm:text-2xl"
                    >
                      {{ item.title }}
                    </a>
                  </h3>
                </div>
              </div>
            </div>
          </template>
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Portfolio Section End -->
</template>
