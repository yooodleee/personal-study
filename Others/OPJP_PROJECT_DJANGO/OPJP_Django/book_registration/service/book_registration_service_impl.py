import os
import pandas as pd

from book_registration.repository.book_registration_repository_impl import BookRegistrationRepositoryImpl
from book_registration.service.book_registration_service import BookRegistrationService


class BookRegistrationServiceImpl(BookRegistrationService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__bookRegistrationRepository = BookRegistrationRepositoryImpl.getInstance()
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    def __readBookDescriptionFromFile(self, filePath):
        try:
            # 엑셀 파일 읽기
            df = pd.read_excel(filePath)

            # 데이터가 잘 읽혔는지 확인
            print(df.head())

            # 데이터프레임을 리스트로 반환
            bookDescriptionList = df.to_dict(orient='records')
            return bookDescriptionList
        except Exception as e:
            print(
                f"파일을 읽는 중 오류가 발생했습니다: {str(e)}"
            )
            return []
    
    def createBookRegistration(self):
        csvFilePath = os.path.join("resource", "book_registration.xlsx")
        currentWorkingDirectory = os.getcwd()
        absPath = os.path.join(
            currentWorkingDirectory, csvFilePath
        )

        # 파일에서 데이터를 읽는 것은 헬퍼로 위임
        bookDescriptionList = self.__readBookDescriptionFromFile(absPath)
        if not bookDescriptionList:
            return False
        
        print(
            f"bookDescriptionList: {bookDescriptionList}"
        )
        
        self.__bookRegistrationRepository.createMany(bookDescriptionList)
        return True
    
    def bookRegistrationList(self):
        return self.__bookRegistrationRepository.findAll()