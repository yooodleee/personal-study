from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK

from seriallizer.kakao_oauth_access_token_serializer import kakaoOauthAccessTokenSerializer
from service.kakao_oauth_service_impl import kakaoOauthServiceImpl

class kakaoOauthController(viewsets.ViewSet):
    kakaoOauthService=kakaoOauthServiceImpl.getInstance()

    def resquestkakaoOauthLink(self, request):
        url=self.kakaoOauthService.requestkakaoOauthLink()

        return JsonResponse({"url": url}, status=status.HTTP_200_OK)

    def requestAccessToken(self, request):
        serializer=kakaoOauthAccessTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code=serializer.validated_data['code']

        try:
            accessToken=self.kakaoOauthService.requestAccessToken(code)
            print(f"accessToken: {accessToken}")
            return JsonResponse({'accessToken': accessToken})
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)