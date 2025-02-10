import * as axiosUtility from "../../utility/axiosInstance";
import { AxiosResponse } from "axios"

export const naverAuthenticationAction = {

    async requestNaverOauthRedirectionToDjango(): Promise<void> {
        const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
        try{
            return djangoAxiosInst.get('/naver_oauth/naver').then((res)=>{
                window.location.href = res.data.url
            })
        }catch(error){
            console.error('requestNaverOauthRedirectionToDjango() 중 오류 발생',error)
            throw error
        }
    },
    async requestNaverAccessTokenToDjangoRedirection(code:string):Promise<void>{
        const {djangoAxiosInst} = axiosUtility.createAxiosInstances()
        try{
            const response = await djangoAxiosInst.post('/naver_oauth/naver/access-token',code)
            sessionStorage.setItem("naverAccessToken", response.data.accessToken.access_token)
            sessionStorage.setItem("loginType","NAVER")
        }catch (error) {
            console.log('Naver Access Token 요청 중 문제 발생:', error)
            throw error
        }
    },
    async requestNaverUserInfoToDjango():Promise<any>{
        const {djangoAxiosInst} = axiosUtility.createAxiosInstances()
        try {
            const accessToken = sessionStorage.getItem("naverAccessToken")
            const userInfoResponse: AxiosResponse<any> =
                await djangoAxiosInst.post(
                    '/naver_oauth/naver/user-info',
                    { access_token: accessToken })
            
            const naverUserInfo = userInfoResponse.data.user_info
            return naverUserInfo
        } catch (error) {
            alert('네이버 사용자 정보 가져오기 실패!')
            throw error
        }
    },
    async requestAddNaverRedisAccessTokenToDjango(payload:{email:string,accessToken:string}):Promise<any>{
        const {djangoAxiosInst} = axiosUtility.createAxiosInstances()
        try {
            const response: AxiosResponse<any> = await djangoAxiosInst.post(
                '/naver_oauth/redis-access-token',
                {
                    'email': payload.email,
                    'accessToken': payload.accessToken
                },
            );
            // console.log('userToken:', response.data.userToken)

            sessionStorage.removeItem("naverAccessToken")
            sessionStorage.setItem("naverUserToken",response.data.userToken)
            this.isAuthenticatedNaver = true
            return response.data
            
        } catch (error) {
            console.error('Error adding naver redis access token:', error)
        }
    },
    async requestNaverLogoutToDjango(userToken: string):Promise<void>{
        const {djangoAxiosInst} = axiosUtility.createAxiosInstances()
        try {
            const userToken = sessionStorage.getItem("naverUserToken")
            const res =
                await djangoAxiosInst.post('/naver_oauth/logout', {
                    userToken: userToken
                })
            // console.log('naverOauth logout res:', res.data.isSuccess)
            if (res.data.isSuccess === true) {
                this.isAuthenticatedNaver = false
            }
        } catch (error) {
            console.error('requestNaverLogoutToDjango() 중 에러 발생:', error)
            throw error
        }
        sessionStorage.removeItem("naverUserToken")
        sessionStorage.removeItem("email")
        sessionStorage.removeItem("loginType")
        if (sessionStorage.getItem("fileKey")) {
            sessionStorage.removeItem("fileKey")
        }
    }
}