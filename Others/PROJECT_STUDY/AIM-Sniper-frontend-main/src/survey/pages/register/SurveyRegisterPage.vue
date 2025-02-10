<template>
  <v-container :style="{ maxWidth: '50%' }">
    <v-container v-if="start" align="center">
      <v-btn @click="createForm">설문 조사 제작하기</v-btn>
    </v-container>
    <v-form v-if="formCreated" ref="form" v-model="valid">
      <v-card-title>
        <form v-if="showTitleDescription" @submit.prevent>
          <v-text-field 
            class="headline"
            label="설문지 이름을 작성하세요."
            v-model="surveyTitle"
            @keyup.enter="disableEnter"
            :rules="[v => !!v || '설문지 이름은 필수 항목입니다']"
            required
          ></v-text-field>
          <v-text-field 
            class="headline"
            label="설문지에 대한 설명을 작성하세요."
            v-model="surveyDescription"
            @keyup.enter="disableEnter"
            :rules="[v => !!v || '설명은 필수 항목입니다']"
            aria-required=""
          ></v-text-field>
          <v-btn 
          :disabled="surveyTitle === null || surveyTitle === '' || 
            surveyDescription === null || surveyDescription ===''" 
          @click="sendTitleAndDescription">완료</v-btn>
        </form>
      </v-card-title>

      <v-btn v-if="titleAndDescriptionCreated" @click="addQuestion">질문 추가</v-btn>
      <v-select v-if="isAdded"
        v-model="questionType"
        :items="generateOptions"
        label="질문 유형을 선택하세요"/>

      <v-row>
        <v-col cols="12" v-if="questionType">
          <v-card v-if="questionType === 'text'" outlined>
            <v-card-text>
              <v-checkbox
                v-model="isEssential"
                label="이 질문을 필수 항목으로 설정합니다."
              />
              <v-text-field
                v-model="questionTitle"
                label="질문 제목을 입력하세요"
                :rules="[v => !!v || '질문 제목은 필수 항목입니다.']"
                required
              ></v-text-field>
              <v-row>
                <v-col cols="8">
                  <v-file-input
                    v-model="uploadedImage"
                    label="사진 등록"
                    multiple
                    @change="onFileChange(uploadedImage)"
                  />
                  <v-container v-if="uploadedImages.length !== 0">
                    <ul>
                      <li class="li-margin" v-for="(image, index) in uploadedImages" :key="index">{{ image.name }}</li>
                    </ul>
                  </v-container>
                </v-col>
              </v-row>
              <v-btn :disabled="questionTitle === null || questionTitle === ''" 
              @click="createQuestion(questionType)">완료</v-btn>
            </v-card-text>
          </v-card>

          <v-card v-if="questionType === 'radio' || questionType === 'checkbox'" outlined>
            <v-card-text>
              <v-checkbox
                v-model="isEssential"
                label="이 질문을 필수 항목으로 설정합니다."
              />
              <v-text-field 
                v-model="questionTitle"
                label="질문 제목을 입력하세요" 
                :rules="[v => !!v || '질문 제목은 필수 항목입니다.']"
                required
              ></v-text-field>
              <v-row>
                <v-col cols="8">
                  <v-file-input
                    v-model="uploadedImage"
                    label="사진 등록"
                    multiple
                    @change="onFileChange(uploadedImage)"
                  />
                  <v-container v-if="uploadedImages.length !== 0">
                    <ul>
                      <li class="li-margin" v-for="(image, index) in uploadedImages" :key="index">{{ image.name }}</li>
                    </ul>
                  </v-container>
                </v-col>
              </v-row>
              <v-btn v-if="readyToCreateQuestionTitle" 
              :disabled="questionTitle === null || questionTitle === ''" 
              @click="createQuestion(questionType)">질문 생성</v-btn>
              <v-text-field v-if="!readyToCreateQuestionTitle"
                v-model="option" 
                @keyup.enter="createSelection" 
                label="항목 이름을 입력하세요"
                required
              />
              <v-btn v-if="!readyToCreateQuestionTitle" @click="createSelection"> 항목 생성</v-btn>
              <br>
              <ul><br>
                <li class="li-margin" v-for="(option, index) in selection" :key="index">{{ option }}</li>
              </ul><br>
              <v-btn v-if="selection.length!==0" @click="finishCreateSelection">완료</v-btn>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <br><br><br><br><br>
      <hr class="tuning-hr" v-if="surveyQuestions.length !== 0"><br>
      <v-row v-if="surveyQuestions.length !== 0">
        <v-card-title>
          <span>설문 폼 미리보기</span><br><br><br>
          <span class="headline">{{ surveyTitle }}</span>
          <v-card-subtitle class="survey-subtitle">
            <br>
            <span>{{ surveyDescription }}</span>
          </v-card-subtitle>
        </v-card-title>
      </v-row>
      <v-row v-for="(question, index) in surveyQuestions" :key="index" class="mb-4">   
        <v-col cols="12">
          <v-card outlined>
            <v-card-text>
              <h4 v-html="formatQuestionTitle(index, question)"></h4><br>
              <v-row v-if="question.images.length !==0">
                <v-col v-for="(image, index) in question.images" :key="index" cols="4" class="mb-4">
                  <span>추가된 이미지 {{ image.name }}</span>
                  <!-- <v-img :src="getImageUrl(image.name)" aspect-ratio="1.0" contain></v-img> -->
                </v-col>
              </v-row>
              <v-text-field
                v-if="question.questionType === 'text'"
                label="답변을 입력하세요"
              />
              <v-radio-group v-if="question.questionType==='radio'">
                <v-radio v-for="option in question.selection"
                  :key="option"
                  :label="option"
                  :value="option"/>
              </v-radio-group>

              <v-checkbox-group
                v-if="question.questionType==='checkbox'">
                <v-checkbox
                  v-for="option in question.selection"
                  :key="option"
                  :label="option"
                  :value="option"
                ></v-checkbox>
              </v-checkbox-group>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <v-btn 
        v-if="surveyQuestions.length !== 0 && surveyTitle !== null" 
        :disabled="!valid || surveyQuestions.length === 0 || surveyTitle === ''" 
        @click="submitForm" 
        color="primary"
      >제출</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import { mapActions } from 'vuex'
import router from "@/router";

const surveyModule = 'surveyModule'

export default {
  data() {
    return {
      start: true,
      showTitleDescription: true,
      titleAndDescriptionCreated: false,
      readyToCreateQuestionTitle: true,
      formCreated: false,
      surveyId: null,
      questionId: null,
      selectionId: null,
      surveyTitle: null,
      surveyDescription: null,
      surveyQuestions: [],
      option: '',
      questionTitle: '',
      questionType: null,
      selection: [], 
      isAdded: false,
      isEssential: false,
      generateOptions: ['text', 'radio', 'checkbox'],
      isFormDirty: false,
      randomString: '',
      uploadedImages: [],
      uploadedImage: null
    };
  },
  methods: {
    ...mapActions(surveyModule, ['requestCreateSurveyFormToDjango', 'requestRegisterTitleAndDescriptionToDjango',
                                 'requestCreateQuestionToDjango', 'requestRegisterSelectionToDjango']),

    async createForm() {
      const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
      const charactersLength = characters.length;
      for (let i = 0; i < 32; i++) {
        this.randomString += characters.charAt(Math.floor(Math.random() * charactersLength));
      }
    
      this.surveyId = await this.requestCreateSurveyFormToDjango({ randomString: this.randomString })

      if (this.surveyId !== '') {
        this.formCreated = true;
        this.start = false;
      }
    },

    async sendTitleAndDescription() {
      const payload = {surveyId : this.surveyId, surveyTitle: this.surveyTitle, surveyDescription : this.surveyDescription}
      const titleDescriptionSaved = await this.requestRegisterTitleAndDescriptionToDjango(payload)

      if (titleDescriptionSaved) {
        this.titleAndDescriptionCreated = true
        this.showTitleDescription = false;
      }
    },
    async createQuestion(questionType) {
      if (!this.questionTitle) {
          alert('내용을 입력하세요');
          return;
      }

      const imageFormData = new FormData();
      imageFormData.append("surveyId", this.surveyId);
      imageFormData.append("questionTitle", this.questionTitle);
      imageFormData.append("questionType", this.questionType);
      imageFormData.append("isEssential", this.isEssential ? 'true' : 'false');
      
      this.uploadedImages.forEach(image => {
          imageFormData.append("images", image);
      });

      this.questionId = await this.requestCreateQuestionToDjango(imageFormData);
      this.readyToCreateQuestionTitle = false;

      if (this.questionId !== null && questionType === 'text') {
          const preForm = { questionTitle: this.questionTitle, questionType: questionType, isEssential: this.isEssential, images: this.uploadedImages }
          this.surveyQuestions.push(preForm);
        this.resetQuestionFields();
        }
    },
    async createSelection() {
      if (this.option.trim() !== '') {
        this.selection.push(this.option);
        const payload = { questionId: this.questionId, selection: this.option}
        this.selectionId = await this.requestRegisterSelectionToDjango(payload)
        this.option = '';
        this.isFormDirty = true;
      } else {
        alert('항목에 내용을 입력하세요');
      }
    },
    finishCreateSelection() {
      if (this.selection.length === 0) {
        alert('항목을 입력해주세요.');
        return;
      }
      if (this.questionId !== null && this.selectionId !== null) {
        const preForm = {questionTitle: this.questionTitle, questionType: this.questionType, isEssential: this.isEssential, selection: this.selection, images : this.uploadedImages }
        this.surveyQuestions.push(preForm);
        this.resetQuestionFields();
      }
    },
    addQuestion() {
      this.isAdded = true;
      this.questionType = null;
      this.isFormDirty = true; 
    },
    onFileChange(files) {
      const newImages = Array.from(files);
      this.uploadedImages = [...this.uploadedImages, ...newImages]; 
      console.log('값 추가됨? ', this.uploadedImages)
      this.uploadedImage=null
    },
    resetQuestionFields() {
      this.questionTitle = '';
      this.selection = [];
      this.isAdded = false;
      this.questionType = null;
      this.isEssential = false;
      this.uploadedImages= [];
      this.isFormDirty = true;
      this.readyToCreateQuestionTitle = true;
    },
    submitForm() {
        alert('제출 완료');
        router.push("/survey/created");
    },
    formatQuestionTitle(index, question) {
      if (question.questionType === 'checkbox') {
        return `${index +1}. ${question.questionTitle} (중복 선택 가능) <span class="essential"> ${question.isEssential ? '* 필수' : '* 선택'}</span>`;
      }
      else {
        return `${index +1}. ${question.questionTitle} <span class="essential">${question.isEssential ? '* 필수' : '* 선택'}</span>`;
      }
    },
    sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    },
    async getImageUrl(imageName) {
      try {
          await this.sleep(2500);
          return require(`@/assets/images/uploadImages/${imageName}`);
      } catch (e) {
          console.error("Image not found:", imageName);
          return '';
        }
    },
    disableEnter(event) {
      event.preventDefault();
      event.stopPropagation();
    },
    handleBeforeUnload(event) {
      if (this.isFormDirty) {
        const confirmationMessage = '작성 중인 정보가 저장되지 않을 수 있습니다.';
        event.returnValue = confirmationMessage;
        return confirmationMessage;
      }
    }
  },
  mounted() {
    window.addEventListener('beforeunload', this.handleBeforeUnload);
  },
  beforeUnmount() {
    window.removeEventListener('beforeunload', this.handleBeforeUnload);
  }
};
</script>

<style>
.headline {
  font-size: 30px;
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

.li-margin {
  margin-left: 4%;
}
.tuning-hr {
  border: none;
  border-top: 1px solid #d1d1d1;
}
</style>
