<template>
  <div>
    <v-row class="justify-center align-center mt-15 mb-15">
      <v-col
        v-for="(companyReport, index) in topNCompanyReports"
        :key="index"
        cols="12"
        sm="4"
        md="3"
        lg="2"
      >
        <div class="popular-company">
          <div class="border-top"></div>
          <div class="img">
              <img 
              :src="getImageUrl(companyReport.companyReportTitleImage)">
          </div>
          <span>{{ companyReport.companyReportName }}</span>
          <p class="price"> ✨조회 Top {{ index + 1 }}✨ </p>
          <button 
            @click="goToCompanyReportReadPage(companyReport.companyReportId)"> 
            click
          </button>
        </div>
      </v-col>
    </v-row>
  </div>
  <div class="background-image">
    <v-container class="custom-padding">
      <v-row>
        <v-col v-if="isNormalAdmin || isGoogleAdmin || isKakaoAdmin || isNaverAdmin" cols="auto" class="text-right">
          <v-btn
            :to="{ name: 'CompanyReportRegisterPage' }"
            class="register-btn"
            width="100vw"
            color="white"
            outlined
          >
            상품 등록
          </v-btn>
        </v-col>
      </v-row>
          

      <v-row>
        <v-col cols="3">
          <h2 class="section-title"> 전체 보고서 </h2>
        </v-col>
        <v-col cols="3">
          <!-- 여백용 -->
        </v-col>
        
        <v-col cols="2">
          <v-select
            v-model="selectedCategory"
            :items="categories"            
            class="category-select"
            outlined            
          ></v-select>
        </v-col>
        
        <v-col cols="4">
          <v-text-field
            v-model="searchQuery"
            label="검색 내용을 입력하세요"
            prepend-inner-icon="mdi-magnify"
            clearable
            class="search-input"
            outlined
          ></v-text-field>
        </v-col>        
      </v-row>
      <v-row class="justify-center align-center">
        <v-col cols="12">
          <h3 class="mb-4">산업 키워드 선택</h3>
          <v-row class="keyword-container">
            <v-col cols="auto" v-for="keyword in keywords" :key="keyword" class="pa-2">
              <v-btn
                :color="selectedKeywords.includes(keyword) ? 'primary' : ''"
                @click="toggleKeyword(keyword)"
                outlined
                rounded
                class="keyword-btn"
              >
                {{ keyword }}
              </v-btn>
            </v-col>
          </v-row>
        </v-col>
      </v-row>

      
      <br>
      <br>
      <br>
      <v-row
        v-if="allCompanyReportsVisible && paginatedCompanyReports.length > 0"
      >
        <v-col
          v-for="(companyReport, index) in paginatedCompanyReports"
          :key="index"
          cols="12"
          sm="6"
          md="4"
          lg="3"          
        >
          <v-card
            class="companyReport-card"
            @click="goToCompanyReportReadPage(companyReport.companyReportId)"
            hover
            outlined
          >
            <v-img
              :src="getImageUrl(companyReport.companyReportTitleImage)"
              aspect-ratio="1.5"
            >
              <template v-slot:placeholder>
                <v-row class="fill-height ma-0" align="center" justify="center">
                  <v-progress-circular indeterminate color="grey lighten-5" />
                </v-row>
              </template>
            </v-img>
            <v-card-title class="companyReport-title">{{
              companyReport.companyReportName
            }}</v-card-title>
            <v-card-subtitle class="companyReport-price"
              >{{ companyReport.companyReportPrice }}원</v-card-subtitle
            >
          </v-card>
        </v-col>
      </v-row>

      <v-row v-else-if="allCompanyReportsVisible">
        <v-col cols="12" class="text-center">
          <v-alert type="info">등록된 보고서가 없습니다!</v-alert>
        </v-col>
      </v-row>

      <v-row v-if="filteredCompanyReports.length > itemsPerPage">
        <v-col cols="12" class="text-center">
          <v-pagination
            v-model="currentPage"
            :length="Math.ceil(filteredCompanyReports.length / itemsPerPage)"
            @input="changePage"
          />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
const accountModule = "accountModule";
const authenticationModule = "authenticationModule";
const googleAuthenticationModule = "googleAuthenticationModule";
const naverAuthenticationModule = "naverAuthenticationModule";

export default {
  computed: {
    ...mapState("companyReportModule", ["companyReports"]),
    ...mapState(authenticationModule, ["isKakaoAdmin"]),
    ...mapState(googleAuthenticationModule, ['isGoogleAdmin']),
    ...mapState(accountModule, ['isNormalAdmin']),
    ...mapState(naverAuthenticationModule, ['isNaverAdmin']),
    paginatedCompanyReports() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      return this.filteredCompanyReports.slice(
        startIndex,
        startIndex + this.itemsPerPage
      );
    },
    filteredCompanyReports() {
      let companyReports = this.companyReports;

      // 키워드 필터링: '전체'를 선택하면 필터링을 하지 않음
      if (!this.selectedKeywords.includes('전체')) {
        companyReports = companyReports.filter((companyReport) => {
          if (companyReport.keyword) {
            // companyReport.keyword가 쉼표로 구분된 문자열이면 배열로 변환
            const keywordsArray = companyReport.keyword.split(',');

            // 선택된 키워드 중 하나라도 포함된 보고서만 필터링
            return this.selectedKeywords.some((keyword) =>
              keywordsArray.includes(keyword)
            );
          }
          return false; // keyword가 없는 경우 필터링 제외
        });
      }

      // 카테고리 필터링
      if (this.selectedCategory !== '전체') {
        companyReports = companyReports.filter(
          (companyReport) => {
            const categories = Array.isArray(companyReport.categories) 
              ? companyReport.categories 
              : companyReport.categories ? companyReport.categories.split(',') : [];
            return categories.includes(this.selectedCategory);
          }
        );
      }

      // 검색 필터링
      if (this.searchQuery) {
        const query = this.searchQuery.toLowerCase();
        companyReports = companyReports.filter((companyReport) =>
          companyReport.companyReportName.toLowerCase().includes(query)
        );
      }

      return companyReports;
    },
    topNCompanyReports() {
      let companyReports = this.companyReports;
      companyReports = companyReports.filter(
          (companyReport) => {
            return this.topList.some(topId => topId === companyReport.companyReportId);
      });
      
      return companyReports;
    },
  },
  data() {
    return {
      selectedKeywords: ['전체'],
      keywords: [
      '플랫폼', '정보보안', '빅데이터', '소프트웨어', '하드웨어', '클라우드', '컨설팅', '헬스케어', '메타버스', '인프라', '게임', '의료', 'AI', '디스플레이', '마케팅/광고', '영상 분석', '네트워크', '금융지원'
      ],
      categories: ["전체", "IT", "플랫폼", "은행"],
      selectedCategory: "전체",
      searchQuery: "",
      currentPage: 1,
      itemsPerPage: 8,
      allCompanyReportsVisible: true,
      purchase: false,
      topN: 5,
      topList: [],
    };
  },
  methods: {
    ...mapActions("companyReportModule", ["requestCompanyReportListToDjango", "requestTopNCompanyReportListToDjango"]),
    ...mapActions("userLogModule", ["requestCountClickToDjango"]), //유저가 상품을 눌렀을 때 상품 클릭 수가 늘어남
    goToCompanyReportReadPage(companyReportId) {
      const email = sessionStorage.getItem('email');
      
      this.$router.push({
        name: "CompanyReportReadPage",
        params: { companyReportId },
      });

      if (!email) {
        // email이 없으면 함수가 동작하지 않음
        // console.log("로그인 정보가 없습니다. 상품 클릭 수가 기록되지 않습니다.");
        return;
      }
      if(this.isGoogleAdmin || this.isKakaoAdmin || this.isNaverAdmin || this.isNormalAdmin){
        // 관리자는 갯수를 세지 않습니다.
        // console.log("로그인 정보가 없습니다. 상품 클릭 수가 기록되지 않습니다.");
        return;
      }
      this.requestCountClickToDjango({
        email: email,
        companyReport_id: companyReportId,
        purchase: this.purchase,
      });
    },
    changePage(page) {
      this.currentPage = page;
    },
    getImageUrl(imageName) {
      if (!imageName) {
        // companyReportTitleImage가 null이거나 undefined인 경우 기본 이미지를 반환
        return require('@/assets/images/fixed/AIM_BI_Blue.png');
      }
      return require(`@/assets/images/uploadImages/${imageName}`);
    },
    toggleKeyword(keyword) {
      if (keyword === '전체') {
        // '전체'를 선택하면 다른 모든 키워드를 해제하고 '전체'만 선택
        this.selectedKeywords = ['전체'];
      } else {
        // '전체'가 선택된 상태에서 다른 키워드를 선택하면 '전체'를 해제
        const index = this.selectedKeywords.indexOf('전체');
        if (index !== -1) {
          this.selectedKeywords.splice(index, 1); // '전체' 해제
        }

        // 키워드가 이미 선택되어 있으면 해제하고, 선택되어 있지 않으면 추가
        if (this.selectedKeywords.includes(keyword)) {
          this.selectedKeywords = this.selectedKeywords.filter(
            (k) => k !== keyword
          );
        } else {
          this.selectedKeywords.push(keyword);
        }

        // 만약 선택된 키워드가 없으면 '전체'를 다시 추가
        if (this.selectedKeywords.length === 0) {
          this.selectedKeywords.push('전체');
        }
      }
    },
  },
  async mounted() {
    this.requestCompanyReportListToDjango();

    const response = await this.requestTopNCompanyReportListToDjango(this.topN);
    if (response && response.data) {
      this.topList = response.data;
    }
  },
};
</script>

<style scoped>

@font-face {
  font-family:'Pretendard';
  src: url('@/assets/fonts/Pretendard.ttf') format('truetype');
  font-weight: 400;
}

.register-btn {
  font-size: 16px;
  background-color: #f5f5f5;
  color: blue !important;
  border: 1px solid #ccc !important;
  box-shadow: none;
  border: 1px solid (109, 109, 109, 0.5);
  text-transform: none;
}

.section-title {
  color: #0A28B0;
  font-family: "Pretendard", sans-serif !important;
  font-weight: bold;
  font-size: 30px;
  margin-left: 10px;
  margin-top: 10px;   
}

::v-deep .v-field {  
  background-color: #ffffff !important; 
  color: rgb(37, 47, 133) !important;    
  border-radius: 5px !important;    
}


.custom-padding {
  padding-left: 10%;
  padding-right: 10%;
}

.companyReport-card {
  transition: transform 0.2s ease-in-out;
  border-radius: 32px;  
  box-shadow: 0 1px 3px rgb(206, 205, 205); 
}

.companyReport-card:hover {
  transform: scale(1.05);
}

.companyReport-title {
  font-size: 18px;
  font-weight: bold;
  margin-left: 10px;
}

.companyReport-price {  
  color: #9452ff;
  font-weight: 600;
  margin-left: 10px;
  margin-bottom: 10px;
}

.companyReport-image {
  border-bottom: 1px solid #f5f5f5;
}

.popular-company {
  width: 190px;
  height: 240px;
  width: 190px;
  height: 240px;
  background: #0A28B0;
  border-radius: 15px;
  box-shadow: 1px 5px 60px 11px #1f199d6b;
}

.popular-company .border-top {
  width: 60%;
  height: 3%;
  background: #8094F4;
  margin: auto;
  border-radius: 0px 0px 15px 15px;
}

.popular-company span {
  font-weight: 600;
  color: white;
  text-align: center;
  display: block;
  padding-top: 10px;
  font-size: 16px;
}

.popular-company .price {
  font-weight: 400;
  color: white;
  display: block;
  text-align: center;
  padding-top: 3px;
  font-size: 12px;
}

.popular-company .img {
  width: 100px;
  height: 70px;
  /* background: #8094F4; */
  border-radius: 15px;
  margin: auto;
  margin-top: 25px;
}

.popular-company button {
  padding: 8px 25px;
  display: block;
  margin: auto;
  border-radius: 8px;
  border: none;
  margin-top: 20px;
  background: #8094F4;
  color: white;
  font-weight: 600;
}

.popular-company button:hover {
  background: #534bf3;
}
.keyword-btn{
  border-radius: 8px;
  color: #1e68d1;
  padding: 4px 12px;
  width: auto;
  height: 4vh;
}
</style>