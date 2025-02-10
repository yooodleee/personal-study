import { ActionContext } from "vuex"
import { NaverAuthenticationState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"

export type NaverAuthenticationActions = {
    requestNaverOauthRedirectionToDjango(): Promise<void>
    requestNaverAccessTokenToDjangoRedirection(
        context: ActionContext<NaverAuthenticationState, any>,
        payload: { code: string }): Promise<void>
    requestNaverUserInfoToDjango(
        context: ActionContext<NaverAuthenticationState, any>): Promise<any>
    requestAddNaverRedisAccessTokenToDjango(
        { commit, state }: ActionContext<NaverAuthenticationState, any>,
        { email, accessToken }: { email: string, accessToken: string }
    ): Promise<any>
    requestNaverLogoutToDjango(
        context: ActionContext<NaverAuthenticationState, any>,
        userToken: string
    ): Promise<void>
}

const actions: NaverAuthenticationActions = {
    async requestNaverOauthRedirectionToDjango(): Promise<void> {
        return axiosInst.djangoAxiosInst.get('naver_oauth/naver').then((res) =>{
            window.location.href = res.data.url
        })
    },
    async requestNaverAccessTokenToDjangoRedirection(
        context: ActionContext<NaverAuthenticationState, any>,
        payload: { code: string }): Promise<void> {
            try {
                // console.log('requestNaverAccessTokenToDjangoRedirection()')
                const { code } = payload
                
                const response = await axiosInst.djangoAxiosInst.post(
                    'naver_oauth/naver/access-token', { code })
                sessionStorage.setItem("naverAccessToken", response.data.accessToken.access_token)
                sessionStorage.setItem("loginType","NAVER")
            } catch (error) {
                console.log('Naver Access Token 요청 중 문제 발생:', error)
                throw error
            }
    },
    async requestNaverUserInfoToDjango(
        context: ActionContext<NaverAuthenticationState, any>): Promise<any> {
            try {
                const accessToken = sessionStorage.getItem("naverAccessToken")
                const userInfoResponse: AxiosResponse<any> =
                    await axiosInst.djangoAxiosInst.post(
                        '/naver_oauth/naver/user-info',
                        { access_token: accessToken })
                
                const naverUserInfo = userInfoResponse.data.user_info
                return naverUserInfo
            } catch (error) {
                alert('네이버 사용자 정보 가져오기 실패!')
                throw error
            }
    },
    async requestAddNaverRedisAccessTokenToDjango(
        { commit, state }: ActionContext<NaverAuthenticationState, any>,
        { email, accessToken }: { email: string, accessToken: string }
    ): Promise<any> {
        try {
            const response: AxiosResponse<any> = await axiosInst.djangoAxiosInst.post(
                '/naver_oauth/redis-access-token', {
                email: email,
                accessToken: accessToken
            })

            // console.log('userToken:', response.data.userToken)

            sessionStorage.removeItem("naverAccessToken")
            sessionStorage.setItem("naverUserToken",response.data.userToken)
            commit('REQUEST_IS_NAVER_AUTHENTICATED_TO_DJANGO', true)
            return response.data
            
        } catch (error) {
            console.error('Error adding naver redis access token:', error)
        }
    },
    async requestNaverLogoutToDjango(
        context: ActionContext<NaverAuthenticationState, any>,
        userToken: string
    ): Promise<void> {
        try {
            const userToken = sessionStorage.getItem("naverUserToken")
            const res =
                await axiosInst.djangoAxiosInst.post('/naver_oauth/logout', {
                    userToken: userToken
                })
            // console.log('naverOauth logout res:', res.data.isSuccess)
            if (res.data.isSuccess === true) {
                context.commit('REQUEST_IS_NAVER_AUTHENTICATED_TO_DJANGO', false)
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

export default actions


