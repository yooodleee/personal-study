import { MutationTree } from "vuex";
import { GoogleAuthenticationState } from "./states"
import { REQUEST_IS_GOOGLE_AUTHENTICATED_TO_DJANGO,REQUEST_IS_GOOGLE_ADMIN_TO_DJANGO } from "./mutation-types"

export interface GoogleAuthenticationMutations extends MutationTree<GoogleAuthenticationState> {
    [REQUEST_IS_GOOGLE_AUTHENTICATED_TO_DJANGO](state: GoogleAuthenticationState, settingValue: boolean): void
    [REQUEST_IS_GOOGLE_ADMIN_TO_DJANGO](state: GoogleAuthenticationState,settingValue:boolean): void
}

const mutations: MutationTree<GoogleAuthenticationState> = {
    [REQUEST_IS_GOOGLE_AUTHENTICATED_TO_DJANGO](state: GoogleAuthenticationState, settingValue: boolean): void {
        state.isAuthenticatedGoogle = settingValue
    },
    [REQUEST_IS_GOOGLE_ADMIN_TO_DJANGO](state: GoogleAuthenticationState, settingValue: boolean): void {
        state.isGoogleAdmin = settingValue
    }
}

export default mutations as GoogleAuthenticationMutations