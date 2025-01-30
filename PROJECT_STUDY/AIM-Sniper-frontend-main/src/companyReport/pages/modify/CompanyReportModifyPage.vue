<template>
    <v-container>
        <v-card v-if="companyReport">
        <v-card-title>게시물 수정</v-card-title>
        <v-card-text>
            <v-container>
            <v-row>
                <v-col cols="12">
                <v-text-field v-model="companyReportName" label="제목" />
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12">
                <v-text-field
                    v-model="companyReportPrice"
                    label="가격"
                    auto-grow
                />
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12">
                <v-textarea
                    v-model="content"
                    label="내용"
                    auto-grow
                />
                </v-col>
            </v-row>
            <v-row justify="end">
                <v-col cols="auto">
                <v-btn color="primary" @click="onModify">
                    <v-icon>mdi-check</v-icon>
                    <span>수정 완료</span>
                </v-btn>
                </v-col>
                <v-col cols="auto">
                <router-link :to="{ name: 'CompanyReportReadPage', params: { companyReportId: companyReportId } }">
                    <v-btn color="secondary">
                    <v-icon>mdi-arrow-left</v-icon>
                    <span>돌아가기</span>
                    </v-btn>
                </router-link>
                </v-col>
            </v-row>
            </v-container>
        </v-card-text>
        </v-card>
    </v-container>
</template>
  
<script>
import { mapActions, mapState } from 'vuex'

const companyReportModule = 'companyReportModule'

export default {
  props: {
    companyReportId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      companyReportName: '',
      content: '',
      companyReportPrice: 0,
      keyword: '',
    }
  },
  computed: {
    ...mapState(companyReportModule, ['companyReport']),
  },
  methods: {
    ...mapActions(companyReportModule, [
      'requestCompanyReportToDjango',
      'requestModifyCompanyReportToDjango',
    ]),
    async onModify() {
      try {
        const payload = {
          companyReportId: Number(this.companyReportId), // 타입 변환
          companyReportName: this.companyReportName,
          content: this.content,
          companyReportPrice: this.companyReportPrice
        };

        // console.log('수정할 payload:', payload);

        await this.requestModifyCompanyReportToDjango(payload);
        alert('수정이 완료되었습니다.');
        await this.$router.push({
          name: 'CompanyReportReadPage',
          params: { companyReportId: this.companyReportId },
        });
      } catch (error) {
        console.error('수정 중 에러 발생:', error);
        alert('수정에 실패하였습니다. 다시 시도해 주세요.');
      }
    },
    async fetchCompanyReportData(companyReportId) {
      await this.requestCompanyReportToDjango(companyReportId);
      if (this.companyReport && this.companyReport.companyReportCategory) {
        // console.log(this.companyReport.companyReportCategory);
      }
    },
  },
  async created() {
    await this.fetchCompanyReportData(this.companyReportId);
  },
}
</script>
