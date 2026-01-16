<script setup>
import { ref, computed } from 'vue'
import { RouterLink } from 'vue-router'
import teamData from '@/data/team.json'

const activeTab = ref('current')

const teachers = teamData.teachers
const currentStudents = computed(() => 
  teamData.students.filter(s => s.year.includes('present'))
)

const graduatedStudents = computed(() => 
  teamData.students.filter(s => s.year.includes('毕业生'))
)
</script>

<template>
  <div class="team-page">
    <div class="container">
      <!-- Teachers Section -->
      <div class="section">
        <div class="section-title">
          <h3>师资队伍</h3>
        </div>
        <div class="teacher-grid">
          <RouterLink 
            v-for="teacher in teachers" 
            :key="teacher.id" 
            :to="`/teacher/${teacher.id}`"
            class="teacher-card"
          >
            <div class="teacher-photo">
              <img :src="`/people/teacher/${teacher.photo}`" :alt="teacher.name" />
            </div>
            <div class="teacher-info">
              <h4 class="teacher-name">{{ teacher.name }}</h4>
              <p class="teacher-title">{{ teacher.title }}</p>
            </div>
          </RouterLink>
        </div>
      </div>
      
      <!-- Students Section -->
      <div class="section">
        <div class="section-title">
          <h3>学生团队</h3>
        </div>
        
        <div class="tabs">
          <button 
            :class="{ active: activeTab === 'current' }"
            @click="activeTab = 'current'"
          >
            硕士研究生
          </button>
          <button 
            :class="{ active: activeTab === 'graduated' }"
            @click="activeTab = 'graduated'"
          >
            毕业学生
          </button>
        </div>
        
        <div v-if="activeTab === 'current'" class="student-grid">
          <component 
            v-for="student in currentStudents" 
            :key="student.name" 
            :is="student.link ? 'a' : 'div'"
            :href="student.link || undefined"
            :target="student.link ? '_blank' : undefined"
            :rel="student.link ? 'noopener noreferrer' : undefined"
            class="student-card"
            :class="{ 'has-link': student.link }"
          >
            <div class="student-photo">
              <img :src="`/people/student/${student.photo}`" :alt="student.name" />
            </div>
            <div class="student-info">
              <h5 class="student-name">{{ student.name }}</h5>
              <p class="student-year">{{ student.year }}</p>
              <p class="student-research">{{ student.research }}</p>
            </div>
          </component>
        </div>
        
        <div v-else-if="activeTab === 'graduated'" class="student-grid">
          <component 
            v-for="student in graduatedStudents" 
            :key="student.name" 
            :is="student.link ? 'a' : 'div'"
            :href="student.link || undefined"
            :target="student.link ? '_blank' : undefined"
            :rel="student.link ? 'noopener noreferrer' : undefined"
            class="student-card"
            :class="{ 'has-link': student.link }"
          >
            <div class="student-photo">
              <img :src="`/people/student/${student.photo}`" :alt="student.name" />
            </div>
            <div class="student-info">
              <h5 class="student-name">{{ student.name }}</h5>
              <p class="student-year">{{ student.year }}</p>
              <p class="student-research">{{ student.research }}</p>
            </div>
          </component>
        </div>
        
        <div v-if="activeTab === 'graduated' && graduatedStudents.length === 0" class="empty-state">
          <p>暂无毕业学生信息</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.team-page {
  padding: 30px 0 50px;
}

.section {
  margin-bottom: 50px;
}

/* Teacher Grid */
.teacher-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.teacher-card {
  background: #fff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: all var(--transition-normal);
  cursor: pointer;
}

.teacher-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.teacher-photo {
  position: relative;
  padding-top: 120%;
  overflow: hidden;
}

.teacher-photo img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--transition-normal);
}

.teacher-card:hover .teacher-photo img {
  transform: scale(1.05);
}

.teacher-info {
  padding: 16px;
  text-align: center;
}

.teacher-name {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--text-color);
  margin-bottom: 4px;
}

.teacher-title {
  font-size: 0.9rem;
  color: var(--primary-color);
  font-weight: 500;
}

/* Tabs */
.tabs {
  display: flex;
  gap: 10px;
  margin-bottom: 24px;
  border-bottom: 2px solid var(--border-color);
  padding-bottom: 0;
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

.tabs button:hover {
  color: var(--primary-color);
}

/* Student Grid */
.student-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

.student-card {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
  background: #fff;
  border-radius: 10px;
  box-shadow: var(--shadow-sm);
  transition: all var(--transition-fast);
  text-decoration: none; /* Ensure no underline for basic card */
}

.student-card.has-link {
  cursor: pointer;
}

.student-card.has-link:hover {
  transform: translateX(5px);
  box-shadow: var(--shadow-md);
  background-color: var(--bg-light); /* Slight highlight */
}

.student-card:not(.has-link):hover {
  transform: translateX(5px);
  box-shadow: var(--shadow-md);
}

.student-photo {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
  border: 3px solid var(--primary-light);
}

.student-photo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.student-info {
  flex: 1;
  min-width: 0;
}

.student-name {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-color);
  margin-bottom: 2px;
}

.student-year {
  font-size: 0.8rem;
  color: var(--text-muted);
  margin-bottom: 2px;
}

.student-research {
  font-size: 0.8rem;
  color: var(--primary-color);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.empty-state {
  text-align: center;
  padding: 60px 20px;
  color: var(--text-muted);
}

/* Responsive */
@media (max-width: 992px) {
  .teacher-grid {
    grid-template-columns: repeat(3, 1fr);
  }
  
  .student-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 768px) {
  .teacher-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .student-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .teacher-grid {
    grid-template-columns: 1fr;
  }
  
  .student-grid {
    grid-template-columns: 1fr;
  }
}
</style>
