from books.entity.books import Books
from books.repository.books_repository import BooksRepository

import pandas as pd


class BooksRepositoryImpl(BooksRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    def create(self, bookData):
        book = Books(**bookData)
        book.save()
        return book
    
    def createMany(self, bookDataList):
        books = []
        for bookData in bookDataList:
            book = Books(**bookData)
            book.save()
            books.append(book)
        
        return books
    
    def findAll(self)-> pd.DataFrame:
        books = Books.objects.all().values()
        return pd.DataFrame(books)
    
    def save(self, bookData):
        try:
            # 데이터베이스에서 ID로 기존 레코드 검색(id)
            book = Books.objects.get(id=bookData['bookId'])

            # 업데이트할 필드 설정
            book.bookDescription = bookData['bookDescription']

            # 저장
            book.save()
            print(
                f"Book with ID {book.bookId} successfully updated."
            )
        except Books.DoesNotExist:
            print(
                f"Book with ID {bookData['bookId']} does not exist in the database."
            )
        except Exception as e:
            print(
                f"An error occurred while saving the book data; {e}"
            )