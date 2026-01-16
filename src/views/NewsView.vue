<script setup>
import newsData from '@/data/news.json'

const allNews = [...newsData.news, ...newsData.papers].sort((a, b) => {
  return parseInt(b.date) - parseInt(a.date)
})
</script>

<template>
  <div class="news-page">
    <div class="container">
      <div class="section-title">
        <h3>新闻动态</h3>
      </div>
      
      <div class="news-grid">
        <article v-for="item in allNews" :key="item.id" class="news-card">
          <div class="news-date-badge">
            <span class="year">{{ item.date }}</span>
          </div>
          <div class="news-content">
            <h4 class="news-title">
              <a v-if="item.link" :href="item.link" target="_blank" rel="noopener">
                {{ item.title }}
                <span class="external-icon">↗</span>
              </a>
              <span v-else>{{ item.title }}</span>
            </h4>
          </div>
        </article>
      </div>
    </div>
  </div>
</template>

<style scoped>
.news-page {
  padding: 30px 0 50px;
}

.news-grid {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.news-card {
  display: flex;
  align-items: flex-start;
  gap: 20px;
  padding: 20px 24px;
  background: #fff;
  border-radius: 12px;
  box-shadow: var(--shadow-sm);
  transition: all var(--transition-fast);
}

.news-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateX(5px);
}

.news-date-badge {
  flex-shrink: 0;
  width: 70px;
  height: 70px;
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #fff;
}

.news-date-badge .year {
  font-size: 1.3rem;
  font-weight: 700;
}

.news-content {
  flex: 1;
  padding: 8px 0;
}

.news-title {
  font-size: 1rem;
  font-weight: 500;
  line-height: 1.6;
  color: var(--text-color);
}

.news-title a {
  color: var(--text-color);
  text-decoration: none;
  transition: color var(--transition-fast);
}

.news-title a:hover {
  color: var(--primary-color);
}

.external-icon {
  display: inline-block;
  margin-left: 6px;
  font-size: 0.8rem;
  color: var(--primary-color);
}

@media (max-width: 576px) {
  .news-card {
    flex-direction: column;
    gap: 12px;
  }
  
  .news-date-badge {
    width: auto;
    height: auto;
    padding: 8px 16px;
    flex-direction: row;
    gap: 8px;
  }
  
  .news-date-badge .year {
    font-size: 1rem;
  }
}
</style>
