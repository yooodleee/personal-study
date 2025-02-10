<template>
  <v-app>
    <!-- NavigationBar 고정 -->
    <NavigationBar />
    <main>
      <!-- NuxtPage를 메인 영역으로 설정 -->
      <NuxtPage /> 
    </main>
    <div class="footer-container">
      <p class="reserved-info">2024-2025 AIM-Sniper Korea LLC. All Rights Reserved.</p>
    </div>
  </v-app>
</template>

<script setup>
import { defineComponent } from 'vue';
import NavigationBar from '~/navigationBar/pages/NavigationMenuBar.vue';
import { useCompanyReportStore } from './companyReport/stores/companyReportStore';

const companyReportStore = useCompanyReportStore()
const topN = ref(5);
companyReportStore.requestCompanyReportListToDjango()
companyReportStore.requestTopNCompanyReportListToDjango(topN.value)
</script>

<style>
/* v-app 전체 영역 설정 */
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* 화면 전체 높이를 차지하도록 설정 */
  margin: 0;
  padding: 0;
  overflow: hidden; /* 스크롤바 문제 방지 */
}

/* v-main을 flex로 설정하여 남은 공간 차지 */
v-main {
  flex-grow: 1; /* 메인 컨텐츠가 가능한 모든 공간을 차지 */
}

/* 전체적으로 스크롤을 막고, 필요 시만 스크롤 허용 */
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow-x: hidden; /* 가로 스크롤 제거 */
  overflow-y: auto; /* 세로 스크롤만 허용 */
}

/* 네비게이션바 관련 CSS */
.menu-bar {
  background: var(--Gradient-Liner-1, linear-gradient(94deg, #0A28B0 1.69%, #8094F4 116.61%));
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 999; /* 네비게이션바가 항상 맨 위에 위치 */
}

/* 푸터 설정 */
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
