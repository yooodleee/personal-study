<template>
  <v-card class="result" max-width="600" v-if="resultForm" style="margin-top: 10%; margin-left: 30%">
    <v-card-title>
      <span class="headline">{{ resultForm.surveyTitle }}</span>
    </v-card-title>
    <v-card-subtitle>
      <span>{{ resultForm.surveyDescription }}</span>
    </v-card-subtitle>
    <v-card-text>
      <v-row v-for="(question, index) in resultForm.surveyQuestions" :key="index" class="mb-4">
        <v-col cols="12">
          <v-card outlined>
            <v-card-text>
              <h4>{{ index + 1 }}. {{ question.questionTitle }}</h4>
              <v-container v-if="question.questionType === 'text'">
                <v-container style="max-height: 200px; overflow-y: auto; border: 1px solid #ccc; padding: 6px;">
                  <v-row v-for="answer in question.answer" :key="answer">
                    <v-col>{{ answer }}</v-col>
                  </v-row>
                </v-container>
              </v-container>
              <v-container v-if="question.questionType === 'radio' || question.questionType === 'checkbox'">
                <div :ref="`chart_${index}`" class="chart-container"></div>
              </v-container>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>



<script setup>
import { ref, onMounted, toRefs } from 'vue';
import { useSurveyStore } from '@/stores/surveyStore';
import * as d3 from 'd3';
import { useRoute } from 'vue-router';

const route = useRoute();
const surveyId = ref(route.params.surveyId);
const surveyStore = useSurveyStore();
const { resultForm } = toRefs(surveyStore);

const drawBarChart = (question, index) => {
  const data = question.selection;
  const keys = Object.keys(data);
  const values = Object.values(data);
  const colorScale = d3.scaleOrdinal(d3.schemeCategory10);

  const element = document.querySelector(`.chart_${index}`);
  d3.select(element).selectAll('*').remove();

  const svg = d3.select(element)
    .append('svg')
    .attr('width', 400)
    .attr('height', 250);

  const xScale = d3.scaleBand()
    .domain(keys)
    .range([0, 400])
    .padding(0.1);

  const yScale = d3.scaleLinear()
    .domain([0, d3.max(values)])
    .range([200, 0]);

  svg.selectAll('.bar')
    .data(values)
    .enter()
    .append('rect')
    .attr('class', 'bar')
    .attr('x', (d, i) => xScale(keys[i]))
    .attr('y', d => yScale(d))
    .attr('width', xScale.bandwidth())
    .attr('height', d => 200 - yScale(d))
    .attr('fill', (d, i) => colorScale(i));

  svg.selectAll('.text')
    .data(values)
    .enter()
    .append('text')
    .attr('class', 'value-text')
    .attr('x', (d, i) => xScale(keys[i]) + xScale.bandwidth() / 2)
    .attr('y', d => (yScale(d) > 20 ? yScale(d) - 5 : yScale(d) + 15))
    .attr('text-anchor', 'middle')
    .style('font-size', '12px')
    .style('fill', 'black')
    .text(d => d);

  svg.append("g")
    .attr("class", "grid")
    .attr("transform", "translate(0," + 200 + ")")
    .call(d3.axisBottom(xScale)
    .ticks(5)
    .tickSize(0)
    .tickPadding(10))
    .selectAll("text")
    .attr("transform", "rotate(45)")
    .style("text-anchor", "start");
};

onMounted(async () => {
  await surveyStore.requestSurveyResultToDjango(surveyId.value);
  
  resultForm.value.surveyQuestions.forEach((question, index) => {
    if (question.questionType === 'radio' || question.questionType === 'checkbox') {
      drawBarChart(question, index);
    }
  });
});
</script>


<style scoped>
.headline {
  font-weight: bold;
}

.chart-container {
  width: 100%;
  height: 100%;
}
</style>
