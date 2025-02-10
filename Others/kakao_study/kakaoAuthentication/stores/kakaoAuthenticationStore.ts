import { defineStore } from "pinia";
import { kakaoAuthenticationState } from "./kakaoAuthenticationState";
import { kakaoAuthenticationAction } from "./kakaoAuthenticationActions";

export const useKakaoAuthenticationStore = defineStore('kakaoAuthenticationStore', {
    state: kakaoAuthenticationState,
    actions: kakaoAuthenticationAction,
})