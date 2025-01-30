<template>
  <div>
    <h1>User List</h1>
    <v-data-table
      :headers="headers"
      :items="userList.data"
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

<script>
import { useStore, mapActions, mapState } from "vuex";

export default {
  data() {
    return {
      headers: [
        { text: "User ID", value: "userId" },
        { text: "Email", value: "email" },
        { text: "Gender", value: "gender" },
        { text: "Birth Year", value: "birthyear" },
        { text: "Login Type", value: "login_type" },
        { text: "Role Type", value: "role_type" },
        { text: "Last Login", value: "last_login" },
        { text: "Actions", value: "actions", sortable: false }
      ]
    };
  },
  computed: {
    ...mapState('managementModule', ["userList"]),
  },
  methods: {
    ...mapActions('managementModule', ['requestUserListToDjango', 'grantAdminRoleInDjango', 'revokeAdminRoleInDjango']),
    
    translateGender(gender) {
      return gender === 'MALE' ? '남성' : gender === 'FEMALE' ? '여성' : '';
    },
    
    translateLoginType(loginType) {
      const types = {
        'KAKAO': '카카오',
        'NAVER': '네이버',
        'GOOGLE': '구글',
        'NORMAL': '일반 로그인',
      };
      return types[loginType] || '알 수 없음';
    },
    
    translateRoleType(roleType) {
      return roleType === 'ADMIN' ? '관리자' : roleType === 'NORMAL' ? '일반 회원' : '';
    },
    
    formatDate(dateString) {
      const options = { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit' };
      return new Date(dateString).toLocaleString('ko-KR', options);
    },
    
    async loadUserList() {
      await this.requestUserListToDjango();
    },

    async toggleAdminRole(user) {
      if (user.role_type === 'ADMIN') {
        await this.revokeAdminRoleInDjango(user.email);
        alert('관리자 권한이 해제되었습니다.');
      } else {
        await this.grantAdminRoleInDjango(user.email);
        alert('관리자 권한이 부여되었습니다.');
      }
      this.loadUserList();
    },
  },
  mounted() {
    this.loadUserList();
  },
};
</script>

<style scoped>
.elevation-1 {
  box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.2);
}
.v-btn {
  background-color: #007bff;
  color: white;
}
.v-btn:hover {
  background-color: #0056b3;
}
</style>
