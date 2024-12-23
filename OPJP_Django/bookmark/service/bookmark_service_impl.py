# 우리가 선언해주었던 클래스들에 대한 정보들을 빠르게 보고 싶나요?
# 그렇다면 ctrl을 누르고 해당 클래스를 클릭하면 우리가 선언했던 클래스 로직으로 빠르게 이동합니다.
# 이를 통해 우리는 빠르게 클래스 로직을 확인할 수 있죠.
from kakao_account.repository.account_repository_impl import AccountRepositoryImpl
from bookmark.repository.bookmark_repository_impl import BookmarkRepositoryImpl
from bookmark.service.bookmark_service import BookmarkService
from books.repository.books_repository_impl import BookRepositoryImpl


class BookmarkServiceImpl(BookmarkService):
    # 싱글턴을 선언했네요.
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            # 아래 세 줄을 쉽게 말하면 각각의 클래스들에서 필요한 객체들을 가져오겠다는 의미입니다.
            cls.__instance.__bookmarkRepository = BookmarkRepositoryImpl.getInstance()
            cls.__instance.__booksRepostiroy = BookRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
        
        return cls.__instance
    
    # 싱글턴을 재사용하려면 @classmethod
    # 싱글턴의 장점은 재사용할 수 있다는 점입니다!
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    # 이 메서드 로직은 이상하네요. 일단 pass할게요.
    def bookmarkRegister(self, bookmarkData, accountId):
        account = self.__accountRepository.findById(accountId)
        bookmark = self.__bookmarkRepository.findByAccount(account)
        if bookmark is None:
            print("북마크 새롭게 등록")
            bookmark = self.__bookmarkRepository.register(account)
        else:
            pass

        bookmarkId = bookmarkData.get('bookmarkId')
        print(f"bookmarkId:", {bookmarkId})

        bookmarkItemList = self.__bookmarkItemRepository.findAllByBookmarkId(bookmarkId)
        print(f"bookmarkItemList: {bookmarkItemList}")

        bookmarkItem = None
        for item in bookmarkItemList:
            bookmarkFromBookmarkItem = item.bookmark
            accountFromBookmark = bookmarkFromBookmarkItem.account
            if accountFromBookmark.id == account.id:
                bookmarkItem = item
                break
        
        if bookmarkItem is None:
            print('신규 북마크 추가')
            book = self.__bookRepository.findByBookId(bookmarkId)
            self.__bookmarkItemRepository.register(bookmarkData, bookmark, book)
        else:
            print("기존 북마크 추가")
            self.__bookmarkItemRepository.update(bookmarkItem)
    
    # 이 메서드도 이상하네요. 일단 pass할게요.
    def bookmarkList(self, accountId):
        account = self.__accountRepository.findById(accountId)
        bookmark = self.__bookmarkRepository.findByAccount(account)
        print(f"bookmarkList -> bookmark: {bookmark}")
        bookmarkItemList = self.__bookmarkItemRepository.findByBookmark(bookmark)
        print(f"bookmarkList -> bookmarkItemList: {bookmarkItemList}")
        bookmarkItemListResponseForm = []

        for bookmarkItem in bookmarkItemList:
            bookmarkItemResponseForm = {
                'bookmarkItemId': bookmarkItem.bookmarkItemId,
                'bookName': bookmarkItem.books.bookName,
                'bookId': bookmarkItem.books.bookId,
                'bookImage': bookmarkItem.books.bookImage,
            }
            bookmarkItemListResponseForm.append(bookmarkItemResponseForm)
        
        return bookmarkItemListResponseForm
    
    def removeBookmarkItem(self, bookmarkItemId):
        return self.__bookmarkItemRepository.deleteByBookmarkItemId(bookmarkItemId)