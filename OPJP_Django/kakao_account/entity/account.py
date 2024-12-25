# kakao_account에서 테이블을 굳이 나눈 이유는 무엇일까요?
# 우선 kakao_account 도메인의 역할에 대해서 생각해봅시다.
# 도메인 이름 그대로 카카오톡 계정에 대한 정보를 다룰 것 같습니다.
# 계정 도메인에 필요한 테이블을 3개로 나누었는데 각각의 역할이 있는 것 같습니다.
# 우선, account는 말 그대로 계정에 필요한 정보들이 담겨 있겠네요. 자세한 건 클래스를 살펴보도록 하겠습니다.

from django.db import models
# AccountRoleType 테이블에서 필요한 정보를 가져오는 것 같습니다.
from kakao_account.entity.accout_role_type import AccountRoleType


class Account(models.Model):
    # id는 테이블의 고유한 값이자, 식별되는 값이죠. 아래 메서드(getId)가 있는 것으로 보아 이 id를 이용해서
    # 필요한 작업이 있다는 것을 예상해볼 수 있습니다.
    id = models.AutoField(primary_key=True)
    # 계정에 필요한 첫 번째 객체(정보)로는 email을 적어주었군요. 
    # 추후에 우리가 필요한 정보들을 적어줄 수도 있을 것 같습니다(예컨대 성별, 나이대, 이름 등등)
    email = models.CharField(max_length=32)
    # roleType이 여기서 쓰여졌군요.
    # 계정에 필요한 정보가 관리자인지, 일반 고객인지, 결제한 구독권은 무엇인지를 나타내주는 것 같습니다.
    roleType = models.ForeignKey(AccountRoleType, on_delete=models.CASCADE)

    class Meta:
        db_table = 'account'
        app_label = 'account'
    
    def getId(self):
        return self.id