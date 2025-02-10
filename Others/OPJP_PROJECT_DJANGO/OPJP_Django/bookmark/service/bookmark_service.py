from abc import ABC, abstractmethod


class BookmarkService(ABC):

    @abstractmethod
    def createBookmark(self, accountId, bookmark):
        pass
    
    @abstractmethod
    def listBookmark(self, accountId, page, pageSize):
        pass

    @abstractmethod
    def removeBookmark(self, accountId, bookmarkId):
        pass