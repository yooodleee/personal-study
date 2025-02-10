from abc import ABC, abstractmethod


class BooksService(ABC):

    @abstractmethod
    def bookList(self):
        pass

    @abstractmethod
    def requestModifyBookDescription(self):
        pass