<template>
  <div class="main">
    <h1>User Log List</h1>
    <v-data-table
      :headers="headers"
      :items="managementStore.userLogList.data"
      item-key="userId"
      class="elevation-1"
    >
      <template v-slot:header="{ props }">
        <thead>
          <tr>
            <th v-for="header in props.headers" :key="header.value" class="header-cell">
              {{ header.text }}
            </th>
          </tr>
        </thead>
      </template>
      <template v-slot:item="{ item }">
        <tr>
          <td>{{ item.userId }}</td>
          <td>{{ item.companyReportName }} ({{ item.companyReportId }})</td>
          <td>{{ item.clickCount }}회</td>
          <td>{{ item.purchase }}</td>
          <td>{{ item.lastClickDate }}</td>
        </tr>
      </template>
    </v-data-table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useManagementStore } from '../stores/mangementStore';

const headers = ref([
  { text: 'User ID', value: 'userId' },
  { text: 'Company Report (ID, Name)', value: 'companyReportId' },
  { text: 'Click Count', value: 'clickCount' },
  { text: 'Purchase', value: 'purchase' },
  { text: 'Last Click Date', value: 'lastClickDate' },
]);

const managementStore = useManagementStore();

// 로그 리스트 가져오기 메서드
async function loadUserLogList() {
  await managementStore.requestUserLogListToDjango();
}

onMounted(() => {
  loadUserLogList();
});
</script>

<style scoped>
.main{
  margin-top: 10vh;
  text-align: center
}

.elevation-1 {
  box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  margin-top: 20px;
}

.header-cell {
  background-color: #f5f5f5; /* 헤더 배경색 */
  color: #333; /* 헤더 글자색 */
  font-weight: bold; /* 글자 두껍게 */
  padding: 12px; /* 패딩 추가 */
  border-bottom: 2px solid #ccc; /* 하단 경계선 추가 */
}

td {
  padding: 12px; /* 셀 패딩 */
}
</style>
