from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from bookmark.service.bookmark_service_impl import BookmarkServiceImpl

from kakao_authentication.service.kakao_oauth_service_impl import KakaoOauthServiceImpl


class BookmarkViews(viewsets.ViewSet):
    bookmarkService = BookmarkServiceImpl.getInstance()
    redisService = KakaoOauthServiceImpl.getInstance()

    def bookmarkItemList(self, request):
        data = request.data
        userToken = data.get('userToken')

        if not userToken:
            return Response({'error': 'User token is required'}, status=status.HTTP_400_BAD_REQUEST)

        accountId = self.redisService.getValueByKey(userToken)
        if not accountId:
            return Response({'error': 'Invalid user token'}, status=status.HTTP_400_BAD_REQUEST)
        
        bookmarkItemListResponseForm = self.bookmarkService.bookmarkList(accountId)
        return Response(bookmarkItemListResponseForm, status=status.HTTP_200_OK)
    
    def bookmarkRegister(self, request):
        try:
            data = request.data
            print('data:', data)

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            self.bookmarkService.bookmarkRegister(data, accountId)
            return Response(status=status.HTTP_200_OK)
        
        except Exception as e:
            print('북마크 등록 과정 중 문제 발생:', e)
            return Response({ 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def removeBookmarkItem(self, request):
        try:
            data = request.data
            if list(data.keys())[0] == 'BookmarkItemId':
                bookmarkItemId = data['BookmarkItemId']
                self.bookmarkService.removeBookmarkItem(bookmarkItemId)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print("북마크 정리 중 에러 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)