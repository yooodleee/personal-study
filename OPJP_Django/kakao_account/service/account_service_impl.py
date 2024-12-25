from kakao_account.repository.account_repository_impl import AccountRepositoryImpl
from kakao_account.service.account_service import AccountService


class AccountServiceImpl(AccountService):
    # 싱글턴을 선언해줍니다.
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            # AccountRepositoryImpl 테이블에서 필요한 객체를 가져옵니다.
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
        
        return cls.__instance
    

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    # AccountRepositoryImpl 테이블에서 필요에 따라 가져온 정보들을 save 등록해줍니다.
    def createAccount(self, email):
        return self.__accountRepository.save(email)