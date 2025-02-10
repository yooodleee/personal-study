<template>
    <div></div>
  </template>
  
  <script setup>
  import { useRouter, useRoute } from 'vue-router';
  import { onMounted } from 'vue';
  import { useAccountStore } from '../../../account/stores/accountStore'; // accountStore를 Pinia에서 가져오기
  import { useAuthenticationStore } from '@/stores/authenticationStore'; // authenticationStore를 Pinia에서 가져오기
  
  // Pinia 스토어 가져오기
  const accountStore = useAccountStore();
  const authenticationStore = useAuthenticationStore();
  
  // Vue Router
  const router = useRouter();
  const route = useRoute();
  
  // Methods
  const setRedirectData = async () => {
    const code = route.query.code; // 쿼리에서 'code' 값 가져오기
  
    await authenticationStore.requestAccessTokenToDjangoRedirection({ code });
    const userInfo = await authenticationStore.requestUserInfoToDjango();
    const email = userInfo.kakao_account.email;
  
    const isEmailDuplication = await accountStore.requestEmailDuplicationCheckToDjango({ email });
    
    if (isEmailDuplication === true) {
      const accessToken = sessionStorage.getItem('accessToken');
  
      if (accessToken) {
        await authenticationStore.requestAddRedisAccessTokenToDjango({ email, accessToken });
      } else {
        console.error('AccessToken is missing');
      }
  
      const roleType = await accountStore.requestRoleTypeToDjango(email);
  
      if (roleType.data.roleType === 'ADMIN') {
        sessionStorage.setItem('adminToken', sessionStorage.getItem('userToken'));
        sessionStorage.removeItem('userToken');
        authenticationStore.isAuthenticatedKakao = true
        authenticationStore.isAdmin = true; // 상태를 변경하는 Pinia 방식
      }
  
      sessionStorage.setItem('email', email);
      sessionStorage.setItem('loginType', 'KAKAO');
      router.push('/');
    } else {
      router.push('/account/register');
    }
  };
  
  // onMounted hook (created 대신 사용)
  onMounted(async () => {
    await setRedirectData();
  });
  </script>
  