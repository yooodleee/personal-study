<template lang="">
    <v-container max-width="800">
        <br>
        <h2>작성된 설문 조사 확인</h2><br><br>
        <v-data-table
            v-model:items-per-page="perPage"
            :headers="headerTitle"
            :items="pagedItems"
            v-model:pagination="pagination"
            class="elevation-1"
        >
            <template v-slot:item="{ item }">
                <tr @click="readRow(item)">
                    <td>
                        {{ item.surveyId }}
                    </td>
                    <td>
                        <span @click.stop="readRow(item)">
                            {{ item.surveyTitle }}
                        </span>
                    </td>
                    <td>
                        <v-btn @click.stop="goToSurveyResultPage(item)">
                            응답 확인
                        </v-btn>
                    </td>
                </tr>
            </template>
        </v-data-table>
        <v-pagination
            v-model="pagination.page"
            :length="Math.ceil(surveyTitleList.length / perPage)"
            color="primary"
            @input="updateItems"
        />
        <v-container align="end">
            <v-btn
                class="ml-2"
                color="primary"
                @click="goToSurveyRegisterPage">설문조사 만들기
            </v-btn>
        </v-container>
    </v-container>
</template>



<script setup>
import { ref, computed, onMounted } from 'vue';
import { useSurveyStore } from '@/stores/surveyStore';
import { useRouter } from 'vue-router';

const router = useRouter();
const surveyStore = useSurveyStore();

const headerTitle = ref([
    {
        title: 'No',
        align: 'start',
        sortable: true,
        key: 'surveyId',
        width: '50px'
    },
    { title: '제목', align: 'start', key: 'surveyTitle' },
    { title: '설문 응답 확인', align: 'start', key: 'actions', sortable: false },
]);

const perPage = ref(5);
const pagination = ref({
    page: 1,
});

const surveyTitleList = computed(() => surveyStore.surveyTitleList);

const pagedItems = computed(() => {
    const startIdx = (pagination.value.page - 1) * perPage.value;
    const endIdx = startIdx + perPage.value;
    return surveyTitleList.value.slice(startIdx, endIdx);
});

const readRow = (item) => {
    router.push({
        name: 'SurveyReadPage',
        params: { randomString: item.randomString.toString() }
    });
};

const goToSurveyResultPage = (item) => {
    router.push({
        name: 'SurveyResultPage',
        params: { surveyId: item.surveyId }
    });
};

const goToSurveyRegisterPage = () => {
    router.push("/survey/register");
};

const updateItems = () => {
    // 페이지 변경 시 실행할 함수
};

onMounted(() => {
    surveyStore.requestSurveyListToDjango();
});
</script>

