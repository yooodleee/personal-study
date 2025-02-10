from kakao_authentication.repository.kakao_oauth_repository_impl import KakaoOauthRepositoryImpl
from kakao_authentication.service.kakao_oauth_service import KakaoOauthService


class KakaoOauthServiceImpl(KakaoOauthService):
    # 싱글턴 선언언
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__kakaoOauthRepository = KakaoOauthRepositoryImpl.getInstance()
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    # 우리가 Repository에서 생성해주었던 객체들을 필요에 따라 가져와주고 있습니다.
    # 각각 getOauthLink(), getAccessToken(), getUserInfo()로 보아 권한 링크 가져오고, 접근 토큰 가져오고, 사용자 정보를 가져오는 것 같군요.
    def requestKakaoOauthLink(self):
        return self.__kakaoOauthRepository.getOauthLink()
    
    def requestAccessToken(self, code):
        return self.__kakaoOauthRepository.getAccessToken(code)
    
    def requestUserInfo(self, accessToken):
        return self.__kakaoOauthRepository.getUserInfo(accessToken)