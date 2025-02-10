export const userLogState = () => ({
    isPurchase: false as UserLog | false,
})

export type UserLog = {
    isPurchase: boolean
}