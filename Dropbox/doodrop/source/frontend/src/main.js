import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from './views/Dashboard.vue'
import PetProfile from './views/PetProfile.vue'

const routes = [
  { path: '/', component: Dashboard },
  { path: '/pets/:id', component: PetProfile }
]
const router = createRouter({ history: createWebHistory(), routes })

createApp(App).use(router).mount('#app')