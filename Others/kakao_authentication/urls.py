from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ..kakao_authentication.controller.kakao_oauth_controller import kakaoOauthController

router=DefaultRouter()
router.register(r"kakao-oauth", kakaoOauthController, basename="kakao-oauth")

urlpatterns= [
    path('', include(router.urls)),
    path('request-login-url', kakaoOauthController.as_view({ 'get': 'requestkakaoOauthLink'}), name='kakao Oauth 링크 요청'),
    path('redirect-access-token', kakaoOauthController.as_view({'post': 'requestAccessToken'}), name='kakao Access Token 요청'),
]