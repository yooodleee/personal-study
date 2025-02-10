<template>
    <div class="background">
    <v-container class="container">
      <v-card class="change-card">
        <v-card-title class="title">프로필 수정</v-card-title>
  
        <v-card-text>
          <v-form ref="form" v-model="valid" lazy-validation>
            <template v-if="isAuthenticatedNormal">
              <v-text-field
                v-model="currentPassword"
                label="Current Password"
                :type="showPassword ? 'text' : 'password'"
                :append-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
                @click:append="togglePasswordVisibility"
                :rules="[rules.required]"
                :error-messages="passwordErrorMessage"
              ></v-text-field>
              <v-text-field
                v-model="newPassword"
                label="New Password"
                :type="showPassword ? 'text' : 'password'"
                :append-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
                @click:append="togglePasswordVisibility"
                :rules="passwordRules"
              ></v-text-field>
  
              <v-text-field
                v-model="confirmPassword"
                label="Confirm New Password"
                :type="showPassword ? 'text' : 'password'"
                :append-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
                @click:append="togglePasswordVisibility"
                :rules="[rules.required, rules.matchPassword]"
              ></v-text-field>
  
              <v-btn class="mt-4" color=#212121 @click="validateAndChangePassword">
                Change Password
              </v-btn>
  
              <v-divider class="mt-4 mb-4"></v-divider>
            </template>
  
            <v-text-field
              v-model="newNickname"
              label="New Nickname"
              :rules="[rules.required]"
              @input="updateValidState"
              :error-messages="nicknameErrorMessages"
            ></v-text-field>
  
            <v-btn class="mt-4" @click="validateAndChangeNickname">
              닉네임 수정하기
            </v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useAccountStore } from '../../stores/accountStore'; // accountStore로 수정
import { useRouter } from 'vue-router';
// import { useSessionStorage } from '@vueuse/core'; // VueUse 라이브러리를 사용하여 세션 스토리지 관리

const router = useRouter();
const accountStore = useAccountStore()
// Data
const currentPassword = ref('');
const newPassword = ref('');
const confirmPassword = ref('');
const newNickname = ref('');
const valid = ref(false); // Track form validity
const showPassword = ref(false);
const isPasswordValid = ref(false);
const isNicknameValid = ref(false);
const passwordErrorMessage = ref('');
const nicknameErrorMessages = ref('');
const isGeneralLogin = ref(false); // Add this flag to determine if generalLogin exists

// Rules
const rules = {
  required: value => !!value || '변경할 닉네임을 입력해주세요.',
  matchPassword: value => value === newPassword.value || 'Passwords do not match',
};

const passwordRules = computed(() => [
  rules.required,
  v => v.length >= 8 || 'Password must be at least 8 characters long.',
  v => /[a-z]/.test(v) || 'Password must contain at least one lowercase letter.',
  v => /[!@#$%^&*(),.?":{}|<>]/.test(v) || 'Password must contain at least one special character.',
]);

// State from Pinia
const loginType = computed(() => accountStore.loginType);
const isAuthenticatedNormal = computed(() => accountStore.isAuthenticatedNormal);

// Check if generalLogin exists in sessionStorage on created
onMounted(() => {
  isGeneralLogin.value = !!sessionStorage.getItem('generalLogin');
});

// Methods
const togglePasswordVisibility = () => {
  showPassword.value = !showPassword.value;
};

const checkPassword = async () => {
  try {
    const isAccountCheck = await accountStore.requestAccountCheckToDjango({
      email: sessionStorage.getItem('email'),
      password: currentPassword.value,
    });

    if (isAccountCheck) {
      passwordErrorMessage.value = ''; // Clear the error message if the password is correct
      isPasswordValid.value = true;
    } else {
      passwordErrorMessage.value = '현재 비밀번호가 틀렸습니다.';
      isPasswordValid.value = false;
    }
  } catch (error) {
    passwordErrorMessage.value = '비밀번호 확인에 실패했습니다.';
    isPasswordValid.value = false;
  }
};

const validateAndChangePassword = async () => {
  await checkPassword();

  if (!isPasswordValid.value) {
    return;
  }

  if (newPassword.value !== confirmPassword.value) {
    alert('변경 비밀번호가 일치하지 않습니다.');
    return;
  }

  if (confirm("비밀번호를 변경하시겠습니까?")) {
    onChangePassword();
  }
};

const onChangePassword = () => {
  if (process.client){
  accountStore.requestPasswordModifyToDjango({
    email: sessionStorage.getItem('email'),
    newPassword: newPassword.value,
  })
    .then(() => {
      router.push('/account/login');
      sessionStorage.removeItem('loginType');
      sessionStorage.removeItem('email');
      sessionStorage.removeItem('normalToken');
      accountStore.isAuthenticatedNormal = false;
      alert('비밀번호가 성공적으로 변경되었습니다. 다시 로그인을 진행해주세요');
    })
    .catch(err => {
      console.error('Failed to change password:', err);
    });
  }
};

const onChangeNickname = () => {
  if (process.client){
    if (newNickname.value) {
      accountStore.requestNicknameModifyToDjango({
        email: sessionStorage.getItem('email'),
        newNickname: newNickname.value,
      })
        .then(() => {
          router.push('/');
          alert("닉네임이 성공적으로 변경되었습니다.");
        })
        .catch(err => {
          console.error('Failed to change nickname:', err);
        });
    }
  }
};

const checkNicknameDuplication = async () => {
  try {
    const isDuplicate = await accountStore.requestNicknameDuplicationCheckToDjango({
      newNickname: newNickname.value.trim(),
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

const validateAndChangeNickname = async () => {
  await checkNicknameDuplication();

  if (!isNicknameValid.value) {
    return;
  }

  if (confirm("닉네임을 변경하시겠습니까?")) {
    onChangeNickname();
  }
};

const updateValidState = () => {
  valid.value = !!newNickname.value; // Check if the nickname field is not empty
};
</script>

<style scoped>
.background{    
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.container {
  top: 0;
  position: absolute;  
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  
}

.change-card {
  position: relative;
  width: 500px;
  height: auto;
  overflow: hidden;
  text-align: center;  
  color: black;
  background-color: white;
  border: 2px solid white;
  border-radius: 32px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
}

.title {
  text-align: center;
  font-size: 24px;
  font-weight: bold;
}

.mt-4 {
  display: flex;
  justify-content: center !important;
  align-items: center !important;
  background: white;
  border: 1px solid lightgray;
  border-radius: 12px;
  color: black;
  margin-left: 35%;
}

</style>
