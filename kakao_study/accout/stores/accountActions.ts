import * as axiosUtility from "../../utility/axiosInstance";
import { AxiosResponse } from "axios"
import { useAccountStore } from "./accountStore"

export const accountAction = {

        async requestAccountIdToDjango(email: string): Promise<any> {
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstance();
        try{
            const res: AxiosResponse = await djangoAxiosInstance.post('/account/get-account-id', { email })
            return res.data.accountId

        }catch(error){
            console.error("requestAccountIdToDjango() axios 오류!", error);
        }
    },
    // 