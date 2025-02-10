import * as axiosUtility from "../../utility/axiosInstance"
import { useUserLogStore } from "./userLogStore"

export const userLogActions = {
    async requestCountClickToDjango(payload: { companyReport_id: string, purchase: boolean,email:string }): Promise<any> {
        const { djangoAxiosInst } = axiosUtility.createAxiosInstances()
        try {
            djangoAxiosInst.post('/marketing/make-count', {
                email: payload.email,
                companyReport_id: payload.companyReport_id,
                purchase: payload.purchase
            })
        } catch (error) {
            console.error('Error fetching userLog request:', error)
			throw error
        }
    },
};
