<script setup lang="ts">
import { ref } from 'vue'

const pricingPlans = ref([
  {
    dotShape: 'text-secondary',
    type: 'Starter',
    price: '25',
    button: {
      text: 'Purchase Now',
      bg: 'bg-secondary'
    },
    features: [
      'Core UI Components',
      'Use on Unlimited Projects',
      'Personal and Commercial Use',
      'Lifetime Free Updates',
      'Figma Source File'
    ]
  },
  {
    dotShape: 'text-primary',
    type: 'Business',
    price: '59',
    button: {
      text: 'Purchase Now',
      bg: 'bg-primary'
    },
    features: [
      'Core UI Components',
      'Use on Unlimited Projects',
      'Personal and Commercial Use',
      'Lifetime Free Updates',
      'Figma Source File'
    ]
  },
  {
    dotShape: 'text-dark',
    type: 'Extended',
    price: '199',
    button: {
      text: 'Purchase Now',
      bg: 'bg-dark'
    },
    features: [
      'Core UI Components',
      'Use on Unlimited Projects',
      'Personal and Commercial Use',
      'Lifetime Free Updates',
      'Figma Source File'
    ]
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
            <span class="mb-2 block text-lg font-semibold text-primary"> Pricing Table </span>
            <h2
              class="mb-4 text-3xl leading-[1.208] font-bold text-dark dark:text-white sm:text-4xl md:text-[40px]"
            >
              Our Pricing Plan
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
              class="relative z-10 mb-10 overflow-hidden rounded-xl bg-white dark:bg-dark-2 py-10 px-8 text-center shadow-pricing-5 sm:p-12 lg:py-10 lg:px-6 xl:p-14"
            >
              <span class="mb-4 block text-xl font-medium text-dark dark:text-white">
                {{ plan.type }}
              </span>
              <h2
                class="mb-10 xl:mb-[50px] text-4xl font-semibold text-dark dark:text-white xl:leading-[1.24] xl:text-[42px]"
              >
                <sup class="text-xl font-medium -top-5">$</sup>
                <span class="px-0.5">{{ plan.price }}</span>
                <span class="text-base text-body-color dark:text-dark-6"> Month </span>
              </h2>
              <div class="mb-11 space-y-[14px]">
                <template v-for="(item, index) in plan.features" :key="index">
                  <p class="text-base text-body-color dark:text-dark-6">{{ item }}</p>
                </template>
              </div>
              <a
                href="javascript:void(0)"
                class="inline-block rounded-md py-[13px] px-7 text-center text-base font-medium text-white transition hover:bg-opacity-90"
                :class="plan.button.bg"
              >
                {{ plan.button.text }}
              </a>

              <div>
                <span class="absolute bottom-3 left-3 -z-10" :class="plan.dotShape">
                  <svg width="28" height="64" viewBox="0 0 28 64" class="fill-current">
                    <circle
                      cx="26.4157"
                      cy="62.489"
                      r="1.42021"
                      transform="rotate(180 26.4157 62.489)"
                    />
                    <circle
                      cx="26.4157"
                      cy="38.3454"
                      r="1.42021"
                      transform="rotate(180 26.4157 38.3454)"
                    />
                    <circle
                      cx="26.4157"
                      cy="13.6335"
                      r="1.42021"
                      transform="rotate(180 26.4157 13.6335)"
                    />
                    <circle
                      cx="26.4157"
                      cy="50.2751"
                      r="1.42021"
                      transform="rotate(180 26.4157 50.2751)"
                    />
                    <circle
                      cx="26.4157"
                      cy="26.1315"
                      r="1.42021"
                      transform="rotate(180 26.4157 26.1315)"
                    />
                    <circle
                      cx="26.4157"
                      cy="1.42012"
                      r="1.42021"
                      transform="rotate(180 26.4157 1.42012)"
                    />
                    <circle
                      cx="13.9177"
                      cy="62.489"
                      r="1.42021"
                      transform="rotate(180 13.9177 62.489)"
                    />
                    <circle
                      cx="13.9177"
                      cy="38.3454"
                      r="1.42021"
                      transform="rotate(180 13.9177 38.3454)"
                    />
                    <circle
                      cx="13.9177"
                      cy="13.6335"
                      r="1.42021"
                      transform="rotate(180 13.9177 13.6335)"
                    />
                    <circle
                      cx="13.9177"
                      cy="50.2751"
                      r="1.42021"
                      transform="rotate(180 13.9177 50.2751)"
                    />
                    <circle
                      cx="13.9177"
                      cy="26.1315"
                      r="1.42021"
                      transform="rotate(180 13.9177 26.1315)"
                    />
                    <circle
                      cx="13.9177"
                      cy="1.42012"
                      r="1.42021"
                      transform="rotate(180 13.9177 1.42012)"
                    />
                    <circle
                      cx="1.41963"
                      cy="62.489"
                      r="1.42021"
                      transform="rotate(180 1.41963 62.489)"
                    />
                    <circle
                      cx="1.41963"
                      cy="38.3454"
                      r="1.42021"
                      transform="rotate(180 1.41963 38.3454)"
                    />
                    <circle
                      cx="1.41963"
                      cy="13.6335"
                      r="1.42021"
                      transform="rotate(180 1.41963 13.6335)"
                    />
                    <circle
                      cx="1.41963"
                      cy="50.2751"
                      r="1.42021"
                      transform="rotate(180 1.41963 50.2751)"
                    />
                    <circle
                      cx="1.41963"
                      cy="26.1315"
                      r="1.42021"
                      transform="rotate(180 1.41963 26.1315)"
                    />
                    <circle
                      cx="1.41963"
                      cy="1.42012"
                      r="1.42021"
                      transform="rotate(180 1.41963 1.42012)"
                    />
                  </svg>
                </span>
                <span class="absolute top-3 right-3 -z-10" :class="plan.dotShape">
                  <svg width="28" height="64" viewBox="0 0 28 64" class="fill-current">
                    <circle
                      cx="26.4157"
                      cy="62.489"
                      r="1.42021"
                      transform="rotate(180 26.4157 62.489)"
                    />
                    <circle
                      cx="26.4157"
                      cy="38.3454"
                      r="1.42021"
                      transform="rotate(180 26.4157 38.3454)"
                    />
                    <circle
                      cx="26.4157"
                      cy="13.6335"
                      r="1.42021"
                      transform="rotate(180 26.4157 13.6335)"
                    />
                    <circle
                      cx="26.4157"
                      cy="50.2751"
                      r="1.42021"
                      transform="rotate(180 26.4157 50.2751)"
                    />
                    <circle
                      cx="26.4157"
                      cy="26.1315"
                      r="1.42021"
                      transform="rotate(180 26.4157 26.1315)"
                    />
                    <circle
                      cx="26.4157"
                      cy="1.42012"
                      r="1.42021"
                      transform="rotate(180 26.4157 1.42012)"
                    />
                    <circle
                      cx="13.9177"
                      cy="62.489"
                      r="1.42021"
                      transform="rotate(180 13.9177 62.489)"
                    />
                    <circle
                      cx="13.9177"
                      cy="38.3454"
                      r="1.42021"
                      transform="rotate(180 13.9177 38.3454)"
                    />
                    <circle
                      cx="13.9177"
                      cy="13.6335"
                      r="1.42021"
                      transform="rotate(180 13.9177 13.6335)"
                    />
                    <circle
                      cx="13.9177"
                      cy="50.2751"
                      r="1.42021"
                      transform="rotate(180 13.9177 50.2751)"
                    />
                    <circle
                      cx="13.9177"
                      cy="26.1315"
                      r="1.42021"
                      transform="rotate(180 13.9177 26.1315)"
                    />
                    <circle
                      cx="13.9177"
                      cy="1.42012"
                      r="1.42021"
                      transform="rotate(180 13.9177 1.42012)"
                    />
                    <circle
                      cx="1.41963"
                      cy="62.489"
                      r="1.42021"
                      transform="rotate(180 1.41963 62.489)"
                    />
                    <circle
                      cx="1.41963"
                      cy="38.3454"
                      r="1.42021"
                      transform="rotate(180 1.41963 38.3454)"
                    />
                    <circle
                      cx="1.41963"
                      cy="13.6335"
                      r="1.42021"
                      transform="rotate(180 1.41963 13.6335)"
                    />
                    <circle
                      cx="1.41963"
                      cy="50.2751"
                      r="1.42021"
                      transform="rotate(180 1.41963 50.2751)"
                    />
                    <circle
                      cx="1.41963"
                      cy="26.1315"
                      r="1.42021"
                      transform="rotate(180 1.41963 26.1315)"
                    />
                    <circle
                      cx="1.41963"
                      cy="1.42012"
                      r="1.42021"
                      transform="rotate(180 1.41963 1.42012)"
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
