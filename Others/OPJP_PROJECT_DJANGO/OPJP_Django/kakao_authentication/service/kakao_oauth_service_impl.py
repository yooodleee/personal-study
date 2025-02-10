from kakao_authentication.repository.kakao_oauth_repository_impl import KakaoOauthRepositoryImpl
from kakao_authentication.service.kakao_oauth_service import KakaoOauthService


class KakaoOauthServiceImpl(KakaoOauthService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__KakaoOauthRepository = KakaoOauthRepositoryImpl.getInstance()

        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    def requestKakaoOauthLink(self):
        return self.__KakaoOauthRepository.getOauthLink()
    
    def requestAccessToken(self, code):
        return self.__KakaoOauthRepository.getAccessToken(code)
    
    def requestUserInfo(self, accessToken):
        return self.__KakaoOauthRepository.getUserInfo(accessToken)