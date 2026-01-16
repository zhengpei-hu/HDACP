<script setup>
import { computed } from 'vue'
import publicationsData from '@/data/publications.json'

// Ensure data is sorted by year descending
const papersByYear = computed(() => {
  return publicationsData.map(group => ({
    ...group,
    year: parseInt(group.year)
  })).sort((a, b) => b.year - a.year)
})
</script>

<template>
  <div class="papers-page">
    <div class="container">
      <div class="section-title">
        <h3>论文发表</h3>
      </div>
      
      <div class="papers-list">
        <div v-for="group in papersByYear" :key="group.year" class="year-group">
          <div class="year-label">{{ group.year }}</div>
          <div class="paper-items">
            <div v-for="(item, index) in group.items" :key="index" class="paper-item">
              <div class="paper-content">
                <span v-if="item.content.includes('[')" class="venue-tag">
                  {{ item.content.match(/\[(.*?)\]/)?.[1] || 'Paper' }}
                </span>
                <span class="paper-text" v-html="item.content.replace(/\[(.*?)\]/, '').trim()"></span>
                <a v-if="item.link" :href="item.link" target="_blank" class="paper-link">
                  [PDF]
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.papers-page {
  padding: 30px 0 50px;
}

.year-group {
  margin-bottom: 40px;
}

.year-label {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary-color);
  border-bottom: 2px solid var(--primary-light);
  padding-bottom: 10px;
  margin-bottom: 20px;
}

.paper-item {
  margin-bottom: 15px;
  padding-bottom: 15px;
  border-bottom: 1px dashed var(--border-color);
}

.paper-item:last-child {
  border-bottom: none;
}

.paper-content {
  font-size: 1rem;
  line-height: 1.6;
  color: var(--text-color);
}

.venue-tag {
  display: inline-block;
  background-color: var(--primary-light);
  color: var(--primary-color);
  font-size: 0.85rem;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 4px;
  margin-right: 8px;
  vertical-align: middle;
}

.paper-text {
  vertical-align: middle;
}

.paper-link {
  color: var(--primary-color);
  font-weight: 600;
  margin-left: 8px;
  text-decoration: none;
}

.paper-link:hover {
  text-decoration: underline;
}
</style>
