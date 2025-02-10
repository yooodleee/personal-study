<template>
    <div></div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

import { useAccountStore } from '../../account/stores/accountStore';
import { useKakaoAuthenticationStore } from '../../kakaoAuthentication/stores/kakaoAuthenticationStore'

const accountStore = useAccountStore()
const kakaoAuthenticationStore = useKakaoAuthenticationStore()

const router = useRouter()
const route = useRoute()

const setRedirectKakaoData = async() => {
    const code = route.query.code
    const userToken = await kakaoAuthenticationStore.requestAccessToken(code);

    localStorage.setItem("userToken", userToken)
    kakaoAuthenticationStore.isAuthenticated = true

    router.push('/')
}

onMounted(async () => {
    await setRedirectKakaoData()
})
</script>