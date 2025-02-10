<template>
  <div class="main">
    <h1>User List</h1>
    <v-data-table
      :headers="headers"
      :items="managementStore.userList.data"
      item-key="userId"
      class="elevation-1"
    >
      <template v-slot:[`item.gender`]="{ item }">
        {{ translateGender(item.gender) }}
      </template>

      <template v-slot:[`item.login_type`]="{ item }">
        {{ translateLoginType(item.login_type) }}
      </template>

      <template v-slot:[`item.role_type`]="{ item }">
        {{ translateRoleType(item.role_type) }}
      </template>

      <template v-slot:[`item.last_login`]="{ item }">
        {{ formatDate(item.last_login) }}
      </template>

      <template v-slot:[`item.actions`]="{ item }">
        <v-btn @click="toggleAdminRole(item)" color="primary">
          {{ item.role_type === 'ADMIN' ? 'Revoke Admin' : 'Grant Admin' }}
        </v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useManagementStore } from '../stores/mangementStore';

const headers = ref([
  { text: 'User ID', value: 'userId' },
  { text: 'Email', value: 'email' },
  { text: 'Gender', value: 'gender' },
  { text: 'Birth Year', value: 'birthyear' },
  { text: 'Login Type', value: 'login_type' },
  { text: 'Role Type', value: 'role_type' },
  { text: 'Last Login', value: 'last_login' },
  { text: 'Actions', value: 'actions', sortable: false },
]);

const managementStore = useManagementStore();

// 유저 리스트 가져오기 메서드
async function loadUserList() {
  await managementStore.requestUserListToDjango();
}

onMounted(() => {
  loadUserList();
});

function translateGender(gender) {
  return gender === 'MALE' ? '남성' : gender === 'FEMALE' ? '여성' : '';
}

function translateLoginType(loginType) {
  const types = {
    'KAKAO': '카카오',
    'NAVER': '네이버',
    'GOOGLE': '구글',
    'NORMAL': '일반 로그인',
  };
  return types[loginType] || '알 수 없음';
}

function translateRoleType(roleType) {
  return roleType === 'ADMIN' ? '관리자' : roleType === 'NORMAL' ? '일반 회원' : '';
}

function formatDate(dateString) {
  const options = { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit' };
  return new Date(dateString).toLocaleString('ko-KR', options);
}

async function toggleAdminRole(user) {
  if (user.role_type === 'ADMIN') {
    await managementStore.revokeAdminRoleInDjango(user.email);
    alert('관리자 권한이 해제되었습니다.');
  } else {
    await managementStore.grantAdminRoleInDjango(user.email);
    alert('관리자 권한이 부여되었습니다.');
  }
  loadUserList();
}
</script>

<style scoped>
.main{
  margin-top: 10vh;
  text-align: center;
}
h1 {
  margin-top: 20px; /* 제목 위쪽 여백 */
  font-weight: bold; /* 강조 스타일 추가 */
  font-size: 1.8rem; /* 글자 크기 키우기 */
  color: #333; /* 색상 추가 */
}

.v-data-table-header {
  background-color: #e0e0e0; /* 테이블 헤더 배경색을 더 명확하게 설정 */
  color: #333; /* 헤더 텍스트 색상 */
  font-weight: bold;
  font-size: 1rem; /* 글자 크기 */
}

.v-data-table thead th {
  background-color: #f5f5f5; /* 테이블 헤더의 배경색을 좀 더 구분되게 설정 */
  color: #333;
  font-weight: bold;
  text-align: center; /* 테이블 헤더 중앙 정렬 */
}

.v-data-table-header th {
  padding: 16px; /* 헤더 셀에 여백을 추가 */
}

.v-data-table {
  margin-top: 20px; /* 테이블과 상단 요소 간 여백 설정 */
  border: 1px solid #ddd; /* 테이블 주변에 경계선 추가 */
}

.elevation-1 {
  box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.2);
  margin-top: 5vh; /* 위쪽 여백을 좀 더 줄여 테이블과 제목을 가까이 */
  border-radius: 8px; /* 테이블의 모서리를 둥글게 */
}

.v-btn {
  background-color: #007bff;
  color: white;
  font-size: 0.85rem; /* 버튼 글자 크기를 줄여서 시각적으로 균형 있게 조정 */
  padding: 8px 16px; /* 버튼의 여백 설정 */
}

.v-btn:hover {
  background-color: #0056b3;
}

.v-data-table tbody td {
  text-align: center; /* 테이블 셀 내용 중앙 정렬 */
}

</style>
