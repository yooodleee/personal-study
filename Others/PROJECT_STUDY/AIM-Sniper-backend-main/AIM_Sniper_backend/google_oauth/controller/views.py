import uuid

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.service.account_service_impl import AccountServiceImpl
from google_oauth.serializers.google_oauth_access_token_serializer import GoogleOauthAccessTokenSerializer
from google_oauth.serializers.google_oauth_url_serializer import GoogleOauthUrlSerializer
from google_oauth.service.google_oauth_service_impl import GoogleOauthServiceImpl
from redis_service.service.redis_service_impl import RedisServiceImpl


class GoogleOauthView(viewsets.ViewSet):
    googleOauthService = GoogleOauthServiceImpl.getInstance()
    RedisService = RedisServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()

    def googleOauthURI(self, request):
        # googleOuathService의 googlaLoginAddress 가져옴.
        url = self.googleOauthService.googleLoginAddress()
        print(f"url: ", url)
        # GoogleOauthUrlSerializer에서 'url'에 대한 data 가져오기
        serializer = GoogleOauthUrlSerializer(data={ 'url': url } )
        # serializer가 타당한 값인가?
        serializer.is_valid(raise_exception=True)
        print(f"validated_data: {serializer.validated_data}")
        return Response(serializer.validated_data)

    def googleAccessTokenURI(self, request):
        # GoogleOauthAccessTokenSerializer에 요청한 data
        serializer = GoogleOauthAccessTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['code']

        try:
            # googleOauthService의 code에 해당하는 requestAccessToken을 가져옴.
            accessToken = self.googleOauthService.requestAccessToken(code)
            print(f"accessToken : {accessToken}")
            return JsonResponse({'accessToken': accessToken})
        
        # code에 해당하는 requestAccessToken을 가져오지 못할 경우
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def googleUserInfoURI(self, request):
        # 'access_token'에 해당하는 data를 요청함.
        accessToken = request.data.get('access_token')
        print(f"accessToken: {accessToken}")

        try:
            # googleOauthService에서 accessToken에 해당하는 정보를 가져옴.
            user_info = self.googleOauthService.requestUserInfo(accessToken)
            return JsonResponse({'user_info': user_info})
        
        # 해당 정보를 가져올 수 없는 경우
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def redisAccessToken(self, request):
        try:
            # 'email'에 대한 정보를 요청함.
            email = request.data.get('email')
            print(f"googleRedisAccessToken -> email: {email}")
            account = self.accountService.findAccountByEmail(email)
            # email로 account를 찾을 수 없는 경우(account를 찾을 수 없음)
            if not account:
                return Response(
                    {'error': 'Account not found'}, 
                    status=status.HTTP_404_NOT_FOUND
                )

            userToken = str(uuid.uuid4())
            print(f"type of account.id: {type(account.id)}")
            self.RedisService.store_access_token(account.id, userToken)

            accountId = self.RedisService.getValueByKey(userToken)
            print(f"accountId: {accountId}")

            return Response(
                {'userToken': userToken}, 
                status=status.HTTP_200_OK
            )
        
        except Exception as e:
            print("Error storing access token in Redis:", e)
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def dropRedisTokenForLogout(self, request):
        try:
            userToken = request.data.get('userToken')
            isSuccess = self.RedisService.deleteKey(userToken)

            return Response(
                {'isSuccess': isSuccess}, 
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print(f'레디스 토큰 해제 중 에러 발생:', e)
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )











