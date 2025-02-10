export const surveyState = () => ({
    surveyTitleList: [] as string[],
    surveyForm: null as Survey | null,
    resultForm: null as Survey | null,
  });
  
  type Survey = {
    surveyId: number;
    surveyTitle: string;
    surveyDescription: string;
    surveyQuestions: any[];
    randomString: string;
  };
  