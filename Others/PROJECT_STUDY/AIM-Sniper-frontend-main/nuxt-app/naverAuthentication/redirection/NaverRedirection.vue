<template>
    <div></div>
  </template>
  
  <script setup>
  import { onMounted, ref } from 'vue';
  import { useRouter, useRoute } from 'vue-router';
  import { useAccountStore } from '../../account/stores/accountStore';  // Pinia에서 AccountStore 가져오기
  import { useNaverAuthenticationStore } from '@/stores/naverAuthenticationStore'; // Pinia에서 NaverAuthenticationStore 가져오기
  
  // Pinia 스토어 사용
  const accountStore = useAccountStore();
  const naverAuthenticationStore = useNaverAuthenticationStore();
  
  // Vue Router 사용
  const router = useRouter();
  const route = useRoute();
  
  // 이메일 중복 확인 후 Redirect 처리 함수
  const setRedirectData = async () => {
    try {
      const code = route.query.code;
  
      // Naver Access Token을 가져오기 위한 요청
      await naverAuthenticationStore.requestNaverAccessTokenToDjangoRedirection({ code });
  
      // 사용자 정보 가져오기
      const naverUserInfo = await naverAuthenticationStore.requestNaverUserInfoToDjango();
      if (!naverUserInfo) {
        console.error('userInfo is undefined.');
        return;
      }
  
      const email = naverUserInfo.response.email;
      // 이메일 중복 확인
      const isEmailDuplication = await accountStore.requestEmailDuplicationCheckToDjango({'email':email});
      
      if (isEmailDuplication === true) {
        // 기존 가입 고객 처리
        const accessToken = sessionStorage.getItem("naverAccessToken");
  
        if (accessToken) {
          await naverAuthenticationStore.requestAddNaverRedisAccessTokenToDjango({email, accessToken});
        } else {
          console.error('AccessToken is missing');
        }
  
        // 사용자 Role Type 확인
        const roleType = await accountStore.requestRoleTypeToDjango(email);
        // console.log(roleType.data.roleType);
  
        if (roleType.data.roleType === "ADMIN") {
          sessionStorage.setItem('adminToken', sessionStorage.getItem('userToken'));
          sessionStorage.removeItem('userToken');
  
          naverAuthenticationStore.isAuthenticatedNaver = false; // 구글 인증 상태 해제
          naverAuthenticationStore.isNaverAdmin = true; // 구글 관리자 설정
        }
  
        sessionStorage.setItem('loginType', 'NAVER');
        sessionStorage.setItem('email', email);
  
        router.push('/');
      } else {
        // 신규 가입 고객 처리
        router.push('/account/register');
      }
    } catch (error) {
      console.error('오류 발생:', error);
    }
  };
  
  // onMounted를 사용하여 컴포넌트가 생성될 때 함수 호출
  onMounted(async () => {
    await setRedirectData();
  });
  </script>
  