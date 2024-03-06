<script setup lang="ts">
import { ref } from 'vue'

const featuresItems = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/marketing/images/services/services-06/image-01.jpg',
    title: `Website Development`,
    details:
      'Lorem ipsum is simply dummy text of the printing typesetting lorem ipsum been dummy text.',
    button: {
      link: '#',
      text: 'View Details'
    }
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/marketing/images/services/services-06/image-02.jpg',
    title: `Graphic Design`,
    details:
      'Lorem ipsum is simply dummy text of the printing typesetting lorem ipsum been dummy text.',
    button: {
      link: '#',
      text: 'View Details'
    }
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/marketing/images/services/services-06/image-03.jpg',
    title: `App Development`,
    details:
      'Lorem ipsum is simply dummy text of the printing typesetting lorem ipsum been dummy text.',
    button: {
      link: '#',
      text: 'View Details'
    }
  }
])
</script>

<template>
  <!-- ====== Services Section Start -->
  <section class="bg-[#090E34] dark:bg-dark pt-20 pb-12 lg:pt-[120px] lg:pb-[90px]">
    <div class="container mx-auto">
      <div class="-mx-4 mb-10 flex flex-wrap items-end lg:mb-[70px]">
        <div class="w-full px-4 lg:w-8/12">
          <div class="mb-5 max-w-[625px]">
            <span class="text-primary mb-2 block text-lg font-semibold"> Project Planing </span>
            <h2 class="text-3xl leading-[1.2] font-bold text-white sm:text-4xl md:text-[40px]">
              We help our clients to build There Dream Projects
            </h2>
          </div>
        </div>
        <div class="w-full px-4 lg:w-4/12">
          <div class="mb-5 flex lg:justify-end">
            <a
              href="javascript:void(0)"
              class="group hover:text-primary text-lg font-medium text-white relative"
            >
              EXPLORE SERVICES
              <span
                class="block w-full h-0.5 bg-white absolute left-0 bottom-0 ease-linear duration-300 group-hover:w-full group-hover:bg-primary"
              ></span>
            </a>
          </div>
        </div>
      </div>

      <div class="-mx-4 flex flex-wrap justify-center">
        <template v-for="(item, index) in featuresItems" :key="index">
          <div class="w-full px-4 md:w-1/2 lg:w-1/3">
            <div class="mb-10 bg-white dark:bg-dark-2">
              <a :href="item.button.link" class="block w-full">
                <img :src="item.image" alt="image" class="w-full" />
              </a>
              <div class="p-8 sm:p-11 md:p-8 lg:px-6 xl:p-10 2xl:p-11">
                <h3>
                  <a
                    :href="item.button.link"
                    class="text-dark dark:text-white hover:text-primary mb-4 block text-lg font-bold sm:leading-[35px] sm:text-[22px]"
                  >
                    {{ item.title }}
                  </a>
                </h3>
                <p
                  class="text-body-color dark:text-dark-6 mb-8 border-b border-stroke dark:border-dark-3 pb-8 text-base"
                >
                  {{ item.details }}
                </p>
                <a
                  :href="item.button.link"
                  class="text-body-color dark:text-dark-6 hover:text-primary inline-flex items-center text-base"
                >
                  {{ item.button.text }}
                  <span class="ml-3">
                    <svg
                      width="20"
                      height="20"
                      viewBox="0 0 20 20"
                      fill="none"
                      xmlns="http://www.w3.org/2000/svg"
                      class="fill-current"
                    >
                      <path
                        d="M18 9.5L11.5312 2.9375C11.25 2.65625 10.8125 2.65625 10.5312 2.9375C10.25 3.21875 10.25 3.65625 10.5312 3.9375L15.7812 9.28125H2.5C2.125 9.28125 1.8125 9.59375 1.8125 9.96875C1.8125 10.3438 2.125 10.6875 2.5 10.6875H15.8437L10.5312 16.0938C10.25 16.375 10.25 16.8125 10.5312 17.0938C10.6562 17.2188 10.8437 17.2812 11.0312 17.2812C11.2187 17.2812 11.4062 17.2188 11.5312 17.0625L18 10.5C18.2812 10.2187 18.2812 9.78125 18 9.5Z"
                        fill=""
                      />
                    </svg>
                  </span>
                </a>
              </div>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>
  <!-- ====== Services Section End -->
</template>
