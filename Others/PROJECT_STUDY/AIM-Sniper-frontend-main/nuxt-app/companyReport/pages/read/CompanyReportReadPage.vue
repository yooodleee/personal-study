<template>
  <v-container class="template">
    <v-container
      v-if="companyReport"
      class="d-flex flex-column justify-center ml-10"
      style="margin: 0 auto"
    >
      <v-row>
        <v-col cols="3" class="d-flex justify-end" style="margin-right: 20px">
          <v-img
            :src="getImageUrl(companyReport.companyReportTitleImage)"
            class="custom-img grey lighten-2"
            aspect-ratio="1"
            style="max-width: 150px; height: 150px"
          >
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular indeterminate color="grey lighten-5" />
              </v-row>
            </template>
          </v-img>
        </v-col>
        <!-- 보고서 상품 정보 -->
        <v-col cols="9" md="6" class="d-flex flex-column justify-center">
          <v-row>
            <v-col cols="12">
              <!-- 산업 키워드 태그 -->
              <v-row>
                <v-btn
                  v-for="(keyword, index) in companyReport.keyword.split(',')"
                  :key="index"
                  outlined
                  rounded
                  class="keyword-btn"
                  style="pointer-events: none; margin-right: 1.5vh"
                >
                  {{ keyword.trim() }}
                </v-btn>
              </v-row>
            </v-col>
          </v-row>
          <!-- 제목 및 일반 정보 -->
          <v-row>
            <v-col cols="9">
              <h2>{{ companyInfo.company_name }} 기업•사업 분석 리포트</h2>
            </v-col>
            <v-col cols="3" class="d-flex align-end justify-end">
              <p class="companyReport-price">
                <span class="original-price"> 200 </span>
                <span> → </span>
                {{ companyReport.companyReportPrice }}
                <span class="currency">원</span>
              </p>
            </v-col>
          </v-row>
          <!-- 구매 및 장바구니 버튼 -->
          <v-row style="margin-bottom: 20px">
            <v-btn
              v-if="!isAdmin"
              @click="onPurchase"
              class="order-action-button"
              style="margin-right: 10px"
            >
              <v-icon v-if="!isAdmin" left>mdi-cart</v-icon>
              구매하기
            </v-btn>

            <v-btn
              v-if="!isAdmin"
              @click="onAddToCartAndAsk"
              class="cart-action-button"
            >
              <v-icon left>mdi-cart-plus</v-icon>
              장바구니 담기
            </v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
    <v-divider class="my-4"></v-divider>

    <v-card v-if="companyReport" class="report-container">
      <v-card-text>
        <v-container>
          <!-- 기업/사업 리포트 -->
          <!-- 미리보기 섹션 -->
          <v-row ref="overviewRow" class="overview" justify="center">
            <v-col
              ref="overviewRef"
              cols="auto"
              class="overview-content mb-2 mt-2"
            >
              <v-row no-gutters>
                <v-col cols="auto" class="mb-2">
                  <span><b>주소</b> {{ companyInfo.address }}</span>
                </v-col>
                <v-col cols="auto" class="mb-2">
                  <span><b>대표이사</b> {{ companyInfo.ceo_name }}</span>
                </v-col>
                <v-col cols="auto" class="mb-2">
                  <span><b>설립연도</b> {{ companyInfo.est_date }}</span>
                </v-col>
                <v-col cols="auto">
                  <span>
                    <b>웹사이트</b>
                    <a
                      :href="'https://' + companyInfo.website"
                      target="_blank"
                      rel="noopener"
                    >
                      {{ companyInfo.website }}
                    </a>
                  </span>
                </v-col>
                <v-divider class="mt-5"></v-divider>
              </v-row>
            </v-col>
          </v-row>

          <!-- 프리뷰 영역 (그라데이션 효과) -->
          <div :class="{ 'preview-section': !isPurchased }">
            <!-- 재무정보 차트 -->
            <v-row class="finance" justify="center">
              <v-col
                ref="financeRef"
                cols="auto"
                class="my-5 d-flex justify-center align-center"
              >
                <div ref="chartRef"></div>
              </v-col>
            </v-row>

            <!-- 그라데이션 오버레이 -->
            <div :class="{ 'gradient-overlay': !isPurchased }"></div>
          </div>

          <!-- 블러 처리된 섹션 -->
          <div :class="{ 'blur-section': !isPurchased }">
            <!-- 재무제표 설명 -->
            <v-row
              class="finance-desc mb-11"
              align="center"
              justify="start"
              :style="{ width: financeWidth + 'px', margin: '0 auto' }"
            >
              <v-col>
                <p class="finance-desc-title">💡 재무제표 보는 팁 TIP</p>
                <!-- 재무제표 설명 내용 -->
                <p class="finance-desc-content">
                  • 직전년도({{ financeYears[1] }}) 대비 변동폭이 10%내
                  <span class="graph-stay">유지</span>, 10%이상
                  <span class="graph-up">증가</span> 10%이하
                  <span class="graph-down">하락</span>
                </p>
                <p class="finance-desc-content">
                  1️⃣ <b>매출액</b> : 기업이 1년 동안 번 총 수입으로,
                  <u>기업의 전체적인 규모</u>를 볼 수 있습니다.
                </p>
                <p class="finance-desc-detail">
                  - 유지(±10%)는 안정적인 시장 지위를, 증가(+10%)는 시장 확대를,
                  하락(-10%)은 시장 점유율 감소를 의미할 수 있습니다.
                </p>
                <p class="finance-desc-content">
                  2️⃣ <b>영업이익</b> : 순수 사업 수익(매출 - 운영비용)으로,
                  <u>기업의 수익성</u>을 판단할 수 있습니다.
                </p>
                <p class="finance-desc-detail">
                  - 유지(±10%)는 일관된 경영 효율을, 증가(+10%)는 비용 관리
                  개선이나 고수익 사업 확대를, 하락(-10%)은 비용 부담 증가나
                  시장 경쟁 심화를 의미할 수 있습니다.
                </p>
                <p class="finance-desc-content">
                  3️⃣<b>자기자본</b> : 기업이 보유한 순수 재산으로,
                  <u>재무 안정성</u>을 평가할 수 있습니다.
                </p>
                <p class="finance-desc-detail">
                  - 유지(±10%)는 안정적인 재무구조를, 증가(+10%)는 수익의 내부
                  축적을, 하락(-10%)은 적자 누적이나 투자 집행을 의미할 수
                  있습니다.
                </p>
              </v-col>
            </v-row>

            <div
              class="width-divider my-2"
              :style="{ width: maxWidth + 'px', margin: '0 auto' }"
            >
              <v-divider></v-divider>
            </div>
            <!-- 요약 -->
            <v-row
              v-if="isPurchased"
              :style="{ width: financeWidth + 'px' }"
              class="summary my-5 d-flex justify-center align-center"
            >
              <v-col cols="auto">
                <span v-html="companyInfo.business_summary"></span>
              </v-col>
            </v-row>
            <!-- 매출액 표 -->
            <v-row
              v-if="isPurchased"
              class="revenue-table my-5 d-flex justify-center align-center"
            >
              <v-col cols="auto">
                <span
                  v-html="companyInfo.revenue_table"
                  class="table-content"
                ></span>
              </v-col>
            </v-row>

            <!-- 로그인 유도 오버레이 -->
            <div v-if="!isPurchased && !isAuthenticated" class="login-overlay">
              <v-card class="login-card">
                <v-card-text class="text-center">
                  <h3>로그인 후 전체 리포트를 확인하실 수 있습니다</h3>
                  <p class="mt-3">✨오픈 베타 서비스 이벤트✨</p>
                  <p>모든 리포트를 무료로 확인하실 수 있습니다!</p>
                  <v-btn color="primary" class="mt-4" @click="navigateToLogin">
                    로그인하러 가기
                  </v-btn>
                </v-card-text>
              </v-card>
            </div>

            <!-- 구매 유도 오버레이 -->
            <div v-if="!isPurchased && isAuthenticated" class="login-overlay">
              <v-card class="login-card">
                <v-card-text class="text-center">
                  <h3>구매 후 전체 리포트를 확인하실 수 있습니다</h3>
                  <p class="mt-3">✨오픈 베타 서비스 이벤트✨</p>
                  <!-- <p class="mt-3"><u>한 Step만 더</u> 따라와주세요!</p> -->
                  <br />
                  <p>
                    위에서 <b style="color: blue">[구매하기]</b> 버튼을 눌러서
                    결제를 진행해주세요
                  </p>
                  <br />
                  <p>
                    결제창이 나오지만 <u><b>실제로 결제는 되지 않습니다</b></u>
                  </p>
                  <!-- <v-btn color="primary" class="mt-4" @click="onPurchase">
                    구매하러 가기
                  </v-btn> -->
                </v-card-text>
              </v-card>
            </div>
          </div>
        </v-container>
      </v-card-text>
    </v-card>

    <!-- 로딩 -->
    <v-row
      v-else-if="companyInfo"
      class="report-loader"
      justify="center"
      align="center"
    >
      <v-col cols="auto">
        <div class="typewriter ml-10">
          <div class="slide"><i></i></div>
          <div class="paper"></div>
          <div class="keyboard"></div>
        </div>
        <p class="text-center mt-5">기업 요약을 만들고 있습니다</p>
      </v-col>
    </v-row>

    <v-spacer></v-spacer>
    <v-row justify="center" class="mt-4">
      <v-col cols="auto">
        <v-btn
          class="return-action-button"
          @click="$router.push('/companyReport/list')"
        >
          <v-icon left>mdi-arrow-left</v-icon>
          <span>목록으로 돌아가기</span>
        </v-btn>
      </v-col>
      <v-col cols="auto">              
        <button  v-if="isAdmin" class="delete_button" @click="deleteCompanyReport">
          <span class="delete_button_text">삭제</span>
          <span class="delete_button_icon"
            ><svg
              class="svg"
              height="512"
              viewBox="0 0 512 512"
              width="512"
              xmlns="http://www.w3.org/2000/svg"
            >
              <title></title>
              <path
                d="M112,112l20,320c.95,18.49,14.4,32,32,32H348c17.67,0,30.87-13.51,32-32l20-320"
                style="fill:none;stroke:#fff;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px"
              ></path>
              <line
                style="stroke:#fff;stroke-linecap:round;stroke-miterlimit:10;stroke-width:32px"
                x1="80"
                x2="432"
                y1="112"
                y2="112"
              ></line>
              <path
                d="M192,112V72h0a23.93,23.93,0,0,1,24-24h80a23.93,23.93,0,0,1,24,24h0v40"
                style="fill:none;stroke:#fff;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px"
              ></path>
              <line
                style="fill:none;stroke:#fff;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px"
                x1="256"
                x2="256"
                y1="176"
                y2="400"
              ></line>
              <line
                style="fill:none;stroke:#fff;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px"
                x1="184"
                x2="192"
                y1="176"
                y2="400"
              ></line>
              <line
                style="fill:none;stroke:#fff;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px"
                x1="328"
                x2="320"
                y1="176"
                y2="400"
              ></line></svg>
            </span>
        </button>
      </v-col>
      <button v-if="isAdmin" class="pushable" @click="goToModifyPage">
        <span class="shadow"></span>
        <span class="edge"></span>
        <span class="front"> Modify </span>
      </button>
    </v-row>
    <v-dialog v-model="isCheckoutDialogVisible" max-width="500">
      <v-card>
        <v-card-title>Message</v-card-title>
        <v-card-text> 정말 구매하시겠습니까? </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="isCheckoutDialogVisible = false"
            >취소</v-btn
          >
          <v-btn color="blue darken-1" text @click="confirmCheckout"
            >확인</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="isGoToCartListDialogVisible" max-width="500">
      <v-card>
        <v-card-title>Message</v-card-title>
        <v-card-text>
          장바구니에 추가 되었습니다. 장바구니로 이동하시겠습니까?
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="isGoToCartListDialogVisible = false"
            >취소</v-btn
          >
          <v-btn color="blue darken-1" text @click="goToCartList">확인</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script setup>
import { ref, onMounted, watch, onBeforeUnmount } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useCompanyReportStore } from "../../stores/companyReportStore";
import * as d3 from "d3";
import { useAccountStore } from "../../../account/stores/accountStore";
import { useAuthenticationStore } from "../../../authentication/stores/authenticationStore";
import { useNaverAuthenticationStore } from "../../../naverAuthentication/stores/naverAuthenticationStore";
import { useGoogleAuthenticationStore } from "../../../googleAuthentication/stores/googleAuthenticationStore";
import { useUserLogStore } from "../../../userLog/store/userLogStore";
import { useCartStore } from "../../../cart/stores/cartStore";
import { useOrderStore } from "../../../order/stores/orderStore";

const route = useRoute();
const router = useRouter();
const companyReportName = route.query.companyReportName || "기업";
const companyReportId = ref(route.params.id);

const companyReportStore = useCompanyReportStore();
const accountStore = useAccountStore();
const authenticationStore = useAuthenticationStore();
const naverAuthenticationStore = useNaverAuthenticationStore();
const googleAuthenticationStore = useGoogleAuthenticationStore();
const userLogStore = useUserLogStore();
const cartStore = useCartStore();
const orderStore = useOrderStore();

const selectedCompanyName = ref(null);
const isCheckoutDialogVisible = ref(false);
const isGoToCartListDialogVisible = ref(false);
const maxWidth = ref(0);

// 보고서 관련 변수
const financeWidth = ref(0);
const purchase = ref(true);
const financeData = ref([]);
const financeYears = ref([]);
const companyInfo = ref([]);

// DOM ref 변수
const chartRef = ref(null);
const overviewRef = ref(null);
const financeRef = ref(null);

// 계정 변수
const email = ref(null);
const isAdmin = ref(false); // true면 관리자
const isAuthenticated = ref(false); // true면 로그인한 사용자
const isPurchased = ref(false);

const companyReport = ref(null);

function checkAdmin() {
  if (
    authenticationStore.isKakaoAdmin ||
    naverAuthenticationStore.isNaverAdmin ||
    googleAuthenticationStore.isGoogleAdmin ||
    accountStore.isNormalAdmin
  ) {
    isAdmin.value = true;
  }
}

function checkAuthenticated() {
  if (
    authenticationStore.isAuthenticatedKakao ||
    naverAuthenticationStore.isAuthenticatedNaver ||
    googleAuthenticationStore.isAuthenticatedGoogle
  ) {
    isAuthenticated.value = true;
  }
}

async function checkPurchased() {
  if (companyReportStore.topList.includes(Number(companyReportId.value))){
    isPurchased.value = true;
  }

  if (isAdmin.value) {
    isPurchased.value = true;
  } else {
    if (isAuthenticated.value) {
      const res = await orderStore.requestOrderItemDuplicationCheckToDjango({
        email: email.value,
        companyReportId: Number(companyReportId.value),
      });

      if (res) {
        isPurchased.value = true;
      }
    }
  }
}

function navigateToLogin() {
  router.push("/account/login");
}

function navigateToPurchase() {
  const amount = companyReport.value.companyReportPrice;
  router.push({ path: "/payments/test/page", query: { amount } }); // 결제 페이지 경로로 이동
}

const onPurchase = async () => {
  try {
    const payload = {
      email: email.value,
      companyReportId: companyReportId.value,
    };
    const checkOrdersItemDuplication =
      await orderStore.requestOrderItemDuplicationCheckToDjango(payload);

    if (checkOrdersItemDuplication) {
      alert("이미 구매하신 보고서입니다.");
    } else {
      // 이미 구매하지 않은 경우에만 다이얼로그 열기
      isCheckoutDialogVisible.value = true;
      try {
        const clickPayload = {
          email: email.value,
          companyReport_id: companyReportId.value,
          purchase: purchase.value,
        };
        await userLogStore.requestCountClickToDjango(clickPayload);

        const orderPayload = {
          email: email.value,
          companyReportId: Number(companyReportId.value),
          companyReportPrice: Number(companyReport.value.companyReportPrice),
        };

        await orderStore.requestCompanyReportReadToAddOrderToDjango(
          orderPayload
        );
        await cartStore.requestDeleteCartItemToDjango({
          companyReportId: [companyReportId.value],
        });
      } catch (error) {
        console.log("상품 구매 중 에러 발생:", error);
      }
    }
  } catch (error) {
    console.log("이미 구매한 상품인지 확인 중 에러 발생:", error);
  }
};

const onAddToCartAndAsk = async () => {
  try {
    const payload = {
      email: email.value,
      companyReportId: companyReportId.value,
    };

    const checkOrdersItemDuplication =
      await orderStore.requestOrderItemDuplicationCheckToDjango(payload);
    const isDuplicatedCartItem =
      await cartStore.requestCartItemDuplicationCheckToDjango(payload);

    if (checkOrdersItemDuplication) {
      alert("이미 구매하신 보고서입니다.");
    } else if (isDuplicatedCartItem) {
      alert("장바구니에 있는 보고서입니다.");
    } else {
      try {
        isGoToCartListDialogVisible.value = true;
        const cartData = {
          companyReportId: companyReportId.value,
          companyReportName: companyReport.value.companyReportName,
          companyReportPrice: companyReport.value.companyReportPrice,
          email: email.value,
        };
        await cartStore.requestAddCartToDjango(cartData);
      } catch (error) {
        console.log("장바구니 추가 과정에서 에러 발생:", error);
      }
    }
  } catch (error) {
    console.log("이미 구매한 상품인지 확인 중 에러 발생:", error);
  }
};

const deleteCompanyReport = async () => {
  await companyReportStore.requestDeleteCompanyReportToDjango(
    companyReportId.value
  );
  alert("보고서가 삭제되었습니다.");
  router.push("/companyReport/list");
};

async function getFinanceData() {
  let data = await companyReportStore.requestCompanyReportFinanceToDjango(
    companyReport.value.companyReportName
  );
  financeData.value = data.data;
  financeYears.value = Object.keys(data.data);
}

async function getCompanyInfo() {
  let data = await companyReportStore.requestCompanyReportInfoToDjango(
    companyReport.value.companyReportName
  );
  companyInfo.value = data.data[0];
}

const getImageUrl = (imageName) => {
  if (!imageName) {
    return new URL(`/assets/images/fixed/AIM_BI_Simple.png`, import.meta.url).href;
  }
  
  const imageUrl = new URL(`/assets/images/uploadImages/${imageName}`, import.meta.url).href;

  const img = new Image();
  img.src = imageUrl;
  // 이미지가 존재하지 않는 경우 기본 이미지로 설정
  if(img.src=="http://localhost:3000/_nuxt/companyReport/pages/list/undefined") {
    img.src = new URL(`/assets/images/fixed/AIM_BI_Simple.png`, import.meta.url).href;
    };

  return img.src;
};

function confirmCheckout() {
  //alert("구매가 완료되었습니다.");
  isCheckoutDialogVisible.value = false;

  // 해당 보고서의 금액을 amount 변수로 저장
  const amount = companyReport.value.companyReportPrice;
  router.push({ path: "/payments/test/page", query: { amount } }); // 결제 페이지 경로로 이동
}

function goToCartList() {
  router.push(`/cart/list`);
}

function goToModifyPage() {
  router.push(`/companyReport/modify/${companyReportId.value}`);
}

function createChart() {
  if (chartRef.value) {
    const margin = { top: 55, right: 25, bottom: 20, left: 40 };
    const width = 250 - margin.right * 2;
    const height = 260 - margin.top - margin.bottom;
    const years = financeYears.value;

    // 숫자를 한국식으로 변환하는 함수
    function formatKoreanNumber(number) {
      const isNegative = number < 0; // 음수 여부 확인
      number = Math.abs(number); // 절대값으로 변환하여 처리

      let result = "";

      if (number >= 1e12) {
        const trillion = Math.floor(number / 1e12);
        const billion = Math.round((number % 1e12) / 1e8);
        result = `${trillion}조 ${billion > 0 ? billion + "억" : ""}`;
      } else if (number >= 1e8) {
        result = `${Math.round(number / 1e8)}억`;
      } else if (number >= 1e6) {
        result = `${Math.round(number / 1e6)}백만`;
      } else if (number >= 1e3) {
        result = `${Math.round(number / 1e3)}천`;
      } else {
        result = number.toLocaleString();
      }

      return isNegative ? `-${result}` : result; // 음수인 경우 '-' 추가
    }

    // 각 지표에 대한 막대 생성
    const metrics = [
      { key: "revenue", label: "수익성 (매출액)" },
      { key: "profit_trend", label: "수익성 (영업이익)" },
      { key: "owners_capital", label: "안정성 (자기자본)" },
    ];

    metrics.forEach((metric) => {
      const svg = d3
        .select(chartRef.value)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

      // x축
      const x0 = d3.scaleBand().domain(years).range([0, width]).padding(0.2);

      // x축 추가
      svg
        .append("g")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(x0))
        .style("color", "#808080");

      // y축
      const yMax = d3.max(
        years.map((year) => financeData.value[year][0][metric.key])
      );
      const yMin = d3.min(
        years.map((year) => financeData.value[year][0][metric.key])
      );
      const yMaxAbs = Math.max(Math.abs(yMin), Math.abs(yMax));
      const y = d3
        .scaleLinear()
        .domain([yMin < 0 ? -yMaxAbs : 0, yMax])
        .range([height, 0]);

      svg
        .append("g")
        .call(
          d3
            .axisLeft(y)
            .ticks(3)
            .tickFormat((d) => d.toString().slice(0, 2))
        )
        .style("color", "#808080");

      // 기준선(0) 그리기
      if (yMin < 0) {
        svg
          .append("line")
          .attr("x1", 0)
          .attr("x2", width)
          .attr("y1", y(0))
          .attr("y2", y(0))
          .attr("stroke", "#808080")
          .attr("stroke-width", 1);
      }

      // 막대 색상 설정
      const getBarColor = (value, preValue) => {
        if (preValue !== undefined) {
          const change = (() => {
            if (preValue > 0) {
              return ((value - preValue) / preValue) * 100;
            } else if (preValue < 0) {
              if (value > 0) {
                return ((value - preValue) / Math.abs(preValue)) * 100;
              } else {
                return (
                  ((Math.abs(preValue) - Math.abs(value)) /
                    Math.abs(preValue)) *
                  100
                );
              }
            } else {
              // preValue가 0일 때 처리
              return value > 0 ? 100 : value < 0 ? -100 : 0;
            }
          })();
          if (change >= 10) return "#77DD77"; // 초록색 (증가)
          if (change <= -10) return "#FF6961"; // 빨간색 (감소)
          return "#AEC6CF"; // 파란색 (변화 거의 없음)
        }
        return "#D3D3D3"; // 회색 (기본값)
      };

      // 막대 추가
      svg
        .selectAll(`.${metric.key}`)
        .data(
          years.map((year, index) => {
            const value =
              financeData.value[year].length > 0
                ? financeData.value[year][0][metric.key]
                : 0;
            const preValue =
              index > 0
                ? financeData.value[years[index - 1]].length > 0
                  ? financeData.value[years[index - 1]][0][metric.key]
                  : 0
                : undefined;
            return {
              year,
              value,
              color:
                index === years.length - 1
                  ? getBarColor(value, preValue)
                  : "#D3D3D3", // 회색 (이전), 조건부 색상 (최신)
            };
          })
        )
        .enter()
        .append("rect")
        .attr("class", metric.key)
        .attr("x", (d) => x0(d.year))
        .attr("y", (d) => (d.value >= 0 ? y(d.value) : y(0)))
        .attr("width", x0.bandwidth())
        .attr("height", (d) => Math.abs(y(d.value) - y(0))) // 양수는 y(0) - y(d.value), 음수는 y(d.value) - y(0)
        .attr("fill", (d) => d.color);

      // 막대 상단에 값 표시
      svg
        .selectAll(`.${metric.key}-label`)
        .data(
          years.map((year) => ({
            year: year,
            value:
              financeData.value[year].length > 0
                ? financeData.value[year][0][metric.key]
                : 0,
          }))
        )
        .enter()
        .append("text")
        .attr("class", `${metric.key}-label`)
        .attr("x", (d) => x0(d.year) + x0.bandwidth() / 2)
        .attr("y", (d) => y(d.value) - 7)
        .attr("text-anchor", "middle")
        .attr("fill", "#6b6b6b")
        .attr("font-size", 10)
        .text((d) => formatKoreanNumber(d.value));

      // 제목 추가
      svg
        .append("text")
        .attr("class", "chart-title")
        .attr("x", width / 2) // 가운데 정렬
        .attr("y", -40) // Y축 위쪽으로 위치 조정
        .attr("text-anchor", "middle")
        .attr("font-weight", "bold")
        .text(metric.label);
    });
  } else {
    console.error("chartRef is not available");
  }
}

const calculateMaxWidth = () => {
  const overviewWidth = overviewRef.value.$el.getBoundingClientRect().width;
  const financeWidthLocal = financeRef.value.$el.getBoundingClientRect().width;

  financeWidth.value = financeWidthLocal;
  maxWidth.value = Math.max(overviewWidth, financeWidthLocal);
};

onMounted(async () => {
  watch(
    () => companyReportStore.companyReportList,
    async (newList) => {
      if (newList.length > 0) {
        // companyReportList가 채워지고 데이터 가져오기
        companyReport.value = newList[companyReportId.value - 1];

        await getFinanceData();
        await getCompanyInfo();
        createChart();
        calculateMaxWidth();
      }
    },
    { immediate: true } // 데이터가 이미 있을 경우 바로 실행
  );

  window.addEventListener("resize", calculateMaxWidth);

  email.value = sessionStorage.getItem("email");
  checkAdmin();
  checkAuthenticated();
  checkPurchased();
});

onBeforeUnmount(() => {
  window.removeEventListener("resize", calculateMaxWidth);
});

useHead({
  title: `${companyReportName}의 핵심정보 분석 및 요약 | `,
  meta: [
    {
      name: "description",
      content: `${companyReportName}에 대한 기업의 사업 내용, 공략 포인트, 재무제표, 핵심만 요약했습니다. 전자공시시스템(DART) 기반 기업 핵심 정보 분석 🎯AIM에서 확인해보세요.`,
    },
    {
      hid: "keywords",
      name: "keywords",
      content: `${companyReportName}, 기업 분석, ${companyReportName} 기업 분석, ${companyReportName} 사업 내용, ${companyReportName} 기업 요약, ${companyReportName} 주사업, ${companyReportName} 회사 소개, ${companyReportName} 기업 소개, ${companyReportName} 자소서, ${companyReportName} 면접, ${companyReportName} 사업 내용, 취업 준비, AIM, AIM Sniper, AIM 기업 분석, AIM 기업 요약`,
    },
  ],
});
</script>

<style scoped>
.template {
  margin-top: 13vh;
  margin-bottom: 5vh;
}

svg {
  font-family: sans-serif;
}

u {
  text-underline-offset: 0.15rem;
  text-decoration-color: #c8c8c8;
  text-decoration-style: wavy;
}

.custom-img {
  max-width: 200px;
  height: 200px;
  border: 1px solid #ccc !important;
  border-radius: 32px;
  box-shadow: 0 1px 3px rgb(206, 205, 205);
  margin-bottom: 30px;
}

.keyword-btn {
  border-radius: 10px;
  color: #1e68d1;
  width: auto;
  height: 4.5vh;
  margin-top: 10px;
  padding: 2px 12px;
  box-shadow: 0 1px 3px rgb(206, 205, 205);
}

.companyReport-name {
  font-size: 40px;
  font-weight: bold;
  margin: 0;
}

.companyReport-writer {
  font-size: 16px;
  color: grey;
  margin-top: 0;
}

.companyReport-price {
  font-size: 20px;
  color: grey;
}

.original-price {
  font-size: 18px;
  color: grey;
  text-decoration: line-through;
  margin-left: 10px;
}

.order-action-button {
  width: 130px;
  height: 45px;
  border-radius: 13px;
  background: #0a28b0;
  color: #ffffff;
}

.cart-action-button {
  width: 130px;
  height: 45px;
  border-radius: 13px;
  border: 1px solid #e6e8ec !important;
  background: white;
  color: #7b8094;
}

.return-action-button {
  width: 158px;
  height: 40px;
  border-radius: 8px;
  color: black;
  margin-bottom: 40px;
  padding: 0;
  min-width: auto;
}

.no-underline {
  text-decoration: none;
}

.currency {
  font-size: 14px;
  vertical-align: baseline;
  margin-left: 3px;
}

.category-text {
  color: rgb(183, 100, 93);
  font-size: 18px;
  /* 원하는 크기로 조정 */
}

/* From Uiverse.io by Tsiangana */
.Btn {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  width: 45px;
  height: 45px;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition-duration: 0.3s;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.199);
  background: rgb(255, 135, 65);
  background: linear-gradient(
    250deg,
    rgba(255, 135, 65, 1) 15%,
    rgba(255, 65, 65, 1) 65%
  );
}

/* plus sign */
.sign {
  width: 100%;
  transition-duration: 0.3s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.sign svg {
  width: 17px;
}

.sign svg path {
  fill: white;
}

/* text */
.text {
  position: absolute;
  right: 0%;
  width: 0%;
  opacity: 0;
  color: white;
  font-size: 1.2em;
  font-weight: 600;
  transition-duration: 0.3s;
}

/* hover effect on button width */
.Btn:hover {
  width: 125px;
  border-radius: 40px;
  transition-duration: 0.3s;
}

.Btn:hover .sign {
  width: 30%;
  transition-duration: 0.3s;
  padding-left: 20px;
}

/* hover effect button's text */
.Btn:hover .text {
  opacity: 1;
  width: 70%;
  transition-duration: 0.3s;
  padding-right: 10px;
}

/* button click effect*/
.Btn:active {
  transform: translate(2px, 2px);
}

.pushable {
  position: relative;
  background: transparent;
  padding: 0; /* 버튼 자체의 패딩 제거 */
  border: none;
  cursor: pointer;
  outline-offset: 2px;
  outline-color: deeppink;
  transition: filter 250ms;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
  display: inline-flex;
  align-items: center; /* 세로 정렬을 가운데로 */
  justify-content: center;
  margin-top: 10px;
  width: 120px; /* 버튼 너비를 조정 */
  height: 40px; /* 높이를 적당히 줄여 조정 */
  border-radius: 8px; /* 전체적으로 둥근 모서리 */
  overflow: hidden; /* 내부 요소가 삐져나오지 않도록 */
}

.shadow {
  position: absolute;
  top: 3px; /* 그림자 위치 조정 */
  left: 3px;
  height: calc(100% - 6px); /* 그림자 높이를 줄여 세로 크기 조정 */
  width: calc(100% - 6px);
  background: hsl(226, 25%, 69%);
  border-radius: 8px;
  filter: blur(1.5px);
  will-change: transform;
  transform: translateY(1px);
  transition: transform 600ms cubic-bezier(0.3, 0.7, 0.4, 1);
}

.edge {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  border-radius: 8px;
  background: linear-gradient(
    to right,
    hsl(248, 39%, 39%) 0%,
    hsl(248, 39%, 49%) 8%,
    hsl(248, 39%, 39%) 92%,
    hsl(248, 39%, 29%) 100%
  );
}

.front {
  display: block;
  position: relative;
  border-radius: 8px;
  background: hsl(248, 53%, 58%);
  padding: 6px 12px; /* 세로 패딩을 줄여 버튼 높이 조정 */
  color: white;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: 0.875rem; /* 버튼 글자 크기 줄이기 */
  line-height: 1.2; /* 줄 높이를 줄여 텍스트 공간 줄이기 */
  transform: translateY(-2px);
  transition: transform 600ms cubic-bezier(0.3, 0.7, 0.4, 1);
}

.pushable:hover {
  filter: brightness(110%);
}

.pushable:hover .front {
  transform: translateY(-4px);
  transition: transform 250ms cubic-bezier(0.3, 0.7, 0.4, 1.5);
}

.pushable:active .front {
  transform: translateY(-1px);
  transition: transform 34ms;
}

.pushable:hover .shadow {
  transform: translateY(3px);
  transition: transform 250ms cubic-bezier(0.3, 0.7, 0.4, 1.5);
}

.pushable:active .shadow {
  transform: translateY(0.5px);
  transition: transform 34ms;
}

.pushable:focus:not(:focus-visible) {
  outline: none;
}

a {
  color: rgb(107, 107, 107);
  text-decoration: none;
}

a:hover {
  color: rgb(27, 59, 173);
}

a:visited {
  color: rgb(107, 107, 107);
}

a:active {
  color: rgb(27, 59, 173);
}
/* 프리뷰 섹션 스타일 */
.preview-section {
  position: relative;
  overflow: hidden;
  padding-bottom: 50px;
}

/* 그라데이션 오버레이 */
.gradient-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 20rem; /* 그라데이션 높이 조절 */
  background: linear-gradient(
    to bottom,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 0.8) 50%,
    rgba(255, 255, 255, 1) 100%
  );
  pointer-events: none;
}

/* 블러 섹션 스타일 */
.blur-section {
  position: relative;
  margin-top: -30px; /* 그라데이션과 겹치게 */
}

.blur-section::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  backdrop-filter: blur(5px);
  background: rgba(255, 255, 255, 0.1);
  z-index: 1;
}

/* 로그인 오버레이 */
.login-overlay {
  position: absolute;
  top: 8%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
  width: 100%;
  text-align: center;
}

.login-card {
  width: 90%;
  max-width: 400px;
  margin: 0 auto;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* 애니메이션 효과 */
.login-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.login-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}

/* 콘텐츠 스타일 */
.finance-desc-title {
  font-weight: bold;
  font-size: 1.1em;
  margin-bottom: 1rem;
}

.report-container {
  width: 90%;
  margin: 0 auto;
  margin-top: 5vh;
}

.overview-content span {
  padding: 2rem;
  color: rgb(107, 107, 107);
}

.overview-content span b {
  font-size: 1rem;
}

.finance-desc {
  background-color: #f2f1f1;
  padding: 1rem;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.finance-desc-title {
  font-size: 1rem;
  font-weight: bold;
}

.finance-desc-content {
  padding-left: 1.5rem;
  padding-top: 0.5rem;
  margin: 0;
  color: #333;
  line-height: 1.6;
  font-size: 1rem;
}

.finance-desc-detail {
  padding-left: 2.5rem;
  padding-top: 0.2rem;
  margin: 0;
  color: #5c5c5c;
  line-height: 1.6;
  font-size: 0.8rem;
}

.graph-stay {
  background-color: #aec6cf;
  color: #ffffff;
  padding: 0.15rem;
  border-radius: 6px;
  font-weight: bold;
  font-size: 0.9rem;
}

.graph-up {
  background-color: #77dd77;
  color: #ffffff;
  padding: 0.15rem;
  border-radius: 6px;
  font-weight: bold;
  font-size: 0.9rem;
}

.graph-down {
  background-color: #ff6961;
  color: #ffffff;
  padding: 0.15rem;
  border-radius: 6px;
  font-size: 0.9rem;
  font-weight: bold;
}

/* if (change >= 5) return "#77DD77"; // 초록색 (증가)
          if (change <= -5) return "#FF6961"; // 빨간색 (감소)
          return "#AEC6CF" */

/* 사업별 매출액 테이블 */
.table-content :deep(table) {
  width: 90%;
  border-collapse: collapse;
  margin: 0 auto;
}

.table-content :deep(th),
.table-content :deep(td) {
  border: 1px solid #ddd;
  padding: 8px;
}

.table-content :deep(th) {
  background-color: #f2f2f2;
  font-weight: bold;
}

.summary {
  margin: auto;
}

::v-deep .summary p {
  margin-bottom: 30px;
  line-height: 1.8;
}

::v-deep .summary span > ul > li {
  list-style-type: none;
  margin-bottom: 30px;
}

::v-deep .summary li ul {
  padding-left: 20px;
  margin: 10px 0 10px 10px;
}

/* 로딩 */
.report-loader {
  margin-top: 130px;
  color: #646464;
}

.typewriter {
  --blue: #5c86ff;
  --blue-dark: #275efe;
  --key: #fff;
  --paper: #eef0fd;
  --text: #d3d4ec;
  --tool: #fbc56c;
  --duration: 3s;
  position: relative;
  -webkit-animation: bounce05 var(--duration) linear infinite;
  animation: bounce05 var(--duration) linear infinite;
}

.typewriter .slide {
  width: 92px;
  height: 20px;
  border-radius: 3px;
  margin-left: 14px;
  transform: translateX(14px);
  background: linear-gradient(var(--blue), var(--blue-dark));
  -webkit-animation: slide05 var(--duration) ease infinite;
  animation: slide05 var(--duration) ease infinite;
}

.typewriter .slide:before,
.typewriter .slide:after,
.typewriter .slide i:before {
  content: "";
  position: absolute;
  background: var(--tool);
}

.typewriter .slide:before {
  width: 2px;
  height: 8px;
  top: 6px;
  left: 100%;
}

.typewriter .slide:after {
  left: 94px;
  top: 3px;
  height: 14px;
  width: 6px;
  border-radius: 3px;
}

.typewriter .slide i {
  display: block;
  position: absolute;
  right: 100%;
  width: 6px;
  height: 4px;
  top: 4px;
  background: var(--tool);
}

.typewriter .slide i:before {
  right: 100%;
  top: -2px;
  width: 4px;
  border-radius: 2px;
  height: 14px;
}

.typewriter .paper {
  position: absolute;
  left: 24px;
  top: -26px;
  width: 40px;
  height: 46px;
  border-radius: 5px;
  background: var(--paper);
  transform: translateY(46px);
  -webkit-animation: paper05 var(--duration) linear infinite;
  animation: paper05 var(--duration) linear infinite;
}

.typewriter .paper:before {
  content: "";
  position: absolute;
  left: 6px;
  right: 6px;
  top: 7px;
  border-radius: 2px;
  height: 4px;
  transform: scaleY(0.8);
  background: var(--text);
  box-shadow: 0 12px 0 var(--text), 0 24px 0 var(--text), 0 36px 0 var(--text);
}

.typewriter .keyboard {
  width: 120px;
  height: 56px;
  margin-top: -10px;
  z-index: 1;
  position: relative;
}

.typewriter .keyboard:before,
.typewriter .keyboard:after {
  content: "";
  position: absolute;
}

.typewriter .keyboard:before {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border-radius: 7px;
  background: linear-gradient(135deg, var(--blue), var(--blue-dark));
  transform: perspective(10px) rotateX(2deg);
  transform-origin: 50% 100%;
}

.typewriter .keyboard:after {
  left: 2px;
  top: 25px;
  width: 11px;
  height: 4px;
  border-radius: 2px;
  box-shadow: 15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key),
    60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key),
    22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key),
    60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key);
  -webkit-animation: keyboard05 var(--duration) linear infinite;
  animation: keyboard05 var(--duration) linear infinite;
}

@keyframes bounce05 {
  85%,
  92%,
  100% {
    transform: translateY(0);
  }

  89% {
    transform: translateY(-4px);
  }

  95% {
    transform: translateY(2px);
  }
}

@keyframes slide05 {
  5% {
    transform: translateX(14px);
  }

  15%,
  30% {
    transform: translateX(6px);
  }

  40%,
  55% {
    transform: translateX(0);
  }

  65%,
  70% {
    transform: translateX(-4px);
  }

  80%,
  89% {
    transform: translateX(-12px);
  }

  100% {
    transform: translateX(14px);
  }
}

@keyframes paper05 {
  5% {
    transform: translateY(46px);
  }

  20%,
  30% {
    transform: translateY(34px);
  }

  40%,
  55% {
    transform: translateY(22px);
  }

  65%,
  70% {
    transform: translateY(10px);
  }

  80%,
  85% {
    transform: translateY(0);
  }

  92%,
  100% {
    transform: translateY(46px);
  }
}

@keyframes keyboard05 {
  5%,
  12%,
  21%,
  30%,
  39%,
  48%,
  57%,
  66%,
  75%,
  84% {
    box-shadow: 15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key),
      60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key),
      22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key),
      60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key);
  }

  9% {
    box-shadow: 15px 2px 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key),
      60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key),
      22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key),
      60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key);
  }

  18% {
    box-shadow: 15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key),
      60px 2px 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key),
      22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key),
      60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key);
  }

  27% {
    box-shadow: 15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key),
      60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key),
      22px 12px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key),
      60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key);
  }

  36% {
    box-shadow: 15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key),
      60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key),
      22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 12px 0 var(--key),
      60px 12px 0 var(--key), 68px 12px 0 var(--key), 83px 10px 0 var(--key);
  }

  45% {
    box-shadow: 15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key),
      60px 0 0 var(--key), 75px 0 0 var(--key), 90px 2px 0 var(--key),
      22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key),
      60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key);
  }

  54% {
    box-shadow: 15px 0 0 var(--key), 30px 2px 0 var(--key), 45px 0 0 var(--key),
      60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key),
      22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key),
      60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key);
  }

  63% {
    box-shadow: 15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key),
      60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key),
      22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key),
      60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 12px 0 var(--key);
  }

  72% {
    box-shadow: 15px 0 0 var(--key), 30px 0 0 var(--key), 45px 2px 0 var(--key),
      60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key),
      22px 10px 0 var(--key), 37px 10px 0 var(--key), 52px 10px 0 var(--key),
      60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key);
  }

  81% {
    box-shadow: 15px 0 0 var(--key), 30px 0 0 var(--key), 45px 0 0 var(--key),
      60px 0 0 var(--key), 75px 0 0 var(--key), 90px 0 0 var(--key),
      22px 10px 0 var(--key), 37px 12px 0 var(--key), 52px 10px 0 var(--key),
      60px 10px 0 var(--key), 68px 10px 0 var(--key), 83px 10px 0 var(--key);
  }
}
.delete_button {
  position: relative;
  border-radius: 12px;
  width: 120px;
  height: 36px;
  cursor: pointer;
  display: flex;
  align-items: center;
  border: 1px solid #cc0000;
  background-color: #e50000;
  overflow: hidden;
}

.delete_button,
.delete_button_icon,
.delete_button_text {
  transition: all 0.3s;
}

.delete_button .delete_button_text {
  transform: translateX(25px);
  color: #fff;
  font-weight: 600;
}

.delete_button .delete_button_icon {
  position: absolute;
  transform: translateX(95px);
  height: 100%;
  width: 20px;
  background-color: #cc0000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.delete_button .svg {
  width: 20px;
}

.delete_button:hover {
  background: #cc0000;
}

.delete_button:hover .delete_button_text {
  color: transparent;
}

.delete_button:hover .delete_button_icon {
  width: 120px;
  transform: translateX(0);
}

.delete_button:active .delete_button_icon {
  background-color: #b20000;
}

.delete_button:active {
  border: 1px solid #b20000;
}
</style>
