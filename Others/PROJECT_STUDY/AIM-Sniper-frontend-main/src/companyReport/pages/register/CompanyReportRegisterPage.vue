<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-text-field
          v-model="companyReportName"
          label="기업 분석 보고서 제목"
          data-testid="input-companyReport-name"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-text-field
          v-model="companyReportPrice"
          label="가격"
          data-testid="input-companyReport-price"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-select
          v-model="companyReportCategory"
          :items="categories"
          label="카테고리"
          clearable
          solo
          data-testid="input-companyReport-category"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-textarea
          v-model="content"
          label="기업 보고서"
          auto-grow
          data-testid="input-companyReport-description"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-file-input
          v-model="companyReportTitleImage"
          label="회사 사진"
          prepend-icon="mdi-camera"
          data-testid="input-companyReport-title-image"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <p v-if="uploadedTitleImageFilename">
          업로드된 파일: {{ uploadedTitleImageFilename }}
        </p>
      </v-col>
    </v-row>
    <v-col cols="12" class="text-right">
      <v-btn
        class="ml-2"
        color="primary"
        @click="onSubmit"
        data-testid="btn-submit"
      >
        <v-icon>mdi-check</v-icon>
        <span>등록</span>
      </v-btn>
      <router-link :to="{ name: 'CompanyReportListPage' }">
        <v-btn
          class="ml-1"
          color="error"
          @click="onCancel"
          data-testid="btn-cancel"
        >
          <v-icon>mdi-cancel</v-icon>
          <span>취소</span>
        </v-btn>
      </router-link>
    </v-col>
  </v-container>
</template>

<script>
import { mapActions } from "vuex";

const companyReportModule = "companyReportModule";
const accountModule = "accountModule";
const authenticationModule = "authenticationModule";

export default {
  data() {
    return {
      companyReportName: "",
      companyReportPrice: "",
      companyReportCategory: "",
      content: "",
      companyReportTitleImage: null,
      uploadedTitleImageFilename: "",
      categories: ["IT", "플랫폼", "은행"],
    };
  },
  methods: {
    ...mapActions(companyReportModule, ["requestCreateCompanyReportToDjango"]),
    ...mapActions(accountModule, ["requestNicknameToDjango"]),
    async onSubmit() {
      // console.log('작성 완료 버튼 누름')

      try {
        if (this.companyReportTitleImage) {
          const imageFormData = new FormData();
          imageFormData.append("companyReportName", this.companyReportName);
          imageFormData.append("companyReportPrice", this.companyReportPrice);
          imageFormData.append(
            "companyReportCategory",
            this.companyReportCategory
          );
          imageFormData.append("content", this.content);
          imageFormData.append(
            "companyReportTitleImage",
            this.companyReportTitleImage
          );

          const response = await this.requestCreateCompanyReportToDjango(
            imageFormData
          );
          this.uploadedFilename = response.data.imageName;
          await this.$router.push({ name: "CompanyReportListPage" });
          window.location.reload(true);
        } else {
          alert("이미지 파일을 선택하세요!");
        }
      } catch (error) {
        console.log("파일 처리 과정에서 에러 발생:", error);
      }
    },
    async onCancel() {
      // console.log('취소 버튼 누름')
      alert("상품 등록이 취소되었습니다.");
      this.$router.go(-1);
    },
  },
};
</script>
