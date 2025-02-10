from kakao_account.repository.account_repository_impl import AccountRepositoryImpl
from kakao_account_profile.repository.account_profile_repository_impl import AccountProfileRepositoryImpl
from kakao_account_profile.service.account_profile_service import AccountProfileService


class AccountProfileServiceImpl(AccountProfileService):
    # 싱글턴 선언언
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            # 각각 AccountProfileRepositoryImpl, AccountrepositoryImpl 테이블에서 필요한 객체들을 가져옵니다.
            cls.__instance.__accountProfileRepository = AccountProfileRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
    
    def createAccountProfile(self, accountId, nickname):
        # 서비스에 등록되는 account(계정)이 한 두개가 아닐 겁니다(단순히 한 두명을 운영하는 서버가 아니라는 뜻이죠)
        # 각 사용자들을 id로 식별하기 위해 findById 메서드를 적극 활용해줍니다.
        # 이러면 각 사용자에 대한 계정을 구별할 수 있겠죠(A는 A에 대한 고유 계정, b는 b에 대한 고유 계정...)
        account = self.__accountRepository.findById(accountId)
        # account, nickname을 accountProfileRepository에서 가져와서 profile에 저장해줄게요.
        savedAccountProfile = self.__accountProfileRepository.save(account, nickname)
        # 만약 필요한 정보들(account, nickname)이 잘 저장되었다면 True(참)
        if savedAccountProfile is not None:
            return True
        
        # 잘 저장되지 않았더라면 False(거짓)
        return False