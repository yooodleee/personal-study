import requests

from OPJP_Django import settings
from kakao_authentication.repository.kakao_oauth_repository import KakaoOauthRepository


class KakaoOauthRepositoryImpl(KakaoOauthRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.loginUrl = settings.KAKAO['LOGIN_URL']
            cls.__instance.clientId = settings.KAKAO['CLIENT_ID']
            cls.__instance.redirectUri = settings.KAKAO['REDIRECT_URI']
            cls.__instance.tokenRequestUri = settings.KAKAO['TOKEN_REQUEST_URI']
            cls.__instance.userInfoRequestUri = settings.KAKAO['USER_INFO_REQUEST_URI']
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    def getOauthLink(self):
        print("getOauthLink() for Login")

        return (f"{self.loginUrl}/oauth/authorize?"
                f"client_id={self.clientId}&redirect_uri={self.redirectUri}&response_type=code")
    
    def getAccessToken(self, code):
        accesstokenRequest = {
            'grant_type': 'authorize_code',
            'client_id': self.clientId,
            'redirect_uri': self.redirectUri,
            'code': code,
            'client_secret': None
        }

        response = requests.post(self.tokenRequestUri, data=accesstokenRequest)
        return response.json()
    
    def getUserInfo(self, accessToken):
        headers = {'Authorization': f"Bearer {accessToken}"}
        response = requests.post(self.userInfoRequestUri, headers=headers)
        return response.json()