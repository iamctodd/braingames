<script setup lang="ts">
import { ref } from 'vue';

const selectedShipping = ref(1);
</script>

<template>
  <!-- ====== Shipping Address Section Start -->
  <section class="bg-gray-2 dark:bg-dark py-20 lg:py-[120px]">
    <div class="container mx-auto">
      <div>
        <h3 class="mb-6 text-lg font-semibold text-dark dark:text-white">
          Shipping Address
        </h3>
        <div class="flex flex-wrap">
          <!-- FedEx Shipping Option -->
          <div class="mr-6 w-full max-w-[310px]">
            <div class="mb-3">
              <input type="radio" name="shipping" id="shipping1" class="shipping select-box sr-only" v-model="selectedShipping" :value="1" />
              <label for="shipping1" class="flex cursor-pointer items-center overflow-hidden rounded-lg border-2 border-transparent bg-white dark:bg-dark-2 p-[14px] shadow-1 dark:shadow-box-dark sm:px-[22px]">
                <div class="mr-5">
                  <img src="https://cdn.tailgrids.com/2.0/image/dashboard/images/box-select/box-select-02/fedex-express.svg" alt="fedex" class="h-[18px]" />
                </div>
                <div class="border-l border-stroke dark:border-dark-3 pl-5">
                  <span class="mb-1 block text-sm font-semibold text-dark dark:text-white sm:text-base">FedEx Fast Delivery</span>
                  <span class="block text-sm text-body-color dark:text-dark-6 mb-1">Delivery: Friday, 25</span>
                  <span class="block text-sm font-medium text-body-color dark:text-dark-6">$10.99</span>
                </div>
              </label>
            </div>
          </div>
          <!-- End FedEx Shipping Option -->

          <!-- DHL Shipping Option -->
          <div class="mr-6 w-full max-w-[285px]">
            <div class="mb-3">
              <input type="radio" name="shipping" id="shipping2" class="shipping select-box sr-only" v-model="selectedShipping" :value="2" />
              <label for="shipping2" class="flex cursor-pointer items-center overflow-hidden rounded-lg border-2 border-transparent bg-white dark:bg-dark-2 p-[14px] shadow-1 dark:shadow-box-dark sm:px-[22px]">
                <div class="mr-5">
                  <img src="https://cdn.tailgrids.com/2.0/image/dashboard/images/box-select/box-select-02/dhl-express.svg" alt="dhl" class="h-[18px]" />
                </div>
                <div class="border-l border-stroke dark:border-dark-3 pl-5">
                  <span class="mb-1 block text-sm font-semibold text-dark dark:text-white sm:text-base">DHL Fast Delivery</span>
                  <span class="block text-sm text-body-color dark:text-dark-6 mb-1">Delivery: Sunday, 27</span>
                  <span class="block text-sm font-medium text-body-color dark:text-dark-6">$10.99</span>
                </div>
              </label>
            </div>
          </div>
          <!-- End DHL Shipping Option -->
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Shipping Address Section End -->
</template>
