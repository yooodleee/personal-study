import * as axiosUtility from "../../utility/axiosInstance";
import { AxiosResponse } from "axios"

export const cartAction = {
    async requestAddCartToDjango(payload): Promise<AxiosResponse> {
        const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
    
        try {
            if (!payload.email) {
                throw new Error('User token not found');
            }
            const response = await djangoAxiosInst.post('/cart/register', payload);
            return response; // AxiosResponse 타입 반환
        } catch (error) {
            console.error('Error adding to cart:', error);
            throw error;
        }
    },    
    async requestCartListToDjango(email: string):Promise<AxiosResponse> {
        const {djangoAxiosInst} = axiosUtility.createAxiosInstances()
        try {
            const email = sessionStorage.getItem('email');
            if (!email) {
                throw new Error('email not found');
            }

            const response = await djangoAxiosInst.post('/cart/list', {email});
            return response.data;
        } catch (error) {
            console.error('Error fetching cart list:', error);
            throw error;
        }
    },
    async requestDeleteCartItemToDjango(cartItemId: number[]): Promise<void> {
        const {djangoAxiosInst} = axiosUtility.createAxiosInstances()
        try {
            await djangoAxiosInst.delete('/cart/delete', { data: cartItemId })
        } catch (error) {
            console.log('requestDeleteCartItemToDjango() 과정에서 문제 발생')
            throw error
        }
    },
    async requestCartItemDuplicationCheckToDjango(payload: {email: string, companyReportId: number}): Promise<void> {
        const {djangoAxiosInst} = axiosUtility.createAxiosInstances()
        try{

            const res = await djangoAxiosInst.post('/cart/cart-item-duplication-check', { payload })
            return res.data
        }catch(error){
            console.log('requestCartItemDuplicationCheckToDjango() 과정에서 문제 발생')
            throw error
        }
    }
}

