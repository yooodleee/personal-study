export interface Account {
    nickname: string,
    
}

export interface AccountState {
    loginType: string
    email: string
    isauthenticatedNormal: boolean
    account: Account | null
    isNormalAdmin: boolean
}

const state: AccountState = {
    loginType: '',
    email: '',
    isauthenticatedNormal: false,
    account: null,
    isNormalAdmin: false
}

export default state