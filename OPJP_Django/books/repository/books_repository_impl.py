import os

from OPJP_Django import settings
from books.entity.books import Books
from books.repository.books_repository import BooksRepository


class BookRepositoryImpl(BooksRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    def list(self):
        return Books.objects.all().order_by('registerDate')
    
    def create(self, bookName, bookPrice, bookDescription, bookImage):
        uploadDirectory = os.path.join(
            settings.BASE_DIR,
            # 무엇을 넣어야 할까요?
        )
        if not os.path.exists(uploadDirectory):
            os.makedirs(uploadDirectory)
        
        imagePath = os.path.join(uploadDirectory, bookImage.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in bookImage.chunks():
                destination.write(chunk)
            
            destination.flush()
            os.fsync(destination.fileno())
        
        book = Books(
            bookName=bookName,
            bookDescription=bookDescription,
            bookPrice=bookPrice,
            bookImage=bookImage.name
        )
        book.save()

        savedBook = Books.objects.get(bookId=book.bookId)
        print(f"savedBook: {savedBook.bookImage}")
        return savedBook
    
    def findByBookId(self, bookId):
        try:
            return Books.objects.get(bookId=bookId)
        except Books.DoesNotExist:
            return None