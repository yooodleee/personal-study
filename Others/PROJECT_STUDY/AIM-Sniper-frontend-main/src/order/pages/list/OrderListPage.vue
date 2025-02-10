<template lang="">
  <div class="background-image">
    <v-container>
      <!-- 주문 목록 있을 때 -->
      <v-row justify="center" v-if="orderList.length > 0">
        <v-col cols="12" md="10" lg="8">
          <h2 class="title">
            <span>구매한 보고서 목록</span>
            <v-icon class="ml-auto" color="primary"
              >mdi-clipboard-list-outline</v-icon
            >
          </h2><br>
          <v-data-table
            v-model:items-per-page="perPage"
            :headers="headerTitle"
            :items="pagedItems"
            v-model:pagination="pagination"
            class="elevation-1 order-table"
            @click:row="readRow"
            item-value="ordersId"
          />

          <!-- 페이지네이션 -->
          <v-row justify="center">
            <v-col cols="auto">
              <v-pagination
                v-model="pagination.page"
                :length="Math.ceil(orderList.length / perPage)"
                total-visible="7"
                size="small"
                color="primary"
                @input="updateItems"
              />
            </v-col>
          </v-row>
        </v-col>
      </v-row>

      <!-- 주문 목록 없을 때 -->
      <v-row justify="center" v-else class="no-orders">
        <v-col cols="12" md="6">
          <v-card outlined class="pa-4 text-center">
            <v-icon size="64" color="grey lighten-1"
              >mdi-package-variant-closed</v-icon
            >
            <p class="no-orders-text">구매 기록이 없습니다.</p>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";

const orderModule = "orderModule";

export default {
  computed: {
    ...mapState(orderModule, ["orderList"]),
    pagedItems() {
      if (this.perPage === -1) {
        // Return the full list if items-per-page is set to 'all' (-1)
        return this.orderList.map((item) => ({
          ...item,
          totalPrice: this.formatPrice(item.totalPrice), // Format totalPrice
          createdDate: this.formatDate(item.createdDate), // Format createdDate
        }));
      } else {
        const startIdx = (this.pagination.page - 1) * this.perPage;
        const endIdx = startIdx + this.perPage;
        return this.orderList.slice(startIdx, endIdx).map((item) => ({
          ...item,
          totalPrice: this.formatPrice(item.totalPrice), // Format totalPrice
          createdDate: this.formatDate(item.createdDate), // Format createdDate
        }));
      }
    },
  },
  mounted() {
    this.requestMyOrderListToDjango();
  },
  methods: {
    ...mapActions(orderModule, ["requestMyOrderListToDjango"]),
    readRow(event, { item }) {
      this.$router.push({
        name: "OrderReadPage",
        params: { ordersId: item["ordersId"].toString() },
      });
    },
    formatDate(dateString) {
      const options = { year: "numeric", month: "2-digit", day: "2-digit" };
      const date = new Date(dateString);
      return date.toLocaleDateString("ko-KR", options);
    },
    formatPrice(price) {
      return Math.round(price).toLocaleString(); // 반올림하고 천 단위로 콤마 추가
    },
    goToLastPage() {
      this.$router.go(-1);
    },
  },
  data() {
    return {
      headerTitle: [
        {
          title: "No",
          align: "start",
          sortable: true,
          key: "ordersId",
        },
        { title: "수량", align: "start", key: "totalQuantity", width: "20%" },
        { title: "금액", align: "start", key: "totalPrice", width: "40%" },
        {
          title: "구매 일자",
          align: "start",
          key: "createdDate",
          width: "40%",
        },
      ],
      perPage: 5,
      pagination: {
        page: 1,
      },
    };
  },
};
</script>

<style>
.table-header th {
  font-size: 1.3em;
  font-weight: 900;
  color: #3f51b5;
}

.order-table {
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
}

.companyReport-image {
  max-width: 50px;
  max-height: 50px;
  object-fit: contain;
}

.no-orders {
  text-align: center;
  margin-top: 20px;
  font-size: 1.2em;
}

.no-orders-text {
  margin-top: 10px;
  color: #616161;
  font-size: 1.1em;
}
</style>
