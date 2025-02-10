export interface AuthenticationState {
    isAuthenticatedKakao: boolean
    isKakaoAdmin: boolean
}

const state: AuthenticationState = {
    isAuthenticatedKakao: false,
    isKakaoAdmin: false
}

export default state