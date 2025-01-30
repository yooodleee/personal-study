<template>
    <v-container class="register-container" fill-height>
        <v-row align="center" justify="center">
            <v-col cols="12" md="8" lg="6">
                <v-card>
                    <v-card-title>
                        <span class="headline">간편 신규 회원가입</span>
                    </v-card-title>
                    

                    <v-responsive class="mx-auto" min-width="400">
                        <v-form ref="form" v-model="formValid" lazy-validation>
                            <v-text-field v-if="loginType === 'KAKAO'"
                                    v-model="kakaoEmail"
                                    label="Email"
                                    variant="solo"                                    
                                    required
                                    :rules="emailRules"
                                    :disabled="true"/>
                            <v-text-field v-if="loginType === 'NAVER'"
                                    v-model="naverEmail"
                                    label="Email"
                                    variant="solo"                                    
                                    required
                                    :rules="emailRules"
                                    :disabled="true"/>
                            <v-text-field v-if="loginType === 'GOOGLE'"
                                v-model="googleEmail"
                                label="Email"
                                variant="solo"                                    
                                required
                                :rules="emailRules"
                                :disabled="true"/> 
                            <v-row align="center">
                                <v-col cols="10">
                                    <v-text-field
                                            v-model="nickname"
                                            label="Nickname"
                                            required
                                            :rules="nicknameRules"
                                            :error-message="nicknameErrorMessages"/>
                                </v-col>
                                
                                <v-col cols="2">
                                    <v-btn
                                        color="gb(200, 255, 0)"
                                        style="color: black; width:90px"                                        
                                        small
                                        :disabled="
                                            nickname == '' ||
                                            isNicknameValid == true"
                                        type="button"
                                        @click="checkNicknameDuplication">
                                        중복 검사
                                    </v-btn>
                                </v-col>
                            </v-row>
                            
                            <div v-if="isNicknameValid" class="valid-nickname-box" style="color: chartreuse;">
                                        사용 가능한 닉네임입니다.
                            </div>

                            <div style="margin-top: 32px;">
                                <v-radio-group
                                    v-model="gender"
                                    inline
                                    label="성별"
                                    color="black">
                                    <v-radio
                                        label="남성"
                                        value="MALE"
                                        color="cyan"
                                        base-color="white"
                                    ></v-radio>
                                    <v-radio
                                        label="여성"
                                        value="FEMALE"
                                        color="pink"
                                        base-color="white"
                                    ></v-radio>
                                </v-radio-group>
                            </div>

                            

                        <v-text-field
                                v-model="birthyear"
                                label="출생년도" 
                                :rules="birthyearRules"
                                required            
                        />                       
                        
                        </v-form>
                    </v-responsive>    
                    

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="black" 
                                @click="submitForm" 
                                :disabled="!isValidForSubmission">
                            회원가입 하기
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAccountStore } from '@/stores/accountStore';
import { useAuthenticationStore } from '../../../authentication/stores/authenticationStore';
import { useGoogleAuthenticationStore } from '../../../googleAuthentication/stores/googleAuthenticationStore';
import { useNaverAuthenticationStore } from '../../../naverAuthentication/stores/naverAuthenticationStore';

// Pinia 스토어 사용
const accountStore = useAccountStore();
const authenticationStore = useAuthenticationStore();
const googleAuthenticationStore = useGoogleAuthenticationStore();
const naverAuthenticationStore = useNaverAuthenticationStore();

// Router 사용
const router = useRouter();

// form validation 관련 상태 정의
const formValid = ref(false);
const email = ref('');
const kakaoEmail = ref('');
const googleEmail = ref('');
const naverEmail = ref('');
const password = ref('');
const nickname = ref('');
const gender = ref('MALE');
const birthyear = ref('');
const nicknameErrorMessages = ref([]);
const isNicknameValid = ref(false);

// 규칙들
const emailRules = [
  v => !!v || 'Email 은 필수입니다!',
  v => /.+@.+\..+/.test(v) || '유효한 Email 주소를 입력하세요!',
];
const nicknameRules = [v => !!v || 'Nickname은 필수입니다!'];
const birthyearRules = [
  v => !!v || '출생년도는 필수입니다!',
  v => /^\d+$/.test(v) || '출생년도는 숫자여야 합니다!',
  v => v.length === 4 || '출생년도는 4자리여야 합니다!',
];

// 로그인 타입 가져오기
const loginType = ref(sessionStorage.getItem('loginType'));

// 컴퓨티드: form 유효성 검증
const isValidForSubmission = computed(() => {
  return formValid.value && isNicknameValid.value && birthyear.value !== '';
});

// 사용자 정보 요청
const requestUserInfo = async () => {
  try {
    if (loginType.value === 'KAKAO') {
      const kakaoUserInfo = await authenticationStore.requestUserInfoToDjango();
      kakaoEmail.value = kakaoUserInfo.kakao_account.email;
    } else if (loginType.value === 'GOOGLE') {
      const googleUserInfo = await googleAuthenticationStore.requestGoogleUserInfoToDjango();
      googleEmail.value = googleUserInfo.email;
    } else if (loginType.value === 'NAVER') {
      const naverUserInfo = await naverAuthenticationStore.requestNaverUserInfoToDjango();
      naverEmail.value = naverUserInfo.response.email;
    }
  } catch (error) {
    console.error('에러:', error);
    alert('사용자 정보를 가져오는데 실패하였습니다!');
  }
};

// 닉네임 중복 확인
const checkNicknameDuplication = async () => {
  try {
    const isDuplicate = await accountStore.requestNicknameDuplicationCheckToDjango({
      newNickname: nickname.value.trim(),
    });

    if (isDuplicate) {
      nicknameErrorMessages.value = ['이 nickname은 이미 사용중입니다!'];
      isNicknameValid.value = false;
    } else {
      nicknameErrorMessages.value = [];
      isNicknameValid.value = true;
    }
  } catch (error) {
    alert('닉네임 중복 확인에 실패했습니다!');
    isNicknameValid.value = false;
  }
};

// 폼 제출
const submitForm = async () => {
  if (isValidForSubmission.value) {
    if (loginType.value === 'KAKAO') {
      email.value = kakaoEmail.value;
    } else if (loginType.value === 'GOOGLE') {
      email.value = googleEmail.value;
    } else if (loginType.value === 'NAVER') {
      email.value = naverEmail.value;
    } else {
      alert('알 수 없는 로그인 타입입니다. 다시 시도해 주세요.');
      return;
    }

    if (!email.value) {
      alert('이메일이 설정되지 않았습니다. 다시 시도해 주세요.');
      return;
    }

    const accountInfo = {
      email: email.value,
      password: password.value,
      nickname: nickname.value,
      gender: gender.value,
      birthyear: birthyear.value,
      loginType: loginType.value,
    };

    await accountStore.requestCreateNewAccountToDjango(accountInfo);

    let accessToken;
    if (loginType.value === 'KAKAO') {
      accessToken = sessionStorage.getItem('accessToken');
    } else if (loginType.value === 'GOOGLE') {
      accessToken = sessionStorage.getItem('googleAccessToken');
    } else if (loginType.value === 'NAVER') {
      accessToken = sessionStorage.getItem('naverAccessToken');
    }

    if (accessToken) {
      if (loginType.value === 'KAKAO') {
        await authenticationStore.requestAddRedisAccessTokenToDjango({ email: accountInfo.email, accessToken });
      } else if (loginType.value === 'GOOGLE') {
        await googleAuthenticationStore.requestAddGoogleRedisAccessTokenToDjango({ email: accountInfo.email, accessToken });
      } else if (loginType.value === 'NAVER') {
        await naverAuthenticationStore.requestAddNaverRedisAccessTokenToDjango({ email: accountInfo.email, accessToken });
      }
    } else {
      console.error('AccessToken is missing');
    }

    sessionStorage.setItem('email', accountInfo.email);
    router.push('/');
  }
};

// onMounted 훅을 사용해 created 훅 대신 설정
onMounted(async () => {
  await requestUserInfo();
});
</script>


<style scoped>
/* 전체 화면을 가득 채우는 컨테이너 */
.register-container {
    margin: 0;
    width: 100%;
    max-width: 100vw;
    height: 100vh;
    display: flex;                  /* Flexbox 사용하여 가운데 정렬 */
    justify-content: center;        /* 수평 가운데 정렬 */
    align-items: center;            /* 수직 가운데 정렬 */
    padding: 0;
    background: url("@/assets/images/fixed/login_bg.png") no-repeat center center; /* 배경 이미지 설정 */
    background-size: cover;                                                     /* 배경 이미지 크기 조정 */
}

/* 카드 스타일링 */
.v-card {
    position: relative;
    z-index: 1;
    background-color: rgba(0, 0, 0, 0.9); /* 반투명한 검은색 배경 */
    color: white; /* 텍스트 색상: 흰색 */
    min-width: 400px; /* 카드의 최소 너비 */
    min-height: 500px; /* 카드의 최소 높이 */
    padding: 20px; /* 카드 내부의 패딩 */
    border-radius: 20px; /* 카드의 모서리 둥글게 */
}

/* 버튼 스타일링 */
.v-btn {
    position: relative;
    padding: 8px 16px; /* 버튼 내부 패딩 */
    margin-right: 10px; /* 오른쪽 여백 */
    background-color: rgba(0, 255, 55, 0.75); /* 버튼 배경색 */
}

/* 성별 라디오 그룹의 레이블 스타일링 */
:deep(.v-radio-group > .v-input__control > .v-label) {
    color: #fff !important; /* 레이블 색상: 흰색 */
    margin-inline-start: 0px !important; /* 레이블 시작 마진 제거 */
    margin-bottom: 12px !important; /* 레이블 하단 여백 */
    opacity: 1 !important; /* 투명도: 100% */
}

/* 성별 라디오 그룹의 선택 컨트롤 스타일링 */
:deep(
        .v-radio-group
            > .v-input__control
            > .v-label
            + .v-selection-control-group
    ) {
    padding-inline-start: 0px !important; /* 패딩 시작 부분 제거 */
    margin-top: 0px !important; /* 상단 여백 제거 */
}

/* 오류 메시지 스타일링 */
:deep(.v-messages__message) {
    color: rgba(0, 255, 55, 0.75)!important; /* 메시지 색상 */
    font-size: 15px; /* 메시지 폰트 크기 */
}

/* 텍스트 필드 에러 상태의 레이블 색상을 초록색으로 변경 */
:deep(.v-field--error:not(.v-field--disabled) .v-label.v-field-label) {
    color: rgba(0, 255, 55, 0.75) !important; /* 에러 상태의 레이블 색상을 초록색으로 변경 */
}

</style>