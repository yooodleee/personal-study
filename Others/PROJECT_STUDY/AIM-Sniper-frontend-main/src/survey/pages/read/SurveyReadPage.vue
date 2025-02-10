<template>
    <v-container>
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
  
<script>
import { mapActions, mapState } from 'vuex'
import router from "@/router";
const surveyModule = 'surveyModule'
const accountModule = 'accountModule'

export default {
    props: {
      randomString: {
          type: String,
          required: true,
      }
    },
    data() {
      return {
        accountId: null,
        email: null,
        valid: false,
        isFirstAccept : false,
        rules: {
          textRequired: (value) => !!value || '필수 입력 항목입니다.',
          radioRequired: (value) => !!value || '옵션을 선택해주세요.',
        },
        submitForm: [],
        payload: null
      };
    },
    computed: {
        ...mapState(surveyModule, ['surveyForm'])
    },
    async mounted() {
      this.email = sessionStorage.getItem("email");
      if (this.email) {
        this.accountId = await this.requestAccountIdToDjango(this.email)
        this.isFirstAccept = await this.requestCheckIsFirstSubmit({accountId : this.accountId})
        if (this.isFirstAccept) {
          router.push("/survey/submitted")
        }
      }
      else {
        // console.log('비회원 유저')
      }
    },
    created () {
      this.requestSurveyFormToDjango(this.randomString);
    },
    methods: {
        
      ...mapActions(surveyModule, ['requestSurveyFormToDjango', 'requestSubmitSurveyToDjango', 'requestCheckIsFirstSubmit']),
      ...mapActions(accountModule, ['requestAccountIdToDjango']),

      isChecked(index, option) {
        return this.surveyForm.surveyQuestions[index].answer.includes(option);
      },
  
      toggleCheckbox(index, option, questionType, questionId) {
        const answerArray = this.surveyForm.surveyQuestions[index].answer
        const optionIndex = answerArray.indexOf(option);
        if (optionIndex === -1) {
          answerArray.push(option);
        } else {

          answerArray.splice(optionIndex, 1);
        }
  
        this.updateCheckboxSubmitForm(answerArray, questionType, questionId);
      },
      updateCheckboxSubmitForm(answerArray, questionType, questionId) {
        this.submitForm = this.submitForm.filter((item) => item.questionId !== questionId);
        this.submitForm.push({ questionId, answer: answerArray, questionType });
      },
  
      updateSubmitForm(questionType, questionId, answer) {
        this.submitForm = this.submitForm.filter((item) => item.questionId !== questionId);
          this.submitForm.push({ questionId, answer, questionType });
      },
  
      formatQuestionTitle(index, question) {
        if (question.questionType === 'checkbox') {
        return `${index +1}. ${question.questionTitle} (중복 선택 가능) <span class="essential"> ${question.essential ? '* 필수' : '* 선택'}</span>`;
        }
        else {
            return `${index +1}. ${question.questionTitle} <span class="essential">${question.essential ? '* 필수' : '* 선택'}</span>`;
        }
      },
      getImageUrl(imageName) {
        return require(`@/assets/images/uploadImages/${imageName}`);
      },
      async onSubmit() {
        console.log("surveyForm : ", this.surveyForm)
        let isValid = true;
        this.surveyForm.surveyQuestions.forEach((question, index) => {
          if (question.essential && question.questionType === 'checkbox' && question.answer.length === 0) {
            isValid = false;
            alert('필수 작성 항목을 점검해주세요.');
          }
        });
  
        isValid = await this.$refs.form.validate() && isValid;
          
        if (isValid) {
          this.payload = {submitForm: this.submitForm, accountId : this.accountId}
          const isSubmitted = await this.requestSubmitSurveyToDjango(this.payload)
          if (isSubmitted) {
            alert('제출이 완료되었습니다.');
            router.push("/survey/submitted");
          } else {
            alert('제출 과정 중 문제가 발생했습니다. 다시 시도해주세요.')
          }
          this.submitForm = [];
        }
      }
    },
  };
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
  