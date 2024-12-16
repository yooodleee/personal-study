import requests

from db_automation import settings
from kakao_authentication.repository.kakao_oauth_repository import kakaOauthRepository


class kakaoOauthRepositoryImpl(kakaOauthRepository):
    __instance=None

    def __new__(cls):
        if cls.__instance is None:

            cls.__instance.loginUrl=settings.KAKAO["LOGIN_URL"]
            cls.__instance.clientId=settings.KAKAO["CLIENT_ID"]
            cls.__instance.redirectUri=settings.KAKAO["REDIRECT_URI"]
            cls.__instance.tokenRequestUri=settings