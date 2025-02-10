import actions, { CompanyReportActions } from "./actions"
import mutations, { CompanyReportMutations } from "./mutations"
import state, { CompanyReportState } from "./states"

export interface CompanyReportModule {
    namespaced: true
    state: CompanyReportState
    actions: CompanyReportActions
    mutations: CompanyReportMutations
}

const companyReportModule: CompanyReportModule = {
    namespaced: true,
    state,
    actions,
    mutations,
}

export default companyReportModule