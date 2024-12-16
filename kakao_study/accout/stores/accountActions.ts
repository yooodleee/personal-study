import * as axiosUtility from "../../utility/axiosInstance"
import { AxiosResponse } from "axios"
import { useAccountStore } from "./accountStore"

export const accountAction = {

        async requestAccountIdToDjango(email: string): Promise<any> {
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
        try{
            const res: AxiosResponse = await djangoAxiosInstance.post('/account/get-account-id', { email })
            return res.data.accountId

        }catch(error){
            console.error("requestAccountIdToDjango() axios 오류!", error);
        }
    },
    // async requestEmailDuplicationCheckToDjango(emal: string): Promise<boolean> {
    //     const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    //     try {
    //         const res = await djangoAxiosInstance.post('/account/email-duplication-check', email );

    //         if (res.data.isDuplicate) {
    //             return true;
    //         } else {
    //             alert('사용 가능한 이메일입니다.');
    //             return false;
    //         }
    //     } catch(error) {
    //         console.error('requestEmailDuplicationCheckToDjango() axios 오류!', error);
    //         throw error;    // 필요하다면 오류를 다시 던질 수 있습니다.
    //     }
    // },
    // async requestNicknameDuplicationCheckToDjango(nickname: string): Promise<boolean> {
    //     const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    //     try {
    //         const res = await djangoAxiosInstance.post('/account/nickname-duplication-check', nickname);

    //         if (res.data.isDuplicate) {
    //             return true;
    //         } else {
    //             return false;
    //         }
    //     } catch(error) {
    //         console.error('requestNicknameDuplicationcheckToDjango() axios 오류!', error);
    //         throw error;    // 필요하다면 오류를 다시 던질 수 있습니다.
    //     }
    // },
    // async requestCreateNewAccountToDjango(accountInfo:{email:string, nickname:string}): Promise<void>{
    //     const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
    //     try {
    //         await djangoAxiosInst.post('/account/register', accountInfo);
    //     } catch (error) {
    //         console.error('신규 계정 생성 실패:', error)
    //         throw error
    //     }
    // },
    // async requestNickNameToDjango(email:string): Promise<any>{
    //     const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
    //     const accountStore = useAccountStore()
    //     try{
    //         const res: AxiosResponse = await djangoAxiosInst.post('/account/nickname', email)
    //         accountStore.nickname = res.data
    //     } catch(error) {
    //         console.error('requestNicknameToDjango() 문제 발생: ', error);
    //         throw error
    //     }
    // },
    // async requestAccountCheckToDjango(payload: any): Promise<boolean> {
    //     const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    //     const { email, password } = payload;

    //     try {
    //         // await는 axios.post 호출 앞에 있어야 합니다.
    //         const res : AxiosResponse = await djangoAxiosInstance.post('/account/account-check', { email: email, password: password});

    //         if (res.data.isDuplicate) {
    //             return true;
    //         } else {
    //             return false;
    //         }
    //     } catch(error) {
    //         console.error('requestAccountCheckToDjango() 문제 발생: ', error);
    //         throw error;
    //     }
    // },
    // async requestWithdrawlToDjango(payload:{reason: string}): Promise<AxiosResponse>{
    //     const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
    //     const { reason } = payload
    //     try {
    //         const res: AxiosResponse = await djangoAxiosInst.post('/account/withdraw', {reason: reason, userToken: userToken})
    //     } catch(error) {
    //         alert('requestWithdrawlToDjango() 문제 발생!')
    //         throw error
    //     }
    // },
    // async requestGenderToDjango(email: string): Promise<any>{
    //     const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
    //     const accountStore = useAccountStore()
    //     try{
    //         const res : AxiosResponse = await djangoAxiosInst.post('/account/gender', {email});
    //         accountStore.gender = res.data
    //         return res.data
    //     } catch(error) {
    //         console.error('requestGenderToDjango() 문제 발생: ', error);
    //         throw error
    //     }
    // },
    // async requestBirthyearToDjango(email:string): Promise<any>{
    //     const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
    //     const accountStore = useAccountStore()
    //     try{
    //         const res: AxiosResponse = await djangoAxiosInst.post('/account/birthyear', email);
    //         accountStore.birthyear = res.data
    //         return res.data
    //     } catch(error) {
    //         console.error('requestBirthyearToDjango() 문제 발생: ', error);
    //         throw error
    //     }
    // },
    // async requestPasswordModifyToDjango(payload:{email:string, newPassword: string}): Promise<void>{
    //     const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
    //     try{
    //         await djangoAxiosInst.post('/account/modify-password', {email:payload.email, newPassword: payload.newPassword})
    //     } catch(error) {
    //         console.error('비밀번호 변경 실패: ', error);
    //         throw error;
    //     }
    // },
    // async requestNicknameModifyToDjango(payload:{email:string, newNickname: string}):Promise<void>{
    //     const {djangoAxiosInst } = axiosUtility.createAxiosInstances();
    //     try{
    //         await djangoAxiosInst.post('/account/modify-nickname', { email: payload.email, newNickname: payload.newNickname});
    //     }catch (error) {
    //         console.error('닉네임 변경 실패: ', error);
    //         throw error;
    //     }
    // },
    // async requestRoleTypeToDjango(email: string): Promise<void>{
    //     const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
    //     try{
    //         return await djangoAxiosInst.post('/account/role-type', {'email':email});
    //     } catch (error) {
    //         console.error('roleType 취득 실패: ', error);
    //         throw error;
    //     }
    // },
    // async requestProfileToDjango(email:string): Promise<any>{
    //     const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
    //     const accountStore = useAccountStore()
    //     try{
    //         const res: AxiosResponse = await djangoAxiosInst.post('/account/profile', email);
    //         this.nickname = res.data.nickname
    //         this.gender = res.data.gender
    //         this.birthyear = res.data.birthyear
    //     } catch(error) {
    //         console.error('requestBirthyearToDjango() 문제 발생: ', error);
    //         throw error
    //     }
    // },
};