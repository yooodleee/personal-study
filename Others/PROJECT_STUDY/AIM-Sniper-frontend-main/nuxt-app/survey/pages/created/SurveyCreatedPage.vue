<template>
    <v-container align="center">
        <br><br>
        <v-card-text>
            <span class="text">설문 제작이 완료되었습니다.</span>
        </v-card-text>
        <br>
        <v-btn @click="goToSurveyRegisterPage">다른 설문 제작하기</v-btn>
        <br><br>
        <v-btn @click="goToSurveyListPage">제작한 설문 보기</v-btn>
    </v-container>
</template>



<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const goToSurveyRegisterPage = () => {
    router.push("/survey/register");
};

const goToSurveyListPage = () => {
    router.push("/survey/list");
};
</script>




<style>
.text {

    font-size: 30px;
    font-weight: bold;
}
</style>
