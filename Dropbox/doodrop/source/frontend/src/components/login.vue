<template>
  <form @submit.prevent="onSubmit">
    <input v-model="email" placeholder="Email" />
    <input v-model="password" type="password" placeholder="Password" />
    <button>Login</button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import api, { setAuthToken } from '../api/api'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const router = useRouter()

async function onSubmit(){
  const res = await api.post('/users/login', { email: email.value, password: password.value })
  const token = res.data.token
  setAuthToken(token)
  localStorage.setItem('doodrop_token', token)
  router.push('/')
}
</script>