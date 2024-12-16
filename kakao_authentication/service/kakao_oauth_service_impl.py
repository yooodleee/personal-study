from repository.kakao_oauth_repository_impl import kakaoOauthRepositoryImpl
from service.kakao_oauth_service import kakaoOauthService

class kakaoOauthServiceImpl(kakaoOauthService):
    __inistance=None

    def __new__(cls):
        if cls.__inistance is None:
            cls.__inistance=super().__new__(cls)

            cls.__inistance.__kakaoOauthRepository=kakaoOauthRepositoryImpl.getInstance()
        
        return cls.__inistance
    
    @classmethod
    def getInstance(cls):
        if cls.__inistance is None:
            cls.__inistance=cls()
        
        return cls.__inistance
    
    def requestkakaoOauthLink(self):
        return self.__kakaOauthRepository.getOauthLink()
    
    def requestAccessToken(self, code):
        return self.__kakaoOauthRepository.getAccessToken(code)