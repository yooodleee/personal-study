from django.urls import path, include
from rest_framework.routers import DefaultRouter

from kakao_authentication.controller.kakao_oauth_controller import KakaoOauthcontroller

router = DefaultRouter()
router.register(r"kakao-oauth", KakaoOauthcontroller, basename='kakao-oauth')

urlpatterns = [
    path('', include(router.urls)),
    path('request-login-url', KakaoOauthcontroller.as_view({ 'get': 'requestKakaoOauthLink' }), name='Kakao Oauth 링크 요청'),
    path('redirect-access-token', KakaoOauthcontroller.as_view({ 'post': 'requestAccessToken' }), name='Kakao Access Token 요청'),
]