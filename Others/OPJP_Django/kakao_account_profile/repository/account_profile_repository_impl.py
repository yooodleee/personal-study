from django.db import IntegrityError

from kakao_account_profile.entity.account_profile import AccountProfile
from kakao_account_profile.repository.account_profile_repository import AccountProfileRepository


class AccountProfileRepositoryImpl(AccountProfileRepository):
    # 싱글턴을 선언해줍니다.
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    # AccountProfile 테이블의 account(계정)와 nickname(별명) 객체를 등록해줍니다.
    def save(self, account, nickname):
        try:
            accountProfile = AccountProfile.objects.create(account=account, nickname=nickname)
            # 사실 더 정확한 건 이 라인에 accountProfile.save()를 해주는 게 더 정확하긴 하죠.
            # 제가 빼먹은 것 같습니다. ㅎㅎㅎ
            return accountProfile
        
        except IntegrityError:
            raise IntegrityError(f"Nickname '{nickname}' 이미 존재함.")