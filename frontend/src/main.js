import { createApp } from 'vue'
import './style.css'
import 'github-markdown-css/github-markdown-dark.css'
import App from './App.vue'
import router from './routes.js'

const app = createApp(App)
app.use(router)
app.mount('#app')
