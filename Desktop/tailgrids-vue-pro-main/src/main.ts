import VueApexCharts from 'vue3-apexcharts'

import 'swiper/swiper-bundle.css'
import './assets/style.css'

import { createPinia } from 'pinia'
import { createApp } from 'vue'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(VueApexCharts)
app.use(createPinia())
app.use(router)

app.mount('#app')
