from books.repository.books_repository_impl import BookRepositoryImpl
from books.service.books_service import BookService


class BookServiceImpl(BookService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__bookRepository = BookRepositoryImpl.getInstance()
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    def list(self):
        return self.__bookRepository.list()
    
    def createdBook(self, bookName, bookPrice, bookDescription, bookImage):
        return self.__bookRepository.create(
            bookName, bookPrice, bookDescription, bookImage)
    
    def readBook(self, bookId):
        return self.__bookRepository.findByBookId(bookId)