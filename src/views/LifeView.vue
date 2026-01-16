<script setup>
import { ref } from 'vue'
import lifeData from '@/data/life.json'

const activeTab = ref('academic')
const baseUrl = import.meta.env.BASE_URL

const tabs = [
  { id: 'academic', name: '学术交流' },
  { id: 'honors', name: '奖励荣誉' },
  { id: 'competitions', name: '科技竞赛' }
]
</script>

<template>
  <div class="life-page">
    <div class="container">
      <div class="section-title">
        <h3>科研成果</h3>
      </div>
      
      <div class="tabs">
        <button 
          v-for="tab in tabs" 
          :key="tab.id"
          :class="{ active: activeTab === tab.id }"
          @click="activeTab = tab.id"
        >
          {{ tab.name }}
        </button>
      </div>

      <!-- Academic Exchange -->
      <div v-if="activeTab === 'academic'" class="tab-content fade-in">
        <div v-for="(event, index) in lifeData.academic" :key="index" class="event-section">
          <h4 class="event-title">{{ event.event }}</h4>
          <div class="gallery-grid">
            <div v-for="(img, idx) in event.images" :key="idx" class="gallery-item">
              <img :src="`${baseUrl}images/life/academic/${img}`" :alt="event.event" />
            </div>
          </div>
        </div>
      </div>

      <!-- Honors -->
      <div v-if="activeTab === 'honors'" class="tab-content fade-in">
        <div v-for="(category, index) in lifeData.honors" :key="index" class="honor-section">
          <h4 class="category-title">{{ category.category }}</h4>
          <div class="gallery-grid">
            <div v-for="(img, idx) in category.images" :key="idx" class="gallery-item honor-item">
              <img :src="`${baseUrl}images/life/honors/${img}`" :alt="category.category" />
            </div>
          </div>
        </div>
      </div>

      <!-- Competitions -->
      <div v-if="activeTab === 'competitions'" class="tab-content fade-in">
        <div class="competitions-grid">
          <a 
            v-for="(comp, index) in lifeData.competitions" 
            :key="index" 
            :href="comp.link" 
            target="_blank" 
            rel="noopener noreferrer"
            class="competition-card"
          >
            <div class="comp-logo">
              <img :src="`${baseUrl}images/life/competitions/${comp.logo}`" :alt="comp.name" />
            </div>
          </a>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
.life-page {
  padding: 30px 0 50px;
}

.tabs {
  display: flex;
  gap: 10px;
  margin-bottom: 30px;
  border-bottom: 2px solid var(--border-color);
  padding-bottom: 0px;
  overflow-x: auto;
}

.tabs button {
  padding: 12px 24px;
  font-size: 1rem;
  font-weight: 500;
  color: var(--text-muted);
  background: none;
  border: none;
  cursor: pointer;
  position: relative;
  transition: all var(--transition-fast);
  white-space: nowrap;
}

.tabs button::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--primary-color);
  transform: scaleX(0);
  transition: transform var(--transition-fast);
}

.tabs button.active {
  color: var(--primary-color);
}

.tabs button.active::after {
  transform: scaleX(1);
}

/* Gallery Grid */
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 40px;
}

.gallery-item {
  border-radius: 8px;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: transform var(--transition-fast);
}

.gallery-item:hover {
  transform: scale(1.02);
  box-shadow: var(--shadow-md);
}

.gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.event-title, .category-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--primary-color);
  margin-bottom: 20px;
  padding-left: 10px;
  border-left: 4px solid var(--primary-color);
}

/* Competitions */
.competitions-grid {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 40px;
  padding: 40px 0;
}

.competition-card {
  display: block;
  width: 250px;
  padding: 20px;
  background: #fff;
  border-radius: 12px;
  box-shadow: var(--shadow-sm);
  transition: all var(--transition-normal);
  display: flex;
  align-items: center;
  justify-content: center;
}

.competition-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.comp-logo img {
  max-width: 100%;
  max-height: 100px;
  object-fit: contain;
}

.fade-in {
  animation: fadeIn 0.3s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
