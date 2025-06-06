import axios from 'axios'

export const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1/'
})

// Interceptor para suprimir erros de rede no console
api.interceptors.response.use(
  response => response,
  error => {
    // Retorna o erro sem mostrar no console
    return Promise.reject(error);
  }
);