<template>
  <main>
    <v-container v-if="!start"  align=center height="100%" class="control-margin">
      <br><br><br>
      <h2>안녕하십니까? AI 모의 면접 서비스입니다.</h2><br>
      <v-container class="draw-line" align=start>
        <v-card-title align=center><strong>※ 사전 공지 ※</strong></v-card-title><br>
        <li class="li">본 면접은 특정 기업 및 직무에 맞추어진 면접이 아닌 <strong>인성 면접</strong>임을 알려드립니다.</li><br>
        <li class="li">총 <strong>5개</strong>의 질문이 제공됩니다.</li><br>
        <li class="li">면접 질문 당 답변 제한 시간은 <strong>1분 30초</strong>입니다. 시간 내에 작성 부탁드립니다.</li><br>
      </v-container><br>
      <v-card-text><strong>면접 서비스를 시작하시려면 아래 버튼을 눌러주세요.</strong></v-card-text>
      <v-btn @click="startInterview" color="primary">START</v-btn>
      
    </v-container>
    <v-container v-if="start" align="center">
      <div v-if="visible" class="interview-container">
        <v-icon>mdi-account-tie</v-icon><br>
        <v-text v-html="startMessage"></v-text>
      </div>
      <div v-if="!visible" class="interview-container">
        <v-icon>mdi-account-tie</v-icon>
        <h2 v-html="formattedAIMessage"></h2><br>
        <div :class="{'timer': true, 'red-text': remainingTime <= 10}">
          남은 시간: {{ Math.floor(remainingTime / 60) }}:{{ (remainingTime % 60).toString().padStart(2, '0') }}
        </div>
      </div>

      <div v-if="isLoading && !finished" class="message ai">
        <br>
        <p><strong>다음 질문을 준비 중입니다.</strong></p>
        <v-icon>mdi:account-tie</v-icon>
        <div class="loading-message">
          <div class="dot"></div>
          <div class="dot"></div>
          <div class="dot"></div>
        </div>
      </div>
      <div v-if="isLoading && finished" class="message ai">
        <br>
        <p><strong>답변을 채점 중입니다. 잠시만 기다려 주세요.</strong></p>
        <v-icon>mdi:account-tie</v-icon>
        <div class="loading-message">
          <div class="dot"></div>
          <div class="dot"></div>
          <div class="dot"></div>
        </div>
      </div>
    </v-container>

    <v-container v-if="start && !visible" class="input-area">
      <textarea
        v-model="userInput" 
        placeholder="메시지를 입력하세요..." 
        @keydown.enter.exact.prevent="handleEnterKey"  
        @keydown.shift.enter="handleShiftEnter"
        @input="adjustTextareaHeight"
        :disabled="finished || isLoading"
        ref="messageInput"
      ></textarea>
        <button class="send-button" @click="sendMessage" :disabled="finished || isLoading">입력</button>
    </v-container>
  </main>
</template>

<script setup>
import { ref, watch, computed, onMounted } from 'vue';
import { useAiInterviewStore } from '@/stores/aiInterviewStore'; // Pinia store import
import { useAccountStore } from '../../../account/stores/accountStore';
import markdownIt from 'markdown-it';
import { useRouter } from 'vue-router';
import '@mdi/font/css/materialdesignicons.css';

// Pinia Stores
const aiInterviewStore = useAiInterviewStore();
const accountStore = useAccountStore();
const router = useRouter();

// Component State
const accountId = ref('');
const start = ref(false);
const finished = ref(false);
const visible = ref(true);
const userInput = ref('');
const aiOutput = ref('');
const startMessage = '<h2>안녕하세요. AI 모의 면접 서비스입니다.</h2><br><strong><span>제한 시간 내에 답변 작성 부탁드립니다.</span><br><span>지금부터 면접을 시작하겠습니다.</span></strong>';
const currentAIMessage = ref('');
const chatHistory = ref([{ type: 'ai', content: '' }]);
const isLoading = ref(false);
const sendCount = ref(0);
const maxMessages = 5;
const aiResponseList = ref([]);
const questionIndex = ref(0);
const intentList = ['대처 능력', '소통 능력', '프로젝트 경험', '자기 개발'];
const intentIndex = ref(0);

const formattedAIMessage = computed(() => {
      return currentAIMessage.value.replace(/([.?])/g, '$1<br>');
    });

// Computed Properties
const isCheckoutDisabled = computed(() => sendCount.value >= maxMessages);

const timeLimit = 90;
const remainingTime = ref(timeLimit);
const timer = ref(null);

// Watchers
watch(start, (newVal) => {
  if (newVal === true) {
    showStartMessage();
  }
});

watch(visible, (newVal) => {
  if (newVal === false) {
    getAIQuestions();
  }
});

// Lifecycle Hooks
onMounted(async () => {
  const email = sessionStorage.getItem("email");
  if (email) {
    accountId.value = await accountStore.requestAccountIdToDjango(email);
  } else {
    alert('로그인이 필요합니다.');
    router.push('/account/login');
  }
});

const startTimer = () => {
  clearInterval(timer.value);
  remainingTime.value = timeLimit;

  // 타이머 설정
  timer.value = setInterval(() => {
    if (remainingTime.value > 0) {
      remainingTime.value--;
    } else {
      clearInterval(timer.value);
      sendMessage();
    }
  }, 1000);
};

watch(currentAIMessage, () => {
  startTimer();
});

onBeforeUnmount(() => {
  clearInterval(timer.value);
});

// Methods
const startInterview = () => {
  start.value = true;
};

const getAIQuestions = async () => {
  if (aiResponseList.value.length === 0) {
    const questionId = Math.floor(Math.random() * 3061) + 1;
    aiResponseList.value = await aiInterviewStore.requestFirstQuestionToDjango({ questionId: questionId });
  }
  currentAIMessage.value = aiResponseList.value.firstQuestion || '질문을 불러오는 데 실패하였습니다. 다시 시도해주세요.';
  // intentIndex.value++;
  chatHistory.value.push({ type: "ai", content: currentAIMessage.value });

  const chunks = chunkText(currentAIMessage.value, 1);
  streamText(chunks);
};

const renderMessageContent = (message) => {
  if (message.type !== 'user') {
    return `<h2>${markdownIt().render(message.content)}</h2>`;
  }
};

const chunkText = (text, chunkSize) => {
  const chunks = [];
  for (let i = 0; i < text.length; i += chunkSize) {
    chunks.push(text.substring(i, i + chunkSize));
  }
  return chunks;
};

const streamText = async (chunks) => {
  currentAIMessage.value = '';
  let index = 0;
  const interval = setInterval(() => {
    if (index < chunks.length) {
      currentAIMessage.value += chunks[index];
      updateAIMessage();
      index++;
    } else {
      clearInterval(interval);
    }
  }, 10);
};

const updateAIMessage = () => {
  const lastIndex = chatHistory.value.length - 1;
  if (chatHistory.value[lastIndex] && chatHistory.value[lastIndex].type === 'ai') {
    chatHistory.value[lastIndex].content = currentAIMessage.value;
  } else {
    chatHistory.value.push({ type: 'ai', content: currentAIMessage.value });
  }
};

const adjustTextareaHeight = () => {
  const textarea = document.getElementById("messageInput");
  if (textarea) {
    textarea.style.height = "auto";
    textarea.style.height = `${textarea.scrollHeight}px`;
  }
};

const handleEnterKey = (event) => {
  if (!event.shiftKey) {
    sendMessage();
  }
};

const handleShiftEnter = () => {
  adjustTextareaHeight();
};

const sendMessage = async () => {
  if (sendCount.value >= maxMessages) {
    finished.value = true;
    return;
  }
  if (userInput.value.trim()) {
    chatHistory.value.push({ type: 'user', content: userInput.value });
  } else {
    chatHistory.value.push({ type: 'user', content: '질문에 답변하지 못했습니다.' });
  }
    userInput.value = '';
    adjustTextareaHeight();
    isLoading.value = true;
    sendCount.value++;

    setTimeout(async () => {
      if (aiResponseList.value.length === 0) {
        const questionId = Math.floor(Math.random() * 3061) + 1;
        aiResponseList.value = await aiInterviewStore.requestFirstQuestionToDjango({ questionId: questionId});
      }

      if (intentIndex.value === 4) {
        currentAIMessage.value = "수고하셨습니다. 면접이 종료되었습니다. 추후에 더 발전된 서비스로 찾아뵙겠습니다.";
        chatHistory.value.push({ type: "ai", content: currentAIMessage.value });
        finished.value = true;
        if (finished.value) {
          chatHistory.value.shift();
          chatHistory.value.pop();
          const contents = chatHistory.value.map(item => item.content);
          const pairedContents = [];
          const interviewIntents = ['자기 분석', '대처 능력', '소통 능력', '프로젝트 경험', '자기 개발'];

          for (let i = 0; i < contents.length; i += 2) {
            pairedContents.push([contents[i], contents[i + 1], interviewIntents[Math.floor(i / 2)]]);
          }

          const payload = { 'interviewResult': pairedContents };
          try {
            await aiInterviewStore.requestInferScoreResultToFastAPI(payload);
            const response = await aiInterviewStore.requestInferedResultToFastAPI(); //[1,2,3,4,5]
            for (let i = 0; i < response.resultList.length; i++) {
              pairedContents[i].push(response.resultList[i]);
            }

            const result = { scoreResultList: pairedContents, accountId: accountId.value };
            const saveDone = await aiInterviewStore.requestSaveInterviewResultToDjango(result);
            if (saveDone) {
              alert('면접 결과 확인하기');
              router.push(`/ai-interview/result/${accountId.value}`);
            }
          } catch {
            alert('죄송합니다. 지금은 채점 기능을 지원할 수 없습니다.')
          }
        }
      } else {
        const nextIntent = intentList[intentIndex.value];
        intentIndex.value++;

        let lastUserInput = null;
        for (let i = chatHistory.value.length - 1; i >= 0; i--) {
          if (chatHistory.value[i].type === 'user') {
            lastUserInput = chatHistory.value[i].content;
            break;
          }
        }

        const payload = { answer: lastUserInput, nextIntent: nextIntent };
        try {
          await aiInterviewStore.requestInferNextQuestionToFastAPI(payload);
          const response = await aiInterviewStore.requestInferedResultToFastAPI();
          if (response && response.nextQuestion) {
            currentAIMessage.value = response.nextQuestion;
            chatHistory.value.push({ type: "ai", content: currentAIMessage.value });
          }
        } catch {
          if ( nextIntent == '대처 능력' ) {
            const tempQuestionList = [
              "어려운 상황이나 갈등이 발생했을 때, 어떻게 대처하시는 편인가요? 그 사례를 들어 설명해 주세요.",
              "어려운 상황에서 예상치 못한 문제가 발생했을 때, 어떻게 대처하시는 편인가요? 구체적인 예시가 있다면 말씀해 주세요.",
              "스트레스를 받는 상황이나 예상치 못한 문제에 직면했을 때, 보통 어떤 방식으로 대처하시나요? 구체적인 예시를 들어주시면 좋겠습니다.",
              "스트레스를 받는 상황이 생겼을 때, 어떻게 대처하는 편인가요? 구체적인 사례와 함께 설명해 주세요."
            ]
            const randomIndex = Math.floor(Math.random() * tempQuestionList.length);
            currentAIMessage.value = tempQuestionList[randomIndex];
          }
          if ( nextIntent == '소통 능력' ) {
            const tempQuestionList = [
              "팀원 간에 소통이 원활하지 않을 때, 이를 어떻게 개선할 수 있다고 생각하나요?",
              "팀원 간의 의사소통이 원활하지 않을 때, 이를 개선하기 위해 어떤 노력을 기울였는지 구체적인 사례를 들어 설명해 주세요.",
              "팀원 간의 갈등이 발생했을 때, 그 상황을 어떻게 해결하실 건가요?",
              "팀원들과의 소통에서 가장 중요하게 생각하는 점은 무엇이며, 이를 실천하기 위해 어떤 노력을 하고 있나요?"
            ]
            const randomIndex = Math.floor(Math.random() * tempQuestionList.length);
            currentAIMessage.value = tempQuestionList[randomIndex];
          }
          if ( nextIntent == '프로젝트 경험' ) {
            const tempQuestionList = [
              "최근에 참여한 프로젝트에 대해 소개해주실 수 있나요? 프로젝트의 목표와 주요 내용을 말씀해 주세요.",
              "이전에 참여했던 프로젝트에 대해 설명해 주실 수 있나요? 어떤 목표를 가지고 진행되었고, 어떤 결과를 이끌어냈는지 궁금합니다.",
              "이전에 참여했던 프로젝트 중 가장 기억에 남는 프로젝트에 대해 설명해 주실 수 있나요? 어떤 목표가 있었고, 어떤 방식으로 진행되었는지 궁금합니다.",
              "최근에 참여했던 프로젝트에 대해 설명해 주실 수 있나요? 어떤 목표를 가지고 진행했으며, 어떤 결과가 있었는지 궁금합니다."
            ]
            const randomIndex = Math.floor(Math.random() * tempQuestionList.length);
            currentAIMessage.value = tempQuestionList[randomIndex];
          }
          if ( nextIntent == '자기 개발' ) {
            const tempQuestionList = [
              "자기 개발을 위해 최근에 어떤 새로운 기술이나 지식을 배우셨나요? 그 과정에서 느낀 점은 무엇인가요?",
              "최근에 본인에게 가장 큰 발전이 있다고 느꼈던 경험은 무엇이었나요? 그 경험이 왜 중요했는지 설명해 주시겠습니까?",
              "최근에 어떤 자기 개발 활동을 진행했는지 설명해 주시고, 그 경험이 어떻게 도움이 되었는지도 이야기해 주시기 바랍니다.",
              "최근에 자신이 개발한 기술이나 역량이 있나요? 그 기술을 어떻게 익히게 되었는지 구체적으로 말씀해 주세요."
            ]
            const randomIndex = Math.floor(Math.random() * tempQuestionList.length);
            currentAIMessage.value = tempQuestionList[randomIndex];
          }
        }
      }
        
      const chunks = chunkText(currentAIMessage.value, 1);
      streamText(chunks);
      isLoading.value = false;
    }, 1000);
};

const showStartMessage = () => {
  setTimeout(() => {
    visible.value = false;
  }, 2500);
};

useHead({
  title: `AI 모의면접 & 인성면접 | `,
  meta: [
    {
      name: 'description',
      content: 'AI 모의면접, AI 인성면접 🎯AIM에서 확인해보세요.',
    },
    {
      hid: 'keywords',
      name: 'keywords',
      content: '모의면접, ai 모의면접, 인성면접, ai 인성면접, 인적성 검사 준비, ai 인적, ai 면접, aim 모의면접, aim ai 모의면접, 에임 모의면접, 에임, 애임, AIM, AIM Sniper',
    },
  ],
});
</script>

<style scoped>
.draw-line {
  border: 1px solid #333; 
  padding: 16px;
  border-radius: 10px;
  width: 57%;
}

.li {
  margin-left: 3%;
}
.timer {
  font-size: 15px;
  color: black;
}

.red-text {
  color: red;
}

.control-margin {
  margin-top: 5%;
}

.interview-container {
  margin-top: 20%;
  border: 1px solid #333; 
  padding: 16px;
  border-radius: 10px;
  width: 70%;
}

.input-area {
  display: flex;
  align-items: center;
  gap: 20px;
  width: 50%;
  margin-bottom: 0;
}

textarea {
  flex-grow: 1;
  border: 1px solid #ccc;
  padding: 12px;
  resize: none; 
  border-radius: 10px;
  box-sizing: border-box;
  font-size: 15px;
  background-color: rgba(255, 255, 255, 1);
  color: black;  
  height: 50px;
  max-height: 70px;
}

.send-button {
  padding: 10px 12px;
  background-color: black;
  color: white;
  border: none;
  border-radius: 20px;
  cursor: pointer; 
  font-size: 16px;
}

.loading-message {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px 15px;
  border-radius: 18px;
  background-color: rgba(233, 233, 235, 0.8);
  color: black;
  font-style: italic;
  width: 50px;
}

.loading-message .dot {
  height: 10px;
  width: 10px;
  margin: 0 2px;
  background-color: black;
  border-radius: 50%;
  display: inline-block;
  opacity: 0;
  animation: loading-animation 1.5s infinite ease-in-out;
}

.loading-message .dot:nth-child(1) {
  animation-delay: 0s;
}

.loading-message .dot:nth-child(2) {
  animation-delay: 0.3s;
}

.loading-message .dot:nth-child(3) {
  animation-delay: 0.6s;
}

@keyframes loading-animation {
  0%, 80%, 100% {
    opacity: 0;
  }
  40% {
    opacity: 1;
  }
}
</style>