<script setup lang="ts">
import { ref } from 'vue'

const pricingPlans = ref([
  {
    type: 'BASIC',
    price: '25',
    subscription: 'per Month',
    subtitle: 'Lorem Ipsum simply dummy text of the printing.',
    features: [
      'Up to 1 User',
      'All UI components',
      'Lifetime access',
      'Free updates',
      'Community Support',
      'Downloadable Files'
    ],
    button: {
      text: 'Purchase Now'
    }
  },
  {
    popular: true,
    type: 'BUSINESS',
    price: '89',
    subscription: 'per Month',
    subtitle: 'Lorem Ipsum simply dummy text of the printing.',
    features: [
      'Up to 5 User',
      'All UI components',
      'Lifetime access',
      'Free updates',
      'Community Support',
      'Downloadable Files'
    ],
    button: {
      text: 'Purchase Now'
    }
  },
  {
    type: 'ENTERPRISE',
    price: '395 ',
    subscription: 'per Month',
    subtitle: 'Lorem Ipsum simply dummy text of the printing.',
    features: [
      'Up to 50 User',
      'All UI components',
      'Lifetime access',
      'Free updates',
      'Community Support',
      'Downloadable Files'
    ],
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
          <div class="mx-auto mb-[60px] max-w-[510px] text-center">
            <span class="mb-2 block text-lg font-semibold text-primary"> Our Pricing Plans </span>
            <h2
              class="mb-3 text-3xl leading-[1.208] font-bold text-dark dark:text-white sm:text-4xl md:text-[40px]"
            >
              Choose your best plan
            </h2>
            <p class="text-base text-body-color dark:text-dark-6">
              There are many variations of passages of Lorem Ipsum available but the majority have
              suffered alteration in some form.
            </p>
          </div>
        </div>
      </div>

      <div class="-mx-4 flex flex-wrap justify-center">
        <template v-for="(plan, index) in pricingPlans" :key="index">
          <div class="w-full max-w-[300px] px-4">
            <div
              :class="{
                ' relative z-10 mb-10 overflow-hidden rounded-xl bg-primary px-7 py-10 text-center shadow-card sm:px-9':
                  plan.popular,
                'relative z-10 mb-10 overflow-hidden rounded-xl bg-white px-7 py-10 text-center shadow-pricing-6 dark:bg-dark-2 sm:px-9':
                  !plan.popular
              }"
            >
              <span
                class="mb-5 block text-lg font-medium uppercase"
                :class="{
                  ' text-white': plan.popular,
                  'text-body-color dark:text-dark-6': !plan.popular
                }"
              >
                {{ plan.type }}
              </span>

              <h2
                class="mb-4 text-4xl font-extrabold xl:text-[42px] xl:leading-[1.21]"
                :class="{
                  ' text-white': plan.popular,
                  'text-primary': !plan.popular
                }"
              >
                <sup class="-top-5 text-xl font-semibold">$</sup>
                <span>
                  {{ plan.price }}
                </span>

                <span
                  class="block text-base font-normal"
                  :class="{
                    ' text-white': plan.popular,
                    'text-body-color dark:text-dark-6': !plan.popular
                  }"
                >
                  {{ plan.subscription }}
                </span>
              </h2>

              <p
                class="mb-8 text-sm"
                :class="{
                  '  text-white': plan.popular,
                  'text-body-color dark:text-dark-6': !plan.popular
                }"
              >
                {{ plan.subtitle }}
              </p>

              <div class="mb-9">
                <a
                  href="javascript:void(0)"
                  :class="{
                    ' inline-block rounded-full bg-white px-7 py-[13px] text-center text-base font-medium text-dark transition hover:bg-opacity-90':
                      plan.popular,
                    'inline-block rounded-full bg-primary px-7 py-[13px] text-center text-base font-medium text-white transition hover:bg-blue-dark ':
                      !plan.popular
                  }"
                >
                  {{ plan.button.text }}
                </a>
              </div>

              <div class="space-y-[14px]">
                <template v-for="(item, index) in plan.features" :key="index">
                  <p
                    :class="{
                      ' text-base text-white': plan.popular,
                      'text-base text-body-color dark:text-dark-6': !plan.popular
                    }"
                  >
                    {{ item }}
                  </p>
                </template>
              </div>

              <div v-if="plan.popular">
                <span class="absolute -top-10 left-0 -z-10">
                  <svg
                    width="310"
                    height="279"
                    viewBox="0 0 310 279"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <rect
                      opacity="0.15"
                      x="-15.1777"
                      y="36.5864"
                      width="271.285"
                      height="275.397"
                      transform="rotate(-28.5338 -15.1777 36.5864)"
                      fill="url(#paint0_linear_1343_342)"
                    />
                    <defs>
                      <linearGradient
                        id="paint0_linear_1343_342"
                        x1="120.465"
                        y1="36.5864"
                        x2="120.465"
                        y2="311.984"
                        gradientUnits="userSpaceOnUse"
                      >
                        <stop stop-color="white" />
                        <stop offset="1" stop-color="white" stop-opacity="0" />
                      </linearGradient>
                    </defs>
                  </svg>
                </span>
                <span class="absolute top-7 left-0 -z-10">
                  <svg
                    width="90"
                    height="197"
                    viewBox="0 0 90 197"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <rect
                      opacity="0.15"
                      x="-38"
                      y="17.0093"
                      width="34.1632"
                      height="204.648"
                      transform="rotate(-28.5338 -38 17.0093)"
                      fill="url(#paint0_linear_1343_343)"
                    />
                    <defs>
                      <linearGradient
                        id="paint0_linear_1343_343"
                        x1="-20.9184"
                        y1="17.0093"
                        x2="-20.9184"
                        y2="221.658"
                        gradientUnits="userSpaceOnUse"
                      >
                        <stop stop-color="white" />
                        <stop offset="1" stop-color="white" stop-opacity="0" />
                      </linearGradient>
                    </defs>
                  </svg>
                </span>
                <span class="absolute -bottom-10 right-0 -z-10">
                  <svg
                    width="310"
                    height="269"
                    viewBox="0 0 310 269"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <rect
                      opacity="0.15"
                      x="313.564"
                      y="234.562"
                      width="270.976"
                      height="266.92"
                      transform="rotate(151.466 313.564 234.562)"
                      fill="url(#paint0_linear_1343_344)"
                    />
                    <defs>
                      <linearGradient
                        id="paint0_linear_1343_344"
                        x1="449.053"
                        y1="234.562"
                        x2="449.053"
                        y2="501.482"
                        gradientUnits="userSpaceOnUse"
                      >
                        <stop stop-color="white" />
                        <stop offset="1" stop-color="white" stop-opacity="0" />
                      </linearGradient>
                    </defs>
                  </svg>
                </span>
                <span class="absolute bottom-7 right-0 -z-10">
                  <svg
                    width="91"
                    height="191"
                    viewBox="0 0 91 191"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <rect
                      opacity="0.15"
                      x="129.059"
                      y="170.938"
                      width="40.8041"
                      height="194.57"
                      transform="rotate(151.466 129.059 170.938)"
                      fill="url(#paint0_linear_1343_345)"
                    />
                    <defs>
                      <linearGradient
                        id="paint0_linear_1343_345"
                        x1="149.461"
                        y1="170.937"
                        x2="149.461"
                        y2="365.508"
                        gradientUnits="userSpaceOnUse"
                      >
                        <stop stop-color="white" />
                        <stop offset="1" stop-color="white" stop-opacity="0" />
                      </linearGradient>
                    </defs>
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
