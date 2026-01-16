<script setup>
const links = [
  { name: '青海大学', url: 'https://www.qhu.edu.cn/' },
  { name: '青海大学计算机技术与应用系', url: 'https://cs.qhu.edu.cn/' },
  { name: '中国计算机学会', url: 'https://www.ccf.org.cn/' }
]
</script>

<template>
  <footer class="footer">
    <div class="footer-content">
      <div class="container">
        <div class="footer-grid">
          <!-- Address Section -->
          <div class="footer-section">
            <h4 class="footer-title">地址</h4>
            <ul class="footer-list">
              <li>青海省西宁市宁大路251号</li>
              <li>青海大学计算机技术与应用系111实验室</li>
            </ul>
          </div>
          
          <!-- QR Code Section -->
          <div class="footer-section">
            <h4 class="footer-title">扫描下方二维码关注青海大学计算机系公众号</h4>
            <div class="qrcode-wrap">
              <img src="@/assets/images/qrcode.jpg" alt="公众号二维码" class="qrcode-img" />
            </div>
          </div>
          
          <!-- Links Section -->
          <div class="footer-section">
            <h4 class="footer-title">常用链接</h4>
            <ul class="footer-list">
              <li v-for="link in links" :key="link.url">
                <a :href="link.url" target="_blank" rel="noopener noreferrer">
                  {{ link.name }}
                  <span class="external-icon">↗</span>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    
    <div class="footer-bottom">
      <div class="container">
        <p>© {{ new Date().getFullYear() }} 青海大学HDACP实验室 All Rights Reserved</p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background: #111;
  color: #999;
  margin-top: auto;
}

.footer-content {
  background: #1e1e1e;
  padding: 40px 0;
}

.footer-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
}

.footer-section {
  padding: 0 10px;
}

.footer-title {
  color: #e0e0e0;
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 16px;
  padding-bottom: 10px;
  border-bottom: 2px solid var(--primary-color);
}

.footer-list {
  margin: 0;
  padding: 0;
}

.footer-list li {
  padding: 6px 0;
  font-size: 0.9rem;
  color: #999;
}

.footer-list a {
  color: #999;
  text-decoration: none;
  transition: color var(--transition-fast);
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.footer-list a:hover {
  color: var(--primary-color);
}

.external-icon {
  font-size: 0.75rem;
  opacity: 0.7;
}

.qrcode-wrap {
  margin-top: 10px;
}

.qrcode-img {
  width: 120px;
  height: 120px;
  border-radius: 8px;
  border: 2px solid rgba(255, 255, 255, 0.1);
  transition: transform var(--transition-fast);
}

.qrcode-img:hover {
  transform: scale(1.05);
}

.footer-bottom {
  background: #111;
  padding: 16px 0;
  text-align: center;
  font-size: 0.85rem;
  color: #666;
  border-top: 1px solid #2a2a2a;
}

@media (max-width: 992px) {
  .footer-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 576px) {
  .footer-grid {
    grid-template-columns: 1fr;
    gap: 30px;
  }
  
  .footer-content {
    padding: 30px 0;
  }
  
  .footer-section {
    text-align: center;
  }
  
  .qrcode-wrap {
    display: flex;
    justify-content: center;
  }
}
</style>
