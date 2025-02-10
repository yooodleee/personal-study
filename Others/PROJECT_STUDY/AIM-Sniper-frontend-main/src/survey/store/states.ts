export interface SurveyState {
    surveyTitleList: Survey[]
    surveyForm: Survey | null
    resultForm: Survey | null
    
}

export interface Survey {
    surveyId: number
    surveyTitle: string
    surveyDescription: string
    surveyQuestions: []
    randomString: string
}

const state: SurveyState = {
    surveyTitleList: [],
    surveyForm: null,
    resultForm: null
}

export default state