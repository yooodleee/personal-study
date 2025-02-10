from abc import ABC, abstractmethod


class BookRegistrationService(ABC):

    @abstractmethod
    def createBookRegistration(self):
        pass

    @abstractmethod
    def bookRegistrationList(self):
        pass