import * as axiosUtility from "../../utility/axiosInstance";
import { companyReportState } from "./companyReportState";
import { useCompanyReportStore } from "./companyReportStore";

export const companyReportActions = {
	async requestCompanyReportToDjango(companyReportId: number): Promise<void> {
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
		const companyReportStore = useCompanyReportStore();

        try {
            const res = await djangoAxiosInst.get(`/company_report/read/${companyReportId}`);
			companyReportStore.companyReport = res.data;
        } catch (error) {
            console.error('requestCompanyReportToDjango() -> error:', error);
            throw error;
        }
    },

	async requestCompanyReportListToDjango(): Promise<void> {
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
		const companyReportStore = useCompanyReportStore();

		try {
			const res = await djangoAxiosInst.get('/company_report/list/');
			const data = res.data;
			const sortedData = data.sort((a, b) => a.companyReportId - b.companyReportId)
			companyReportStore.companyReportList = sortedData;
		} catch (error) {
			console.error('Error fetching companyReport list:', error);
			throw error;
		}
	},

	async requestCreateCompanyReportToDjango(imageFormData: FormData): Promise<void> {
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
	
		try {
			await djangoAxiosInst.post('/company_report/register', imageFormData, {
				headers: {
					'Content-Type': 'multipart/form-data',
				},
			});
			alert('보고서를 성공적으로 등록하셨습니다.');
		} catch (error) {
			console.log('requestCreateCompanyReportToDjango() -> error:', error);
			throw error;
		}
	},

	async requestDeleteCompanyReportToDjango(companyReportId: number): Promise<void> {
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
		
		try {
			await djangoAxiosInst.delete(`/company_report/delete/${companyReportId}`);
		} catch (error) {
			console.log('requestDeleteCompanyReportToDjango() -> error:', error);
			throw error;
		}
	},
	
    async requestModifyCompanyReportToDjango(payload: {
        companyReportName: string;
		content: string;
		companyReportId: number;
		companyReportPrice: number;
		keyword:string
    }): Promise<void> {
        const { companyReportName, content, companyReportId,companyReportPrice,keyword } = payload
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();

        try {
            await djangoAxiosInst.put(`/company_report/modify/${companyReportId}`, {
				companyReportName, 
				content, 
				companyReportPrice,
				keyword 
			});
        } catch (error) {
            console.log('requestModifyCompanyReportToDjango() 과정에서 문제 발생')
            throw error
        }
    },

	async requestCompanyReportFinanceToDjango(companyReportName: string): Promise<any> {
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();

		try {
			const data = await djangoAxiosInst.post('company_report/finance', { companyReportName });
			return data;
		} catch (error) {
			console.log('requestCompanyReportFinanceToDjango() -> error:', error);
			throw error;
		}
	},

	async requestCompanyReportInfoToDjango(companyReportName: string): Promise<any> {
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
		
		try {
			return await djangoAxiosInst.post('company_report/info', { companyReportName });
		} catch (error) {
			console.log('requestCompanyReportInfoToDjango() -> error:', error);
			throw error;
		}
	},
	
	async requestTopNCompanyReportListToDjango(topN: number): Promise<void> {
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
		const companyReportStore = useCompanyReportStore();
		
		try {
			const res = await djangoAxiosInst.post('company_report/top', { params: { topN } });
			companyReportStore.topList = res.data;
		} catch (error) {
			console.log('requestTopNCompanyReportListToDjango() -> error:', error);
			throw error;
		}
	},
};