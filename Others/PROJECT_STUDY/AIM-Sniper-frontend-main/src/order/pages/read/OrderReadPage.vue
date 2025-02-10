<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-card-title>
            <span>구매한 보고서</span><br>
          </v-card-title>
          <v-card-text>
            <v-table>
              <thead>
                <tr class="table-header">
                  <th></th>
                  <th>기업명</th>
                  <th>가격</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in orderItemList" :key="item.orderItemId">
                  <td>
                    <v-img
                      :src="getImageUrl(item.companyReportTitleImage)"
                      aspect-ratio="1"
                      class="companyReport-image"
                    >
                      <template v-slot:placeholder>
                        <v-row
                          class="fill-height ma-0"
                          align="center"
                          justify="center"
                        ></v-row>
                      </template>
                    </v-img>
                  </td>
                  <td>{{ item.companyReportName }}</td>
                  <td>{{ item.companyReportPrice }}</td>
                </tr>
              </tbody>
            </v-table>
            <v-divider></v-divider>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <br>
    <v-row justify="center">
      <v-col cols="auto">
        <v-btn color="primary" @click="goToLastPage">
          <v-icon left>mdi-arrow-left</v-icon>
          <span>돌아가기</span>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions, mapState } from "vuex";

const orderModule = "orderModule";

export default {
  props: {
    ordersId: {
      type: String,
      required: true,
    },
    companyReportId: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      orderItem: [],
    };
  },
  computed: {
    ...mapState(orderModule, ["orderItemList"]),
  },
  methods: {
    ...mapActions(orderModule, ["requestMyOrderItemListToDjango"]),
    getImageUrl(imageName) {
      return require(`@/assets/images/uploadImages/${imageName}`);
    },
    goToLastPage() {
      this.$router.go(-1);
    },
  },
  async mounted() {
    const response = await this.requestMyOrderItemListToDjango(this.ordersId);
    this.orderItem = response;
  },
};
</script>

<style>
.table-header th {
  font-size: 1.3em; /* Increase the font size */
  font-weight: 900; /* Make the font bold */
}

.companyReport-image {
  max-width: 50px; /* 이미지의 최대 너비 */
  max-height: 50px; /* 이미지의 최대 높이 */
  object-fit: contain; /* 이미지의 비율을 유지하면서 컨테이너에 맞춤 */
}
</style>
