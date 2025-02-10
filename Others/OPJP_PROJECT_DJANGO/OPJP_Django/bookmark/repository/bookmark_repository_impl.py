from django.core.paginator import EmptyPage, Paginator
from django.db.models import Subquery, OuterRef, Value
from django.db.models.functions import Coalesce

from bookmark.entity.bookmark import BookMark
from bookmark.repository.bookmark_repository import BookmarkRepository
from books.entity.books import Books


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
    
    def save(self, bookmark):
        try:
            if bookmark.getId():
                existingBookmark = BookMark.objects.get(id=bookmark.bookmarkId)
                existingBookmark.quantity = bookmark.quantity # 수량 업데이트
                existingBookmark.save()
                return existingBookmark
            
            new_bookmark = BookMark.objects.create(
                account = bookmark.account,
                bookmarkName = bookmark.bookmarkName,
                bookmarkImage = bookmark.bookmarkImage,
                quantity = bookmark.quantity,
            )
            return new_bookmark
        except Exception as e:
            print(f"북마크 저장 중 오류 발생: {e}")
            raise
    
    def findBookmarkByAccount(self, account, bookmark):
        try:
            bookmark = BookMark.objects.get(
                account = account,
                bookmark = bookmark,
            )
            return bookmark
        
        except BookMark.DoesNotExist:
            print("오류: 조건에 만족하는 북마크가 여러 개 존재합니다.")
            return None
        
        except Exception as e:
            print(f"북마크 조회 중 오류 발생: {e}")
            return None
    
    def findById(self, bookmarkId):
        try:
            bookmark = BookMark.objects.get(id = bookmarkId)    # id로 단일 Bookmark 조회
            return bookmark
        except BookMark.DoesNotExist:
            print(f"id {bookmarkId} 존재하지 않음")
            return None
        except Exception as e:
            print(f"BookRepository.findById 에러: {e}")
            return None
    
    def deleteById(self, bookmarkId):
        try:
            bookmark = BookMark.objects.filter(id = bookmarkId).first()
            if not bookmark:
                return False
            bookmark.delete()
            return True
        except Exception as e:
            print(f"Error in BookRepository.deleteById: {e}")
            return False