from account.repository.account_repository_impl import AccountRepositoryImpl
from interview_result.repository.interview_result_repository_impl import InterviewResultRepositoryImpl
from interview_result.service.interview_result_service import InterviewResultService

class InterviewResultServiceImpl(InterviewResultService):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__interviewResultRepository = \
                InterviewResultRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def saveInterviewResult(self, scoreResultList, accountId):
        # accountId 필드
        account = self.__accountRepository.findById(accountId)
        # account 필드
        interviewResult = \
            self.__interviewResultRepository.registerInterviewResult(account)
        # interviewResult, scoreResultList 필드
        self.__interviewResultRepository.registerInterviewResultQAS(
            interviewResult, 
            scoreResultList
        )

    def getInterviewResult(self, accountId):
        # accountId 필드
        account = self.__accountRepository.findById(accountId)
        # LastInterviewResult를 get
        interviewResult = \
            self.__interviewResultRepository.getLastInterviewResult()
        # interviewResult 필드를 LastInterviewResultQASList에서 get
        interviewResultList = \
            self.__interviewResultRepository.getLastInterviewResultQASList(
                interviewResult
        )
        return interviewResultList
