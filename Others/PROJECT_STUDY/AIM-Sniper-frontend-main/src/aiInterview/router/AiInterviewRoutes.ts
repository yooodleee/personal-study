import AiInterviewPage from "@/aiInterview/pages/AiInterviewPage.vue"
import AIInterviewLLMTestPage from "@/aiInterview/pages/llmTest/AIInterviewLLMTestPage.vue"
import AIInterviewAnswerResultPage from "@/aiInterview/pages/result/AIInterviewAnswerResultPage.vue"
const AiInterviewRoutes = [
    {
        path: '/ai-interview',
        name: 'AiInterviewPage',
        components: {
            default: AiInterviewPage
        }
    },
    {
        path: '/ai-interview/llmTest',
        name: 'AIInterviewLLMTestPage',
        components: {
            default: AIInterviewLLMTestPage
        }
    },
    {
        path: '/ai-interview/result/:accountId',
        name: 'AIInterviewAnswerResult',
        components: {
            default: AIInterviewAnswerResultPage
        },
        props: {
            default: true
        }
    },
]
export default AiInterviewRoutes