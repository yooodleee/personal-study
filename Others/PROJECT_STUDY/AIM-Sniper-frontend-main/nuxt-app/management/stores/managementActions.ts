import { AxiosResponse } from "axios";
import * as axiosUtility from "../../utility/axiosInstance";
import { useManagementStore } from "./mangementStore";
import { managementState } from "./managementState";

export const managementActions = {
    async requestUserListToDjango() {
        const {djangoAxiosInst} = axiosUtility.createAxiosInstances()
        try {
            const response: AxiosResponse = await djangoAxiosInst.get('/management/userList'); // Django API 엔드포인트
            const userList = response.data;
            // 여기서 commit을 통해 Vuex 상태를 업데이트할 수 있습니다.
            this.userList = userList
        } catch (error) {
            console.error("Error fetching user list:", error);
            // 에러 처리 로직 추가 가능
        }
    },
    async requestUserLogListToDjango(){
        const {djangoAxiosInst} = axiosUtility.createAxiosInstances()
        try {
            const response: AxiosResponse = await djangoAxiosInst.post('/management/userLogList'); // Django API 엔드포인트
            const userLogList = response.data;
            // 여기서 commit을 통해 Vuex 상태를 업데이트할 수 있습니다.
            this.userLogList = userLogList
        } catch (error) {
            console.error("Error fetching user list:", error);
            // 에러 처리 로직 추가 가능
        }
    },
    async grantAdminRoleInDjango(email: string): Promise<any>{
        const {djangoAxiosInst} = axiosUtility.createAxiosInstances()
        try{
            await djangoAxiosInst.post('/management/grant-roleType',{'email':email});
        } catch(error){
            console.error('roleType 변경 실패:',error)
            throw error
        }
    },
    async revokeAdminRoleInDjango(email: string): Promise<any>{
        const {djangoAxiosInst} = axiosUtility.createAxiosInstances()
        try{
            await djangoAxiosInst.post('/management/revoke-roleType',{'email':email});
        } catch(error){
            console.error('roleType 변경 실패:',error)
            throw error
        }
    }
}