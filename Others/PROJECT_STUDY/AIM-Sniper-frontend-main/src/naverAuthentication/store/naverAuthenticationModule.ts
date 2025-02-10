import actions, { NaverAuthenticationActions } from "./actions"
import mutations, { NaverAuthenticationMutations } from "./mutations"
import state, { NaverAuthenticationState } from "./states"

export interface NaverAuthenticationModule {
    namespaced: true
    state: NaverAuthenticationState
    actions: NaverAuthenticationActions
    mutations: NaverAuthenticationMutations 
}

const naverAuthenticationModule: NaverAuthenticationModule = {
    namespaced: true,
    state,
    actions,
    mutations,
}

export default naverAuthenticationModule
