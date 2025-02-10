import { defineStore } from "pinia"
import { userLogActions } from "./userLogAction"
import { userLogState } from "./userLogStates"

export const useUserLogStore = defineStore("userLogStore", {
    state: userLogState,
    actions: userLogActions,
})