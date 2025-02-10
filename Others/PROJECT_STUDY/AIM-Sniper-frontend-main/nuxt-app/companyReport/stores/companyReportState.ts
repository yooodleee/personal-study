export const companyReportState = () => ({
	companyReportList: [] as CompanyReport[],
	companyReport: null as CompanyReport | null,
  topList: [],
});

export type CompanyReport = {
    companyReportId: number;
    companyReportName: string;
    companyReportPrice: number;
    companyReportTitleImage: string;
    content: string;
    keyword: string;
    companyReportCategory: string;
    regDate: string;
    updDate: string;
  };    