import { AxiosResponse } from "axios";
import * as axiosUtility from "../../utility/axiosInstance";
import { useSurveyStore } from "./surveyStore";
import { Survey } from "./surveyState";

export const surveyActions = {
	async requestCreateSurveyFormToDjango(
		randomString: string
	): Promise<AxiosResponse> {
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
		try {
			const res: AxiosResponse = await djangoAxiosInst.post(
				"/survey/creat-form",
				randomString
			);
			return res.data;
		} catch (e) {
			console.error("requestCreateSurveyFormToDjango() -> error:", e);
			throw e;
		}
	},

	async requestRegisterTitleAndDescriptionToDjango(payload: {
		surveyId: number;
		surveyTitle: string;
		surveyDescription: string;
	}): Promise<AxiosResponse> {
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
		try {
			const res: AxiosResponse = await djangoAxiosInst.post(
				"/survey/register-title-description",
				payload
			);
			return res.data;
		} catch (e) {
			console.error(
				"requestRegisterTitleAndDescriptionToDjango() -> error:",
				e
			);
			throw e;
		}
	},

	async requestCreateQuestionToDjango(
		imageFormData: FormData
	): Promise<AxiosResponse> {
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
		try {
			const res: AxiosResponse = await djangoAxiosInst.post(
				"/survey/register-question",
				imageFormData,
				{
					headers: {
						"Content-Type": "multipart/form-data",
					},
				}
			);
			return res.data;
		} catch (e) {
			console.error("requestCreateQuestionToDjango() -> error:", e);
			throw e;
		}
	},

	async requestRegisterSelectionToDjango(payload: {
		questionId: number;
		selection: string;
	}): Promise<AxiosResponse> {
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
		try {
			const res: AxiosResponse = await djangoAxiosInst.post(
				"/survey/register-selection",
				payload
			);
			return res.data;
		} catch (e) {
			console.error("requestRegisterSelectionToDjango() -> error:", e);
			throw e;
		}
	},

	async requestSurveyListToDjango() {
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
		try {
			const res: AxiosResponse<{ surveyTitleList: Survey[] }> =
				await djangoAxiosInst.get("/survey/survey-title-list");
			this.surveyTitleList = res.data.surveyTitleList;
		} catch (e) {
			console.error("requestSurveyListToDjango() -> error:", e);
			throw e;
		}
	},

	async requestSurveyFormToDjango(randomString: string) {
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
		try {
			const res: AxiosResponse<Survey> = await djangoAxiosInst.get(
				`/survey/read-survey-form/${randomString}`
			);
			this.surveyForm = res.data;
		} catch (e) {
			console.error("requestSurveyFormToDjango() -> error:", e);
			throw e;
		}
	},

	async requestSubmitSurveyToDjango(payload: {
		submitForm: [];
	}): Promise<AxiosResponse> {
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
		try {
			const res: AxiosResponse = await djangoAxiosInst.post(
				"/survey/submit-survey",
				payload
			);
			return res.data;
		} catch (e) {
			console.error("requestSubmitSurveyToDjango() -> error:", e);
			throw e;
		}
	},

	async requestRandomStringToDjango(surveyId: number): Promise<any> {
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
		try {
			const res: AxiosResponse = await djangoAxiosInst.post(
				"/survey/randomstring", surveyId
			);
			return res.data;
		} catch (e) {
			console.error(
				"Django 서버에서 랜덤 문자열을 받아오지 못했습니다:",
				e
			);
			return null;
		}
	},

	async requestSurveyResultToDjango(surveyId: number) {
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
		try {
			const res: AxiosResponse<Survey> = await djangoAxiosInst.get(
				`/survey/survey-result/${surveyId}`
			);
			this.resultForm = res.data;
		} catch (e) {
			console.error("requestSurveyResultToDjango() -> error:", e);
			throw e;
		}
	},

	async requestCheckIsFirstSubmit(accountId: {
		accountId: string;
	}): Promise<AxiosResponse> {
		const { djangoAxiosInst } = axiosUtility.createAxiosInstances();
		try {
			const res: AxiosResponse = await djangoAxiosInst.post(
				"/survey/check-first-submit",
				accountId
			);
			return res.data;
		} catch (e) {
			console.error("requestCheckIsFirstSubmit() -> error:", e);
			throw e;
		}
	},
};
