export const managementState = () => ({
    userLogList: [] as UserLog[],
	userLog: null as UserLog | null,
    userList : [] as User[],
    user: null as User | null,
});

type UserLog = {
    userId:number,
    companyReportId: number,
    companyReportName:string,
    clickCount: number,
    purchase:boolean
    last_click:Date
}

type User = {
    userId: number
    email: string,
    gender: string,
    birthyear: number,
    login_type: string,
    role_type: string,
    last_login: Date
}
