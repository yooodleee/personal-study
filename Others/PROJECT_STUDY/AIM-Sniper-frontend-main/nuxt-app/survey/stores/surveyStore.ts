import { defineStore } from "pinia";
import { surveyState } from "./surveyState";
import { surveyActions } from "./surveyActions";

export const useSurveyStore = defineStore("surveyStore", {
	state: surveyState,
	actions: surveyActions,
});