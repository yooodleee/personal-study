<template>
    <div></div>
  </template>
  
<script setup lang="ts">
  import { useRoute, useRouter } from 'vue-router'
  import { useAccountStore } from '../../account/stores/accountStore'
  import { onMounted } from 'vue'
  import { useGoogleAuthenticationStore } from '../stores/googleAuthenticationStore';
  
  const googleAuthStore = useGoogleAuthenticationStore()
  const accountStore = useAccountStore()
  
  const route = useRoute()
  const router = useRouter()
  
  const setRedirectData = async () => {
    const code = route.query.code as string

    await googleAuthStore.requestGoogleAccessTokenToDjangoRedirection(code)
    const googleUserInfo = await googleAuthStore.requestGoogleUserInfoToDjango()
  
    if (!googleUserInfo) {
      console.error('userInfo is undefined.')
      return
    }
  
    const email = googleUserInfo.email
    
    const isEmailDuplication = await accountStore.requestEmailDuplicationCheckToDjango({'email':email})
    // console.log(isEmailDuplication)
    if (isEmailDuplication === true) {
      const accessToken = sessionStorage.getItem('googleAccessToken')
      if (accessToken) {
        await googleAuthStore.requestAddGoogleRedisAccessTokenToDjango({email, accessToken})
      } else {
        console.error('AccessToken is missing')
      }
  
      const roleType = await accountStore.requestRoleTypeToDjango(email)
      // console.log(roleType.data.roleType)
  
      if (roleType.data.roleType === 'ADMIN') {
        sessionStorage.setItem('adminToken', sessionStorage.getItem('userToken')!)
        sessionStorage.removeItem('userToken')
        googleAuthStore.isAuthenticatedGoogle = false
        googleAuthStore.isGoogleAdmin = true
      }
  
      sessionStorage.setItem('loginType', 'GOOGLE')
      sessionStorage.setItem('email', email)
      router.push('/')
    } else {
      router.push('/account/register')
    }
  }
  
  // 컴포넌트가 로드될 때 `setRedirectData` 함수 실행
  onMounted(async () => {
    await setRedirectData()
  })
  </script>
  