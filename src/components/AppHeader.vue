<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <header class="header-wrap">
    <div class="container">
      <div class="header-row">
        <div class="header-left">
          <RouterLink to="/" class="logo-link">
            <img src="@/assets/images/icon.jpg" alt="HDACP实验室" class="logo-img" />
          </RouterLink>
        </div>
        <div class="header-right">
          <img src="@/assets/images/head.jpg" alt="青海大学" class="header-banner" />
        </div>
      </div>
    </div>
  </header>
</template>

<style scoped>
.header-wrap {
  background: #fff;
  padding: 10px 0;
  border-bottom: 1px solid var(--border-color);
}

.header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70px;
}

.header-left {
  flex: 0 0 auto;
}

.logo-link {
  display: flex;
  align-items: center;
}

.logo-img {
  height: 55px;
  width: auto;
  transition: transform var(--transition-fast);
}

.logo-img:hover {
  transform: scale(1.02);
}

.header-right {
  flex: 0 0 auto;
}

.header-banner {
  height: 60px;
  width: auto;
  border-radius: 4px;
}

@media (max-width: 768px) {
  .header-row {
    height: 60px;
  }
  
  .logo-img {
    height: 45px;
  }
  
  .header-banner {
    height: 45px;
  }
}

@media (max-width: 576px) {
  .header-banner {
    display: none;
  }
}
</style>
