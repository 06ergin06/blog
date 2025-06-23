<script setup>
import { ref, onMounted } from 'vue';
import axios from "axios"

const posts = ref([]);

onMounted(async() => {
    const response = await axios.get("http://localhost:8000/posts")
    posts.value = response.data.posts
})
</script>

<template>
    <div v-for="post in posts" :key="post">{{ post }}</div>
</template>