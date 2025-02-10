from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status

from bookmark.service.bookmark_service_impl import BookmarkServiceImpl
from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl


# Create your views here.
class BookmarkController(viewsets.ViewSet):
    redisCacheService = RedisCacheServiceImpl.getInstance()
    bookmarkService = BookmarkServiceImpl.getInstance()

    def requestCreateBookmark(self, request):
        postRequest = request.data
        bookmark = postRequest.get("bookmark")
        userToken = postRequest.get("userToken")

        if not userToken:
            return JsonResponse(
                {"error": "userToken이 필요합니다.", "success": False},
                status = status.HTTP_400_BAD_REQUEST,
            )
        try:
            accountId = self.redisCacheService.getValueByKey(userToken)

            updatedBookmark = self.bookmarkService.createBookmark(
                accountId, bookmark
            )
            if updatedBookmark is not None:
                return JsonResponse(
                    {"message": "북마크에 도서가 추가되었습니다.", "success": True},
                    status = status.HTTP_200_OK,
                )
        
        except Exception as e:
            print(f"북마크 처리 중 오류 발생: {e}")
            return JsonResponse(
                {"error": "서버 내부 오류", "success": False},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    
    def requestListBookmark(self, request):
        postRequest = request.data
        userToken = postRequest.get("userToken")

        page = postRequest.get("page", 1)
        perPage = postRequest.get("perPage", 10)

        if not userToken:
            return JsonResponse(
                {"error": "userToken이 필요합니다.", "success": False},
                status = status.HTTP_400_BAD_REQUEST,
            )
        try:
            accountId = self.redisCacheService.getValueByKey(userToken)

            bookmarkList, totalItems = self.bookmarkService.listBookmark(
                accountId, page, perPage
            )
            print(f"bookmarkList: {bookmarkList}, totalItems: {totalItems}")

            return JsonResponse({
                "bookmarkList": bookmarkList,
                "totalItems": totalItems,
                "success": True,
            }, status = status.HTTP_200_OK)
        
        except Exception as e:
            return JsonResponse(
                {"error": "서버 내부 오류", "success": False},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    
    def requestRemoveBookmark(self, request):
        postRequest = request.data
        userToken = postRequest.get("userToken")
        bookmarkId = postRequest.get("id")

        if not userToken:
            return JsonResponse(
                {"error": "userToken이 필요합니다.", "success": False},
                status = status.HTTP_400_BAD_REQUEST,
            )
        
        try:
            accountId = self.redisCacheService.getValueByKey(userToken)
            result = self.bookmarkService.removeBookmark(accountId, bookmarkId)

            if result["success"]:
                return JsonResponse(
                    result, status = status.HTTP_200_OK
                )
            else:
                return JsonResponse(
                    result, status = status.HTTP_400_BAD_REQUEST
                )
        
        except Exception as e:
            return JsonResponse(
                {"error": "서버 내부 오류", "success": False},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR,
            )