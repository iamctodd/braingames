<script setup lang="ts">
import { ref, onMounted, onUnmounted  } from 'vue';
import type { Ref } from 'vue';

interface DropdownOpen {
  [key: number]: boolean;
}

const dropdownOpen: Ref<DropdownOpen> = ref({});

const toggleDropdown = (index: number) => {
  dropdownOpen.value[index] = !dropdownOpen.value[index];
};

const closeDropdown = (index: number) => {
  dropdownOpen.value[index] = false;
};

const clickHandler = ({ target }: { target: EventTarget | null }) => {
  if (!target) return;
  const dropdownButtons = document.querySelectorAll('.dropdown');
  dropdownButtons.forEach((button, index) => {
    const dropdown = button.nextElementSibling;
    if (!dropdown || (!dropdownOpen.value[index] && !dropdown.contains(target as Node))) return;
    toggleDropdown(index);
  });
};

const keyHandler = ({ keyCode }: { keyCode: number }) => {
  if (keyCode !== 27) return;
  Object.keys(dropdownOpen.value).map(Number).forEach((index) => {
    if (dropdownOpen.value[index]) {
      closeDropdown(index);
    }
  });
};

onMounted(() => {
  document.addEventListener('click', clickHandler);
  document.addEventListener('keydown', keyHandler);
});

onUnmounted(() => {
  document.removeEventListener('click', clickHandler);
  document.removeEventListener('keydown', keyHandler);
});


const gridItems = ref([
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/application/images/table-grids/table-grid-03/image-01.jpg',
    name: 'Modern Lounge Chair',
    details: 'Lorem ipsum dolor sit amet, consecte adipiscing elit.',
    color: 'Color: White',
    price: '158.99$',
    link: '/'
  },
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/application/images/table-grids/table-grid-03/image-01.jpg',
    name: 'Modern Lounge Chair',
    details: 'Lorem ipsum dolor sit amet, consecte adipiscing elit.',
    color: 'Color: White',
    price: '158.99$',
    link: '/'
  },
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/application/images/table-grids/table-grid-03/image-01.jpg',
    name: 'Modern Lounge Chair',
    details: 'Lorem ipsum dolor sit amet, consecte adipiscing elit.',
    color: 'Color: White',
    price: '158.99$',
    link: '/'
  },
  {
    image:
      'https://cdn.tailgrids.com/2.0/image/application/images/table-grids/table-grid-03/image-01.jpg',
    name: 'Modern Lounge Chair',
    details: 'Lorem ipsum dolor sit amet, consecte adipiscing elit.',
    color: 'Color: White',
    price: '158.99$',
    link: '/'
  }
])
</script>

<template>
  <!-- ====== Table Grid Section Start -->
  <section class="bg-gray-2 pt-[120px] pb-[90px] dark:bg-dark">
    <div class="px-4 mx-auto sm:container">
      <div class="mb-9">
        <h2 class="mb-2 text-2xl font-semibold text-dark dark:text-white sm:text-[28px]">
          Latest Items
        </h2>
        <p class="text-base text-body-color dark:text-dark-6">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        </p>
      </div>

      <div class="flex flex-wrap -mx-4">
        <template v-for="(item, index) in gridItems" :key="index">
          <div class="w-full px-4 lg:w-1/2">
            <div
              class="relative mb-8 items-center rounded-lg bg-white p-3 shadow-1 duration-300 hover:shadow-none dark:bg-dark-2 dark:shadow-3 sm:flex"
            >
              <div
                class="mb-4 mr-6 h-[166px] w-full max-w-[166px] overflow-hidden rounded sm:mb-0 lg:h-[120px] lg:max-w-[120px] xl:h-[166px] xl:max-w-[166px]"
              >
                <img :src="item.image" alt="table grid" class="aspect-square h-full w-full" />
              </div>

              <div class="w-full">
                <a
                  href="{{item.link}}"
                  class="text-base font-semibold text-dark hover:text-primary dark:text-white sm:text-xl lg:text-lg xl:text-xl"
                >
                  {{ item.name }}
                </a>
                <p class="mb-4 text-base text-body-color dark:text-dark-6">{{ item.details }}</p>
                <div class="flex items-center space-x-6">
                  <p class="text-base font-medium text-body-color dark:text-dark-6">
                    {{ item.color }}
                  </p>
                  <p class="text-lg font-semibold text-dark dark:text-white">{{ item.price }}</p>
                </div>
              </div>

              <div class="absolute right-4 top-4">
                <button @click.stop="toggleDropdown(index)" class="text-secondary-color dropdown">
                  <svg width="18" height="18" viewBox="0 0 18 18" class="fill-current">
                    <g clipPath="url(#clip0_3019_3039)">
                      <path
                        d="M15.75 6.75C14.5074 6.75 13.5 7.75736 13.5 9C13.5 10.2426 14.5074 11.25 15.75 11.25C16.9926 11.25 18 10.2426 18 9C18 7.75736 16.9926 6.75 15.75 6.75Z"
                      />
                      <path
                        d="M9 6.75C7.75736 6.75 6.75 7.75736 6.75 9C6.75 10.2426 7.75736 11.25 9 11.25C10.2426 11.25 11.25 10.2426 11.25 9C11.25 7.75736 10.2426 6.75 9 6.75Z"
                      />
                      <path
                        d="M2.25 6.75C1.00736 6.75 3.05336e-07 7.75736 1.96701e-07 9C8.80661e-08 10.2426 1.00736 11.25 2.25 11.25C3.49264 11.25 4.5 10.2426 4.5 9C4.5 7.75736 3.49264 6.75 2.25 6.75Z"
                      />
                    </g>
                    <defs>
                      <clipPath id="clip0_3019_3039">
                        <rect
                          width="18"
                          height="18"
                          fill="white"
                          transform="translate(18 18) rotate(-180)"
                        />
                      </clipPath>
                    </defs>
                  </svg>
                </button>

                <div
                  v-if="dropdownOpen[index]" 
                  @click.stop="closeDropdown(index)"
                  class="absolute right-0 top-full z-40 w-[200px] space-y-1 rounded bg-white p-2 shadow-card dark:bg-dark"
                >
                  <button
                    @click.stop="closeDropdown(index)"
                    class="w-full rounded px-3 py-2 text-left text-sm text-body-color hover:bg-gray-2 dark:text-dark-6 dark:hover:bg-dark-2"
                  >
                    Add to cart
                  </button>
                  <button
                    @click.stop="closeDropdown(index)"
                    class="w-full rounded px-3 py-2 text-left text-sm text-body-color hover:bg-gray-2 dark:text-dark-6 dark:hover:bg-dark-2"
                  >
                    Add to favorite
                  </button>
                </div>
              </div>
            </div>
          </div>
        </template>
      </div>
    </div>
  </section>
  <!-- ====== Table Grid Section End -->
</template>
