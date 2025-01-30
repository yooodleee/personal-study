import glob
import json
import os

from interview.repository.interview_repository_impl import InterviewRepositoryImpl
from interview.service.interview_service import InterviewService


class InterviewServiceImpl(InterviewService):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__interviewRepositoryImpl = \
                InterviewRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def insertSession(self):
        # questionFiles-> assets/json_qa_pair.json
        questionFiles = glob.glob(os.path.join('assets/json_qa_pair', 
                                               '*.json'))
        for questionFile in questionFiles:
            questionList = []
            # questionFile을 읽기 모드, utf-8 타입으로 open.
            with open(questionFile, 'r', encoding='utf-8') as file:
                print('열려는 qu file: ', questionFile)
                # questionFile의 data를 가져옴.
                data = json.load(file)
                # questionList에 data의 'question' 필드를 추가
                for dic in data:
                    questionList.append(dic.get('question'))
            
            # inserviewRepositoryImpl에 intserviewId + 1, questionList 추가
            interviewId = self.__interviewRepositoryImpl.getMaxId()
            self.__interviewRepositoryImpl.insertData(interviewId+1, 
                                                      questionList)
        print('저장 완료')

        return True

    def insertFirstQuestion(self):
        file_path = 'assets\\start_question_3061.json'

        # 파일 열기 및 JSON 파싱
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # inserviewRepositoryImpl에서 "question"인 item 필드를 insert
        [self.__interviewRepositoryImpl.insertFirstQuestion(item["question"]) 
         for item in data]

        return True

    def insertTechQuestion(self):
        file_path = 'assets\\tech_question_3014.json'

        # 파일 열기 및 JSON 파싱
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # interviewRepositoryImpl에 "question", "job"인 item을 data에서 insert.
        [self.__interviewRepositoryImpl.insertTechQuestion(
            item["question"], item["job"]) for item in data]

        return True

    def getSession(self, sessionId):
        # sessionId 필드를 intserviewRepositoryImpl에서 가져옴.
        questionList = self.__interviewRepositoryImpl.getData(sessionId)
        return questionList

    def getFirstQuestion(self, questionId):
        # questionId 필드를 intserviewRepositoryImpl에서 가져옴.
        firstQuestionList = self.__interviewRepositoryImpl.getFirstQuestion(
            questionId
        )
        return firstQuestionList

    def getTechQuestion(self, job):
        # job 필드를 intserviewRepositoryImpl에서 가져옴.
        techQuestion = self.__interviewRepositoryImpl.getTechQuestion(job)
        return techQuestion