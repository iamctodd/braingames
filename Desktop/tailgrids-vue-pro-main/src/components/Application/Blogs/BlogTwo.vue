<script setup lang="ts">
import { ref } from 'vue'

const blogItems = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/blogs/blog-02/image-01.jpg',
    title: 'How to use Facebook ads to sell online courses',
    subtitle: 'Digital Marketing',
    details: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
    buttonText: 'Read More',
    buttonLink: '#'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/blogs/blog-01/image-02.jpg',
    title: 'The Data-Driven Approach to Understanding.',
    subtitle: 'Digital Marketing',
    details: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
    buttonText: 'Read More',
    buttonLink: '#'
  }
])

const blogSideItems = ref([
  {
    title: 'Design is a Plan or The Construction of an Object.',
    subtitle: 'Graphics Design',
    details:
      'Lorem Ipsum is simply dummy text of the printing and industry page when looking at its layout.',
    buttonText: 'Read More',
    buttonLink: '#'
  },
  {
    title: 'How to use Facebook ads to sell online courses',
    subtitle: 'Graphics Design',
    details:
      'Lorem Ipsum is simply dummy text of the printing and industry page when looking at its layout.',
    buttonText: 'Read More',
    buttonLink: '#'
  }
])
</script>

<template>
  <!-- ====== Blog Section Start -->
  <section class="pt-20 pb-12 lg:pt-[120px] bg-white dark:bg-dark lg:pb-[90px]">
    <div class="container mx-auto">
      <div class="flex flex-wrap justify-center -mx-4">
        <div class="w-full px-4">
          <div class="mx-auto mb-[60px] max-w-[510px] text-center lg:mb-20">
            <span class="block mb-2 text-lg font-semibold text-primary"> Our Blogs </span>
            <h2
              class="mb-4 text-3xl font-bold text-dark dark:text-white sm:text-4xl md:text-[40px]"
            >
              Our Recent News
            </h2>
            <p class="text-base text-body-color dark:text-dark-6">
              There are many variations of passages of Lorem Ipsum available but the majority have
              suffered alteration in some form.
            </p>
          </div>
        </div>
      </div>

      <div class="flex flex-wrap -mx-4">
        <div class="w-full px-4 lg:w-8/12">
          <template v-for="(item, index) in blogItems" :key="index">
            <div class="mb-8 bg-gray dark:bg-dark-2">
              <div class="w-full items-stretch md:-mx-4 md:flex">
                <div class="w-full md:w-1/2 md:px-4">
                  <div class="h-full w-full">
                    <img
                      :src="item.image"
                      alt="image"
                      class="h-full w-full object-cover object-center"
                    />
                  </div>
                </div>
                <div class="w-full px-8 md:w-1/2 md:px-4">
                  <div class="w-full py-8">
                    <span class="mb-2 inline-block text-sm font-medium tracking-wide text-primary">
                      {{ item.subtitle }}
                    </span>
                    <h3>
                      <a
                        :href="item.buttonLink"
                        class="mb-3 inline-block text-xl font-semibold text-dark hover:text-primary dark:text-white"
                      >
                        {{ item.title }}
                      </a>
                    </h3>
                    <p class="mb-7 text-base text-body-color dark:text-dark-6">
                      {{ item.details }}
                    </p>
                    <a
                      :href="item.buttonLink"
                      class="group inline-flex items-center text-sm font-medium text-body-color duration-300 hover:text-primary dark:text-dark-6"
                    >
                      {{ item.buttonText }}
                      <span class="ml-1 duration-300 group-hover:translate-x-2">
                        <svg
                          width="18"
                          height="18"
                          viewBox="0 0 18 18"
                          fill="none"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <path
                            d="M16.2 8.54995L10.3781 2.6437C10.125 2.39058 9.73125 2.39058 9.47812 2.6437C9.225 2.89683 9.225 3.29058 9.47812 3.5437L14.2031 8.35308H2.25C1.9125 8.35308 1.63125 8.63433 1.63125 8.97183C1.63125 9.30933 1.9125 9.6187 2.25 9.6187H14.2594L9.47812 14.4843C9.225 14.7375 9.225 15.1312 9.47812 15.3843C9.59062 15.4968 9.75937 15.5531 9.92812 15.5531C10.0969 15.5531 10.2656 15.4968 10.3781 15.3562L16.2 9.44995C16.4531 9.19683 16.4531 8.80308 16.2 8.54995Z"
                            fill="currentColor"
                          />
                        </svg>
                      </span>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </div>

        <div class="w-full px-4 lg:w-4/12">
          <div class="relative mb-8 bg-primary p-8">
            <template v-for="(item, index) in blogSideItems" :key="index">
              <div
                class="first:border-b first:border-white/30 first:pb-6 [&:not(:first-child)]:pt-6"
              >
                <span class="mb-2 inline-block text-sm font-medium text-white">
                  {{ item.subtitle }}
                </span>
                <h3>
                  <a
                    :href="item.buttonLink"
                    class="mb-3 inline-block text-xl font-semibold text-white hover:text-white/80"
                  >
                    {{ item.title }}
                  </a>
                </h3>
                <p class="mb-6 text-base text-gray-3">{{ item.details }}</p>
                <a
                  :href="item.buttonLink"
                  class="group inline-flex items-center text-sm font-medium text-white"
                >
                  {{ item.buttonText }}
                  <span class="ml-1 duration-300 group-hover:translate-x-2">
                    <svg
                      width="18"
                      height="18"
                      viewBox="0 0 18 18"
                      fill="none"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        d="M16.2 8.54995L10.3781 2.6437C10.125 2.39058 9.73126 2.39058 9.47813 2.6437C9.22501 2.89683 9.22501 3.29058 9.47813 3.5437L14.2031 8.35308H2.25001C1.91251 8.35308 1.63126 8.63433 1.63126 8.97183C1.63126 9.30933 1.91251 9.6187 2.25001 9.6187H14.2594L9.47813 14.4843C9.22501 14.7375 9.22501 15.1312 9.47813 15.3843C9.59063 15.4968 9.75938 15.5531 9.92813 15.5531C10.0969 15.5531 10.2656 15.4968 10.3781 15.3562L16.2 9.44995C16.4531 9.19683 16.4531 8.80308 16.2 8.54995Z"
                        fill="currentColor"
                      />
                    </svg>
                  </span>
                </a>
              </div>
            </template>

            <span class="absolute right-0 top-0">
              <svg
                width="46"
                height="45"
                viewBox="0 0 46 45"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <circle
                  cx="1.39737"
                  cy="43.6026"
                  r="1.39737"
                  transform="rotate(-90 1.39737 43.6026)"
                  fill="white"
                  fillOpacity="0.44"
                ></circle>
                <circle
                  cx="1.39737"
                  cy="6.9913"
                  r="1.39737"
                  transform="rotate(-90 1.39737 6.9913)"
                  fill="white"
                  fillOpacity="0.44"
                ></circle>
                <circle
                  cx="13.6943"
                  cy="43.6026"
                  r="1.39737"
                  transform="rotate(-90 13.6943 43.6026)"
                  fill="white"
                  fillOpacity="0.44"
                ></circle>
                <circle
                  cx="13.6943"
                  cy="6.9913"
                  r="1.39737"
                  transform="rotate(-90 13.6943 6.9913)"
                  fill="white"
                  fillOpacity="0.44"
                ></circle>
                <circle
                  cx="25.9911"
                  cy="43.6026"
                  r="1.39737"
                  transform="rotate(-90 25.9911 43.6026)"
                  fill="white"
                  fillOpacity="0.44"
                ></circle>
                <circle
                  cx="25.9911"
                  cy="6.9913"
                  r="1.39737"
                  transform="rotate(-90 25.9911 6.9913)"
                  fill="white"
                  fillOpacity="0.44"
                ></circle>
                <circle
                  cx="38.288"
                  cy="43.6026"
                  r="1.39737"
                  transform="rotate(-90 38.288 43.6026)"
                  fill="white"
                  fillOpacity="0.44"
                ></circle>
                <circle
                  cx="38.288"
                  cy="6.9913"
                  r="1.39737"
                  transform="rotate(-90 38.288 6.9913)"
                  fill="white"
                  fillOpacity="0.44"
                ></circle>
                <circle
                  cx="1.39737"
                  cy="31.3057"
                  r="1.39737"
                  transform="rotate(-90 1.39737 31.3057)"
                  fill="white"
                  fillOpacity="0.44"
                ></circle>
                <circle
                  cx="13.6943"
                  cy="31.3057"
                  r="1.39737"
                  transform="rotate(-90 13.6943 31.3057)"
                  fill="white"
                  fillOpacity="0.44"
                ></circle>
                <circle
                  cx="25.9911"
                  cy="31.3057"
                  r="1.39737"
                  transform="rotate(-90 25.9911 31.3057)"
                  fill="white"
                  fillOpacity="0.44"
                ></circle>
                <circle
                  cx="38.288"
                  cy="31.3057"
                  r="1.39737"
                  transform="rotate(-90 38.288 31.3057)"
                  fill="white"
                  fillOpacity="0.44"
                ></circle>
                <circle
                  cx="1.39737"
                  cy="19.0086"
                  r="1.39737"
                  transform="rotate(-90 1.39737 19.0086)"
                  fill="white"
                  fillOpacity="0.44"
                ></circle>
                <circle
                  cx="13.6943"
                  cy="19.0086"
                  r="1.39737"
                  transform="rotate(-90 13.6943 19.0086)"
                  fill="white"
                  fillOpacity="0.44"
                ></circle>
                <circle
                  cx="25.9911"
                  cy="19.0086"
                  r="1.39737"
                  transform="rotate(-90 25.9911 19.0086)"
                  fill="white"
                  fillOpacity="0.44"
                ></circle>
                <circle
                  cx="38.288"
                  cy="19.0086"
                  r="1.39737"
                  transform="rotate(-90 38.288 19.0086)"
                  fill="white"
                  fillOpacity="0.44"
                ></circle>
              </svg>
            </span>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Blog Section End -->
</template>
