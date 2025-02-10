import * as axiosUtility from "../../utility/axiosInstance";
import { AxiosResponse } from "axios"

export const orderAction = {
    async requestCartToAddOrderToDjango(payload) {
        const {djangoAxiosInst} = axiosUtility.createAxiosInstances()
        try {
            const email = sessionStorage.getItem('email')
            if (!email) {
                throw new Error('email not found')
            }
            
            // console.log('payload:', payload)
            const requestData = { 
                email,
                items: payload.items.map(item => ({
                    cartItemId: item.cartItemId,
                    quantity: item.quantity,
                    orderPrice: item.orderPrice
                }))
            }

            const response = await djangoAxiosInst.post('/orders/cart', requestData)
            // console.log('response data:', response.data)
            
            return response.data
        } catch (error) { 
            console.error('장바구니 페이지에서 상품 구매시 에러 발생:', error)
            throw error
        }
    },
    async requestCompanyReportReadToAddOrderToDjango(payload: {email: string, companyReportId: number, companyReportPrice: number}): Promise<void> {
        const {djangoAxiosInst} = axiosUtility.createAxiosInstances()
        try {
            // console.log('payload:', payload)

            const response = await djangoAxiosInst.post('/orders/company_report', payload )
            console.log('response data:', response.data)
            
        } catch (error) { 
            console.error('상품 페이지에서 상품 구매 시 에러 발생:', error)
            throw error
        }
    },
    async requestMyOrderListToDjango(userToken: string): Promise<void> {
        const {djangoAxiosInst} = axiosUtility.createAxiosInstances()
        try {
            const email = sessionStorage.getItem("email")
            const res: AxiosResponse<any, any> = await djangoAxiosInst.post('/orders/list/', { email: email });
            // console.log('data:', res)
            const data = res.data;
            // console.log('data:', data)
            this.orderList = data
        } catch (error) {
            console.error('나의 주문 내역 출력 과정 중 에러 발생:', error);
            throw error
        }
    },
    async requestMyOrderItemListToDjango(ordersId: number): Promise<void> {
        const {djangoAxiosInst} = axiosUtility.createAxiosInstances()
        try {
            const res = await djangoAxiosInst.post(`/orders/read/${ordersId}`);
            this.orderItemList = res.data
            return this.orderItemList
        } catch (error) {
            console.error('requestMyOrderItemListToDjango() 문제 발생:', error);
            throw error
        }
    },
    async requestOrderItemDuplicationCheckToDjango(payload: {email: string, companyReportId: number}): Promise<void> {
        const {djangoAxiosInst} = axiosUtility.createAxiosInstances()
        
        try{
            const res = await djangoAxiosInst.post('/orders/order-item-duplication-check', { "payload": payload })
            return res.data
        } catch(error){
            console.error('requestOrderItemDuplicationCheckToDjango() 문제 발생:', error);
            throw error
        }
    },
}
