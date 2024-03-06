<script setup lang="ts">
import { ref } from 'vue'

const pricingPlans = ref([
  {
    type: 'Starter',
    price: '9.99',
    subscription: '1 month free trial',
    subtitle: 'Lorem Ipsum simply dummy text of the printing.',
    features: [
      'Application UI Components',
      'Use on Unlimited Projects',
      'Personal and Commercial Use',
      'Use on Unlimited Projects',
      'Downloadable Offline Files',
      'Figma Source File'
    ],
    button: {
      text: 'Buy Now'
    }
  },
  {
    popular: true,
    type: 'Professional',
    price: '29.99',
    subscription: '1 month free trial',
    subtitle: 'Lorem Ipsum simply dummy text of the printing.',
    features: [
      'Application UI Components',
      'Use on Unlimited Projects',
      'Personal and Commercial Use',
      'Use on Unlimited Projects',
      'Downloadable Offline Files',
      'Figma Source File'
    ],
    button: {
      text: 'Buy Now'
    }
  },
  {
    type: 'Premium',
    price: '99.99 ',
    subscription: '1 month free trial',
    subtitle: 'Lorem Ipsum simply dummy text of the printing.',
    features: [
      'Application UI Components',
      'Use on Unlimited Projects',
      'Personal and Commercial Use',
      'Use on Unlimited Projects',
      'Downloadable Offline Files',
      'Figma Source File'
    ],
    button: {
      text: 'Buy Now'
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
              Pricing & plans
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
          <div class="w-full px-4 md:w-1/2 lg:w-1/3">
            <div
              class="relative z-10 mb-10 overflow-hidden bg-white dark:bg-dark-2 py-12 px-6 text-center shadow-pricing-7 sm:px-12 lg:px-6 xl:px-[50px]"
            >
              <div class="mb-8 border-b border-stroke dark:border-dark-3 pb-8">
                <span
                  class="mb-[14px] block leading-[28px] text-[22px] font-semibold text-dark dark:text-white"
                >
                  {{ plan.type }}
                </span>
                <p class="text-sm text-body-color dark:text-dark-6">
                  {{ plan.subtitle }}
                </p>
              </div>

              <div class="mb-11 space-y-[14px]">
                <template v-for="(item, index) in plan.features" :key="index">
                  <p class="text-base text-body-color dark:text-dark-6">
                    {{ item }}
                  </p>
                </template>
              </div>

              <h2
                class="mb-6 text-4xl font-bold text-dark dark:text-white xl:leading-[1.21] xl:text-[42px]"
              >
                <sup class="text-xl font-medium text-body-color dark:text-dark-6 -top-5">$</sup>
                <span>{{ plan.price }}</span>
                <span class="text-base font-medium text-body-color dark:text-dark-6"> /month </span>
              </h2>

              <a
                href="javascript:void(0)"
                :class="{
                  ' mb-3 inline-block rounded-md border border-primary bg-primary py-[11px] px-9 xl:px-[66px] text-center text-base font-medium text-white transition hover:bg-blue-dark':
                    plan.popular,
                  'mb-3 inline-block rounded-md border border-primary bg-transparent py-[11px] px-9 xl:px-[66px] text-center text-base font-medium text-primary transition hover:bg-primary hover:text-white ':
                    !plan.popular
                }"
              >
                {{ plan.button.text }}
              </a>
              <p class="text-sm text-body-color dark:text-dark-6">
                {{ plan.subscription }}
              </p>

              <div v-if="plan.popular">
                <p
                  class="absolute top-5 -right-9 inline-flex rotate-45 bg-primary py-2 px-12 text-base font-medium text-white"
                >
                  Popular
                </p>
              </div>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>

  <!-- ====== Pricing Section End -->
</template>
