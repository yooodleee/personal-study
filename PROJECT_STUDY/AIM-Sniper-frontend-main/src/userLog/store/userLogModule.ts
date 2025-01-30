import actions, { UserLogActions } from "./action"
import state, { UserLogState } from "./states"

export interface UserLogModule {
    namespaced: true
    state: UserLogState
    actions: UserLogActions
}

const userLogModule: UserLogModule = {
    namespaced: true,
    state,
    actions
}

export default userLogModule
