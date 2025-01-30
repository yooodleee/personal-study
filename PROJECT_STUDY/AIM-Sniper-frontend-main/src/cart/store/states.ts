export interface CartState {
    cartItemList: CartItem[]
    cartItem: CartItem | null
}

export interface CartItem {
    companyReportId: number
    companyReportName: string
    companyReportPrice: number
}

const state: CartState = {
    cartItemList: [],
    cartItem: null,
}

export default state