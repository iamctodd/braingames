<script setup lang="ts">
import { ref } from 'vue'

const blogItems = ref([
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/blogs/blog-05/image-01.jpg',
    authorImg: 'https://cdn.tailgrids.com/2.0/image/application/images/blogs/blog-05/author-01.png',
    authorName: 'Samuyl Joshi',
    title: 'How to use Facebook ads to sell online courses',
    description:
      'Avoid burnout, reduce stress, and keep yourself healthy with these practical self-care tips for entrepreneurs.',
    tag: 'Online Courses'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/blogs/blog-05/image-02.jpg',
    authorImg: 'https://cdn.tailgrids.com/2.0/image/application/images/blogs/blog-05/author-02.png',
    authorName: 'Devid Leon',
    title: 'How to earn more money as a wellness coach',
    description:
      'Avoid burnout, reduce stress, and keep yourself healthy with these practical self-care tips for entrepreneurs.',
    tag: 'Online Courses'
  },
  {
    image: 'https://cdn.tailgrids.com/2.0/image/application/images/blogs/blog-05/image-03.jpg',
    authorImg: 'https://cdn.tailgrids.com/2.0/image/application/images/blogs/blog-05/author-03.png',
    authorName: 'Miller Demo',
    title: 'The no-fuss guide to upselling and cross selling',
    description:
      'Avoid burnout, reduce stress, and keep yourself healthy with these practical self-care tips for entrepreneurs.',
    tag: 'Online Courses'
  }
])
</script>

<template>
  <!-- ====== Blog Section Start -->
  <section class="mb-8 pt-20 lg:mb-[70px] lg:pt-[120px] bg-white dark:bg-dark">
    <div class="container mx-auto">
      <div class="-mx-4 mb-[60px] flex flex-wrap items-center justify-center lg:mb-20">
        <div class="w-full px-4 lg:w-8/12">
          <div class="mb-10 max-w-[510px] lg:mb-0">
            <span class="block mb-2 text-lg font-semibold text-primary"> Latest News </span>
            <h2
              class="mb-4 text-3xl font-bold text-dark dark:text-white sm:text-4xl md:text-[40px]"
            >
              Recent Blog Articles
            </h2>
            <p class="text-base text-body-color dark:text-dark-6">
              There are many variations of passages of Lorem Ipsum available but the majority have
              suffered alteration in some form.
            </p>
          </div>
        </div>

        <div class="w-full px-4 lg:w-4/12">
          <div class="lg:text-right">
            <div class="inline-flex justify-end rounded bg-[#F1F3FC] dark:bg-white/5 px-5">
              <a
                href="javascript:void(0)"
                class="py-3 text-base font-semibold pr-7 text-primary dark:text-white"
              >
                Most Popular
              </a>
              <a
                href="javascript:void(0)"
                class="py-3 text-base font-semibold text-body-color hover:text-primary dark:text-dark-6 dark:hover:text-white"
              >
                Most Popular
              </a>
            </div>
          </div>
        </div>
      </div>

      <div class="flex flex-wrap -mx-4">
        <template v-for="(item, index) in blogItems" :key="index">
          <div class="w-full px-4">
            <div class="flex flex-wrap items-center mb-12 -mx-4">
              <div class="w-full px-4 lg:w-6/12 xl:w-6/12">
                <div class="w-full mb-8 overflow-hidden rounded lg:mb-0">
                  <img :src="item.image" alt="image" class="w-full" />
                </div>
              </div>
              <div class="w-full px-4 lg:w-6/12 xl:w-6/12">
                <div class="w-full">
                  <span
                    class="inline-block px-5 py-3 mb-8 text-sm font-semibold text-white rounded bg-primary"
                  >
                    {{ item.tag }}
                  </span>
                  <div class="flex items-center mb-5">
                    <div class="w-10 h-10 mr-4 overflow-hidden rounded-full">
                      <img :src="item.authorImg" alt="image" class="w-full" />
                    </div>
                    <p class="text-base font-medium text-body-color dark:text-dark-6">
                      <span class="pr-0.5">By</span>
                      <a
                        href="javascript:void(0)"
                        class="text-body-color dark:text-dark-6 hover:text-primary"
                      >
                        {{ item.authorName }}
                      </a>
                    </p>
                  </div>
                  <div>
                    <h3>
                      <a
                        href="javascript:void(0)"
                        class="inline-block mb-4 text-xl font-semibold text-dark dark:text-white hover:text-primary sm:text-2xl lg:text-xl xl:text-2xl"
                      >
                        {{ item.title }}
                      </a>
                    </h3>
                    <p class="text-base text-body-color dark:text-dark-6">
                      {{ item.description }}
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>
  <!-- ====== Blog Section End -->
</template>
