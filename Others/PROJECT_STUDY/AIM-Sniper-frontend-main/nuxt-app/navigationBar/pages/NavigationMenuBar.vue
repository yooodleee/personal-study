<template>
  <v-app-bar color="transparent" app dark height="72" class="menu-bar">

    <v-btn text @click="goToHome" class="navbar-logo-btn">
      <v-img class="home-icon" src="@/assets/images/fixed/AIM_BI_White.png" alt="AIM LOGO" contain height="56"
        width="56" cover></v-img>
    </v-btn>

    <v-spacer></v-spacer>

    <v-btn text @click="goToHome" class="btn-text">
      HOME
    </v-btn>

    <v-btn
      v-if="googleAuthenticationStore.isGoogleAdmin || authenticationStore.isKakaoAdmin || naverAuthenticationStore.isNaverAdmin"
      text @click="goToSurveyListPage" class="btn-text">
      SURVEY
    </v-btn>
    <v-btn
      v-if="!googleAuthenticationStore.isGoogleAdmin && !authenticationStore.isKakaoAdmin && !naverAuthenticationStore.isNaverAdmin"
      text @click="goToSurvey" class="btn-text">
      REVIEW
    </v-btn>

    <v-btn text @click="goToProductList" class="btn-text">
      COMPANY REPORT
    </v-btn>
    <v-btn text @click="goToLlmTestPage" class="btn-text">
      AI INTERVIEW
    </v-btn>
    <!-- <v-menu>
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" class="btn-text" style="margin-right: 14px">
          <b>AI Interview</b>
        </v-btn>
      </template>
      <v-list>
        <v-list-item v-for="(item, index) in aiInterviewPageList" :key="index" @click="item.action">
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu> -->

    <v-spacer></v-spacer>

    <v-menu v-if="
      authenticationStore.isAuthenticatedKakao ||
      googleAuthenticationStore.isAuthenticatedGoogle ||
      naverAuthenticationStore.isAuthenticatedNaver
    " close-on-content-click>
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" class="btn-text" style="margin-right: 14px">
          <b>My Page</b>
        </v-btn>
      </template>
      <v-list>
        <v-list-item v-for="(item, index) in myPageItems" :key="index" @click="item.action">
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    <v-menu v-if="googleAuthenticationStore.isGoogleAdmin ||
      authenticationStore.isKakaoAdmin ||
      naverAuthenticationStore.isNaverAdmin" close-on-content-click>
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" class="btn-text" style="margin-right: 14px">
          <b>ADMIN</b>
        </v-btn>
      </template>
      <v-list>
        <v-list-item v-for="(item, index) in adminPageList" :key="index" @click="item.action">
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

    <v-btn
      v-if="!authenticationStore.isAuthenticatedKakao && !googleAuthenticationStore.isAuthenticatedGoogle && !naverAuthenticationStore.isAuthenticatedNaver && !authenticationStore.isKakaoAdmin && !googleAuthenticationStore.isGoogleAdmin && !naverAuthenticationStore.isNaverAdmin"
      text @click="signIn" class="btn-login">
      <!-- <v-icon left>mdi-login</v-icon> -->
      LOGIN
    </v-btn>

    <v-btn v-else text @click="signOut" class="btn-logout">
      <!-- <v-icon left>mdi-logout</v-icon> -->
      LOGOUT
    </v-btn>

  </v-app-bar>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAccountStore } from '../../account/stores/accountStore';
import { useAuthenticationStore } from '../../authentication/stores/authenticationStore';
import { useNaverAuthenticationStore } from '../../naverAuthentication/stores/naverAuthenticationStore';
import { useSurveyStore } from '../../survey/stores/surveyStore';
import { useGoogleAuthenticationStore } from '../../googleAuthentication/stores/googleAuthenticationStore'


// Pinia 스토어 사용
const accountStore = useAccountStore();
const authenticationStore = useAuthenticationStore();
const googleAuthenticationStore = useGoogleAuthenticationStore();
const naverAuthenticationStore = useNaverAuthenticationStore();
const surveyStore = useSurveyStore();

const router = useRouter();

// 데이터 선언
const adminPageList = ref([
  {
    title: "사용자 관리",
    action: () => goToManagementUserPage(),
  },
  {
    title: "사용자 로그 현황",
    action: () => goToManagementUserLogList(),
  },
]);

const myPageItems = ref([
  {
    title: "회원 정보",
    action: () => goToMyPage(),
  },
  {
    title: "장바구니",
    action: () => goToCart(),
  },
  {
    title: "주문 목록",
    action: () => goToOrder(),
  },
]);

const aiInterviewPageList = ref([
  // {
  //   title: "대화형",
  //   action: () => goToAiInterviewPage(),
  // },
  {
    title: "단일 질문 노출형",
    action: () => goToLlmTestPage(),
  },
]);

const surveyId = ref(1);
const isUserAuthenticated = ref(null);

// 브라우저 환경에서만 실행되도록 수정
if (process.client) {
  isUserAuthenticated.value = sessionStorage.getItem("isUserAuthenticated");
}

// 라우터 이동 함수들
const signIn = () => router.push('/account/login')
const goToHome = () => router.push('/');
const goToProductList = () => router.push('/companyReport/list');
const goToCart = () => router.push('/cart/list');
const goToOrder = () => router.push('/order/list');
const goToMyPage = () => router.push('/account/mypage');
const goToSurveyListPage = () => router.push('/survey/list');
const goToManagementUserPage = () => router.push('/management/user');
const goToManagementUserLogList = () => router.push('/management/log');
// const goToAiInterviewPage = () => router.push('/ai-interview');
const goToLlmTestPage = () => router.push('/ai-interview');

// 로그아웃 처리
const signOut = async () => {
  if (process.client) {
    const loginType = sessionStorage.getItem("loginType");

    if (loginType === "KAKAO") {
      await authenticationStore.requestKakaoLogoutToDjango();
      authenticationStore.isAuthenticatedKakao = false;
      authenticationStore.isKakaoAdmin = false;
    } else if (loginType === "GOOGLE") {
      await googleAuthenticationStore.requestGoogleLogoutToDjango();
      googleAuthenticationStore.isAuthenticatedGoogle = false;
    } else if (loginType === "NAVER") {
      await naverAuthenticationStore.requestNaverLogoutToDjango();
      naverAuthenticationStore.isAuthenticatedNaver = false;
    } else if (loginType === "NORMAL") {
      sessionStorage.removeItem("normalToken");
      sessionStorage.removeItem("email");
      sessionStorage.removeItem("loginType");
      sessionStorage.removeItem('adminToken');

      if (sessionStorage.getItem("fileKey")) {
        sessionStorage.removeItem("fileKey");
      }

      accountStore.isAuthenticatedNormal = false;
      accountStore.isNormalAdmin = false;
      authenticationStore.isKakaoAdmin = false;
      googleAuthenticationStore.isGoogleAdmin = false;
      naverAuthenticationStore.isNaverAdmin = false;
    }

    router.push('/');
  }
};

// 설문조사 페이지 이동
const goToSurvey = async () => {
  const randomString = await surveyStore.requestRandomStringToDjango();

  if (randomString) {
    router.push({
      name: 'SurveyReadPage',
      params: { randomString: randomString.toString() },
    });
  }
};

// 사용자 상태 복원
onMounted(() => {
  if (process.client) {
    const userToken = sessionStorage.getItem("userToken");
    if (userToken) {
      authenticationStore.isAuthenticatedKakao = true;
    }

    const googleUserToken = sessionStorage.getItem("googleUserToken");
    if (googleUserToken) {
      googleAuthenticationStore.isAuthenticatedGoogle = true;
    }

    const naverUserToken = sessionStorage.getItem("naverUserToken");
    if (naverUserToken) {
      naverAuthenticationStore.isAuthenticatedNaver = true;
    }

    const normalToken = sessionStorage.getItem("normalToken");
    if (normalToken) {
      accountStore.isAuthenticatedNormal = true;
    }

    const adminToken = sessionStorage.getItem("adminToken");
    if (adminToken) {
      authenticationStore.isKakaoAdmin = true;
      googleAuthenticationStore.isGoogleAdmin = true;
      naverAuthenticationStore.isNaverAdmin = true;
      accountStore.isNormalAdmin = true;
    }
  }
});
</script>



<style scoped>
.menu-bar {
  background: var(--Gradient-Liner-1, linear-gradient(94deg, #0A28B0 1.69%, #8094F4 116.61%)) !important;
}

/* AIM 로고 이미지 버튼 */
.navbar-logo-btn {
  display: flex;
  align-items: center;
  margin-left: 80px !important;
}

.btn-text {
  font-family: 'Pretendard', sans-serif;
  font-size: 16px;
  font-weight: 300;
  color: #FFF;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  padding: 0px 10px;
  margin: 0px 10px;
}

.btn-login {
  font-family: 'Pretendard', sans-serif;
  font-size: 16px;
  font-weight: 700px;
  color: #FFF;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-right: 80px !important;
  border: 1px solid white;
  color: white;
  /* 텍스트 색상도 흰색으로 변경 */
}

.btn-logout {
  font-family: 'Pretendard', sans-serif;
  font-size: 16px;
  font-weight: 700px;
  color: #FFF;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-right: 80px !important;
  border: 1px solid white;
  color: white;
  /* 텍스트 색상도 흰색으로 변경 */
}


.btn-text:hover {
  background-color: rgba(255, 255, 255, 0.25);

}

/* 클릭해서 선택되었을시 표시 */
.btn-text:focus {
  background-color: rgba(255, 255, 255, 0.25);
  color: white;

}

.v-menu>.v-overlay__content>.v-card,
.v-menu>.v-overlay__content>.v-sheet,
.v-menu>.v-overlay__content>.v-list {
  background-color: rgba(0, 0, 0, 0.25);
  color: white;
  border: 3px solid white
}

.v-list-item:hover {
  background-color: rgba(255, 255, 255, 0.25);

}
</style>
