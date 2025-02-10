import { ActionContext } from "vuex";
import { User, ManagementState } from "./states"; // 상태 타입
import { AxiosResponse } from "axios";
import axiosInst from "@/utility/axiosInstance";

export type ManagementActions = {
  requestUserListToDjango(context: ActionContext<ManagementState, any>): Promise<void>;
  requestUserLogListToDjango(context: ActionContext<ManagementState, any>): Promise<void>;
  grantAdminRoleInDjango(context: ActionContext<ManagementState,any>,email: string): Promise<any>
  revokeAdminRoleInDjango(context: ActionContext<ManagementState,any>,email: string): Promise<any>
  requestUserDataToDjango(context: ActionContext<ManagementState, any>): Promise<void>;
};

const actions: ManagementActions = {
    async requestUserListToDjango({ commit }: ActionContext<ManagementState, any>) {
        try {
            const response: AxiosResponse<User[]> = await axiosInst.djangoAxiosInst.get('/management/userList'); // Django API 엔드포인트
            const userList = response.data;
            // 여기서 commit을 통해 Vuex 상태를 업데이트할 수 있습니다.
            commit('REQUEST_USER_LIST_TO_DJANGO', userList);
        } catch (error) {
            console.error("Error fetching user list:", error);
            // 에러 처리 로직 추가 가능
        }
    },
    async requestUserLogListToDjango({commit}: ActionContext<ManagementState,any>){
        try {
            const response: AxiosResponse<User[]> = await axiosInst.djangoAxiosInst.post('/management/userLogList'); // Django API 엔드포인트
            const userLogList = response.data;
            // 여기서 commit을 통해 Vuex 상태를 업데이트할 수 있습니다.
            commit('REQUEST_USER_LOG_LIST_TO_DJANGO', userLogList);
        } catch (error) {
            console.error("Error fetching user list:", error);
            // 에러 처리 로직 추가 가능
        }
    },
    async grantAdminRoleInDjango(
        context: ActionContext<ManagementState,any>,
        email: string
    ): Promise<any>{
        try{
            await axiosInst.djangoAxiosInst.post('/management/grant-roleType',{'email':email});
        } catch(error){
            console.error('roleType 변경 실패:',error)
            throw error
        }
    },
    async revokeAdminRoleInDjango(
        context: ActionContext<ManagementState,any>,
        email: string
    ): Promise<any>{
        try{
            await axiosInst.djangoAxiosInst.post('/management/revoke-roleType',{'email':email});
        } catch(error){
            console.error('roleType 변경 실패:',error)
            throw error
        }
    },
    async requestUserDataToDjango({ commit }: ActionContext<ManagementState, any>) {
        try {
            const response: AxiosResponse<User[]> = await axiosInst.djangoAxiosInst.post('/management/data');
            // console.log("API response data:", response.data); // API 응답 확인
            const userData = response.data;
            // Vuex 상태 업데이트
            commit('REQUEST_USER_DATA_TO_DJANGO', userData);
        } catch (error) {
            console.error("Error fetching user list:", error);
            // 에러 처리 로직 추가 가능
        }
    }
};

export default actions;
