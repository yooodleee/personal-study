import { ActionContext } from "vuex"
import { UserLogState } from "./states"
import { AxiosResponse } from "axios"
import axiosInst from "@/utility/axiosInstance"

export type UserLogActions = {
    requestCountClickToDjango(context: ActionContext<UserLogState, unknown>, payload: { companyReport_id: string, purchase: boolean,email:string }): Promise<any>
}

const actions: UserLogActions = {
    async requestCountClickToDjango(context: ActionContext<UserLogState, unknown>, payload: { companyReport_id: string, purchase: boolean,email:string }): Promise<any> {
        // Return the result of the axios call for better control of success/failure
        axiosInst.djangoAxiosInst.post('/marketing/make-count', {
            email: payload.email,
            companyReport_id: payload.companyReport_id,
            purchase: payload.purchase
        });
    },
}

export default actions
