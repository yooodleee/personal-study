<template>
  <div>
    <h1>User Log List</h1>
    <v-data-table
      :headers="headers"
      :items="userLogList.data"
      item-key="userId"
      class="elevation-1"
    >
      <template v-slot:header="{ props }">
        <thead>
          <tr>
            <th v-for="header in props.headers" :key="header.value" class="header-cell">
              {{ header.text }}
            </th>
          </tr>
        </thead>
      </template>
      <template v-slot:item="{ item }">
        <tr>
          <td>{{ item.userId }}</td>
          <td>{{ item.companyReportName }} ({{ item.companyReportId }})</td>
          <td>{{ item.clickCount }}회</td>
          <td>{{ item.purchase }}</td>
          <td>{{ item.lastClickDate }}</td>
        </tr>
      </template>
    </v-data-table>
    <h2>User Data Chart</h2>
    <div class="chart-container">
      <svg ref="chart" width="600" height="400"></svg>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
import * as d3 from "d3";

export default {
  data() {
    return {
      headers: [
        { text: 'User ID', value: 'userId' },
        { text: 'Company Report (ID, Name)', value: 'companyReportId' },
        { text: 'Click Count', value: 'clickCount' },
        { text: 'Purchase', value: 'purchase' },
        { text: 'Last Click Date', value: 'lastClickDate' },
      ],
    };
  },
  computed: {
    ...mapState('managementModule', ["userLogList", 'userData']),
  },
  methods: {
    ...mapActions('managementModule', ['requestUserLogListToDjango', 'requestUserDataToDjango']),
    
    async loadUserLogList() {
        await this.requestUserLogListToDjango();
    },
    
    async loadUserData() {
        await this.requestUserDataToDjango();
        console.log("User Data Loaded:", this.userData.data); // 데이터 확인

        if (this.userData && Object.keys(this.userData).length > 0) {
            this.drawChart();  // 데이터가 로드된 후 차트를 그리도록 이동
        } else {
            console.error("User data is empty or not valid.");
        }
    },   
    
    drawChart() {
    if (this.userData && Object.keys(this.userData).length) {
        console.log("Drawing chart with data:", this.userData.data); // 데이터 출력
        
        const data = [
            { label: 'User Count', value: this.userData.data.userCount },
            { label: 'Account Count', value: this.userData.data.accountCount },
            { label: 'Purchase Count', value: this.userData.data.purchaseCount },
            { label: 'Revenue Count', value: this.userData.data.revenueCount }
        ];

        // 데이터가 유효한지 확인
        console.log("Chart data:", data);

        const svg = d3.select(this.$refs.chart);
        svg.selectAll("*").remove(); // 기존 요소 제거

        const width = 600;
        const height = 400;
        const margin = { top: 20, right: 20, bottom: 50, left: 50 };

        // 막대 차트 크기 조정
        const chartWidth = width - margin.left - margin.right;
        const chartHeight = height - margin.top - margin.bottom;

        // 각 값에 대해 색상을 다르게 적용
        const colorScale = d3.scaleOrdinal()
            .domain(data.map(d => d.label))
            .range(["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]); // 색상 배열

        const xScale = d3.scaleLinear()
            .domain([0, d3.max(data, d => d.value) || 1])
            .range([0, chartWidth]);

        const yScale = d3.scaleBand()
            .domain(data.map(d => d.label))
            .range([0, chartHeight])
            .padding(0.1);

        // 차트를 그리기 위한 그룹 요소 추가
        const chartGroup = svg.append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);

        // 막대 그리기
        chartGroup.selectAll("rect")
            .data(data)
            .enter().append("rect")
            .attr("y", d => yScale(d.label))
            .attr("x", 0)
            .attr("height", yScale.bandwidth())
            .attr("width", d => xScale(d.value))
            .attr("fill", d => colorScale(d.label)) // 색상 설정
            .on("mouseover", function(event, d) { // 마우스 오버 시 효과
                d3.select(this).attr("fill", "orange");
            })
            .on("mouseout", function(event, d) { // 마우스 아웃 시 원래 색상으로 복원
                d3.select(this).attr("fill", d => colorScale(d.label));
            });

        // 막대 위에 값 표시
        chartGroup.selectAll("text")
            .data(data)
            .enter().append("text")
            .attr("x", d => xScale(d.value) + 5) // 값 위치 약간 오른쪽
            .attr("y", d => yScale(d.label) + yScale.bandwidth() / 2 + 4) // 막대 중앙에 위치
            .text(d => d.value)
            .attr("fill", "black");

        // 범례 추가
        const legendGroup = svg.append("g")
            .attr("transform", `translate(${margin.left},${height - margin.bottom + 20})`);

        // 범례 상자와 텍스트 추가
        data.forEach((d, i) => {
            legendGroup.append("rect")
                .attr("x", i * 150) // 범례 아이템 간 간격
                .attr("y", 0)
                .attr("width", 20)
                .attr("height", 20)
                .attr("fill", colorScale(d.label)); // 각 레이블에 맞는 색상 적용

            legendGroup.append("text")
                .attr("x", i * 150 + 30) // 범례 텍스트 위치
                .attr("y", 15)
                .text(d.label)
                .attr("fill", "black");
        });
    } else {
        console.error("User data is empty or not loaded yet.");
    }
  }
  },
  mounted() {
    this.loadUserLogList();
    this.loadUserData();  // 차트 그리기 로직을 loadUserData 내부로 이동
  }
}
</script>

<style scoped>
.elevation-1 {
  box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  margin-top: 20px;
}

.header-cell {
  background-color: #f5f5f5; /* 헤더 배경색 */
  color: #333; /* 헤더 글자색 */
  font-weight: bold; /* 글자 두껍게 */
  padding: 12px; /* 패딩 추가 */
  border-bottom: 2px solid #ccc; /* 하단 경계선 추가 */
}

td {
  padding: 12px; /* 셀 패딩 */
}

svg {
  background-color: #fff; /* 차트 배경색 */
  border: 1px solid #ccc; /* 차트 경계선 */
}

.chart-container {
  text-align: center; /* 텍스트 및 인라인 요소 가운데 정렬 */
  margin: 20px 0; /* 위아래 여백 추가 */
}
</style>
