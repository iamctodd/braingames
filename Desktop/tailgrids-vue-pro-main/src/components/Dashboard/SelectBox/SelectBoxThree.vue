<script setup lang="ts">
import { ref } from 'vue';

const selectedAddress = ref(1);
</script>

<template>
  <!-- ====== Box Select Section Start -->
  <section class="bg-gray-2 dark:bg-dark py-20 lg:py-[120px]">
    <div class="container mx-auto">
      <div>
        <h3 class="mb-6 text-lg font-semibold text-dark dark:text-white">
          Select Delivery Option
        </h3>
        <div class="flex flex-wrap">
          <!-- Same as Personal Address Option -->
          <div class="mr-6 w-full max-w-[240px]">
            <div class="mb-3">
              <input type="radio" name="shippingAddress" id="shippingAddress1" class="shipping select-box sr-only" v-model="selectedAddress" :value="1" />
              <label for="shippingAddress1" class="block cursor-pointer overflow-hidden rounded-lg border border-stroke dark:border-dark-3 bg-white dark:bg-dark-2 py-5 px-4 lg:px-4 xl:px-6">
                <span class="title mb-[6px] block text-base font-semibold text-dark dark:text-white">
                  Same as Personal
                </span>
                <span class="block text-sm text-dark dark:text-white">
                  New York, USA <br />
                  2707 Davis Avenue
                </span>
              </label>
            </div>
          </div>
          <!-- End Same as Personal Address Option -->

          <!-- Register Now Address Option -->
          <div class="w-full max-w-[240px]">
            <div class="mb-3">
              <input type="radio" name="shippingAddress" id="shippingAddress2" class="shipping select-box sr-only" v-model="selectedAddress" :value="2" />
              <label for="shippingAddress2" class="block cursor-pointer overflow-hidden rounded-lg border border-stroke dark:border-dark-3 bg-white dark:bg-dark-2 py-5 px-4 lg:px-4 xl:px-6">
                <span class="title mb-[6px] block text-base font-semibold text-dark dark:text-white">
                  Register Now
                </span>
                <span class="block text-sm text-body-color dark:text-dark-6">
                  Create an account now to have multiple addresses.
                </span>
              </label>
            </div>
          </div>
          <!-- End Register Now Address Option -->
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Box Select Section End -->
</template>
