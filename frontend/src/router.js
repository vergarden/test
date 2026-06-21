import { createRouter, createWebHistory } from 'vue-router'
import SelfIntro from './components/SelfIntro.vue'
import Guestbook from './components/Guestbook.vue'
import Contact from './components/Contact.vue'

const routes = [
  { path: '/', redirect: '/intro' },
  { path: '/intro', name: 'intro', component: SelfIntro },
  { path: '/guestbook', name: 'guestbook', component: Guestbook },
  { path: '/contact', name: 'contact', component: Contact },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
