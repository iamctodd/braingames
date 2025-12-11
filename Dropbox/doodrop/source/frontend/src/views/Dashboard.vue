<template>
  <div>
    <h1>DooDrop — Dashboard</h1>
    <div v-if="pets.length === 0">No pets yet</div>
    <div v-for="p in pets" :key="p.id">
      <PetCard :pet="p" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../api/api'
import PetCard from '../components/PetCard.vue'

const pets = ref([])

onMounted(async ()=>{
  try{
    const token = localStorage.getItem('doodrop_token')
    if(token) api.defaults.headers.common['Authorization'] = `Bearer ${token}`
    const res = await api.get('/pets')
    pets.value = res.data
  }catch(e){
    console.error(e)
  }
})
</script>