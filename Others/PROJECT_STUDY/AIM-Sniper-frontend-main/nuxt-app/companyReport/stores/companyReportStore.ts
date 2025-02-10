import { defineStore } from "pinia";
import { companyReportActions } from "./companyReportActions";
import { companyReportState } from "./companyReportState";

export const useCompanyReportStore = defineStore("companyReportStore", {
	state: companyReportState,
	actions: companyReportActions,
});