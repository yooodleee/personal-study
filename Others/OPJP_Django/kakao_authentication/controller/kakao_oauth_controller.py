import uuid

# 뭔가 굉장히 임포트한 모듈이 많은 것 같지만 겁먹을 필요는 전혀 없습니다.
# 임포트한 부분을 자세히 살펴보기보다는 class 아래 부분을 더 자세하게 살펴봐야 하죠.
# 이처럼 임포트한 모듈이 굉장히 많다는 것은 우리가 생성해주었던 객체들을 많이 가져다 쓴다는 의미입니다.
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK

from kakao_account.service.account_service_impl import AccountServiceImpl
from kakao_account_profile.service.account_profile_service_impl import AccountProfileServiceImpl
from kakao_authentication.serializer.kakao_oauth_access_token_serializer import KakaoOauthAccessTokenSerializer
from kakao_authentication.service.kakao_oauth_service_impl import KakaoOauthServiceImpl
from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl


# 각각 getInstance(객체를 가져옵니다)를 하고 있습니다.
# 객체를 가져오는 이유는 각각의 변수명에서 대략 그 이유를 추측해볼 수 있습니다.
# 그러면 이러한 유추를 가지고 계속해서 아래 메서드를 살펴보도록 할까요?
class KakaoOauthcontroller(viewsets.ViewSet):
    # kakaoOauthService(카카오 권한 서비스)
    kakaoOauthService = KakaoOauthServiceImpl.getInstance()
    # accountService(계정 서비스)
    accountService = AccountServiceImpl.getInstance()
    # accountProfileService(계정 프로필 서비스)
    accountProfileService = AccountProfileServiceImpl.getInstance()
    # redisCacheService(레디스 캐시 서비스)-> 일단 이 부분은 아직 다루지 않았으므로 그냥 이런게 있구나~하고 넘어가셔도 될 것 같습니다.
    # redis_cache에 대한 설명은 나중에 다루도록 할게요.
    redisCacheService = RedisCacheServiceImpl.getInstance()

    # kakaoOauthLink(카카오 권한 링크)를 요청한다
    # 그렇다면 사용자가 카카오에 회원가입되면 권한이 있을 것 같네요.
    # 따라서, 사용자가 카카오의 회원인지를 요청하는 url을 보내고 있는 것 같네요.
    # 만약, 회원이라면 HTTP_200_OK(정상)을 반환해줍니다.
    def requestKakaoOauthLink(self, request):
        url = self.kakaoOauthService.requestKakaoOauthLink()

        return JsonResponse({"url": url}, status=status.HTTP_200_OK)
    
    # 접근 토큰을 요청하고 있습니다.
    def requestAccessToken(self, request):
        # 이전에 serializer에 대해 한 번 소개한 적인 있는 것 같은데요.
        # 다시 한 번 설명하자면, serializer는 데이터 변환과 검증을 담당하는 핵심 도구로, 특히 Django REST framework(DRF)에서 API
        # 개발 시 자주 사용됩니다.
        # 여기서 serializer는 요청한 데이터를 변환해주고 있는 것 같군요~(data-request.data)
        serializer = KakaoOauthAccessTokenSerializer(data=request.data)
        # 그리고 이 serializer가 타당한지를 보고 있는 것 같습니다.
        serializer.is_valid(raise_exception=True)
        # 일단 이 부분은 pass할게요~
        code = serializer.validated_data['code']

        try:
            # 토큰 요청을 통해 access_token을 받으려고 하고 있군요.
            tokenResponse = self.kakaoOauthService.requestAccessToken(code)
            accessToken = tokenResponse['access_token']

            # 트랜잭션은 작업의 단위를 의미합니다. 이때 atomic() 메서드를 적용해줌으로써 그 작업 단위를 더 작은 단위로 쪼개고 있군요.
            with transaction.atomic():
                # accessToken을 서버에 포함시켜 필요한 사용자 정보를 받아 줍니다.
                userInfo = self.kakaoOauthService.requestUserInfo(accessToken)
                # 사용자 정보에서 nickname을 얻습니다.
                nickname = userInfo.get('properties', {}).get('nickname', '')
                # email도 얻어주고 있군요.
                email = userInfo.get('kakao_account', {}).get('email', '')

                # 이번엔 사용자 정보로부터 획득한 email로 새로운 계정을 만들어주고 있네요.
                createdAccount = self.accountService.createAccount(email)
                # 새로 생성한 계정에서 Id와 nickname을 가져와 프로필을 만들어 줍니다.
                createdAccountProfile = self.accountProfileService.createAccountProfile(
                    createdAccount.getId(), nickname
                )

                # 만들어진 계정에 대한 고유한 토큰을 생성해줍니다.
                userToken = self.__createUserTokenWithAccessToken(createdAccount, accessToken)
            
            return JsonResponse({'userToken': userToken})
        
        # 만약, access_token을 받을 수 없다면 오류가 발생합니다.
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    # 새로 생성한 계정에 대한 토큰을 만들어주는 메서드네여.
    def __createUserTokenWithAccessToken(self, account, accessToken):
        try:
            # uuid의 uuid4는 쉽게 말해 id를 생성해주는데 랜덤하게 생성해준다고 생각하시면 됩니다.
            # 여기서는 Token을 랜덤하게 생성해준다고 할 수 있죠.
            userToken = str(uuid.uuid4())
            # 여기서 redis가 사용되고 있군요. 자세한 내용은 redis_cache에서 다루도록 할게요. 일단 pass~
            self.redisCacheService.storeKeyValue(account.getId(), accessToken)
            self.redisCacheService.storeKeyValue(userToken, account.getId())

            return userToken
        
        except Exception as e:
            print('Redis에 토큰 저장 중 에러:', e)
            raise RuntimeError('Redis에 토큰 저장 중 에러')