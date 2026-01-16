<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import researchData from '@/data/research.json'

const route = useRoute()

const directions = researchData.directions

const activeId = computed(() => {
  return route.params.id || directions[0]?.id || 'hpc'
})

const activeDirection = computed(() => {
  return directions.find(d => d.id === activeId.value) || directions[0]
})
</script>

<template>
  <div class="research-page">
    <div class="container">
      <div class="section-title">
        <h3>研究方向</h3>
      </div>
      
      <div class="research-layout">
        <!-- Sidebar Navigation -->
        <aside class="sidebar">
          <nav class="sidebar-nav">
            <RouterLink 
              v-for="item in directions" 
              :key="item.id"
              :to="`/research/${item.id}`"
              class="sidebar-item"
              :class="{ active: item.id === activeId }"
            >
              {{ item.name }}
            </RouterLink>
          </nav>
        </aside>
        
        <!-- Content Area -->
        <main class="content">
          <div class="content-card">
            <h2 class="content-title">{{ activeDirection.name }}</h2>
            
            <div class="content-intro">
              <h4>方向介绍：</h4>
              <p>{{ activeDirection.description }}</p>
            </div>
            
            <div class="content-body">
              <p v-for="(para, index) in activeDirection.content.split('\n\n')" :key="index">
                {{ para }}
              </p>
            </div>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<style scoped>
.research-page {
  padding: 30px 0 50px;
}

.research-layout {
  display: grid;
  grid-template-columns: 220px 1fr;
  gap: 30px;
  margin-top: 20px;
}

/* Sidebar */
.sidebar {
  position: sticky;
  top: 80px;
  height: fit-content;
}

.sidebar-nav {
  background: var(--bg-light);
  border-radius: 12px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.sidebar-item {
  display: block;
  padding: 14px 18px;
  font-size: 0.95rem;
  font-weight: 500;
  color: var(--primary-color);
  border-radius: 8px;
  transition: all var(--transition-fast);
  text-decoration: none;
}

.sidebar-item:hover {
  background: rgba(80, 125, 188, 0.1);
}

.sidebar-item.active {
  background: var(--primary-color);
  color: #fff;
}

/* Content */
.content {
  min-height: 500px;
}

.content-card {
  background: #fff;
  border-radius: 12px;
  padding: 30px;
  box-shadow: var(--shadow-sm);
}

.content-title {
  font-size: 1.5rem;
  color: var(--primary-color);
  margin-bottom: 24px;
  padding-bottom: 12px;
  border-bottom: 2px solid var(--border-color);
}

.content-intro {
  margin-bottom: 24px;
}

.content-intro h4 {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-color);
  margin-bottom: 12px;
}

.content-intro p {
  font-size: 0.95rem;
  line-height: 1.8;
  color: var(--text-color);
  text-indent: 2em;
}

.content-body p {
  font-size: 0.95rem;
  line-height: 1.8;
  color: var(--text-color);
  margin-bottom: 16px;
  text-indent: 2em;
}

.content-body p:last-child {
  margin-bottom: 0;
}

/* Responsive */
@media (max-width: 768px) {
  .research-layout {
    grid-template-columns: 1fr;
  }
  
  .sidebar {
    position: static;
  }
  
  .sidebar-nav {
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
  }
  
  .sidebar-item {
    padding: 10px 16px;
    font-size: 0.9rem;
  }
  
  .content-card {
    padding: 20px;
  }
}
</style>
