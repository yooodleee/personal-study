from bookmark.entity.bookmark import BookMark
from bookmark.repository.bookmark_repository import BookmarkRepository


class BookmarkRepositoryImpl(BookmarkRepository):
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
    
    def register(cls, account):
        return BookMark.objects.create(account=account)
    
    def findByAccount(self, account):
        try:
            return BookMark.objects.get(account=account)
        except BookMark.DoesNotExist:
            return None