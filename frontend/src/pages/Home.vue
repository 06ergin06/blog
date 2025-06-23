<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const posts = ref([]);

onMounted(async () => {
  const response = await axios.get("http://localhost:8000/posts");
  posts.value = response.data.posts;
});
</script>

<template>
  <div class="min-h-screen bg-neutral-900 text-gray-300 p-8">
    <div class="max-w-2xl mx-auto">
      <h1 class="text-3xl font-bold text-white mb-8 text-center">Blog Posts</h1>
      
      <div class="space-y-4">
        <div 
          v-for="post in posts" 
          :key="post"
          class="bg-gray-700 hover:bg-gray-600 transition-colors duration-200 rounded-lg p-4 border border-gray-600"
        >
          <router-link 
            class="text-lg capitalize block"
            :to="{ name: 'post', params: { slug: post } }"
          >
            {{ post.replace(/-/g, ' ') }}
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>
