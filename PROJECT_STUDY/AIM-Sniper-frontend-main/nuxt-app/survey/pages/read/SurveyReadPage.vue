<template>
    <v-container>
      <br><br><br>
      <v-card class="mx-auto my-12" max-width="800" v-if="surveyForm ">
        <v-card-title>
          <span class="headline">{{ surveyForm.surveyTitle }}</span>
        </v-card-title>
        <v-card-subtitle>
          <span>{{ surveyForm.surveyDescription }}</span>
        </v-card-subtitle>
        <v-card-text>
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-row v-for="(question, index) in surveyForm.surveyQuestions" :key="index" class="mb-4">
              <v-col cols="12">
                <v-card outlined>
                  <v-card-text>
                    <h4 v-html="formatQuestionTitle(index, question)"></h4>
                    <v-row v-if="question.images.length !==0">
                      <v-col v-for="(image, index) in question.images" :key="index" cols="4" class="mb-4">
                        <v-img :src="getImageUrl(image)" aspect-ratio="1.0" contain></v-img>
                      </v-col>
                    </v-row>
                    <v-text-field
                      v-if="question.questionType === 'text'"
                      v-model="question.answer"
                      label="답변을 입력하세요"
                      :rules="question.essential ? [rules.textRequired] : []"
                      @input="updateSubmitForm(question.questionType, question.questionId, question.answer)"
                    />
  
                    <v-radio-group
                      v-if="question.questionType === 'radio'"
                      v-model="question.answer"
                      :rules="question.essential ? [rules.radioRequired] : []"
                      @change="updateSubmitForm(question.questionType, question.questionId, question.answer)"
                    >
                    <v-radio
                        v-for="option in question.selection"
                        :key="option"
                        :label="option"
                        :value="option"
                      />
                    </v-radio-group>
  
                    <v-checkbox-group
                      v-if="question.questionType === 'checkbox'">
                      <v-checkbox
                        v-for="option in question.selection"
                        :key="option"
                        :label="option"
                        :value="option"
                        :input-value="isChecked(index, option)"
                        @change="toggleCheckbox(index, option, question.questionType, question.questionId)"
                      />
                    </v-checkbox-group>
                  </v-card-text>
                </v-card>
              </v-col>
            </v-row>
            <v-col cols="12" class="text-right">
              <v-btn
                class="ml-2"
                color="primary"
                @click="onSubmit"
                :disabled="!valid"
              >
                <v-icon left>mdi-check</v-icon>
                작성 완료
              </v-btn>
            </v-col>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
</template>



<script setup>
import { ref, computed, onMounted } from 'vue';
import { useSurveyStore } from '@/stores/surveyStore';
import { useAccountStore } from '../account/stores/accountStore';
import { useRouter, useRoute } from 'vue-router';

const route = useRoute();
const router = useRouter();

const randomString = ref(route.params.randomString);
//const email = ref(sessionStorage.getItem("email"));
const email = ref(null);
if (process.client) {
  email.value = sessionStorage.getItem("email");
}
const accountId = ref(null);
const isFirstAccept = ref(false);
const submitForm = ref([]);
const payload = ref(null);
const valid = ref(false); // v-form에 사용할 valid 변수
const surveyStore = useSurveyStore();
const accountStore = useAccountStore();

const surveyForm = computed(() => surveyStore.surveyForm);

const rules = {
  textRequired: (value) => !!value || '필수 입력 항목입니다.',
  radioRequired: (value) => !!value || '옵션을 선택해주세요.',
};

const isChecked = (index, option) => {
  return surveyForm.value.surveyQuestions[index].answer.includes(option);
};

const toggleCheckbox = (index, option, questionType, questionId) => {
  const answerArray = surveyForm.value.surveyQuestions[index].answer;
  const optionIndex = answerArray.indexOf(option);
  if (optionIndex === -1) {
    answerArray.push(option);
  } else {
    answerArray.splice(optionIndex, 1);
  }
  updateCheckboxSubmitForm(answerArray, questionType, questionId);
};

const updateCheckboxSubmitForm = (answerArray, questionType, questionId) => {
  submitForm.value = submitForm.value.filter((item) => item.questionId !== questionId);
  submitForm.value.push({ questionId, answer: answerArray, questionType });
};

const updateSubmitForm = (questionType, questionId, answer) => {
  submitForm.value = submitForm.value.filter((item) => item.questionId !== questionId);
  submitForm.value.push({ questionId, answer, questionType });
};

const formatQuestionTitle = (index, question) => {
  if (question.questionType === 'checkbox') {
    return `${index + 1}. ${question.questionTitle} (중복 선택 가능) <span class="essential">${question.essential ? '* 필수' : '* 선택'}</span>`;
  } else {
    return `${index + 1}. ${question.questionTitle} <span class="essential">${question.essential ? '* 필수' : '* 선택'}</span>`;
  }
};

const getImageUrl = (imageName) => {
  return new URL(`../assets/images/uploadImages/${imageName}`, import.meta.url).href;
};

const onSubmit = async () => {
  let isValid = true;
  surveyForm.value.surveyQuestions.forEach((question) => {
    if (question.essential && question.questionType === 'checkbox' && question.answer.length === 0) {
      isValid = false;
      alert('필수 작성 항목을 점검해주세요.');
    }
  });

  if (isValid) {
    payload.value = { submitForm: submitForm.value, accountId: accountId.value };
    const isSubmitted = await surveyStore.requestSubmitSurveyToDjango(payload.value);
    if (isSubmitted) {
      alert('제출이 완료되었습니다.');
      router.push("/survey/submitted");
    } else {
      alert('제출 과정 중 문제가 발생했습니다. 다시 시도해주세요.');
    }
    submitForm.value = [];
  }
};

onMounted(async () => {
  if (email.value) {
    accountId.value = await accountStore.requestAccountIdToDjango(email.value);
    isFirstAccept.value = await surveyStore.requestCheckIsFirstSubmit({ accountId: accountId.value });
    if (isFirstAccept.value) {
      router.push("/survey/submitted");
    }
  }

  await surveyStore.requestSurveyFormToDjango(randomString.value);
});
</script>


  
<style scoped>
.headline {
    font-weight: bold;
  }

.pre-title { 
  margin-top: 5%;
  text-align: start;
}

.survey-subtitle {
  max-width: 600px;
  overflow-wrap: break-word;
  word-break: break-all;
}

.essential {
  font-size: 0.8em;
  color: rgb(255, 123, 0);
}
  </style>
  