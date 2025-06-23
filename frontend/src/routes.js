import { createRouter, createWebHistory } from "vue-router";
import Home from "./pages/Home.vue"
import Post from "./pages/Post.vue"
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
    },
    {
      path: "/posts/:slug",
      name: "post",
      component: Post,
      props: true
    },
  ],
});

export default router;
