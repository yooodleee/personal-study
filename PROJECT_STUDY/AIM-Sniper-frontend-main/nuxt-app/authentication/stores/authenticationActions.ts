import * as axiosUtility from "../../utility/axiosInstance";
import { AxiosResponse } from "axios"

export const authenticationAction = {
    async requestKakaoOauthRedirectionToDjango():Promise<void>{
        const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
        try{
            return djangoAxiosInst.get('/kakao_oauth/kakao').then((res)=>{
                window.location.href = res.data.url
            })
        }catch(error){
            console.error('requestKakaoOauthRedirectionToDjango() 중 오류 발생',error)
            throw error
        }
    },
    async requestAccessTokenToDjangoRedirection(code:string):Promise<void>{
        const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
        try{
            const response = await djangoAxiosInst.post('/kakao_oauth/kakao/access-token', code)
            sessionStorage.setItem("accessToken",response.data.accessToken.access_token)
        } catch(error){
            console.log('Access Token 요청 중 문제 발생:', error)
            throw error
        }
    },
    async requestUserInfoToDjango():Promise<any>{
        const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
        try {
            const accessToken = sessionStorage.getItem("accessToken");
            const userInfoResponse: AxiosResponse<any> =
                await djangoAxiosInst.post(
                    '/kakao_oauth/kakao/user-info',
                    { access_token: accessToken });

            const userInfo = userInfoResponse.data.user_info
            return userInfo

        } catch (error) {
            alert('사용자 정보 가져오기 실패!')
            throw error;
        }
    },
    async requestAddRedisAccessTokenToDjango(payload: {email:string,accessToken:string}):Promise<any>{
        const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
        try {
            const response: AxiosResponse<any> = await djangoAxiosInst.post(
                '/kakao_oauth/redis-access-token/', {
                email: payload.email,
                accessToken: payload.accessToken
            });

            // console.log('userToken:', response.data.userToken)

            sessionStorage.removeItem("accessToken")
            sessionStorage.setItem("userToken", response.data.userToken)
            this.isAuthenticatedKakao=true
            return response.data;
        } catch (error) {
            console.error('Error adding redis access token:', error);
            throw error;
        }
    },
    async requestKakaoLogoutToDjango(userToken:string): Promise<void>{
        const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
        try {
                    const userToken = sessionStorage.getItem("userToken")
                    const adminToken = sessionStorage.getItem("adminToken")
                    if (userToken){
                    const res =
                        await djangoAxiosInst.post('/kakao_oauth/logout', {
                            userToken: userToken
                        })

                    // console.log('res:', res.data.isSuccess)
                    if (res.data.isSuccess === true) {
                        this.isAuthenticatedKakao = false
                        }
                    }else{
                        const res =
                        await djangoAxiosInst.post('/kakao_oauth/logout', {
                            userToken: adminToken
                        })
                    // console.log('res:', res.data.isSuccess)
                    if (res.data.isSuccess === true) {
                        this.isKakaoAdmin = false
                        }
                    }
                } catch (error) {
                    console.error('requestKakaoLogoutToDjango() 중 에러 발생:', error)
                    throw error
                }
                sessionStorage.removeItem("userToken")
                sessionStorage.removeItem('adminToken')
                sessionStorage.removeItem("email")
                sessionStorage.removeItem("loginType")
                if (sessionStorage.getItem("fileKey")) {
                    sessionStorage.removeItem("fileKey")
                }
            }
    };