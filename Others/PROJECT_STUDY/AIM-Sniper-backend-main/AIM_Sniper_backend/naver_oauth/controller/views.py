import uuid
from urllib import parse
import json
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.service.account_service_impl import AccountServiceImpl
from naver_oauth.serializer.naver_oauth_access_token_serializer import NaverOauthAccessTokenSerializer
from naver_oauth.serializer.naver_oauth_url_serializer import NaverOauthUrlSerializer
from naver_oauth.service.naver_oauth_service_impl import NaverOauthServiceImpl
from redis_service.service.redis_service_impl import RedisServiceImpl


class NaverOauthView(viewsets.ViewSet):
    naverOauthService = NaverOauthServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()

    def naverOauthURI(self, request):
        url = self.naverOauthService.naverLoginAddress()
        print(f"url:", url)
        serializer = NaverOauthUrlSerializer(data={ 'url': url })
        serializer.is_valid(raise_exception=True)
        print(f"validated_data: {serializer.validated_data}")
        return Response(serializer.validated_data)

    def naverAccessTokenURI(self, request):
        serializer = NaverOauthAccessTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['code']

        try:
            accessToken = self.naverOauthService.requestNaverAccessToken(code)
            print(f"accessToken: {accessToken}")
            return JsonResponse(
                {'accessToken': accessToken}
            )
        
        except Exception as e:
            return JsonResponse(
                {'error': str(e)}, 
                status=500
            )
        
    def naverUserInfoURI(self, request):
        naverAccessToken = request.data.get('access_token')
        print(f'naverOauthService: {naverAccessToken}')

        try:
            user_info = self.naverOauthService.requestUserInfo(
                naverAccessToken
            )
            return JsonResponse({'user_info': user_info})
        
        except Exception as e:
            return JsonResponse(
                {'error': str(e)}, 
                status=500
            )

    def redisAccessToken(self, request):
        try:
            # request.data에서 email 가져오기
            email = request.data.get('email')

            # email 출력 확인
            print("111111111111111", email)
            print(f"redisAccessToken -> email: {email}")

            # 이메일을 통해 계정 찾기
            account = self.accountService.findAccountByEmail(email)
            if not account:
                return Response(
                    {'error': 'Account not found'}, 
                    status=status.HTTP_404_NOT_FOUND
                )

            # userToken 생성
            userToken = str(uuid.uuid4())
            print(f"type of account.id: {type(account.id)}")

            # Redis에 userToken 저장
            self.redisService.store_access_token(account.id, userToken)

            # key로 value 찾기 테스트
            accountId = self.redisService.getValueByKey(userToken)
            print(f"accountId: {accountId}")

            return Response(
                {'userToken': userToken}, 
                status=status.HTTP_200_OK
            )

        except Exception as e:
            print('Error storing access token in Redis:', e)
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def dropRedisTokenForLogout(self, request):
        try:
            userToken = request.data.get('userToken')
            isSuccess = self.redisService.deleteKey(userToken)

            return Response(
                {'isSuccess': isSuccess}, 
                status=status.HTTP_200_OK
            )
        
        except Exception as e:
            print('레디스 토큰 해제 중 에러 발생:', e)
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )