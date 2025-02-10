import { MutationTree } from "vuex";
import { AuthenticationState } from "./states";
import {
    REQUEST_IS_AUTHENTICATED_TO_DJANGO,REQUEST_IS_ADMIN_TO_DJANGO
} from "./mutation-types";

export interface AuthenticationMutations extends MutationTree<AuthenticationState> {
    [REQUEST_IS_AUTHENTICATED_TO_DJANGO](state: AuthenticationState, settingValue: boolean): void
    [REQUEST_IS_ADMIN_TO_DJANGO](state:AuthenticationState,settingValue: boolean): void
}

const mutations: MutationTree<AuthenticationState> = {
    [REQUEST_IS_AUTHENTICATED_TO_DJANGO](state: AuthenticationState, settingValue: boolean): void {
        state.isAuthenticatedKakao = settingValue
    },
    [REQUEST_IS_ADMIN_TO_DJANGO](state: AuthenticationState, settingValue: boolean): void {
        state.isKakaoAdmin = settingValue
    }
}

export default mutations as AuthenticationMutations