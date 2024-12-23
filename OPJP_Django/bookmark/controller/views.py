# render는 html을 활용하여 response(반응)를 생성하는 메서드입니다.
# django는 앱 폴더 내부에 templates 폴더 내부에서 html 파일을 찾는데, 이를 위해 해당 폴더 및 html 파일을 만들어주어야 합니다.
# 자세한 내용은 -> https://inuplace.tistory.com/589
from django.shortcuts import render
# Django REST Framework는 Django 프로젝트에서 RESTful API를 구축하기 위한 필수 도구입니다.
# 이 도구는 유연한 툴킷을 제공해주어 웹 API의 개발을 단순화하고 관리 및 보안하는 데 도움을 줍니다.
from rest_framework import viewsets, status
from rest_framework.response import Response

# 이 모듈을 임포트하는 이유를 생각해봅시다(BookmarkServiceImpl 클래스에서 구현했던 메서드들의 기능을 떠올려보아요)
from bookmark.service.bookmark_service_impl import BookmarkServiceImpl

# 이 모듈을 임포트하는 이유를 생각해봅시다(kakaoOauthServiceImpl 클래스에서 구현했던 메서드들의 기능을 떠올려보아요)
from kakao_authentication.service.kakao_oauth_service_impl import KakaoOauthServiceImpl



class BookmarkViews(viewsets.ViewSet):
    # bookmarkServiceImpl에서 생성했던 객체들을 가져옵니다(getInstance())
    bookmarkService = BookmarkServiceImpl.getInstance()
    # KakaoOauthServiceImpl에서 생성했던 객체들을 가져옵니다(getInstance())
    redisService = KakaoOauthServiceImpl.getInstance()

    # bookmarkItemList 이 부분은 로직이 조금 잘못된 것 같네요.
    # (나중에 같이 의논해보면서 수정하면 좋을 것 같아요-> 이 메서드는 pass!)
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
    
    # 요 메서드도 일단 pass할게요~
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
        # data(정보)를 요청합니다.
        try:
            data = request.data
            # data의 key들로 이루어진 리스트의 첫 번째 값이 'BookmarkItemId'라면
            if list(data.keys())[0] == 'BookmarkItemId':
                # bookmarkItemId에 'BookmarkItemId'에 대한 정보를 넣어줍니다.
                bookmarkItemId = data['BookmarkItemId']
                # 이 부분은 일단 pass할게요.
                self.bookmarkService.removeBookmarkItem(bookmarkItemId)
            # bookmarkItemId에 대한 정보를 정상적으로 처리했으므로 HTTP_200_OK(정상) 출력합니다.
            return Response(status=status.HTTP_200_OK)
        # 만약 북마크 정리 중 에러가 발생하면 HTTP_400_BAD_REQUEST를 반환합니다(비정상 오류류)
        except Exception as e:
            print("북마크 정리 중 에러 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)