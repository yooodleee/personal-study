from django.db.models import OuterRef, Subquery, Value
from django.db.models.functions import Coalesce
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from account.repository.account_repository_impl import AccountRepositoryImpl
from bookmark.service.bookmark_service import BookmarkService
from bookmark.repository.bookmark_repository_impl import BookmarkRepositoryImpl
from bookmark.entity.bookmark import BookMark
from books.repository.books_repository_impl import BooksRepositoryImpl


class BookmarkServiceImpl(BookmarkService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__bookmarkRepository = BookmarkRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__bookRepository = BooksRepositoryImpl.getInstance()

        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    def createBookmark(self, accountId, bookmark):
        foundAccount = self.__accountRepository.findById(accountId)

        if not foundAccount:
            raise Exception(
                "해당 accountId에 해당하는 account를 찾을 수 없습니다."
            )
        
        foundBook = self.__bookRepository.findById(bookmark['bookmarkId'])

        if not foundAccount:
            raise Exception(
                "해당 bookmarkId에 해당하는 도서를 찾을 수 없습니다."
            )
        
        foundBookmark = self.__bookmarkRepository.findBookmarkByAccountAndBook(
            foundAccount, foundBook
        )

        if foundBookmark:
            foundBookmark.quantity += bookmark['quantity']
            updatedBookmark = self.__bookmarkRepository.save(foundBookmark)
            return updatedBookmark
        
        newBookmark = BookMark(
            account = foundBookmark,
            book = foundBook,
            quantity = bookmark['quantity'],
        )
        savedBookmark = self.__bookmarkRepository.save(newBookmark)
        return savedBookmark
    
    def listBookmark(self, accountId, page, pageSize):
        try:
            print(
                f"listBookmark() pageSize: {pageSize}"
            )

            # Account 확인
            account = self.__accountRepository.findById(accountId)
            if not account:
                raise ValueError(
                    f"Account with ID {accountId} not found."
                )
            print(f"Account found: {account}")

            # Bookmark 목록 가져오기(페이지네이션 적용된 결과)
            paginatedBookList = self.__bookmarkRepository.findBookmarkByAccount(
                account, page, pageSize
            )
            print(
                f"Paginated bookmark list query: {paginatedBookList}"
            )

            # 전체 도서 수 계산
            total_items = paginatedBookList.paginator.count # Paginator에서 count 값을 사용

            # 필요한 데이터만 추출
            bookmarkDataList = [
                {
                    "id": bookmark.bookmarkId,
                    "bookName": bookmark.bookName,
                    "bookImage": bookmark.bookIamge,
                    "quantity": bookmark.quantity,
                }
                for bookmark in paginatedBookList
            ]

            print(f"Total items: {total_items}")
            print(f"Page items: {len(bookmarkDataList)}")

            return bookmarkDataList, total_items
        
        except Exception as e:
            print(f"Unexpected error in listBookmark: {e}")
            raise
    
    def removeBookmark(self, accountId, bookmarkId):
        try:
            bookmark = self.__bookmarkRepository.findById(bookmarkId)
            print(f"bookmark: {bookmark}")
            if bookmark is None or str(bookmark.account.id) != str(accountId):
                return {
                    "error": "해당 북마크를 찾을 수 없거나 소유자가 일치하지 않습니다.",
                    "success": False,
                }
            
            result = self.__bookmarkRepository.deleteById(bookmarkId)
            if result:
                return {
                    "success": True,
                    "message": "북마크 항목이 삭제되었습니다.",
                }
        except Exception as e:
            print(
                f"Error in BookmarkService.removeBookmark: {e}"
            )
            return {
                "error": "서버 내부 오류",
                "success": False,
            }