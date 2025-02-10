from abc import ABC, abstractmethod


class BookmarkRepository(ABC):

    @abstractmethod
    def save(self, bookmark):
        pass

    @abstractmethod
    def findBookmarkByAccount(self, account, bookmark):
        pass

    @abstractmethod
    def findById(self, bookmarkId):
        pass

    @abstractmethod
    def deleteById(self, bookmarkId):
        pass