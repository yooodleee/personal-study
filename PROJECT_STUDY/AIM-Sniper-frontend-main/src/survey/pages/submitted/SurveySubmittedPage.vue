<template>
    <v-container align="center">
        <br><br>
        <v-card-text>
            <span class="text">설문에 응해주셔서 감사합니다.</span>
        </v-card-text>
        <v-card-text class="change-color">
            <span>제출하신 응답이 이미 존재합니다.</span>
        </v-card-text>
        <br>
        <v-btn @click="goToSurveyHome">웹사이트 둘러보기</v-btn>
    </v-container>
</template>
<script>
import router from "@/router";

export default {
    methods: {
        goToSurveyHome() {
            router.push("/");
        },
      
    }
}
</script>

<style>
.text {

    font-size: 30px;
    font-weight: bold;
}

</style>
