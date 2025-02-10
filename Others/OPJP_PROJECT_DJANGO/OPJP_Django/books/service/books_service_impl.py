import os

from books.repository.books_repository_impl import BooksRepositoryImpl
from books.service.books_service import BooksService

import re
import pandas as pd


class BooksServiceImpl(BooksService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__booksRepository = BooksRepositoryImpl.getInstance()
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    def bookList(self):
        return self.__bookRepository.findAll()
    
    def requestModifyBookDescription(self):
        csvFilePath = os.path.join(
            "resource", "book_description_modify.csv"
        )

        # 파일에서 데이터를 읽는 것은 헬퍼로 위임
        bookDescriptionList = self.__readBookDescriptionFromFile(csvFilePath)
        if not csvFilePath:
            return 
        
        print(f"bookDescriptionList: {bookDescriptionList}")

        # 기존 데이터 가져오기
        existingBookList = self.__bookRepository.findAll()
        print(f"existingBookList: {existingBookList}")

        # 기존 데이터와 파일 데이트를 기반으로 업데이트 작업만 수행
        updateBookList = self.__prepareUpdateBooks(existingBookList, bookDescriptionList)
        print(f"updateBooksList: {updateBookList}")

        # 업데이트 실행
        if updateBookList:
            self.__updateExistngBooks(updateBookList)
            return True
        
        print("업데이트할 데이터가 없습니다.")
        return False
    
    # Private Method1: 파일에서 텍스트 읽기
    def __readBookDescriptionFromFile(self, csvFilePath):
        currentWorkingDirectory = os.getcwd()
        print(
            f"현재 작업 디렉터리: {currentWorkingDirectory}"
        )

        # 절대 경로 생성
        absPath = os.path.join(currentWorkingDirectory, csvFilePath)
        print(f"absPath: {absPath}")

        if not os.path.exists(absPath):
            print(f"CSV 파일이 존재하지 않습니다: {absPath}")
            return None
        
        try:
            with open(
                absPath, newline="", encoding="utf-8"
            ) as csvfile:
                # 첫 번째 줄을 건너뛰고 데이터를 읽어들임
                reader = csvfile.readlines()[1:]    # 첫 번째 줄을 건너뛰고 나머지 데이터를 읽음
                return {
                    line.strip() for line in reader if line.strip()
                }   # 빈 줄을 제외하고 데이터만 셋에 추가
        
        except Exception as e:
            print(f"CSV 파일을 읽는 중 오류 발생: {e}")
            return None
    
    # Private Method2: 업데이트 데이터 준비
    def __prepareUpdateBooks(self, existingBookList, bookDescriptionList):
        update_books = []
        print(
            f'len(existingBookList): {len(existingBookList)}'
        )
        print(
            f'len(bookDescriptionList): {len(bookDescriptionList)}'
        )

        # bookDescriptionList가 빈 값이 아니어야 함
        if bookDescriptionList:
            # existingBookList의 각 항목에 대해 bookDescriptionList에서 값을 가져와서 넣기
            bookDescriptionList = list(bookDescriptionList) # set이 아닌 list로 변환(순서 보장)

            if len(existingBookList) == len(bookDescriptionList):
                for i, book in enumerate(existingBookList.to_dict("records")):
                    book['bookDescription'] = bookDescriptionList[i]    # bookDescriptionList에서 해당 인덱스의 값을 넣기
                    update_books.append(
                        {"bookId": book["bookId"], "bookDescription": book["bookDescription"]}
                    )
                    print(
                        f"Updated book with id: {book["bookId"]} and new description: {book["bookDescription"]}"
                    )
            else:
                print("The lengths of existingBookList and bookDescriptionList do not match.")
        else:
            print("bookDescription is empty.")
        
        return update_books
    
    # Private Method3: 기존 데이터 업데이트
    def __updateExistngBooks(self, updateBookList):
        for bookData in updateBookList:
            self.__bookRepository.save(bookData)
            print(
                f"업데이트 도서 데이터: {bookData['bookDescription']}"
            )