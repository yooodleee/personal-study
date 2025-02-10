import * as axiosUtility from "../../utility/axiosInstance";
import { AxiosResponse } from "axios"

export const googleAuthenticationActions = {
    async requestGoogleOauthRedirectionToDjango(): Promise<void> {
        const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
        try{
            return djangoAxiosInst.get('google_oauth/google').then((res) =>{
            window.location.href = res.data.url
        })
        } catch(error){
            console.error('requestGoogleOauthRedirectionToDjango',error)
        }
    },
    async requestGoogleAccessTokenToDjangoRedirection(code:string):Promise<void>{
        const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
        try {
            // console.log('requestGoogleAccessTokenToDjangoRedirection()')
            
            const response = await djangoAxiosInst.post(
                'google_oauth/google/access-token', {code:code})
            // console.log(response.data.accessToken.access_token)
            sessionStorage.setItem("googleAccessToken", response.data.accessToken.access_token)
            sessionStorage.setItem("loginType","GOOGLE")
        } catch (error) {
            console.log('Google Access Token 요청 중 문제 발생:', error)
            throw error
        }
    },
    async requestGoogleUserInfoToDjango(): Promise<any> {
        const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
            try {
                const accessToken = sessionStorage.getItem("googleAccessToken")
                const userInfoResponse: AxiosResponse<any> =
                    await djangoAxiosInst.post(
                        '/google_oauth/google/user-info',
                        { access_token: accessToken })
                
                const googleUserInfo = userInfoResponse.data.user_info
                return googleUserInfo
            } catch (error) {
                alert('구글 사용자 정보 가져오기 실패!')
                throw error
            }
    },
    async requestAddGoogleRedisAccessTokenToDjango(payload:{email: string, accessToken: string}): Promise<any> {
        const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
        try {
            const response: AxiosResponse<any> = await djangoAxiosInst.post(
                '/google_oauth/redis-access-token', {
                email: payload.email,
                accessToken: payload.accessToken
            })

            // console.log('userToken:', response.data.userToken)

            sessionStorage.removeItem("googleAccessToken")
            sessionStorage.setItem("googleUserToken",response.data.userToken)
            this.isAuthenticatedGoogle = true
            return response.data
            
        } catch (error) {
            console.error('Error adding google redis access token:', error)
        }
    },
    async requestGoogleLogoutToDjango(userToken: string): Promise<void> {
        const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
        try {
            const userToken = sessionStorage.getItem("googleUserToken")
            const res =
                await djangoAxiosInst.post('/google_oauth/logout', {
                    userToken: userToken
                })
            // console.log('googleOauth logout res:', res.data.isSuccess)
            if (res.data.isSuccess === true) {
                this.isAuthenticatedGoogle = false
            }
        } catch (error) {
            console.error('requestGoogleLogoutToDjango() 중 에러 발생:', error)
            throw error
        }
        sessionStorage.removeItem("googleUserToken")
        sessionStorage.removeItem("email")
        sessionStorage.removeItem("loginType")
        if (sessionStorage.getItem("fileKey")) {
            sessionStorage.removeItem("fileKey")
        }
    }
}