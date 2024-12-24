from books.repository.books_repository_impl import BookRepositoryImpl
from books.service.books_service import BookService


class BookServiceImpl(BookService):
    # 싱글턴 선언언
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__bookRepository = BookRepositoryImpl.getInstance()
        
        return cls.__instance
    
    # 싱글턴 사용-> @classmethod
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    # 책 정보들을 리스트 형태로 반환환
    def list(self):
        return self.__bookRepository.list()
    
    # 책 정보들을 새로 등록해줍니다.
    def createdBook(self, bookName, bookPrice, bookDescription, bookImage):
        return self.__bookRepository.create(
            bookName, bookPrice, bookDescription, bookImage)
    
    # 저장되있는 책을 가져오려고 하는데 책이 한 두 권도 아니고 어떻게 원하는 책을 가져올까요?
    # 서로 식별되고 구별되면서 유일한 값으로 가져와야 할 것 같습니다.
    # 그렇다면 필요한 값으로는 Id가 적당하겠네요.
    def readBook(self, bookId):
        return self.__bookRepository.findByBookId(bookId)