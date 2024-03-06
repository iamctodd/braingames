<script setup lang="ts">
import { ref } from 'vue'

const pricingPlans = ref([
  {
    type: 'Starter',
    price: '25.00',
    features: {
      users: 'Up to 1 User',
      components: 'All UI components',
      access: 'Lifetime access',
      updates: 'Free updates'
    },
    button: {
      text: 'Purchase Now'
    }
  },
  {
    popular: true,
    type: 'Basic',
    price: '59.00',
    features: {
      users: 'Up to 1 User',
      components: 'All UI components',
      access: 'Lifetime access',
      updates: 'Free updates'
    },
    button: {
      text: 'Purchase Now'
    }
  },
  {
    type: 'Premium',
    price: '99.00',
    features: {
      users: 'Up to 1 User',
      components: 'All UI components',
      access: 'Lifetime access',
      updates: 'Free updates'
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
          <div class="mx-auto mb-[60px] max-w-[510px] text-center">
            <span class="mb-2 block text-lg font-semibold text-primary"> Pricing Table </span>
            <h2
              class="mb-3 text-3xl font-bold text-dark dark:text-white sm:text-4xl md:text-[40px]"
            >
              Awesome Pricing Plan
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
              class="relative z-10 mb-10 overflow-hidden rounded-xl bg-white dark:bg-dark-2 py-10 px-8 shadow-pricing-2 sm:p-12 lg:py-10 lg:px-6 xl:p-14"
            >
              <p
                class="absolute right-[-50px] top-[60px] inline-block -rotate-90 rounded-tl-md rounded-bl-md bg-primary py-2 px-5 text-base font-medium text-white"
                v-if="plan.popular"
              >
                Recommended
              </p>

              <span class="mb-5 block text-xl font-medium text-dark dark:text-white">
                {{ plan.type }}
              </span>

              <h2 class="mb-11 text-4xl font-semibold text-dark dark:text-white xl:text-[42px]">
                <span class="text-xl font-medium">$</span>
                <span class="px-0.5">{{ plan.price }}</span>
                <span class="text-base text-body-color dark:text-dark-6"> Per Month </span>
              </h2>

              <div class="mb-[50px]">
                <h5 class="mb-5 text-lg font-medium text-dark dark:text-white">Features</h5>

                <div class="flex flex-col gap-[14px]">
                  <p class="text-base text-body-color dark:text-dark-6">
                    {{ plan.features.users }}
                  </p>
                  <p class="text-base text-body-color dark:text-dark-6">
                    {{ plan.features.components }}
                  </p>
                  <p class="text-base text-body-color dark:text-dark-6">
                    {{ plan.features.access }}
                  </p>
                  <p class="text-base text-body-color dark:text-dark-6">
                    {{ plan.features.updates }}
                  </p>
                </div>
              </div>

              <a
                href="javascript:void(0)"
                class="inline-block rounded-md bg-primary py-3 px-7 text-center text-base font-medium text-white transition hover:bg-blue-dark"
              >
                {{ plan.button.text }}
              </a>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>
  <!-- ====== Pricing Section End -->
</template>
