<template>
    <v-container class="container">
  
      <div class="id-card-container">    
        <v-card class="id-card mx-auto">
          <!-- <div class="company-name" >AIM</div> -->
          <v-avatar size="120px" class="mt-8 avatar-margin">
            <v-img :src="imageSrc"></v-img>
          </v-avatar>
          
          <v-card-text>
            <h2 class="text-h5 mb-2" style="margin-top: 24px; margin-bottom: 16px; font-weight: 700;">{{ nickname }}</h2>
            
            <v-divider class="my-3"></v-divider>
            <v-row class="myinfo">
              <v-col cols="12">
                <v-icon>{{
                  gender === "MALE" ? "mdi-gender-male" : "mdi-gender-female"
                }}</v-icon>
                <span class="ml-1">{{ gender === "MALE" ? "남성" : "여성" }}</span>
                &nbsp;&nbsp;&nbsp;
                <v-icon>mdi-calendar</v-icon>
                <span class="ml-1">{{ birthyear }}</span>
                &nbsp;&nbsp;&nbsp;
                <v-icon>mdi-email</v-icon>
                <span class="subtitle-1">{{ email }}</span>
              </v-col>            
            </v-row>
            
            <v-row justify="center">
              
              <v-col cols="6">
                <v-btn class="btn-update" @click="$router.push({ name: 'AccountModifyPage' })">
                  프로필 수정
                </v-btn>
              </v-col>
              
              <v-col cols="6">              
                <button class="delete_button" type="button" @click="$router.push({ name: 'AccountWithdrawPage' })">
                  <span class="delete_button_text">탈퇴하기</span>
                  <span class="delete_button_icon"
                    ><svg
                      class="svg"
                      height="512"
                      viewBox="0 0 512 512"
                      width="512"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <title></title>
                      <path
                        d="M112,112l20,320c.95,18.49,14.4,32,32,32H348c17.67,0,30.87-13.51,32-32l20-320"
                        style="fill:none;stroke:#fff;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px"
                      ></path>
                      <line
                        style="stroke:#fff;stroke-linecap:round;stroke-miterlimit:10;stroke-width:32px"
                        x1="80"
                        x2="432"
                        y1="112"
                        y2="112"
                      ></line>
                      <path
                        d="M192,112V72h0a23.93,23.93,0,0,1,24-24h80a23.93,23.93,0,0,1,24,24h0v40"
                        style="fill:none;stroke:#fff;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px"
                      ></path>
                      <line
                        style="fill:none;stroke:#fff;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px"
                        x1="256"
                        x2="256"
                        y1="176"
                        y2="400"
                      ></line>
                      <line
                        style="fill:none;stroke:#fff;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px"
                        x1="184"
                        x2="192"
                        y1="176"
                        y2="400"
                      ></line>
                      <line
                        style="fill:none;stroke:#fff;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px"
                        x1="328"
                        x2="320"
                        y1="176"
                        y2="400"
                      ></line></svg
                  ></span>
                </button>
  
              </v-col>            
            </v-row>
            
          </v-card-text>
        </v-card>
      </div>
      
       <!-- 탈퇴 버튼을 카드 외부로 위치 -->
       <v-row justify="center" class="mt-4">
        
      </v-row>  
      
    </v-container>
      
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useAccountStore } from '../../stores/accountStore'; // Pinia store 사용
import profileImg from '@/assets/images/fixed/profile_img.png';
import { useRouter } from 'vue-router';

const imageSrc = profileImg;
const email = ref('');
const nickname = ref('');
const gender = ref('');
const birthyear = ref(0);
const menuOpen = ref(false);

const accountStore = useAccountStore();
const router = useRouter();

onMounted(async () => {
  try {
    const storedEmail = sessionStorage.getItem('email');
    await accountStore.requestProfileToDjango({'email':storedEmail})
    if (storedEmail) {
      const nicknameValue = await accountStore.nickname;
      const genderValue = await accountStore.gender;
      const birthyearValue = await accountStore.birthyear;
      
      email.value = storedEmail;
      nickname.value = nicknameValue;
      gender.value = genderValue;
      birthyear.value = birthyearValue;
    }
  } catch (error) {
    console.log('사용자 정보를 가져오는 과정에서 에러 발생:', error);
  }
});

function onClickAccountWithdraw() {
  router.push({ name: 'AccountWithdrawPage' });
}

function showMenu() {
  menuOpen.value = true;
}

function hideMenu() {
  menuOpen.value = false;
}
</script>

<style scoped>

/* 전체 컨테이너 설정 */
.container {
  min-height: 100vh;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* id-card-container 설정 */
.id-card-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 60px;
}

/* id-card 스타일 */
.id-card {
  position: relative;
  width: 436px;
  height: auto;
  overflow: hidden;
  text-align: center;  
  padding: 20px;
  color: black;
  background-color: white;
  border: 2px solid white;
  border-radius: 32px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);  
}


/* 최상단 AIN 문구 */
.company-name {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 20px;
}

.myinfo {
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #D7DBEC;
  border: 1px solid D7DBEC;
  border-radius: 12px;
  margin-bottom: 40px; 
}

/* 프로필 수정 버튼 */
.btn-update {  
  display: flex;
  justify-content: center !important;
  align-items: center !important;
  background: white;
  border: 1px solid lightgray;
  border-radius: 12px;
  color: black;
  margin-left: 20%;
}

/* 회원 삭제 버튼 */
.delete_button {
  position: relative;
  border-radius: 12px;
  width: 120px;
  height: 36px;
  cursor: pointer;
  display: flex;
  align-items: center;
  border: 1px solid #cc0000;
  background-color: #e50000;
  overflow: hidden;
}

.delete_button,
.delete_button_icon,
.delete_button_text {
  transition: all 0.3s;
}

.delete_button .delete_button_text {
  transform: translateX(25px);
  color: #fff;
  font-weight: 600;
}

.delete_button .delete_button_icon {
  position: absolute;
  transform: translateX(95px);
  height: 100%;
  width: 20px;
  background-color: #cc0000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.delete_button .svg {
  width: 20px;
}

.delete_button:hover {
  background: #cc0000;
}

.delete_button:hover .delete_button_text {
  color: transparent;
}

.delete_button:hover .delete_button_icon {
  width: 120px;
  transform: translateX(0);
}

.delete_button:active .delete_button_icon {
  background-color: #b20000;
}

.delete_button:active {
  border: 1px solid #b20000;
}


</style>
