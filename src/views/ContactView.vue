<script setup>
const contactInfo = {
  address: {
    province: '青海省西宁市宁大路251号',
    building: '青海大学计算机技术与应用系111实验室'
  },
  links: [
    { name: '青海大学', url: 'https://www.qhu.edu.cn/' },
    { name: '青海大学计算机技术与应用系', url: 'https://cs.qhu.edu.cn/' },
    { name: '中国计算机学会', url: 'https://www.ccf.org.cn/' }
  ]
}

const teachers = [
  { name: '王晓英', email: 'wxy_cta@qhu.edu.cn' },
  { name: '黄建强', email: 'hjqxaly@163.com' },
  { name: '贾金芳', email: 'qhu_jf@163.com' },
  { name: '朱宇', email: 'sdcxzhuyu@163.com' },
  { name: '张国晶', email: 'Zhanggj@qhu.edu.cn' },
  { name: '吴利', email: 'wuli_qhu@163.com' },
  { name: '边浩东', email: 'hpc_bhd@163.com' }
]
</script>

<template>
  <div class="contact-page">
    <div class="container">
      <div class="section-title">
        <h3>联系我们</h3>
      </div>
      
      <div class="contact-grid">
        <!-- Address Card -->
        <div class="contact-card address-card">
          <div class="card-icon">📍</div>
          <h4>实验室地址</h4>
          <p>{{ contactInfo.address.province }}</p>
          <p>{{ contactInfo.address.building }}</p>
        </div>
        
        <!-- QR Code Card -->
        <div class="contact-card qrcode-card">
          <div class="card-icon">📱</div>
          <h4>关注我们</h4>
          <p>扫描二维码关注青海大学计算机系公众号</p>
          <div class="qrcode-wrap">
            <img src="@/assets/images/qrcode.jpg" alt="公众号二维码" />
          </div>
        </div>
        
        <!-- Links Card -->
        <div class="contact-card links-card">
          <div class="card-icon">🔗</div>
          <h4>常用链接</h4>
          <ul class="links-list">
            <li v-for="link in contactInfo.links" :key="link.url">
              <a :href="link.url" target="_blank" rel="noopener noreferrer">
                {{ link.name }}
                <span class="arrow">→</span>
              </a>
            </li>
          </ul>
        </div>
      </div>

      <!-- Recruitment & Contact Table Section -->
      <div class="recruitment-section">
        <div class="row">
          <div class="col-lg-12">
            <div class="recruitment-content">
              <h4>我们组正在寻找积极进取的学生从事前沿研究项目。</h4>
              <p>非常欢迎各本科生和研究生与我们联系，可以在 <strong>科研团队</strong> 中查找 <span class="highlight">各位老师主页</span> 进一步了解信息。</p>
              <p>下面为我们组各位优秀教师的联系方式，欢迎各大学子根据兴趣联系相应老师，HDACP欢迎你们！</p>
            </div>
            
            <div class="table-responsive">
              <table class="contact-table">
                <thead>
                  <tr>
                    <th>老师</th>
                    <th>联系邮箱</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="teacher in teachers" :key="teacher.name">
                    <td>{{ teacher.name }}</td>
                    <td>{{ teacher.email }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Map Placeholder -->
      <div class="map-section">
        <div class="section-title">
          <h3>地理位置</h3>
        </div>
        <div class="map-placeholder">
          <div class="map-content">
            <span class="map-icon">🗺️</span>
            <p>青海大学 · 计算机技术与应用系</p>
            <p class="map-address">青海省西宁市宁大路251号</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.contact-page {
  padding: 30px 0 50px;
}

.contact-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-bottom: 50px;
}

.contact-card {
  background: #fff;
  border-radius: 16px;
  padding: 30px;
  text-align: center;
  box-shadow: var(--shadow-sm);
  transition: all var(--transition-normal);
}

.contact-card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-5px);
}

.card-icon {
  font-size: 2.5rem;
  margin-bottom: 16px;
}

.contact-card h4 {
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--text-color);
  margin-bottom: 12px;
}

.contact-card p {
  font-size: 0.95rem;
  color: var(--text-light);
  line-height: 1.6;
}

/* QR Code */
.qrcode-wrap {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}

.qrcode-wrap img {
  width: 140px;
  height: 140px;
  border-radius: 12px;
  border: 3px solid var(--border-color);
  transition: transform var(--transition-fast);
}

.qrcode-wrap img:hover {
  transform: scale(1.05);
}

/* Links */
.links-list {
  margin-top: 16px;
  text-align: left;
}

.links-list li {
  margin-bottom: 12px;
}

.links-list a {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  background: var(--bg-light);
  border-radius: 8px;
  color: var(--text-color);
  font-size: 0.95rem;
  transition: all var(--transition-fast);
}

.links-list a:hover {
  background: rgba(80, 125, 188, 0.1);
  color: var(--primary-color);
}

.links-list .arrow {
  color: var(--primary-color);
  transition: transform var(--transition-fast);
}

.links-list a:hover .arrow {
  transform: translateX(5px);
}

/* Recruitment Section */
.recruitment-section {
  background: #fff;
  border-radius: 16px;
  padding: 40px;
  margin-bottom: 50px;
  box-shadow: var(--shadow-sm);
}

.recruitment-content {
  text-align: center;
  margin-bottom: 30px;
}

.recruitment-content h4 {
  color: var(--text-color);
  margin-bottom: 16px;
  font-weight: 600;
}

.recruitment-content p {
  color: var(--text-light);
  font-size: 1.05rem;
  margin-bottom: 10px;
}

.highlight {
  color: #ff5252;
  font-weight: 600;
}

/* Table */
.table-responsive {
  max-width: 800px;
  margin: 0 auto;
  overflow-x: auto;
}

.contact-table {
  width: 100%;
  border-collapse: collapse;
  text-align: center;
  border-radius: 8px;
  overflow: hidden;
}

.contact-table th,
.contact-table td {
  padding: 16px;
  border: 1px solid var(--border-color);
}

.contact-table th {
  background-color: var(--bg-light);
  color: var(--text-color);
  font-weight: 600;
}

.contact-table tr:nth-child(even) {
  background-color: #fafafa;
}

.contact-table tr:hover {
  background-color: rgba(80, 125, 188, 0.05);
}

/* Map */
.map-section {
  margin-top: 30px;
}

.map-placeholder {
  background: linear-gradient(135deg, #e8f4f8 0%, #f0f8ff 100%);
  border-radius: 16px;
  height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px dashed var(--border-color);
}

.map-content {
  text-align: center;
}

.map-icon {
  font-size: 4rem;
  display: block;
  margin-bottom: 16px;
}

.map-content p {
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--text-color);
}

.map-address {
  font-size: 1rem !important;
  font-weight: 400 !important;
  color: var(--text-light) !important;
  margin-top: 8px;
}

@media (max-width: 992px) {
  .contact-grid {
    grid-template-columns: 1fr;
  }
}
</style>
