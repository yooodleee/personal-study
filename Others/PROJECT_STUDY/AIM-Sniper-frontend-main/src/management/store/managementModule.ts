import actions, { ManagementActions } from "./actions"
import mutations,{ ManagementMutations } from "./mutaions"
import state, { ManagementState } from "./states"

export interface ManagementModule {
    namespaced: true
    state: ManagementState
    actions: ManagementActions
    mutations: ManagementMutations
}

const managementModule: ManagementModule = {
    namespaced: true,
    state,
    actions,
    mutations,
}

export default managementModule