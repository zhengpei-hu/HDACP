<script setup>
import projectsData from '@/data/projects.json'

const projects = projectsData.projects
</script>

<template>
  <div class="projects-page">
    <div class="container">
      <div class="section-title">
        <h3>科研项目</h3>
      </div>
      
      <div class="projects-table-wrap">
        <table class="projects-table">
          <thead>
            <tr>
              <th class="col-period">时间</th>
              <th class="col-title">项目名称</th>
              <th class="col-funding">资助基金</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="project in projects" :key="project.id">
              <td class="col-period">{{ project.period }}</td>
              <td class="col-title">{{ project.title }}</td>
              <td class="col-funding">
                <span class="funding-badge" :class="getFundingClass(project.funding)">
                  {{ project.funding }}
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    getFundingClass(funding) {
      if (funding.includes('国家自然科学基金')) return 'national'
      if (funding.includes('国家重点实验室')) return 'key-lab'
      if (funding.includes('青海省')) return 'provincial'
      if (funding.includes('横向')) return 'horizontal'
      return 'other'
    }
  }
}
</script>

<style scoped>
.projects-page {
  padding: 30px 0 50px;
}

.projects-table-wrap {
  background: #fff;
  border-radius: 12px;
  box-shadow: var(--shadow-sm);
  overflow: hidden;
}

.projects-table {
  width: 100%;
  border-collapse: collapse;
}

.projects-table th {
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  color: #fff;
  padding: 16px 20px;
  text-align: left;
  font-weight: 600;
  font-size: 0.95rem;
}

.projects-table td {
  padding: 16px 20px;
  border-bottom: 1px solid var(--border-color);
  font-size: 0.9rem;
  color: var(--text-color);
  vertical-align: top;
}

.projects-table tbody tr:hover {
  background: rgba(80, 125, 188, 0.05);
}

.projects-table tbody tr:last-child td {
  border-bottom: none;
}

.col-period {
  width: 12%;
  font-weight: 600;
  color: var(--primary-color) !important;
  white-space: nowrap;
}

.col-title {
  width: 55%;
  line-height: 1.6;
}

.col-funding {
  width: 33%;
}

.funding-badge {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
}

.funding-badge.national {
  background: rgba(231, 76, 60, 0.1);
  color: #c0392b;
}

.funding-badge.key-lab {
  background: rgba(155, 89, 182, 0.1);
  color: #8e44ad;
}

.funding-badge.provincial {
  background: rgba(46, 204, 113, 0.1);
  color: #27ae60;
}

.funding-badge.horizontal {
  background: rgba(52, 152, 219, 0.1);
  color: #2980b9;
}

.funding-badge.other {
  background: rgba(149, 165, 166, 0.1);
  color: #7f8c8d;
}

@media (max-width: 768px) {
  .projects-table-wrap {
    overflow-x: auto;
  }
  
  .projects-table {
    min-width: 700px;
  }
  
  .projects-table th,
  .projects-table td {
    padding: 12px 16px;
  }
}
</style>
