<template>
    <v-container class="container">
        <div class="login-wrapper">
            <div>
                 
                <div class="login_logo">
                    <!-- LOGIN 텍스트 대신 이미지 삽입 -->    
                </div>

                <div v-if="login_flag == false && this.isEmailCollect == false" class="login-error-box">
                    이메일이 올바르지 않습니다.
                    <br />
                    올바른 이메일을 입력하거나,
                    <br />
                    다른 간편로그인을 시도해 보세요.
                </div>
                <div v-if="login_flag == false && this.isEmailCollect == true && this.isPasswordCollect == false" class="login-error-box">
                    비밀번호가 올바르지 않습니다.
                    <br />
                    올바른 비밀번호를 입력하거나,
                    <br />
                    다른 간편로그인을 시도해 보세요.
                </div>

                <v-responsive class="mx-auto" min-width="300">
                    <v-form v-model="form" @submit.prevent="onSubmit">
                        <!-- <v-text-field
                            label="이메일 주소"
                            variant="solo"
                            v-model="email"
                            color="#fff"
                            bg-color="rgba(0, 0, 0, 0.5)"
                            clearable
                            :rules="[emailRequired]"
                            style="width: 75%; margin: 10px auto; display: block;"
                        />

                        <v-text-field
                            label="비밀번호"
                            variant="solo"
                            v-model="password"
                            color="#fff"
                            bg-color="rgba(0, 0, 0, 0.5)"
                            :rules="[passwordRequired]"
                            :append-inner-icon="visible ? 'mdi-eye' : 'mdi-eye-off'"
                            :type="visible ? 'text' : 'password'"
                            @click:append-inner="visible = !visible"
                            style="width: 75%; margin: 10px auto; display: block;"
                        /> -->

                        <!-- 로그인 버튼 -->
                        <!-- <v-btn
                            color="white"
                            :loading="loading"
                            type="submit"
                            variant="elevated"
                            style="width: 75%; margin: 5px auto; display: block; font-size: 12px;"
                        >
                            <b>로그인</b>
                        </v-btn> -->
                    </v-form>
                </v-responsive>

                <!-- 회원가입 버튼 -->
                <!-- <v-btn
                    color="purple darken-2"
                    class="black--text mt-2"
                    style="width: 75%; margin: 5px auto; display: flex; align-items: center; justify-content: center; font-size: 12px;"
                    :to="{ name: 'NomalAccountRegisterPage' }"
                >
                    <b>회원가입</b>
                </v-btn> -->

                <!-- 영역 구분선 -->
                <!-- <v-divider :thickness="3" style="margin-top: 20px; margin-bottom: 20px;"></v-divider> -->

                <!-- 각 소셜 로그인 버튼들 -->
                <v-btn class="kakao-login-btn" @click="goToKakaoLogin">
                    <!-- 카카오 로그인 -->
                </v-btn>

                <v-btn class="google-login-btn" @click="goToGoogleLogin">
                    <!-- Google 로그인 -->
                </v-btn>

                <v-btn class="naver-login-btn" @click="goToNaverLogin">
                    <!-- 네이버 로그인 -->
                </v-btn>
            </div>
        </div>
    </v-container>
</template>


<script>
import router from "@/router";
import { useStore, mapActions, mapState, mapMutations } from "vuex";

const accountModule = 'accountModule'
const authenticationModule = 'authenticationModule'
const googleAuthenticationModule = 'googleAuthenticationModule'
const naverAuthenticationModule = 'naverAuthenticationModule'

export default {
    data: () => ({
        form: false,
        email: null,
        password: null,
        visible: false,
        loading: false,
        login_flag: true,
        isEmailCollect: false,
        isPasswordCollect: false,
    }),

    setup() {
        const store = useStore();

        const goToKakaoLogin = async () => {
            sessionStorage.setItem("loginType", "KAKAO") 

            await store.dispatch(
                "authenticationModule/requestKakaoOauthRedirectionToDjango"
            );
            

        };
        const goToGoogleLogin = async () => {
            // alert("현재 로그인 검수중입니다.")
            sessionStorage.setItem("loginType", "GOOGLE") 
            await store.dispatch(
                "googleAuthenticationModule/requestGoogleOauthRedirectionToDjango"
            )
        }
        const goToNaverLogin = async () => {
            alert("현재 로그인 검수중입니다.")
            // sessionStorage.setItem('loginType', "NAVER")
            // await store.dispatch(
            //     "naverAuthenticationModule/requestNaverOauthRedirectionToDjango"
            // )
        }

        return {
            goToKakaoLogin,
            goToGoogleLogin,
            goToNaverLogin,
        };
    },
    computed: {
    ...mapState(authenticationModule, ["isAuthenticatedKakao"]),
    ...mapState(accountModule, ["isAuthenticatedNormal", "loginType",'isKakaoAdmin']),
    ...mapState(googleAuthenticationModule, ["isAuthenticatedGoogle"]),
    ...mapState(naverAuthenticationModule, ["isAuthenticatedNaver"]),
    },
    methods: {
        ...mapActions(accountModule, ['requestAccountCheckToDjango','requestRoleTypeToDjango']),
        ...mapMutations(accountModule,['REQUEST_IS_ADMIN_TO_DJANGO']),
        goToHome() {
            router.push("/");
        },

        goToSignUp() {
            router.push("/account/register/normal"); 
        },
        async onSubmit() {
            if (!this.form) return;
            this.loading = true;
            try {
                const response = await this.checkPassword();
                const roleType = await this.requestRoleTypeToDjango(this.email);
                if (response) {
                    this.login_flag = true; // 로그인 성공
                    sessionStorage.setItem('email', this.email);
                    sessionStorage.setItem('loginType', 'NORMAL');
                    if (roleType.data.roleType == "ADMIN") {
                        // Admin 처리
                        sessionStorage.removeItem('normalToken');
                        sessionStorage.setItem('adminToken', true);
                        this.REQUEST_IS_ADMIN_TO_DJANGO(true);
                        // console.log(this.$store.state.accountModule.isKakaoAdmin)
                        this.goToHome();
                    } else {
                        // Normal 처리
                        sessionStorage.setItem('normalToken', true);
                        this.$store.state.accountModule.isAuthenticatedNormal = true;
                        this.goToHome();
                    }
                } else {
                    // 로그인 실패 처리
                    this.login_flag = false;
                }
            } catch (error) {
                console.error("로그인 중 에러 발생: ", error);
                this.login_flag = false;
            } finally {
                this.loading = false;
            }
        },

        emailRequired(v) {
            return !!v || "정확한 이메일 주소를 입력하세요.";
        },

        passwordRequired(v) {
            return !!v || "비밀번호는 8~20자 사이여야 합니다.";
        },
        async checkPassword() {
            try {
                const payload = {
                    email: this.email,
                    password: this.password
                }
                const response = await this.requestAccountCheckToDjango(payload)
                return response
            } catch (error) {
                console.error("비밀번호 확인 중 에러 발생: ", error)
            }
        },
    },
};
</script>



<style scoped>
.container {   
    max-width: 100vw;
    height: 100%;    
    display: flex;                  
    justify-content: center;        
    align-items: center;            
    box-sizing: border-box;        
    background-color: white;      
    background: url("@/assets/images/fixed/login_bg.png") no-repeat center center;
    background-size: cover;                                                    
}

.login_logo {
    height: 20vh;
    margin-bottom: 60px;
    overflow: hidden;
    background-image: url("@/assets/images/fixed/AIM_BI_White.png");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;    
}

/* 로그인 박스 설정 */
.login-wrapper {
    position: relative;
    z-index: 1;   
    width: 520px;
    height: 576px;   
    background-color: rgba(255, 255, 255, 0.08);     
    border: 1px solid rgba(128, 128, 128, 0.8);
    border-radius: 40px;    
    padding: 70px 60px;    
}

/* 에러 메시지 박스 설정 */
.login-error-box {
    background-color: rgb(255, 0, 0);
    padding: 10px;
    margin-bottom: 1px;
    border-radius: 20px;
    color: #fff;
}

/* 로그인 및 회원가입 버튼 설정 */
.v-btn {
    width: 100%;
    height: 48px; 
    margin: 10px auto;
    display: flex;
    align-items: center;  
    justify-content: center;  
}


/* Kakao 로그인 버튼 설정 */
.kakao-login-btn {
    background-image: url("@/assets/images/fixed/btn_login_kakao.png");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;   
    display: flex;
    align-items: center;
    justify-content: center;
    background-color:#FFEA00;
    margin-bottom: 12px;
    border-radius: 10px;
}

/* Google 로그인 버튼 설정 */
.google-login-btn {
    background-image: url("@/assets/images/fixed/btn_login_google.png");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;       
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #fff;
    margin-bottom: 12px;
    border-radius: 10px;
}
.naver-login-btn {
    background-image: url("@/assets/images/fixed/btn_login_naver.png");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;      
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #03C75A;
    border-radius: 10px;
}

.v-text-field input {
    background-color: transparent !important;
    color: black !important; /* 입력값을 검정색으로 설정 */
}

.v-label {
    color: black !important; /* 레이블을 검정색으로 설정 */
}


/* 로그인 폼의 텍스트 필드 라벨 색상 설정 */
:deep(.v-label.v-field-label) {
    color: rgba(255, 255, 255, 0.8) !important;
}

/* 로그인 폼의 텍스트 필드 입력값 색상 설정 */
:deep(.v-text-field input) {
    color: #fff;
}

/* 눈 아이콘 색상 설정 */
:deep(.mdi-eye::before), :deep(.mdi-eye-off::before) {
    color: rgba(255, 255, 255, 0.8) !important;
}

/* 오류 메시지 스타일링 */
:deep(.v-messages__message) {
    color: rgb(0, 0, 255)!important; /* 메시지 색상 */
    font-size: 12px; /* 메시지 폰트 크기 */
}

/* 텍스트 필드 에러 상태의 레이블 색상을 초록색으로 변경 */
:deep(.v-field--error:not(.v-field--disabled) .v-label.v-field-label) {
    color: rgba(0, 0, 255) !important; /* 에러 상태의 레이블 색상을 초록색으로 변경 */
}

</style>