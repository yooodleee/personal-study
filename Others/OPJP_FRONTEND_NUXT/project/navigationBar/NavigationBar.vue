<template>
    <v-app-bar app color="primary" dark>
        <v-btn @click="goToHome">
            <v-toolbar-title>OPJP</v-toolbar-title>
        </v-btn>

        <v-spacer></v-spacer>

        <template v-if="!kakaoAuthentication.isAuthenticated">
            <v-btn text @click="signIn" class="btn-text">
                <v-icon left>mdi-login</v-icon>
                <span>로그인</span>
            </v-btn>
        </template>

        <template v-else>
            <v-btn text @click="signOut" class="btn-text">
                <v-icon left>mdi-logout</v-icon>
                <span>로그아웃</span>
            </v-btn>
        </template>
    </v-app-bar>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useRouter } from 'vue-router'
import { useKakaoAuthenticationStore } from '~/kakaoAuthentication/stores/kakaoAuthenticationStore';

const router = useRouter()
const kakaoAuthentication = useKakaoAuthenticationStore();

const goToHome = () => {
  router.push('/')
}

const signIn = () => {
  console.log('로그인 클릭')
  router.push('/account/login')
}

const signOut = () => {
  console.log('로그아웃 클릭')
  const userToken = localStorage.getItem("userToken")

  if (userToken != null) {
    kakaoAuthentication.requestLogout(userToken)
  } else {
    console.log('userToken이 없습니다')
  }

  localStorage.removeItem("userToken")
  kakaoAuthentication.isAuthenticated = false
  router.push('/')
}

onMounted(async () => {
  const userToken = localStorage.getItem('userToken');
  
  if (userToken) {
    const isValid = await kakaoAuthentication.requestValidationUserToken(userToken)
    kakaoAuthentication.isAuthenticated = isValid;
  }
});
</script>


<style scoped>
/* 전체 네비게이션 바 스타일 */
.v-app-bar {
    background-color: #795548 !important; /* 브라운 색상 */
    color: #ffffff;
    font-family: 'Roboto', sans-serif;
}

/* 홈 버튼 스타일 */
.home-btn {
    padding: 0 16px;
    font-size: 1.2rem;
    text-transform: uppercase;
    color: #fbe9e7; /* 브라운 계열 텍스트 색상 */
}

/* 타이틀 스타일 */
.title {
    font-weight: bold;
    font-size: 1.5rem;
}

/* 버튼 텍스트 스타일 */
.btn-text {
    font-size: 1rem;
    color: #ffe0b2; /* 브라운 계열 텍스트 색상 */
    transition: color 0.3s ease;
}

.btn-text:hover {
    color: #ffccbc; /* 호버 시 색상 변경 */
}

/* 아이콘 스타일 */
.icon {
    font-size: 1.2rem;
    margin-right: 4px;
    color: #d7ccc8;
}

/* 여백 조정 */
.v-spacer {
    flex: 1;
}
</style>