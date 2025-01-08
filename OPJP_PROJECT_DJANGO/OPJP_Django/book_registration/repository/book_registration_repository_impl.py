from book_registration.entity.book_registration import BookRegistration
from book_registration.repository.book_registration_repository import BookRegistrationRepository

import pandas as pd


class BookRegistrationRepositoryImpl(BookRegistrationRepository):
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
    
    def create(self, bookRegistrationData):
        bookRegistration = BookRegistration(**bookRegistrationData)
        bookRegistration.save()
        return bookRegistration
    
    def createMany(self, bookRegistrationData):
        bookRegistrationList = []
        for bookRegistrationData in bookRegistrationList:
            bookRegistration = BookRegistration(**bookRegistrationData)
            bookRegistrationList.append(bookRegistration)
        
        return bookRegistrationList
    
    def findAll(self):
        bookRegistrationList = BookRegistration.objects.all().values()
        print(
            f"bookRegistrationList: {bookRegistrationList}"
        )
        return pd.DataFrame(bookRegistrationList)