import requests

from db_automation import settings
from repository.kakao_oauth_repository import kakaOauthRepository


class kakaoOauthRepositoryImpl(kakaOauthRepository):
    __instance=None

    def __new__(cls):
        if cls.__instance is None:

            cls.__instance.loginUrl=settings.KAKAO["LOGIN_URL"]
            cls.__instance.clientId=settings.KAKAO["CLIENT_ID"]
            cls.__instance.redirectUri=settings.KAKAO["REDIRECT_URI"]
            cls.__instance.tokenRequestUri=settings.KAKAO["TOKEN_REQUEST_URI"]
            cls.__instance.userInfoRequestUri=settings.KAKAO["USER_INFO_URI"]

        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance=cls()
        
        return cls.__instance
    
    def getOauthLink(self):
        print("getOauthLink() for Login")

        return (f"{self.loginUrl}/oauth/authorize?"
                f"client_id={self.clinetId}&redirect_uri={self.redirectUri}&response_type=code")
    
    def getAccessToken(self, code):
        accessTokenRequest= {
            'grant_type': 'authorization_code',
            'clinet_id': self.clientId,
            'redirect_url': self.redirectUri,
            'code': code,
            'client_secret': None
        }

        response=requests.post(self.tokenRequestUri, data=accessTokenRequest)
        return response.json()
    
    