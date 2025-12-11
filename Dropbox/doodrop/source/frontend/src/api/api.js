import axios from 'axios'

const api = axios.create({ baseURL: '/api/v1' })

export function setAuthToken(token){
  api.defaults.headers.common['Authorization'] = `Bearer ${token}`
}

export default api