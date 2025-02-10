export interface GoogleAuthenticationState {
    isAuthenticatedGoogle: boolean
    isGoogleAdmin:boolean
}

const state: GoogleAuthenticationState = {
    isAuthenticatedGoogle: false,
    isGoogleAdmin:false
}

export default state