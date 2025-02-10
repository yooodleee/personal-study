export interface ManagementState {
    userLogList: UserLog[]
    userLog: UserLog | null
    userData: UserData | null
    userList: User[]
    user: User | null 
}

export interface UserLog {
    userId:number,
    companyReportId: number,
    companyReportName:string,
    clickCount: number,
    purchase:boolean
    last_click:Date
}
export interface UserData{
    userCount: number,
    accountCount: number,
    purchaseCount: number,
    revenueCount: number,
}

export interface User {
    userId: number
    email: string,
    gender: string,
    birthyear: number,
    login_type: string,
    role_type: string,
    last_login: Date
}

const state: ManagementState = {
    userLogList: [],
    userLog: null,
    userData: null,
    userList: [],
    user: null,
}

export default state