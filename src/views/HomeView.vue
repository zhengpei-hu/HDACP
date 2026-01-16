<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import newsData from '@/data/news.json'
import researchData from '@/data/research.json'
import papersData from '@/data/publications.json'

const router = useRouter()

// Carousel State
const currentSlide = ref(0)
const carouselImages = [
  { src: `${import.meta.env.BASE_URL}carousel/hezhao3.jpg`, caption: '' },
  { src: `${import.meta.env.BASE_URL}carousel/hdacp.png`, caption: '' },
  { src: `${import.meta.env.BASE_URL}carousel/hezhao2.jpg`, caption: '' },
  { src: `${import.meta.env.BASE_URL}carousel/hezhao4.jpg`, caption: '' },
  { src: `${import.meta.env.BASE_URL}carousel/hezhao.jpg`, caption: '' }
]

let slideInterval = null

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % carouselImages.length
}

const prevSlide = () => {
  currentSlide.value = (currentSlide.value - 1 + carouselImages.length) % carouselImages.length
}

const goToSlide = (index) => {
  currentSlide.value = index
}

onMounted(() => {
  slideInterval = setInterval(nextSlide, 5000)
})

onUnmounted(() => {
  if (slideInterval) clearInterval(slideInterval)
})

// Data Subsets
// Data Subsets
const latestNews = (newsData && newsData.news) ? newsData.news.slice(0, 3) : []
const latestPapers = (papersData && Array.isArray(papersData) && papersData.length > 0) ? papersData[0].items.slice(0, 3) : []
</script>

<template>
  <div class="home-view">
    <!-- Hero Carousel -->
    <div class="hero-carousel">
      <div 
        class="carousel-inner" 
        :style="{ transform: `translateX(-${currentSlide * 100}%)` }"
      >
        <div v-for="(img, index) in carouselImages" :key="index" class="carousel-item">
          <img :src="img.src" :alt="img.caption">
          <div class="carousel-caption" v-if="img.caption">
            <h3>{{ img.caption }}</h3>
          </div>
        </div>
      </div>
      
      <!-- Controls -->
      <button class="carousel-control prev" @click="prevSlide">&lt;</button>
      <button class="carousel-control next" @click="nextSlide">&gt;</button>
      
      <!-- Indicators -->
      <div class="carousel-indicators">
        <span 
          v-for="(img, index) in carouselImages" 
          :key="index" 
          :class="{ active: currentSlide === index }"
          @click="goToSlide(index)"
        ></span>
      </div>
    </div>

    <div class="container main-content">
      <!-- Intro Section -->
      <section class="intro-section fade-in">
        <div class="section-title">
          <h3>实验室简介</h3>
        </div>
        <div class="intro-content card">
          <p>
            青海大学高性能与云计算研究所（HDACP Lab）致力于高性能计算、云计算、大数据分析及人工智能等前沿技术的研究与应用。
            我们拥有一支充满活力、勇于创新的科研团队，在分布式系统、并行算法、数据挖掘等领域取得了显著成果。
          </p>
          <div class="actions">
            <button class="btn btn-primary" @click="router.push('/research')">了解更多</button>
            <button class="btn btn-outline" @click="router.push('/contact')">加入我们</button>
          </div>
        </div>
      </section>

      <!-- Latest News -->
      <section class="news-section">
        <div class="section-title">
          <h3>最新动态</h3>
        </div>
        <div class="grid-3">
          <div v-for="(item, index) in latestNews" :key="index" class="card news-card fade-in" :style="{ animationDelay: `${index * 0.1}s` }">
            <span class="news-date">{{ item.date }}</span>
            <h4>{{ item.title }}</h4>
            <a :href="item.link || '#'" target="_blank" class="read-more">阅读更多 &rarr;</a>
          </div>
        </div>
      </section>

      <!-- Research Directions -->
      <section class="research-section">
        <div class="section-title">
          <h3>研究方向</h3>
        </div>
        <div class="research-grid">
          <div v-for="(area, index) in researchData.directions" :key="index" class="card research-card fade-in" :style="{ animationDelay: `${index * 0.1}s` }">
            <div class="icon-box">
              <i class="icon">🔬</i>
            </div>
            <h4>{{ area.name }}</h4>
            <div class="direction-desc">
              <p>{{ area.description }}</p>
            </div>
            <a href="#" @click.prevent="router.push('/research')" class="read-more">了解详情 &rarr;</a>
          </div>
        </div>
      </section>

      <!-- Latest Papers -->
      <section class="papers-section">
        <div class="section-title">
          <h3>最新论文</h3>
        </div>
        <div class="grid-2">
          <div v-for="(paper, index) in latestPapers" :key="index" class="card paper-card fade-in">
            <p class="paper-content">{{ paper.content }}</p>
            <a v-if="paper.link" :href="paper.link" target="_blank" class="read-more">查看论文</a>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
/* Hero Carousel */
.hero-carousel {
  width: 100%;
  height: 600px;
  position: relative;
  overflow: hidden;
  margin-bottom: 60px;
  box-shadow: var(--shadow-md);
}

.carousel-inner {
  display: flex;
  width: 100%;
  height: 100%;
  transition: transform 0.6s var(--ease-spring);
}

.carousel-item {
  min-width: 100%;
  height: 100%;
  position: relative;
}

.carousel-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.carousel-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 40px 20px;
  background: linear-gradient(to top, rgba(0,0,0,0.7), transparent);
  color: #fff;
  text-align: center;
}

.carousel-caption h3 {
  font-size: 2rem;
  margin: 0;
  text-shadow: 0 2px 4px rgba(0,0,0,0.3);
}

.carousel-control {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255,255,255,0.2);
  border: none;
  color: #fff;
  font-size: 2rem;
  padding: 10px 15px;
  cursor: pointer;
  backdrop-filter: blur(4px);
  border-radius: 50%;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s;
}

.carousel-control:hover {
  background: rgba(255,255,255,0.4);
}

.prev { left: 20px; }
.next { right: 20px; }

.carousel-indicators {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;
}

.carousel-indicators span {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(255,255,255,0.5);
  cursor: pointer;
  transition: all 0.3s;
}

.carousel-indicators span.active {
  background: #fff;
  transform: scale(1.2);
}

/* Sections */
section {
  margin-bottom: 80px;
}

.intro-content {
  text-align: center;
  font-size: 1.1rem;
  color: var(--text-secondary);
  max-width: 800px;
  margin: 0 auto;
}

.actions {
  margin-top: 30px;
  display: flex;
  gap: 20px;
  justify-content: center;
}

/* Cards */
.news-date {
  font-size: 0.9rem;
  color: var(--primary-color);
  font-weight: 600;
  display: block;
  margin-bottom: 8px;
}

.read-more {
  display: inline-block;
  margin-top: auto;
  font-size: 0.9rem;
  color: var(--primary-color);
  font-weight: 500;
}

.research-card {
  text-align: center;
}

.icon-box {
  font-size: 2.5rem;
  margin-bottom: 15px;
  color: var(--primary-color);
}

.direction-list {
  text-align: left;
  padding-left: 20px;
  color: var(--text-secondary);
  font-size: 0.9rem;
  margin-top: 15px;
}

.direction-list li {
  margin-bottom: 5px;
  list-style-type: disc;
}

.paper-year {
  display: inline-block;
  background: var(--primary-light);
  color: var(--primary-dark);
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 0.8rem;
  margin-bottom: 10px;
  font-weight: 600;
}

.paper-authors {
  font-size: 0.9rem;
  color: var(--text-muted);
  font-style: italic;
  margin-bottom: 5px;
}

.paper-venue {
  font-weight: 500;
  color: var(--secondary-color);
}


/* Research Grid - 5 Items in One Row */
.research-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 16px; /* Reduced gap to fit 5 items */
}

.research-grid > .research-card {
  /* Reset flex properties if any */
  width: auto;
  height: 100%; /* Ensure full height filling */
  display: flex;
  flex-direction: column;
}

/* Ensure description takes available space so button pushes to bottom */
.direction-desc {
  flex: 1;
}

@media (max-width: 1200px) {
  .research-grid {
    grid-template-columns: repeat(3, 1fr); /* Wrap on medium screens */
  }
}

@media (max-width: 768px) {
  .research-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .research-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .hero-carousel {
    height: 400px;
  }
  
  .carousel-caption h3 {
    font-size: 1.5rem;
  }
}
</style>
