from django.core.exceptions import ObjectDoesNotExist

# 우선 각각 임포트해준 모듈들이 상당히 많습니다.
# 그만큼 유기적이면서 복합적으로 서로 상호작용한다는 것을 알 수 있습니다.
# 개인적으로 이게 ddd 작업의 묘미가 아닐까 싶어요(물론 초반에는 이런 작업이 익숙하지 않다면 무엇을 임포트해야할지 어려워할 수 있지만)
# Account, AccountRoleType, RoleType, AccountRepositry를 임포트해주어 어떤 작업을 할 지 로직을 읽어봅시다.
from kakao_account.entity.account import Account
from kakao_account.entity.accout_role_type import AccountRoleType
from kakao_account.entity.role_type import RoleType
from kakao_account.repository.account_repository import AccountRepository


class AccountRepositoryImpl(AccountRepository):
    # 싱글턴 선언
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

    def save(self, email):
        # defaultRolleType, created 객체를 동시에 생성해주었어요. 만약 각각 생성해준다면
        # defaultRoleType = AccountRoleType.objects.get_or_create(roleType=RoleType.NORMAL)
        # created = AccountRoleType.objects.get_or_create(roleType=RoleType.NORMAL)
        # 이렇게 같은 작업을 두 번 해야되는데 동시에 생성해줌으로써 번거로움을 줄일 수 있죠.
        # AccountRoleType 테이블에서 RoleType의 NORMAL(일반 고객)에 대한 정보를 가져오는 것 같습니다.
        defaultRoleType, created = AccountRoleType.objects.get_or_create(roleType=RoleType.NORMAL)

        # Account 테이블에서 email과 roleType(관리자인지, 일반 고객인지와 어떤 구독권을 등록했는지)를 가져와 계정 정보에 등록해줍니다.
        account = Account(email=email, roleType=defaultRoleType)
        # 계정 정보에 필요한 정보들을 담아왔으니 저장도 해줄게요(save)
        account.save()
        return account
    
    # Account 테이블에서 사용자 ID를 가져오려는 작업을 하는 것 같습니다.
    # 하지만 만약 사용자 ID가 존재하지 않는다면 오류가 발생한 것이므로 "Account ID 존재하지 않음"을 출력해줍니다.
    # 그런데 생각을 한 번 해봅시다. 
    # 장고에서는 테이블(모델)을 만들면 자동으로 ID 값을 생성해준다고 했었습니다.
    # 그런데 굳이 사용자 ID가 없다고 가정하는 오류 상황을 가정할 필요가 있을까요?
    # 이것은 예외 처리라는 파이썬 문법을 살짝 다룰 필요가 있습니다.
    # 일반적으로 우리가 로직을 쓸 때 모든 작업이 순탄하게 흐를 것이라고 생각합니다.
    # 하지만 우리가 쓴 로직에는 생각보다 허점이 많습니다.
    # 컴퓨터는 우리가 쓴 로직대로만 작업을 처리하기 때문에 생각보다 멍청하죠.
    # 그래서 장고에서 자동으로 ID를 생성해준다고 할지라도 혹시라도 모르니 ID가 존재하지 않는다면~ 이라는 오류 사항을 가정하고
    # 이에 대한 예외 처리를 적어줍니다.
    # 그래서 일반적인 로직 흐름 뿐만 아니라 정상적인 흐름을 처리하지 못했을 때를 대비하여 예외 처리 작업도 같이 써주는 게 
    # 훨씬 더 안정성이 높아지는 것이죠.
    def findById(self, accountId):
        try:
            return Account.objects.get(id=accountId)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist(f"Account ID {accountId} 존재하지 않음.")