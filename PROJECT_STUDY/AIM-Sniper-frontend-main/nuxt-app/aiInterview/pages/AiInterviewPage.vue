<template>
  <div class="home-container">    

    <div class="content-wrapper">
      <h2 class="prompt-title">AIM AI INTERVIEW</h2>
      <h4 class="prompt-subtitle">AIM에서 제공하는 AI 인성면접 서비스에요</h4>
      <div class="prompt-container">
        <div class="chat-window">
          <div
            v-for="(message, index) in chatHistory"
            :key="index"
            :class="['message', message.type]"
          >
          <div v-if="message.type === 'user'" class="avatar user-avatar"></div>
              <div v-else class="avatar ai-avatar">
                <v-icon>mdi-account-tie</v-icon>
              </div>
            <div class="message-content" v-html="renderMessageContent(message)"></div>
          </div>


          <div v-if="isLoading" class="message ai">
            <v-icon>mdi:account-tie</v-icon>
            <div class="loading-message">
              <div class="dot"></div>
              <div class="dot"></div>
              <div class="dot"></div>
            </div>
          </div>
        </div>

        <!-- 입력창을 항상 맨 아래에 위치시키기 -->
        <div class="input-area">
          <textarea
            v-model="userInput" 
            placeholder="메시지를 입력하세요..." 
            @keydown.enter.exact.prevent="handleEnterKey"  
            @keydown.shift.enter="handleShiftEnter"
            @input="adjustTextareaHeight"
            @disable="finished"
            ref="messageInput"
          ></textarea>
          <button class="send-button" @click="sendMessage"><b>↑</b></button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAiInterviewStore } from '@/stores/aiInterviewStore'  // Pinia store 가져오기
import markdownIt from 'markdown-it'
import '@mdi/font/css/materialdesignicons.css'
import { ref, reactive, computed, onMounted } from 'vue'

const userInput = ref('')
const userInputMessage = ref('')
const aiOutput = ref('')
const chatHistory = reactive([
  { type: 'ai', content: '안녕하세요! AI 모의 면접 서비스입니다. "면접 시작"을 입력하시면 면접을 시작할 수 있습니다. 총 5번의 질문이 제공됩니다.' }
])

const isLoading = ref(false)  // 로딩 상태 추가
const md = new markdownIt()  // markdown-it 인스턴스 생성
const sendCount = ref(0)  // 메시지 전송 횟수 추적
const maxMessages = 6  // 최대 메시지 전송 횟수 설정
const aiResponseList = reactive([])  // AI 질문 리스트 저장
const questionIndex = ref(0)  // 현재 질문 인덱스
const showContextMenu = ref(false)
const contextMenuX = ref(0)
const contextMenuY = ref(0)
const selectedContent = ref('')
const showModal = ref(false)
const userAvatar = "https://via.placeholder.com/40x40?text=U"
const aiAvatar = "https://via.placeholder.com/40x40?text=AI"
const currentAIMessage = ref('')  // 현재 AI 메시지를 저장하는 변수

const aiInterviewStore = useAiInterviewStore()  // Pinia store 인스턴스 가져오기

function renderMessageContent(message) {
  if (message.type !== 'user') {
    // markdown-it로 렌더링된 내용에 .markdown-content 클래스를 추가
    return `<div class="markdown-content">${md.render(message.content)}</div>`
  } else {
    return message.content
  }
}

function chunkText(text, chunkSize) {
  const chunks = []
  for (let i = 0; i < text.length; i += chunkSize) {
    chunks.push(text.substring(i, i + chunkSize))
  }
  return chunks
}

async function streamText(chunks) {
  currentAIMessage.value = ''  // 초기화
  let index = 0
  const interval = setInterval(() => {
    if (index < chunks.length) {
      currentAIMessage.value += chunks[index]
      updateAIMessage()  // AI 메시지 업데이트 메소드 호출
      index++
    } else {
      clearInterval(interval)
    }
  }, 10) // 10ms마다 조각 추가
}

function updateAIMessage() {
  // chatHistory를 갱신하여 화면에 업데이트
  const lastIndex = chatHistory.length - 1
  if (chatHistory[lastIndex] && chatHistory[lastIndex].type === 'ai') {
    chatHistory[lastIndex].content = currentAIMessage.value
  } else {
    chatHistory.push({ type: 'ai', content: currentAIMessage.value })
  }
}

function adjustTextareaHeight() {
  const textarea = document.querySelector('.messageInput')
  textarea.style.height = "auto"  // 높이를 자동으로 설정
  textarea.style.height = `${textarea.scrollHeight}px`  // 내용에 따라 높이 설정
}

function handleEnterKey(event) {
  if (!event.shiftKey) {
    sendMessage()
  }
}

function handleShiftEnter(event) {
  adjustTextareaHeight()  // 줄바꿈 후 높이 조정
}

async function sendMessage() {
  if (sendCount.value >= maxMessages) {
    chatHistory.push({
      type: "ai",
      content: "면접이 종료되었습니다. 추후에 더 나은 서비스로 찾아오겠습니다."
    })
    return  // 5번 이상이면 메시지 전송 차단
  }
  if (userInput.value.trim()) {
    chatHistory.push({ type: 'user', content: userInput.value })
    userInputMessage.value = userInput.value
    userInput.value = ''
    adjustTextareaHeight()
    isLoading.value = true
    sendCount.value++

    setTimeout(async () => {
      if (aiResponseList.length === 0) {
        const sessionId = Math.floor(Math.random() * 200) + 1
        aiResponseList.push(...(await aiInterviewStore.requestGetQuestionListToDjango({ sessionId })))
      }
      const aiResponse = aiResponseList.questionList[questionIndex.value] || "면접이 종료되었습니다."
      questionIndex.value++
      chatHistory.push({
        type: "ai",
        content: aiResponse
      })
      const chunks = chunkText(aiResponse, 1)
      await streamText(chunks)
      isLoading.value = false
    }, 1000)
  }
}

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
.content-wrapper {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  text-align: center;
  margin-top: 10vh;
  padding-top: 20px; 
}

.prompt-title {
  width: 100%; /* 부모 요소의 전체 너비를 차지하도록 설정 */
  max-width: 70vw; /* 프롬프트창과 일치하는 너비 */
  font-size: 32px;
  color: #0A28B0;
  margin-top: 2%;
  margin-bottom: 10px;
  margin-left: 5%;
  text-align: left;  
}
.prompt-subtitle {
  width: 100%; /* 부모 요소의 전체 너비를 차지하도록 설정 */
  max-width: 70vw; /* 프롬프트창과 일치하는 너비 */
  font-size: 16px;
  color: #222222;
  margin-bottom: 20px;
  margin-left: 5%;
  text-align: left;  
}

/* 채팅 프롬프트 컨테이너 */
.prompt-container {
  width: 70vw;
  height: 60vh; 
  border-radius: 40px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  
  max-height: 80vh; /* 높이를 더 줄여서 타이틀과 서브타이틀이 위로 올라가게 함 */
  overflow-y: auto;
  background-color: white;
  box-shadow: 0 0 10px 0 grey;
}

/* 채팅 창 */
.chat-window {
  flex-grow: 1;  /* 대화 내용이 영역을 채우도록 설정 */
  padding: 20px;
  overflow-y: auto;  /* 대화 내용이 많아지면 스크롤바 추가 */
  display: flex;
  flex-direction: column;
  justify-content: flex-start; /* 대화가 위에서부터 쌓이도록 설정 */
  background-color: transparent; /* 배경을 투명으로 유지 */
}

/* 각 메시지의 스타일 */
.message {
  display: flex;
  align-items: flex-start;
  margin-bottom: 15px;
  max-width: 55%;
}

.user {
  margin-left: auto;
  flex-direction: row-reverse;
}

.ai {
  margin-right: auto;
}



/* 아바타 이미지 스타일 */
.avatar {
  width: 45px;
  height: 45px;
  border-radius: 50%;
  margin: 0 10px;
  border: 2px solid transparent; /* 기본적으로 투명한 테두리 설정 */

}

.ai .avatar {
  font-size: 40px; /* 아이콘 크기 조정 */
  color: black; /* 아이콘 색상 조정 */
}

.user .avatar {
  font-size: 40px; /* 아이콘 크기 조정 */
  color: black; /* 아이콘 색상 조정 */
  margin: 20px 50px; 
}

/* 메시지 내용 스타일 */
.message-content {
  background-color: #f0f0f0; /* 말풍선 배경 색상 */
  border-radius: 10px; /* 말풍선 모서리 둥글게 */
  padding: 10px; /* 말풍선 내부 여백 */
  max-width: 300px; /* 말풍선 최대 너비 */
  margin-left: 0; /* 왼쪽 여백 제거 */
  position: relative; /* 부모 요소 기준으로 절대 위치 설정 가능 */
  bottom: 0; /* 말풍선이 아이콘의 높이와 정렬되도록 설정 */
}
/* AI 말풍선 */
.ai .message-content {
  background-color: #0a28b020; 
  color: black;
  border-radius: 20px 20px 20px 0px;
  max-width: 100%; 
}
/* 사용자 말풍선 */
.user .message-content {
  background: linear-gradient(90deg, #0A28B0, #6a9efc); /* 왼쪽에서 오른쪽으로 파란색 그라데이션 */
  color: white; 
  border-radius: 20px 20px 0px 20px;
  max-width: 100%; /* 사용자 말풍선 너비 제한 */
  padding: 10px; /* 내부 여백 추가 */
}




/* 메시지 입력 영역 스타일 */
.input-area {
  display: flex;
  align-items: center;
  justify-content: space-between; /* 좌우 여백을 자동으로 채움 */
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 30px; /* 둥근 테두리 */
  border: none; /* 테두리 제거 */
  margin: 0 auto; /* 입력창을 중앙으로 정렬 */
  margin-bottom: 10px;
  width: 95%; /* 너비를 전체 화면의 95%로 설정 */
  height: auto; /* 높이를 자동으로 조정 */
  padding: 10px; /* 입력창 안쪽 여백 추가 */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* 부드러운 그림자 추가 */
}

/* 텍스트 입력창 스타일 */
textarea {
  width: 95%; /* 너비를 90%로 설정 */
  height: auto; /* 높이 자동 조정 */
  padding: 10px 20px; /* 안쪽 여백 조정 */
  border-radius: 30px; /* 더 둥글게 조정 */
  border: 1px solid #ccc; /* 테두리 추가 */
  font-size: 16px;
  background-color: rgba(255, 255, 255, 1); /* 흰색 배경 */
  color: black;
  resize: none; /* 사용자가 크기 조정하지 못하도록 설정 */
  outline: none; /* 포커스 시 외곽선 제거 */
  
}

/* 전송 버튼 스타일 */
.send-button {
  padding: 10px 12px; /* 버튼 내부 여백 */
  background: linear-gradient(90deg, #0A28B0, #6a9efc); /* 그라데이션 배경 */
  color: white;
  border: none;
  border-radius: 50%; /* 버튼을 원형으로 */
  cursor: pointer;
  font-size: 16px; /* 버튼 텍스트 크기 */
  width: 40px; /* 버튼 크기 설정 */
  height: 35px; /* 버튼 크기 설정 */
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 부드러운 그림자 추가 */
}




/* ... 로딩 말풍선 */
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

.context-menu ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
.context-menu li {
  padding: 10px;
  cursor: pointer;
}
.context-menu li:hover {
  background-color: #f0f0f0;
}

</style>
