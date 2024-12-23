from abc import abstractmethod, ABC


class BooksRepository(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, bookName, bookPrice, bookDescription, bookIamge):
        pass

    @abstractmethod
    def findByBookId(self, bookId):
        pass