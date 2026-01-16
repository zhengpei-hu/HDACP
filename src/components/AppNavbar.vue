<script setup>
import { RouterLink } from 'vue-router'

const navItems = [
  { path: '/', name: '主页' },
  { path: '/research', name: '研究介绍' },
  { path: '/team', name: '科研团队' },
  { path: '/news', name: '新闻动态' },
  { path: '/projects', name: '科研项目' },
  { path: '/papers', name: '论文发表' },
  { path: '/life', name: '科研成果' },
  { path: '/contact', name: '联系我们' }
]
</script>

<template>
  <nav class="navbar">
    <div class="container nav-container">
      <ul class="nav-links">
        <li v-for="item in navItems" :key="item.path">
          <router-link :to="item.path" class="nav-link" active-class="active">
            {{ item.name }}
          </router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  background: var(--bg-glass);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  padding: 0;
  position: sticky;
  top: 0;
  z-index: 1000;
  box-shadow: var(--shadow-sm);
  border-bottom: 1px solid rgba(229, 231, 235, 0.5);
}

.nav-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 60px;
}

.nav-links {
  display: flex;
  gap: 30px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.nav-link {
  color: var(--text-main);
  text-decoration: none;
  font-weight: 500;
  font-size: 1rem;
  padding: 8px 12px;
  border-radius: 6px;
  transition: all 0.3s ease;
}

.nav-link:hover, .nav-link.active {
  color: var(--primary-color);
  background: var(--primary-light);
}

@media (max-width: 768px) {
  .nav-links {
    gap: 15px;
    font-size: 0.9rem;
  }
}
</style>
