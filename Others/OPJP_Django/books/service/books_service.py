from abc import abstractmethod, ABC


class BookService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createdBook(self, bookName, bookPrice, bookDescription, bookImage):
        pass
    
    @abstractmethod
    def readBook(self, bookId):
        pass