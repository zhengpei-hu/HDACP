<script setup>
import { computed } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import teamData from '@/data/team.json'

const route = useRoute()

const teacher = computed(() => {
  return teamData.teachers.find(t => t.id === route.params.id) || null
})
</script>

<template>
  <div class="profile-page">
    <div class="container">
      <!-- Back Button -->
      <div class="back-nav">
        <RouterLink to="/team" class="back-btn">← 返回科研团队</RouterLink>
      </div>
      
      <div v-if="teacher" class="profile-content">
        <!-- Profile Header -->
        <div class="profile-header">
          <div class="profile-photo">
            <img :src="`/people/teacher/${teacher.photo}`" :alt="teacher.name" />
          </div>
          <div class="profile-info">
            <h1 class="profile-name">{{ teacher.name }}</h1>
            <p class="profile-title">{{ teacher.title }}</p>
            <p v-if="teacher.education" class="profile-edu">
              <span class="icon">🎓</span> {{ teacher.education }}
            </p>
            <p v-if="teacher.email" class="profile-email">
              <span class="icon">📧</span> {{ teacher.email }}
            </p>
          </div>
        </div>
        
        <!-- Details Sections -->
        <div class="profile-details">
          <!-- Academic Title -->
          <section v-if="teacher.academicTitle" class="detail-section">
            <h3>学术职称</h3>
            <p>{{ teacher.academicTitle }}</p>
          </section>
          
          <!-- Academic Service -->
          <section v-if="teacher.academicService?.length" class="detail-section">
            <h3>学术兼职</h3>
            <ul>
              <li v-for="(service, idx) in teacher.academicService" :key="idx">{{ service }}</li>
            </ul>
          </section>
          
          <!-- Research Direction -->
          <section v-if="teacher.research" class="detail-section">
            <h3>主要研究方向</h3>
            <p>{{ teacher.research }}</p>
          </section>
          
          <!-- Bio -->
          <section v-if="teacher.bio" class="detail-section">
            <h3>个人简介</h3>
            <div class="teacher-bio">
              <template v-if="Array.isArray(teacher.bio)">
                <p v-for="(para, idx) in teacher.bio" :key="idx">{{ para }}</p>
              </template>
              <p v-else>{{ teacher.bio }}</p>
            </div>
          </section>
          
          <!-- Awards -->
          <section v-if="teacher.awards?.length" class="detail-section">
            <h3>获奖情况</h3>
            <ul class="awards-list">
              <li v-for="(award, idx) in teacher.awards" :key="idx">
                <span class="award-icon">🏆</span>
                {{ award }}
              </li>
            </ul>
          </section>
          
          <!-- Projects -->
          <section v-if="teacher.projects?.length" class="detail-section">
            <h3>主持/参与科研项目</h3>
            <div class="projects-list">
              <div v-for="(project, idx) in teacher.projects" :key="idx" class="project-item">
                <div class="project-header">
                  <span class="project-type">{{ project.name }}</span>
                  <span v-if="project.period" class="project-period">{{ project.period }}</span>
                </div>
                <p class="project-title">{{ project.title }}</p>
                <div class="project-meta">
                  <span class="project-role">{{ project.role }}</span>
                  <span v-if="project.funding" class="project-funding">{{ project.funding }}</span>
                </div>
              </div>
            </div>
          </section>

          <!-- Tech Achievements -->
          <section v-if="teacher.achievements?.length" class="detail-section">
            <h3>科技成果登记</h3>
            <ul class="achievements-list">
              <li v-for="(item, idx) in teacher.achievements" :key="idx" class="achievement-item">
                <p class="achievement-title">{{ item.name }}</p>
                <p class="achievement-desc">{{ item.desc }}</p>
              </li>
            </ul>
          </section>

          <!-- Patents -->
          <section v-if="teacher.patents?.length" class="detail-section">
            <h3>知识产权（专利/软著）</h3>
            <ul class="patents-list">
              <li v-for="(item, idx) in teacher.patents" :key="idx">{{ item }}</li>
            </ul>
          </section>

          <!-- Publications -->
          <section v-if="teacher.papers?.length" class="detail-section">
            <h3>学术论文</h3>
            <template v-if="teacher.papers[0]?.items">
              <!-- Grouped Papers -->
              <div v-for="(group, gIdx) in teacher.papers" :key="gIdx" class="paper-group">
                <h4 class="paper-year">{{ group.year }}</h4>
                <ul class="papers-list">
                  <li v-for="(paper, pIdx) in group.items" :key="pIdx" class="paper-item">
                    {{ paper }}
                  </li>
                </ul>
              </div>
            </template>
            <ul v-else class="papers-list">
              <!-- Flat List (Legacy support) -->
              <li v-for="(paper, idx) in teacher.papers" :key="idx" class="paper-item">
                {{ paper }}
              </li>
            </ul>
          </section>
        </div>
      </div>
      
      <!-- Not Found -->
      <div v-else class="not-found">
        <p>未找到该教师信息</p>
        <RouterLink to="/team" class="back-btn">返回科研团队</RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped>
.profile-page {
  padding: 30px 0 60px;
}

.back-nav {
  margin-bottom: 24px;
}

.back-btn {
  display: inline-flex;
  align-items: center;
  padding: 8px 16px;
  background: var(--bg-light);
  border-radius: 8px;
  color: var(--text-color);
  font-size: 0.9rem;
  transition: all var(--transition-fast);
}

.back-btn:hover {
  background: var(--primary-color);
  color: #fff;
}

/* Profile Header */
.profile-header {
  display: flex;
  gap: 40px;
  padding: 30px;
  background: linear-gradient(135deg, #f8f9fa 0%, #fff 100%);
  border-radius: 16px;
  margin-bottom: 30px;
  box-shadow: var(--shadow-sm);
}

.profile-photo {
  flex-shrink: 0;
  width: 180px;
  height: 220px;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--shadow-md);
}

.profile-photo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.profile-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.profile-name {
  font-size: 2rem;
  font-weight: 700;
  color: var(--text-color);
  margin-bottom: 8px;
}

.profile-title {
  font-size: 1.2rem;
  color: var(--primary-color);
  font-weight: 600;
  margin-bottom: 16px;
}

.profile-edu,
.profile-email {
  font-size: 0.95rem;
  color: var(--text-light);
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.icon {
  font-size: 1.1rem;
}

/* Details Sections */
.detail-section {
  background: #fff;
  border-radius: 12px;
  padding: 24px;
  margin-bottom: 20px;
  box-shadow: var(--shadow-sm);
}

.detail-section h3 {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--primary-color);
  margin-bottom: 16px;
  padding-bottom: 10px;
  border-bottom: 2px solid var(--border-color);
}

.detail-section p {
  font-size: 0.95rem;
  line-height: 1.8;
  color: var(--text-color);
}

.detail-section ul {
  padding-left: 0;
}

.detail-section li {
  font-size: 0.95rem;
  color: var(--text-color);
  padding: 8px 0;
  border-bottom: 1px dashed var(--border-color);
}

.detail-section li:last-child {
  border-bottom: none;
}

/* Publication Groups */
.paper-group {
  margin-bottom: 24px;
}

.paper-year {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-color);
  margin-bottom: 12px;
  padding-left: 10px;
  border-left: 3px solid var(--primary-color);
}

.papers-list {
  list-style: none;
  padding-left: 0;
}

.paper-item {
  position: relative;
  padding: 10px 0 10px 20px !important;
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--text-color);
  border-bottom: 1px dashed var(--border-color) !important;
}

.paper-item::before {
  content: "•";
  position: absolute;
  left: 0;
  color: var(--primary-color);
  font-weight: bold;
}

/* Achievements & Patents */
.achievement-item {
  margin-bottom: 16px;
  padding: 12px;
  background: #f8f9fa;
  border-radius: 8px;
}

.achievement-title {
  font-weight: 600;
  color: var(--primary-color);
  margin-bottom: 4px;
}

.achievement-desc {
  font-size: 0.9rem;
  color: var(--text-light);
}

.patents-list li {
  font-size: 0.95rem;
  padding: 8px 0;
  color: var(--text-color);
}

/* Responsive */
@media (max-width: 768px) {
  .profile-header {
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 20px;
  }
  
  .profile-photo {
    width: 150px;
    height: 180px;
  }
  
  .profile-name {
    font-size: 1.5rem;
  }
  
  .project-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }
}
</style>
