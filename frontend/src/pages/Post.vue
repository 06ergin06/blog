<script setup>
import {ref,onMounted,watch} from "vue"
import axios from "axios"
import MarkdownIt from "markdown-it"
import { API_BASE_URL } from "../config.js"

const props = defineProps({
  slug: {
    type: String,
    required: true
  }
})
const postContent = ref("")
const postTitle = ref("Yükleniyor...")

// MarkdownIt'i daha fazla özellikle yapılandır
const md = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true
})

const fetchPost = async(currentSlug) => {
    const response = await axios.get(`${API_BASE_URL}/posts/${currentSlug}`)
    postContent.value = md.render(response.data.content)
    postTitle.value = formatPostName(currentSlug)
}

const formatPostName = (name) => {
  return name.replace(/-/g, ' ').split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}

onMounted(() => {
    fetchPost(props.slug)
})

watch(() => props.slug, (newSlug) => {
  if (newSlug) {
    fetchPost(newSlug)
  }
})
</script>

<template>
  <div class="min-h-screen bg-neutral-900 text-gray-300 p-8">
    <div class="w-10/12 mx-auto">
      <!-- Ana sayfaya geri dönme linki -->
      <router-link 
        to="/" 
        class="text-blue-400 hover:text-blue-300 mb-6 inline-block transition-colors duration-200"
      >
        ← Tüm Yazılara Geri Dön
      </router-link>
      
      <!-- Yazı Başlığı -->
      <h1 class="text-3xl font-bold text-white mb-8">{{ postTitle }}</h1>
      
      <!-- Markdown içeriği -->
      <div class="bg-gray-800 border border-gray-600 rounded-lg p-6 markdown-body">
        <div v-html="postContent"></div>
      </div>
    </div>
  </div>
</template>

