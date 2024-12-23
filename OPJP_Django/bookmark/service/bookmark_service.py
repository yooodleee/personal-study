from abc import ABC, abstractmethod


class BookmarkService(ABC):
    @abstractmethod
    def bookmarkRegister(self, bookmarkData, accountId):
        pass

    @abstractmethod
    def bookmarkList(self, accountId):
        pass

    @abstractmethod
    def removeBookmarkItem(self, bookmarkItemId):
        pass