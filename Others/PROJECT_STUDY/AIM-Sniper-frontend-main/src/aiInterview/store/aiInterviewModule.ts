import actions, { AIInterviewActions } from "./actions"
import state, { AiInterviewState } from "./states"


export interface AiInterviewModule {
    namespaced: true
    actions: AIInterviewActions
    state: AiInterviewState
}

const aiInterviewModule: AiInterviewModule = {
    namespaced: true,
    actions,
    state,
}

export default aiInterviewModule