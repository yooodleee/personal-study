from abc import ABC, abstractmethod


# kakao_account, kakao_account_profile 도메인의 테이블만으로도
# kakao_authentication 도메인을 구성할 수 있을 것 같습니다.
# ddd의 가장 큰 장점은 특정 도메인의 기능을 재사용할 수 있다는 것이죠.
# 불필요하게 일일이 모델(테이블)을 필요에 따라 만들 수도, 안 만들 수도 있는 것입니다.
# kakao_authentication에서 왜 entity가 없는지는 kakao_authentication 도메인의 기능과 역할이 무엇인지를 자세하게 
# 살펴보아야 할 것 같습니다.
class KakaoOauthRepository(ABC):

    # 우선 권한(oauth)을 가져와서 부여하는 것 같네요.
    # 자세한 건 impl에서 확인!
    @abstractmethod
    def getOauthLink(self):
        pass

    # 접근 토큰도 가져오고 있는 것 같네요.
    # 토큰이 무엇인지는 impl에서 설명하도록 하겠습니다.
    @abstractmethod
    def getAccessToken(self, code):
        pass

    # 사용자에 대한 정보도 가져오고 있네요.
    # 인자를 유심히 살펴보면 accessToken(접근 토큰)을 가져옵니다.
    # 접근 토큰을 가져오는 이유 역시 impl에서 살펴봐야지 알 수 있을 것 같습니다.
    @abstractmethod
    def getUserInfo(self, accessToken):
        pass