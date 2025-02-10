export interface CompanyReportState {
    companyReports: CompanyReport[]
    companyReport: CompanyReport | null
}

export interface CompanyReport {
    companyReportId: number
    companyReportName: string
    companyReportPrice: number
    companyReportTitleImage: string
    content: string
    keyword: string
    companyReportCategory: string
    regDate: string
    updDate: string
}

const state: CompanyReportState = {
    companyReports: [],
    companyReport: null,
}

export default state