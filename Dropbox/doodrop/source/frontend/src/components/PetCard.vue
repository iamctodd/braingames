<template>
  <div class="pet-card">
    <h3>{{ pet.name }}</h3>
    <div>{{ pet.species }} — {{ pet.breed }}</div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
const props = defineProps({ pet: Object })
</script>