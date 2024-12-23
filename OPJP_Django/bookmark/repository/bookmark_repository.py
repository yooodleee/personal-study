from abc import ABC, abstractmethod


class BookmarkRepository(ABC):
    @abstractmethod
    def register(cls, account):
        pass

    @abstractmethod
    def findByAccount(self, account):
        pass