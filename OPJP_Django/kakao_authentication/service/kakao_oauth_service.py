from abc import ABC, abstractmethod


# repository에서와 거의 유사한 메서드명을 사용하고 있군요!
# 단지 차이점은 service는 실제로 request(요청)을 하는 역할을 수행할 것 같습니다.
# 그렇다면 accessToken을 서버에 보내겠네요~
class KakaoOauthService(ABC):

    @abstractmethod
    def requestKakaoOauthLink(self):
        pass

    @abstractmethod
    def requestAccessToken(self, code):
        pass

    @abstractmethod
    def requestUserInfo(self, accessToken):
        pass