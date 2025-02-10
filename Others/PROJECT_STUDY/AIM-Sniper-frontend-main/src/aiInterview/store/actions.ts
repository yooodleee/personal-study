import { ActionContext } from "vuex"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"

export type AIInterviewActions = {
    requestGetQuestionListToDjango(context: ActionContext<any, any>, sessionId: number): Promise<AxiosResponse>
    requestInferNextQuestionToFastAPI(
        context: ActionContext<any, any>,
        payload: { answer: string, nextIntent: string }): Promise<string>
    requestInferScoreResultToFastAPI(
        context: ActionContext<any, any>,
        payload: { interviewResult: any[] }): Promise<string>
    requestInferedResultToFastAPI(context: ActionContext<any, any>): Promise<string>
    requestSaveInterviewResultToDjango(
        context: ActionContext<any, any>,
        payload: { scoreResultList: [], accountId: string }): Promise<string>
    requestGetScoreResultListToDjango(
        context: ActionContext<any, any>, payload: { accountId: string }): Promise<string>
}   

const actions: AIInterviewActions = {
    async requestGetQuestionListToDjango(context: ActionContext<any, any>, sessionId: number): Promise<AxiosResponse> {
        const res: AxiosResponse = await axiosInst.djangoAxiosInst.post('/interview/get-session', sessionId)
        return res.data
    },
    async requestInferNextQuestionToFastAPI(
        context: ActionContext<any, any>,
        payload: { answer: string, nextIntent: string }): Promise<string> {
        console.log("payload:", payload)
        const { answer, nextIntent } = payload
        try {
            // console.log('requestInferNextQuestionToFastAPI()')
            // console.log("userInput:", answer)
            const command = 7

            const response = await axiosInst.fastapiAxiosInst.post(
                '/request-ai-command', { command, "data":[answer, nextIntent] })
            return response.data
        } catch (error) {
            console.log('requestInferToFastAPI() 중 문제 발생:', error)
            throw error
        }
    },
    async requestInferScoreResultToFastAPI(
        context: ActionContext<any, any>,
        payload: {  interviewResult: any[] }): Promise<string> {
        console.log("payload:", payload)
        const interviewResult = payload.interviewResult
        try {
            // console.log('requestInferScoreResultToFastAPI()')
            const command = 8

            const response = await axiosInst.fastapiAxiosInst.post(
                '/request-ai-command', { command, "data": interviewResult })
            return response.data
        } catch (error) {
            console.log('requestInferScoreResultToFastAPI() 중 문제 발생:', error)
            throw error
        }
    },

    async requestInferedResultToFastAPI(context: ActionContext<any, any>): Promise<string> {
        try {
            // console.log('requestInferedResultToFastAPI()')

            let response: AxiosResponse<any>;
            const maxAttempts = 30; // 최대 시도 횟수
            const delay = 1000; // 각 시도 사이의 지연시간 (ms)
            
            for (let attempt = 1; attempt <= maxAttempts; attempt++) {
                response = await axiosInst.fastapiAxiosInst.get('/polyglot-result');

                if (response.data && response.data.nextQuestion) {
                    // console.log('response.data', response.data);
                    return response.data;
                }

                console.log(`Attempt ${attempt} failed. Retrying in ${delay}ms...`);
                await new Promise(resolve => setTimeout(resolve, delay));
            }

            throw new Error('결과를 가져오는 데 실패했습니다.');
        } catch (error) {
            console.log('requestInferedResultToFastAPI() 중 문제 발생:', error)
            throw error
        }
    },
    async requestSaveInterviewResultToDjango(
        context: ActionContext<any, any>,
        payload: { scoreResultList: [], accountId: string }): Promise<string>{

            const res: AxiosResponse = await axiosInst.djangoAxiosInst.post('/interview_result/save-interview-result', payload)
            return res.data
    },
    async requestGetScoreResultListToDjango(
        context: ActionContext<any, any>, payload: { accountId: string }): Promise<string>{
            const res: AxiosResponse = await axiosInst.djangoAxiosInst.post('/interview_result/get-interview-result', payload)
            return res.data.interviewResultList
        }

}

export default actions;