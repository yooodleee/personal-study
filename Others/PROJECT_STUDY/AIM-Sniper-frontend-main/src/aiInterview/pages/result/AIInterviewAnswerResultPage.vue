<template>
    <main>
        <v-container  v-if="isDone" width="60%">
            <h2>면접 결과</h2>
            <v-row v-for="(item, index) in inputList" :key="index" class="my-4">
                <v-col cols="12" class="card">
                    <p><strong>{{ index + 1 }}. {{ item[0] }}</strong></p>
                    <v-col cols="12">
                        <li><strong>당신의 답변📄</strong></li>
                        <p class="gray-text"> {{ item[1] }}</p><br>
                        <li><strong>AI 평가 결과 🪄</strong>
                            <v-col cols="12" class="card2">
                                    <p><strong>점수 : </strong>{{item[3]}}</p><br>
                                    <v-text><strong>피드백</strong>
                                        <p> 해당 질문의 의도는 당신의 <strong>{{ item[2] }}</strong>을 파악하기 위함입니다.</p>
                                        <p>{{item[4]}}</p>
                                    </v-text>
                            </v-col>
                        </li>
                    </v-col>
                </v-col>
            </v-row>
        </v-container>
    </main>
</template>
<script>
import { mapActions } from 'vuex'
import markdownIt from 'markdown-it'
import '@mdi/font/css/materialdesignicons.css'
const aiInterviewModule = 'aiInterviewModule'

export default ({
    props: {
      accountId: {
          type: String,
          required: true,
      }
    },
    data() {
        return {
            isDone: false,
            inputList: [],
            scoreResult: [],
            md: new markdownIt()
        }
    },
    async created() {

        this.getScoreResultList(this.accountId)
    },
    methods: {
        ...mapActions(aiInterviewModule, ['requestGetScoreResultListToDjango']),

        async getScoreResultList(accountId) {
            this.inputList = await this.requestGetScoreResultListToDjango({accountId : accountId}) //
            
            this.inputList.forEach(item => {
            const feedback = item[3];
            if (feedback) {
                const returnResult = this.splitScoreFeedback(feedback)
                item.pop()
                item.push(returnResult[0])
                item.push(returnResult[1])
                this.isDone= true
            }
            })
        },
        splitScoreFeedback(feedback) {
            const feedbackParts = feedback.split('<s>');
    
            if (feedbackParts.length !== 1) {
                return [feedbackParts[0].replace('score:', ''), feedbackParts[1].replace('feedback:', '')]
            }
            else {
                return ['문제 발생', feedbackParts[0].replace('<s', '').replace('s>', '')]
            }
        }
  
    },
})
</script>
<style>
.card {
    background-color: #f0f5ff;
    border-radius: 10px;
    padding: 20px;
    line-height: 1.8;
}

.card2 {
    background-color: #dee9ff;
    border-radius: 10px;
    padding: 20px;
    padding-left: 20px;
    line-height: 1.8;
}
.gray-text {
    font-size: 14px;
    margin-left: 2%;
    margin-right: 2%
}
</style>