import requests

# Django REST Framework(DRF)에서 인증(Authentication)과 권한 부여(Authorization)는 클라이언트의 신원을 확인하는 과정인 인증과,
# 인증된 클라이언트가 무엇을 할 수 있는지 결정하는 과정인 권한 부여를 의미합니다.
# DRF는 인증과 권한 부여를 처리하기 위한 견고하고 유연한 시스템을 제공합니다.
# 기본적으로 DRF는 간단한 권한 정책을 적용합니다. 인증되지 않은 요청은 읽기 전용 접근으로 허용하며, 인증된 요청은 전체 읽기-쓰기 접근을 허용합니다.
# 다음은 토큰 기반 Authentication(인증) 기법의 개요입니다.

# (1) 사용자 인증: 사용자는 자격 증명(사용자 이름 및 비밀번호)을 서버에 제공합니다.
# (2) 서버 인증: 서버는 사용자의 자격 증명을 서버 내의 저장된 데이터 베이스와 대조해 검증하고, 토큰을 생성합니다.
# (3) 토큰 생성: 서버는 인증된 사용자를 위해 고유한 토큰을 생성합니다. 이 토큰에는 사용자의 신원 및 권한과 같은 정보가 암호화되어 저장됩니다.
# (4) 토큰 저장: 서버는 생성된 토큰을 서버 또는 클라이언트 측에 저장합니다.
# (5) 토큰 발급: 서버는 생성된 토큰을 클라이언트에게 보내줍니다(일반적으로 인증 요청에 대한 응답으로).
# (6) 토큰 사용: 클라이언트는 이후 요청에서 토큰을 서버에 포함시킵니다.
# (7) 토큰 유효성 검증: 각 요청마다 서버는 받은 토큰을 검증하여 그의 진위와 무결성을 확인합니다.
# (8) 접근 제어: 유효한 토큰을 기반으로 서버는 보호된 리소스에 대한 접근을 허용하거나 거부하며, 권한 관련 규칙을 시행합니다. 

from OPJP_Django import settings
from kakao_authentication.repository.kakao_oauth_repository import KakaoOauthRepository


class KakaoOauthRepositoryImpl(KakaoOauthRepository):
    # 싱글턴을 선언해줍니다.
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            # settings에서 LOGIN_URL(로그인 요청 시 서버로 보내지는 URL)이 필요한 것 같군요.
            cls.__instance.loginUrl = settings.KAKAO['LOGIN_URL']
            # settings에서 CLIENT_ID(고객 아이디-> 사용자 아이디)도 필요한 것 같습니다.
            cls.__instance.clientId = settings.KAKAO['CLIENT_ID']
            # settings에서 REDIRECT_URI (재접근 URI)도 가져옵니다.
            # URI과 URL은 장고에서 거의 같다고 보셔도 무방합니다.
            # 차이점은 URI은 식별하고, URL은 위치를 가르킵니다.
            cls.__instance.redirectUri = settings.KAKAO['REDIRECT_URI']
            # TOKEN_REQUEST_URI(토큰 요청 URI)도 가져오고 있군요.
            cls.__instance.tokenRequestUri = settings.KAKAO['TOKEN_REQUEST_URI']
            # USER_INFO_REQUEST_URI(사용자 정보 요청 URI)도 가져오고 있습니다.
            cls.__instance.userInfoRequestUri = settings.KAKAO['USER_INFO_REQUEST_URI']
        
        return cls.__instance
    
    @classmethod
    # 필요한 객체들을 가져와줍니다.
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    def getOauthLink(self):
        print("getOauthLink() for Login")

        # Login을 할 때 우선 loginUrl(로그인 요청)을 보냅니다.
        # 그러면 TOKEN_REQUEST_URI, USER_INFO_REQUEST_URI 요청에 의해 각각 CLIENT_ID(사용자 아이디), REDIRECT_URI(재접근 URI)를 반환하겠군요.
        # 아래 return 문은 단순히 ""(따옴표) 안의 문장을 출력해주고 있습니다.
        # 토큰을 어떻게 처리할 것인지는 아래의 메서드 getAccessToken에서 처리하고 있는 것 같으니 살펴보도록 할까요?
        return (f"{self.loginUrl}/oauth/authorize?"
                f"client_id={self.clientId}&redirect_uri={self.redirectUri}&response_type=code")
    
    # accesstokenRequest 딕셔너리를 살펴보면 grant_type(권한 타입-> 일반 고객인지 아닌지), client_id(고객 아이디)
    # redirect_uri(재접근 URI)를 담고 있습니다.
    # code와 client_secret은 현재 없어도 될 것 같네요. 일단 pass 할게요!
    def getAccessToken(self, code):
        accesstokenRequest = {
            'grant_type': 'authorize_code',
            'client_id': self.clientId,
            'redirect_uri': self.redirectUri,
            'code': code,
            'client_secret': None
        }

        # 인층 요청에 대한 응답이군요.
        # tokenRequestUri(토큰 요청 URI와 accesstokenReuqest(접근 토큰 요청)에 대한 응답)인 것 같습니다.
        response = requests.post(self.tokenRequestUri, data=accesstokenRequest)
        # 응답을 json 형태로 반환하는 것 같습니다.
        return response.json()
    
    # 클라이언트는 일반적으로 요청에서 토큰을 서버에 포함시키는데, Authorization 헤더나 쿼리 매개변수로 전달됩니다.
    # header에서 역시 accessToken을 포함하고 있는 것을 확인할 수 있죠~
    def getUserInfo(self, accessToken):
        headers = {'Authorization': f"Bearer {accessToken}"}
        # userInfoRequestUri(사용자 정보 요청 URI)와 헤더(accessToken 포함)에 대한 응답인 것 같군요.
        response = requests.post(self.userInfoRequestUri, headers=headers)
        return response.json()