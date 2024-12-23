from kakao_account.repository.account_repository_impl import AccountRepositoryImpl
from bookmark.repository.bookmark_repository_impl import BookmarkRepositoryImpl
from bookmark.service.bookmark_service import BookmarkService
from books.repository.books_repository_impl import BookRepositoryImpl


class BookmarkServiceImpl(BookmarkService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__bookmarkRepository = BookmarkRepositoryImpl.getInstance()
            cls.__instance.__booksRepostiroy = BookRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
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