import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from '../routes'

app = createApp(App)
app.mount('#app')
app.use(router)
