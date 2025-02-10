import { ActionContext, Commit } from "vuex"
import { Account, AccountState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"

export type AccountActions = {
    requestAccountIdToDjango(context: ActionContext<AccountState, any>, email: string): Promise<Account>
    requestEmailDuplicationCheckToDjango(context: ActionContext<AccountState, any>, payload: any): Promise<boolean>
    requestNicknameDuplicationCheckToDjango(context: ActionContext<AccountState, any>, payload: any): Promise<boolean>
    requestCreateNewAccountToDjango(context: ActionContext<AccountState, any>, accountInfo: { email: string, nickname: string }): Promise<void>
    requestNicknameToDjango(context: ActionContext<AccountState, any>, email: string): Promise<Account>
    requestAccountCheckToDjango(context: ActionContext<AccountState, any>,payload: any): Promise<boolean>
    requestWithdrawalToDjango(context: ActionContext<AccountState, unknown>, payload: { reason: string }): Promise<AxiosResponse>
    requestGenderToDjango(context: ActionContext<AccountState, any>, email: string): Promise<Account>
    requestBirthyearToDjango(context: ActionContext<AccountState, any>, email: string): Promise<Account>
    requestNicknameModifyToDjango(
        context: ActionContext<AccountState, any>,
        payload: { email: string; newNickname: string }
    ): Promise<void>;
    requestPasswordModifyToDjango(
        context: ActionContext<AccountState, any>,
        payload: { email: string; newPassword: string }
    ): Promise<void>
    requestRoleTypeToDjango(
        context: ActionContext<AccountState, any>,
        email: string
    ): Promise<void>
}

const actions: AccountActions = {
    async requestAccountIdToDjango(context: ActionContext<AccountState, any>, email: string): Promise<Account> {
        const res: AxiosResponse = await axiosInst.djangoAxiosInst.post('/account/get-account-id', { email })
        return res.data.accountId
    },
    async requestEmailDuplicationCheckToDjango(context: ActionContext<AccountState, any>, payload: any): Promise<boolean> {
        const { email } = payload
        
        return axiosInst.djangoAxiosInst.post(
            '/account/email-duplication-check',
            { email: email }
        )
            .then((res) => {
                if (res.data.isDuplicate) {
                    return true
                } else {
                    alert('사용 가능한 이메일입니다.')
                    return false
                }
            })
    },
    async requestNicknameDuplicationCheckToDjango(context: ActionContext<AccountState, any>, payload: any): Promise<boolean> {
        const { newNickname } = payload

        return axiosInst.djangoAxiosInst.post(
            '/account/nickname-duplication-check',
            { newNickname: newNickname }
        )
            .then((res) => {
                if (res.data.isDuplicate) {
                    alert('중복된 닉네임입니다.')
                    return true
                } else {
                    alert('사용 가능한 닉네임입니다.')
                    return false
                }
            })
    },
    async requestCreateNewAccountToDjango(context: ActionContext<AccountState, any>,
        accountInfo: { email: string, nickname: string }): Promise<void> {
        try {
            alert('신규 계정이 생성되었습니다!')
            await axiosInst.djangoAxiosInst.post('/account/register', accountInfo)
        } catch (error) {
            console.error('신규 계정 생성 실패:', error)
            throw error
        }
    },
    async requestNicknameToDjango(context: ActionContext<AccountState, any>, email: string): Promise<Account> {
        try {
            // const userToken = sessionStorage.getItem("userToken");
            const res: AxiosResponse<Account> =
                await axiosInst.djangoAxiosInst.post('/account/nickname', { email });
            // console.log('data:', res.data)
            context.commit('REQUEST_NICKNAME_TO_DJANGO', res.data);
            return res.data
        } catch (error) {
            console.error('requestNicknameToDjango() 문제 발생:', error);
            throw error
        }
    },
    async requestAccountCheckToDjango(
        context: ActionContext<AccountState, any>,
        payload: any
    ): Promise<boolean> {

        const { email,password } = payload

        return axiosInst.djangoAxiosInst.post(
                    '/account/account-check', 
                    { email:email,password: password }
        )
        .then((res) => {
            if (res.data.isDuplicate) {
                return true
            } else {
                return false
            }
        })
    },
    async requestWithdrawalToDjango(context: ActionContext<AccountState, unknown>, payload: { reason: string }): Promise<AxiosResponse> {
        // console.log('requestWithdrawalToDjango()')
        const userToken = sessionStorage.getItem("userToken");
        const { reason } = payload
        // console.log('전송할 데이터:', { reason })
        try {
            const res: AxiosResponse = await axiosInst.djangoAxiosInst.post('/account/withdraw', { reason: reason, userToken: userToken })
            // console.log('res:', res.data)
            return res.data
        } catch (error) {
            alert('requestWithdrawalToDjango() 문제 발생!')
            throw error
        }
    },
    async requestGenderToDjango(context: ActionContext<AccountState, any>, email: string): Promise<Account> {
        try {
            // const userToken = sessionStorage.getItem("userToken");
            const res: AxiosResponse<Account> =
                await axiosInst.djangoAxiosInst.post('/account/gender', { email });
            // console.log('data:', res.data)
            context.commit('REQUEST_GENDER_TO_DJANGO', res.data);
            return res.data
        } catch (error) {
            console.error('requestGenderToDjango() 문제 발생:', error);
            throw error
        }
    },
    async requestBirthyearToDjango(context: ActionContext<AccountState, any>, email: string): Promise<Account> {
        try {
            // const userToken = sessionStorage.getItem("userToken");
            const res: AxiosResponse<Account> =
                await axiosInst.djangoAxiosInst.post('/account/birthyear', { email });
            // console.log('data:', res.data)
            context.commit('REQUEST_BIRTHYEAR_TO_DJANGO', res.data);
            return res.data
        } catch (error) {
            console.error('requestBirthyearToDjango() 문제 발생:', error);
            throw error
        }
    },
    async requestPasswordModifyToDjango(
        context: ActionContext<AccountState, any>,
        payload: { email: string; newPassword: string }
    ): Promise<void> {
        try {
            await axiosInst.djangoAxiosInst.post('/account/modify-password', { email: payload.email, newPassword: payload.newPassword });
        } catch (error) {
            console.error('비밀번호 변경 실패:', error);
            throw error;
        }
    },
    async requestNicknameModifyToDjango(
        context: ActionContext<AccountState, any>,
        payload: { email: string; newNickname: string }
    ): Promise<void> {
        try {
            await axiosInst.djangoAxiosInst.post('/account/modify-nickname', { email: payload.email, newNickname: payload.newNickname });
        } catch (error) {
            console.error('닉네임 변경 실패:', error);
            throw error;
        }
    },
    async requestRoleTypeToDjango(
        context: ActionContext<AccountState, any>,
        email: string
    ): Promise<void> {
        try {
            return await axiosInst.djangoAxiosInst.post('/account/role-type', { 'email':email });
        } catch (error) {
            console.error('roleType 취득 실패:', error);
            throw error;
        }
    }
};

export default actions;