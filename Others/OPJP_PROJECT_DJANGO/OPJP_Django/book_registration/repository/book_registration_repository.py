from abc import ABC, abstractmethod


class BookRegistrationRepository(ABC):

    @abstractmethod
    def createMany(self, bookRegirationData):
        pass

    @abstractmethod
    def findAll(self):
        pass