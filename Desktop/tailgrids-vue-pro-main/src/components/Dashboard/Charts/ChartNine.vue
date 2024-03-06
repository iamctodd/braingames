<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'
import VueApexCharts from 'vue3-apexcharts'

const dropdownOpen = ref(false)
const dropdownButtonRef = ref<HTMLButtonElement | null>(null)

const toggleDropdown = () => {
  dropdownOpen.value = !dropdownOpen.value
}

// Custom composition function to handle click outside
const handleClickOutside = (event: MouseEvent) => {
  if (dropdownButtonRef.value && !dropdownButtonRef.value.contains(event.target as Node)) {
    dropdownOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})

const chartData = {
  series: [72]
}

const chart = ref(null)

const apexOptions = {
  chart: {
    fontFamily: 'Inter, sans-serif',
    height: 300,
    type: 'radialBar'
  },
  responsive: [
    {
      breakpoint: 1024,
      options: {
        chart: {
          height: 180
        },
        plotOptions: {
          radialBar: {
            dataLabels: {
              total: {
                fontSize: '12px'
              }
            }
          }
        }
      }
    },
    {
      breakpoint: 1280,
      options: {
        chart: {
          height: 250
        }
      }
    }
  ],
  plotOptions: {
    radialBar: {
      hollow: {
        size: '70%'
      },
      dataLabels: {
        name: {
          fontSize: '22px'
        },
        value: {
          fontSize: '24px',
          fontFamily: "'Inter'",
          fontWeight: 'bold',
          offsetY: 8
        },
        total: {
          show: true,
          fontSize: '16px',
          label: 'Conversion Rate',
          fontFamily: "'Inter'"
        }
      }
    }
  },
  dataLabels: {
    enabled: true
  },
  colors: ['#3758F9'],
  legend: {
    show: false,
    position: 'bottom'
  }
}
</script>

<template>
  <!-- ====== Chart Section Start -->
  <section class="bg-gray-2 dark:bg-dark py-20 lg:py-[120px]">
    <div class="mx-auto px-4 md:container">
      <div
        class="mx-auto w-full max-w-[500px] rounded-lg border border-stroke dark:border-dark-3 bg-white dark:bg-dark-2 px-5 pt-[30px] pb-5 sm:px-[30px]"
      >
        <div class="flex justify-between">
          <div>
            <h5 class="text-sm font-semibold text-dark dark:text-white">Conversion Details</h5>
            <p class="text-xs text-body-color dark:text-dark-6">your total sales data analytics</p>
          </div>
          <div>
            <div class="relative">
              <button
                class="text-body-color dark:text-dark-6"
                @click="toggleDropdown"
                ref="dropdownButtonRef"
              >
                <svg
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                  class="fill-current"
                >
                  <path
                    d="M5 14C6.10457 14 7 13.1046 7 12C7 10.8954 6.10457 10 5 10C3.89543 10 3 10.8954 3 12C3 13.1046 3.89543 14 5 14Z"
                  />
                  <path
                    d="M12 14C13.1046 14 14 13.1046 14 12C14 10.8954 13.1046 10 12 10C10.8954 10 10 10.8954 10 12C10 13.1046 10.8954 14 12 14Z"
                  />
                  <path
                    d="M19 14C20.1046 14 21 13.1046 21 12C21 10.8954 20.1046 10 19 10C17.8954 10 17 10.8954 17 12C17 13.1046 17.8954 14 19 14Z"
                  />
                </svg>
              </button>
              <div
                v-show="dropdownOpen"
                class="absolute right-0 top-full z-40 w-[200px] space-y-1 rounded bg-white dark:bg-dark p-2 shadow-card"
              >
                <button
                  class="w-full rounded py-2 px-3 text-left text-sm text-body-color dark:text-dark-6 hover:bg-gray-2 dark:hover:bg-dark-2"
                >
                  Edit
                </button>
                <button
                  class="w-full rounded py-2 px-3 text-left text-sm text-body-color dark:text-dark-6 hover:bg-gray-2 dark:hover:bg-dark-2"
                >
                  Delete
                </button>
              </div>
            </div>
          </div>
        </div>
        <div>
          <div id="chartOne" class="-ml-5">
            <VueApexCharts
              type="radialBar"
              height="300"
              :options="apexOptions"
              :series="chartData.series"
              ref="chart"
            />
          </div>
        </div>
        <div>
          <p
            class="flex flex-wrap items-center justify-center text-xs font-medium text-body-color dark:text-dark-6"
          >
            <span
              class="mr-0.5 flex h-5 w-5 items-center justify-center rounded-full bg-[#E6F9EC] dark:bg-green-light-4 text-green"
            >
              <svg
                width="14"
                height="14"
                viewBox="0 0 14 14"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M6.464 4.76249L3.59043 7.63606L2.83293 6.87856L6.99972 2.71178L11.1665 6.87856L10.409 7.63606L7.53543 4.76249L7.53543 11.2832L6.464 11.2832L6.464 4.76249Z"
                  fill="currentcolor"
                />
              </svg>
            </span>
            <span class="text-green text-sm"> (+8%) </span>
            <span class="pl-1">Compared to prev month</span>
          </p>
        </div>
      </div>
    </div>
  </section>
  <!-- ====== Chart Section End -->
</template>
