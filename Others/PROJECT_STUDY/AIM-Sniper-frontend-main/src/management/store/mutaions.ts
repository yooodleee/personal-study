import { MutationTree } from "vuex";
import { User, UserLog, ManagementState, UserData } from "./states";
import { REQUEST_USER_LIST_TO_DJANGO,
    REQUEST_USER_LOG_LIST_TO_DJANGO,
    REQUEST_USER_DATA_TO_DJANGO
       } from "./mutation-types";

export interface ManagementMutations extends MutationTree<ManagementState> {
    [REQUEST_USER_LIST_TO_DJANGO] (state: ManagementState, receivedData: User[]): void
    [REQUEST_USER_LOG_LIST_TO_DJANGO] (state: ManagementState, receivedData: UserLog[]): void
    [REQUEST_USER_DATA_TO_DJANGO](state:ManagementState,receivedData:UserData):void
}

const mutations: MutationTree<ManagementState> = {
    [REQUEST_USER_LIST_TO_DJANGO] (state: ManagementState, receivedData: User[]): void {
        state.userList = receivedData},
    [REQUEST_USER_LOG_LIST_TO_DJANGO] (state: ManagementState, receivedData: UserLog[]): void {
        state.userLogList = receivedData},
    [REQUEST_USER_DATA_TO_DJANGO] (state: ManagementState, receivedData: UserData): void {
        state.userData = receivedData}
}

export default mutations as ManagementMutations