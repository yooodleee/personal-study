<template>
  <v-app-bar color="transparent" app dark height="72" class="menu-bar">        
    
    <v-btn text @click="goToHome" class="navbar-logo-btn">
      <v-img
        class="home-icon"
        src="@/assets/images/fixed/AIM_BI_White.png"
        alt="AIM LOGO"
        contain
        height="56" 
        width="56"
        cover
      ></v-img>       
    </v-btn>   
    
    <v-spacer></v-spacer>

    <v-btn text @click="goToHome" class="btn-text">
      HOME
    </v-btn>

    <v-btn v-if="isNormalAdmin || isGoogleAdmin || isKakaoAdmin || isNaverAdmin" text @click="goToSurveyListPage" class="btn-text">
      SURVEY
    </v-btn>
    <v-btn v-if="!isNormalAdmin && !isGoogleAdmin && !isKakaoAdmin && !isNaverAdmin" text @click="goToSurvey" class="btn-text">
      SURVEY
    </v-btn>

    <v-btn text @click="goToProductList" class="btn-text">
      COMPANY REPORT
    </v-btn>   
    <!-- <v-btn text @click="goToAiInterviewPage" class="btn-text">
      AI INTERVIEW
    </v-btn> -->
    <v-menu>
      <template v-slot:activator="{ props }">
          <v-btn v-bind="props" class="btn-text" style="margin-right: 14px">
            <b>AI Interview</b>
          </v-btn>
        </template>
        <v-list>
          <v-list-item
            v-for="(item, index) in aiInterviewPageList"
            :key="index"
            @click="item.action"
          >
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
    </v-menu>

    <v-spacer></v-spacer>

    <v-menu
      v-if="
        isAuthenticatedKakao ||
        isAuthenticatedGoogle ||
        isAuthenticatedNormal ||
        isAuthenticatedNaver
      "
      close-on-content-click
    >
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" class="btn-text" style="margin-right: 14px">
          <b>My Page</b>
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in myPageItems"
          :key="index"
          @click="item.action"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    <v-menu
      v-if="isNormalAdmin ||
      isGoogleAdmin ||
      isKakaoAdmin ||
      isNaverAdmin"
      close-on-content-click
    >
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" class="btn-text" style="margin-right: 14px">
          <b>ADMIN</b>
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in adminPageList"
          :key="index"
          @click="item.action"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>    

    <v-btn v-if="!isAuthenticatedKakao && !isAuthenticatedGoogle && !isAuthenticatedNormal && !isAuthenticatedNaver && !isNormalAdmin && !isKakaoAdmin && !isGoogleAdmin && !isNaverAdmin" text @click="signIn" class="btn-login">
      <!-- <v-icon left>mdi-login</v-icon> -->
       LOGIN
    </v-btn>
    
    <v-btn v-else text @click="signOut" class="btn-logout">
      <!-- <v-icon left>mdi-logout</v-icon> -->
       LOGOUT
    </v-btn>
    
  </v-app-bar>
</template>



<script>
import "@mdi/font/css/materialdesignicons.css";
import router from "@/router";
import { mapActions, mapState } from "vuex";

const accountModule = "accountModule";
const authenticationModule = "authenticationModule";
const googleAuthenticationModule = "googleAuthenticationModule";
const naverAuthenticationModule = "naverAuthenticationModule";
const surveyModule = "surveyModule"

export default {
  data() {
    return {
      adminPageList: [
        {
          title: "사용자 관리",
          action: () => {
            this.goToManagementUserPage();
          },
        },
        {
          title: "사용자 로그 현황",
          
          action: () => {
            this.goToManagementUserLogList();
          },
        },
      ],
      myPageItems: [
        {
          title: "회원 정보",
          action: () => {
            this.goToMyPage();
          },
        },
        {
          title: "장바구니",
          action: () =>{
            this.goToCart();
          }
        },
        {
          title: "주문 목록",
          action: () =>{
            this.goToOrder();
          }
        }
      ],
      aiInterviewPageList: [
        {
          title: "대화형",
          action: () => {
            this.goToAiInterviewPage();
          },
        },
        {
          title: "단일 질문 노출형",
          action: () =>{
            this.goToLlmTestPage();
          }
        },
      ],
      surveyId:1,
      isUserAuthenticated: sessionStorage.getItem("isUserAuthenticated"),
    };
  },
  computed: {
    ...mapState(authenticationModule, ["isAuthenticatedKakao", "isKakaoAdmin"]),
    ...mapState(googleAuthenticationModule, ["isAuthenticatedGoogle",'isGoogleAdmin']),
    ...mapState(accountModule, ["loginType", "isAuthenticatedNormal",'isNormalAdmin']),
    ...mapState(naverAuthenticationModule, ["isAuthenticatedNaver",'isNaverAdmin']),
  },
  methods: {
    ...mapActions(authenticationModule, ["requestKakaoLogoutToDjango"]),
    ...mapActions(googleAuthenticationModule, ["requestGoogleLogoutToDjango"]),
    ...mapActions(naverAuthenticationModule, ["requestNaverLogoutToDjango"]),
    ...mapActions(surveyModule,['requestRandomStringToDjango']),
    goToHome() {
      router.push("/");
    },
    goToProductList() {
      router.push("/companyReport/list");
    },

    goToCart() {
      router.push("/cart/list");
    },
    goToOrder() {
      router.push("/order/list");
    },
    goToManagementUserPage(){
      router.push('/management/user')
    },
    goToManagementUserLogList(){
      router.push('/management/log')
    },
    async goToSurvey() {
      const randomString = await this.requestRandomStringToDjango()
      if (randomString) {
        this.$router.push({
                name: 'SurveyReadPage',
                params: { randomString: randomString.toString() }
            })
      }
    },
    goToMyPage() {
      router.push("/account/mypage");
    },
    goToSurveyListPage() {
      router.push("/survey/list");
    },
    goToAiInterviewPage() {
      router.push("/ai-interview")
    },
    goToLlmTestPage() {
      router.push("/ai-interview/llmTest")
    },
    signIn() {
      router.push("/account/login");
    },
    signOut() {
      if (sessionStorage.getItem("loginType") == "KAKAO") {
        this.requestKakaoLogoutToDjango();
        this.$store.state.authenticationModule.isAuthenticatedKakao = false;
        this.$store.state.authenticationModule.isKakaoAdmin = false;
      }
      if (sessionStorage.getItem("loginType") == "GOOGLE") {
        this.requestGoogleLogoutToDjango();
        this.$store.state.googleAuthenticationModule.isAuthenticatedGoogle = false;
      }
      if (sessionStorage.getItem("loginType") == "NAVER") {
        this.requestNaverLogoutToDjango();
        this.$store.state.naverAuthenticationModule.isAuthenticatedNaver = false;
      }
      if (sessionStorage.getItem("loginType") == "NORMAL") {
        sessionStorage.removeItem("normalToken");
        sessionStorage.removeItem("email");
        sessionStorage.removeItem("loginType");
        sessionStorage.removeItem('adminToken')
        if (sessionStorage.getItem("fileKey")) {
          sessionStorage.removeItem("fileKey");
        }
      this.$store.state.accountModule.isAuthenticatedNormal = false;
      this.$store.state.authenticationModule.isKakaoAdmin = false
      this.$store.state.googleAuthenticationModule.isGoogleAdmin = false
      this.$store.state.naverAuthenticationModule.isNaverAdmin = false
      this.$store.state.accountModule.isNormalAdmin = false
      }
      router.push("/");
    },
  },
  mounted() {
    // console.log("navigation bar mounted()");
    const userToken = sessionStorage.getItem("userToken");
    if (userToken) {
      // console.log("You already has a userToken!");
      this.$store.state.authenticationModule.isAuthenticatedKakao = true;
    }
    const googleUserToken = sessionStorage.getItem("googleUserToken");
    if (googleUserToken) {
      // console.log("You already has a googleUserToken!")
      this.$store.state.googleAuthenticationModule.isAuthenticatedGoogle = true;
    }
    const naverUserToken = sessionStorage.getItem("naverUserToken");
    if (naverUserToken) {
      // console.log("You already has a naverUserToken!")
      this.$store.state.naverAuthenticationModule.isAuthenticatedNaver = true;
    }
    const normalToken = sessionStorage.getItem("normalToken");
    if (normalToken) {
      this.$store.state.accountModule.isAuthenticatedNormal = true;
    }
    const adminToken = sessionStorage.getItem("adminToken")
    if (adminToken){
      this.$store.state.authenticationModule.isKakaoAdmin = true
      this.$store.state.googleAuthenticationModule.isGoogleAdmin = true
      this.$store.state.naverAuthenticationModule.isNaverAdmin = true
      this.$store.state.accountModule.isNormalAdmin = true
    }
  },
};
</script>



<style scoped>
.menu-bar {
  background: var(--Gradient-Liner-1, linear-gradient(94deg, #0A28B0 1.69%, #8094F4 116.61%));
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
  color: white; /* 텍스트 색상도 흰색으로 변경 */  
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
  color: white; /* 텍스트 색상도 흰색으로 변경 */  
}


.btn-text:hover {
  background-color: rgba(255, 255, 255, 0.25);
  
}
/* 클릭해서 선택되었을시 표시 */
.btn-text:focus {
  background-color: rgba(255, 255, 255, 0.25); 
  color: white;
  
}

.v-menu > .v-overlay__content > .v-card,
.v-menu > .v-overlay__content > .v-sheet,
.v-menu > .v-overlay__content > .v-list {  
  background-color: rgba(0, 0, 0, 0.25);
  color: white;
  border: 3px solid white
}

.v-list-item:hover {
  background-color: rgba(255, 255, 255, 0.25);
  
}
</style>
