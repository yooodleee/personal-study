<template>
  <v-app>
    <navigation-menu-bar />
    <v-main>
      <router-view />
    </v-main>
    <div class="footer-container">
      <p class="reserved-info">2024-2025 AIM-Sniper Korea LLC. All Rights Reserved.</p>
    </div>
  </v-app>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import NavigationMenuBar from './navigationBar/NavigationMenuBar.vue'

export default defineComponent({
  components: { NavigationMenuBar },
  name: 'App',
})
</script>

<style>

/* 폰트 설정 */
.v-application {
  font-family: 'Pretendard', sans-serif !important;
}
.template {
  font-family: 'Pretendard', sans-serif !important;
}
@font-face {
  font-family:'Pretendard';
  src: url('assets/fonts/Pretendard.ttf') format('truetype');
  font-weight: 400;
}

#app {    
  width : 100vw;
  height : 100vh;
}

/* Reset 기본 적용 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;  
}

html, body {
  width: 100%;
  height: 100%;
  /* font-size: 100%; 기본 폰트 크기 */
  font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden; /* 가로 스크롤 제거 */
}

/* 특정 요소에 폰트 적용을 원하면 추가로 정의할 수 있음 */
h1, h2, h3, h4, h5, h6, p, b, a {
  font-family: 'Pretendard', sans-serif;
} 

/* Flexbox 레이아웃 */
.container {
  display: flex;
  flex-direction: row;
  width: 100%;
  height: 100%;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

button {
  cursor: pointer;
}

/* 반응형 레이아웃 */
@media (max-width: 768px) {
  .container {
    flex-direction: column;
  }

  /* 작은 화면일 때 폰트 크기 조정 */
  body {
    font-size: calc(1vw + 1vh + 0.4vmin);
  }
}

@media (max-width: 480px) {
  /* 아주 작은 화면에서는 더 작은 폰트 크기 */
  body {
    font-size: calc(1vw + 1vh + 0.3vmin);
  }

  /* 이미지의 크기를 화면에 맞춤 */
  img {
    width: 100%;
    height: auto;
  }
}

/* 해상도별 추가 대응 */
@media (max-width: 1024px) {
  .container {
    padding: 20px;
  }
}


.footer-container {
  background-color: rgba(255, 255, 255, 0.025);
  color: rgba(255, 255, 255, 0.75);
  font-size: 12px;
  text-align: center;
  padding: 7px;
  position: fixed;
  width: 100%;
  bottom: 0;
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 3px 5px black;  
}
</style>
