<script setup lang="ts">
import { ref } from 'vue'

const pricingPlans = ref([
  {
    price: '€ 19.99',
    features: {
      users: '1 User',
      components: 'All UI components',
      access: 'Lifetime access',
      updates: 'Free updates',
      projects: 'Use on 1 (one) project',
      support: '3 Months support'
    },
    button: {
      text: 'Purchase Now'
    }
  },
  {
    popular: true,
    price: '€ 19.99',
    features: {
      users: '5 Users',
      components: 'All UI components',
      access: 'Lifetime access',
      updates: 'Free updates',
      projects: 'Use on 3 (Three) project',
      support: '4 Months support'
    },
    button: {
      text: 'Purchase Now'
    }
  },
  {
    price: '€ 70.99',
    features: {
      users: 'Unlimited Users',
      components: 'All UI components',
      access: 'Lifetime access',
      updates: 'Free updates',
      projects: 'Use on Unlimited project',
      support: '12 Months support'
    },
    button: {
      text: 'Purchase Now'
    }
  }
])
</script>

<template>
  <!-- ====== Pricing Section Start -->
  <section
    class="relative z-20 overflow-hidden bg-white dark:bg-dark pt-20 pb-12 lg:pt-[120px] lg:pb-[90px]"
  >
    <div class="container mx-auto">
      <div class="-mx-4 flex flex-wrap">
        <div class="w-full px-4">
          <div class="mx-auto mb-[60px] max-w-[510px] text-center lg:mb-[75px]">
            <span class="text-primary mb-2 block text-lg font-semibold"> Pricing Table </span>
            <h2
              class="text-dark dark:text-white mb-3 text-3xl leading-[1.208] font-bold sm:text-4xl md:text-[40px]"
            >
              Our Pricing Plan
            </h2>
            <p class="text-body-color text-base dark:text-dark-6">
              There are many variations of passages of Lorem Ipsum available but the majority have
              suffered alteration in some form.
            </p>
          </div>
        </div>
      </div>

      <div class="flex flex-wrap items-center justify-center">
        <template v-for="(plan, index) in pricingPlans" :key="index">
          <div
            :class="{
              ' w-full lg:max-w-[370px]': plan.popular,
              'w-full lg:max-w-[406px]': !plan.popular
            }"
          >
            <div
              :class="{
                ' bg-primary from-primary shadow-pricing relative z-10 mb-10 overflow-hidden rounded-xl bg-gradient-to-b to-[#179BEE] py-10 px-8 text-center sm:p-12 lg:py-10 lg:px-6 xl:pt-[55px] xl:pb-10 xl:px-[50px]':
                  plan.popular,
                'border-[#D4DEFF] dark:border-dark-3 drop-shadow-pricing relative z-10 mb-10 overflow-hidden rounded-xl border-2 bg-white dark:bg-dark-2 py-10 px-8 text-center sm:p-12 lg:py-10 lg:px-6 xl:pt-[45px] xl:pb-[50px] xl:px-[50px]':
                  !plan.popular
              }"
            >
              <span
                class="mb-5 inline-block rounded-full border py-2 px-6 text-base font-semibold uppercase text-white"
                v-if="plan.popular"
              >
                POPULAR
              </span>
              <span
                :class="{
                  ' mb-2 block text-base font-medium uppercase text-white': plan.popular,
                  'text-dark dark:text-white mb-2 block text-base font-medium uppercase':
                    !plan.popular
                }"
              >
                STARTING FROM
              </span>

              <h2
                :class="{
                  ' mb-8 text-[28px] font-semibold text-white': plan.popular,
                  'text-primary mb-9 text-[28px] font-semibold': !plan.popular
                }"
              >
                {{ plan.price }}/mo
              </h2>

              <div class="mb-9 flex flex-col gap-4">
                <p
                  :class="{
                    ' text-base text-white': plan.popular,
                    'text-body-color dark:text-dark-6 text-base': !plan.popular
                  }"
                >
                  {{ plan.features.users }}
                </p>
                <p
                  :class="{
                    ' text-base text-white': plan.popular,
                    'text-body-color dark:text-dark-6 text-base': !plan.popular
                  }"
                >
                  {{ plan.features.components }}
                </p>
                <p
                  :class="{
                    ' text-base text-white': plan.popular,
                    'text-body-color dark:text-dark-6 text-base': !plan.popular
                  }"
                >
                  {{ plan.features.access }}
                </p>
                <p
                  :class="{
                    ' text-base text-white': plan.popular,
                    'text-body-color dark:text-dark-6 text-base': !plan.popular
                  }"
                >
                  {{ plan.features.updates }}
                </p>
                <p
                  :class="{
                    ' text-base text-white': plan.popular,
                    'text-body-color dark:text-dark-6 text-base': !plan.popular
                  }"
                >
                  {{ plan.features.projects }}
                </p>
                <p
                  :class="{
                    ' text-base text-white': plan.popular,
                    'text-body-color dark:text-dark-6 text-base': !plan.popular
                  }"
                >
                  {{ plan.features.support }}
                </p>
              </div>
              <div class="w-full">
                <a
                  href="javascript:void(0)"
                  :class="{
                    ' text-primary inline-block rounded-full shadow-1 border border-white bg-white py-3 px-[50px] text-center text-base font-medium transition hover:bg-gray-2 hover:text-body-color':
                      plan.popular,
                    'text-primary hover:border-primary hover:bg-primary inline-block rounded-full border border-stroke dark:border-dark-3 shadow-1 dark:shadow-none bg-transparent py-3 px-[50px] text-center text-base font-medium transition hover:text-white ':
                      !plan.popular
                  }"
                >
                  {{ plan.button.text }}
                </a>
              </div>

              <span
                v-if="index === 0"
                class="bg-primary absolute left-0 bottom-0 z-[-1] block h-14 w-14 rounded-tr-full"
              >
              </span>

              <span
                v-if="index === 2"
                class="bg-secondary absolute right-0 top-0 z-[-1] block h-14 w-14 rounded-bl-full"
              >
              </span>

              <div v-if="plan.popular">
                <span class="absolute right-0 top-0 z-[-1]">
                  <svg
                    width="115"
                    height="188"
                    viewBox="0 0 115 188"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M21.8728 74.7487C-7.29746 54.3102 0.420245 11.2655 2.4266 -7.93432L142.717 -13.0439C158.15 54.3102 178.924 188.74 138.55 187.625C88.0822 186.231 71.1788 165.278 69.562 139.316C67.7108 109.587 53.1242 96.6453 21.8728 74.7487Z"
                      fill="white"
                      fill-opacity="0.06"
                    />
                  </svg>
                </span>
                <span class="absolute bottom-0 left-0 z-[-1]">
                  <svg
                    width="61"
                    height="222"
                    viewBox="0 0 61 222"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M54.4989 22.7537C40.0989 -6.94625 0.165607 -1.32733 -18.0011 5.19463C-36.1677 76.1 -36.4871 199.841 -18.0011 245.002C4.99936 301.191 67.5 262.561 54.4989 217.911C48.8553 198.528 22.9989 168.244 34.9989 136.637C46.9989 105.031 72.4989 59.8787 54.4989 22.7537Z"
                      fill="white"
                      fill-opacity="0.06"
                    />
                  </svg>
                </span>
              </div>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>

  <!-- ====== Pricing Section End -->
</template>
