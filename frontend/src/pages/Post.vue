<script setup>
import {ref,onMounted,watch} from "vue"
import axios from "axios"
import MarkdownIt from "markdown-it"

const props = defineProps({
  slug: {
    type: String,
    required: true
  }
})
const postContent = ref("")
const postTitle = ref("Yükleniyor...")
const md = new MarkdownIt()

const fetchPost = async(currentSlug) => {
    const response = await axios.get(`http://localhost:8000/posts/${currentSlug}`)
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
  <div class="container mx-auto p-4">
    <!-- Ana sayfaya geri dönme linki -->
    <router-link to="/" class="text-blue-600 hover:underline mb-4 inline-block">&larr; Tüm Yazılara Geri Dön</router-link>
    
    <!-- Yazı Başlığı -->
    <h1 class="text-4xl font-bold text-gray-800 mb-6">{{ postTitle }}</h1>
    
    <!-- Markdown içeriğinin render edileceği alan -->
    <!-- 'prose' sınıfı Tailwind Typography eklentisinden gelir ve Markdown'ı güzelce stilize eder -->
    <div class="prose lg:prose-xl max-w-none bg-white p-6 rounded-lg shadow-md">
      <div v-html="postContent"></div>
    </div>
  </div>
</template>