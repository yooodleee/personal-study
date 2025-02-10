<template>
    <v-container>
        <v-form class="reason-section">
            <h3>서비스 품질 향상을 위해 탈퇴 사유를 선택해주세요.</h3>
            <v-radio-group class="radio-group-section" v-model="selectedReason">
                <v-radio
                    v-for="(reason, index) in reasons"
                    :key="index"
                    :label="reason.label"
                    :value="reason.value"
                ></v-radio>
            </v-radio-group>
            <v-btn
                :disabled="!isButtonEnabled"
                @click="submitWithdrawal"
            >
                탈퇴 신청
            </v-btn>
        </v-form>
        <v-dialog v-model="dialog" max-width="500">
            <v-card>
                <v-card-title class="headline">알림</v-card-title>
                <v-card-text>회원 탈퇴가 완료되었습니다.</v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="green darken-1" text @click="closeDialog">확인</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-container>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useAccountStore } from '../../stores/accountStore'
import { useAuthenticationStore } from '../../../authentication/stores/authenticationStore'
import { useRouter } from 'vue-router'

// 탈퇴 사유 리스트
const reasons = ref([
  { label: '서비스 품질 불만족', value: 'SERVICE_DISSATISFACTION' },
  { label: '사용 빈도 낮음', value: 'LOW_USAGE' },
  { label: '다른 서비스 사용', value: 'OTHER_SERVICE' },
  { label: '개인정보 보호 우려', value: 'PRIVACY_CONCERN' },
  { label: '기타', value: 'OTHER' },
])

// 선택된 탈퇴 사유와 다이얼로그 상태
const selectedReason = ref(null)
const dialog = ref(false)

// store와 router 사용 설정
const accountStore = useAccountStore()
const authenticationStore = useAuthenticationStore()
const router = useRouter()

// 버튼 활성화 여부 계산
const isButtonEnabled = computed(() => selectedReason.value !== null)

// 탈퇴 신청 처리
const submitWithdrawal = () => {
  const reasonString = selectedReason.value ? String(selectedReason.value) : ''
  accountStore.requestWithdrawalToDjango({ reason: reasonString })
    .then(() => {
      dialog.value = true
    })
    .catch(err => {
      console.error('탈퇴 신청 실패:', err)
    })
}

// 다이얼로그 닫기 처리 및 로그아웃
const closeDialog = () => {
  dialog.value = false
  authenticationStore.requestKakaoLogoutToDjango()
  router.push('/')
}
</script>

<style scoped>

.reason-section {
    margin-top: 30px;
}

.radio-group-section {
    margin-top: 30px;
    margin-bottom: 10px;
}

</style>
