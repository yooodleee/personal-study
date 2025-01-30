import { MutationTree } from "vuex";
import { CompanyReportState, CompanyReport } from "./states";
import { REQUEST_COMPANYREPORT_LIST_TO_DJANGO,
         REQUEST_COMPANYREPORT_TO_DJANGO} from "./mutation-types";

export interface CompanyReportMutations extends MutationTree<CompanyReportState> {
    [REQUEST_COMPANYREPORT_LIST_TO_DJANGO] (state: CompanyReportState, receivedData: CompanyReport[]): void
    [REQUEST_COMPANYREPORT_TO_DJANGO] (state: CompanyReportState, receivedData: CompanyReport): void

}

const mutations: MutationTree<CompanyReportState> = {
    [REQUEST_COMPANYREPORT_LIST_TO_DJANGO] (state: CompanyReportState, receivedData: CompanyReport[]): void {
        state.companyReports = receivedData
    },
    [REQUEST_COMPANYREPORT_TO_DJANGO] (state: CompanyReportState, receivedData: CompanyReport): void {
        state.companyReport = receivedData
    },
}


export default mutations as CompanyReportMutations