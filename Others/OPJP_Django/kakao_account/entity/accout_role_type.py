from django.db import models
# RoleType 테이블에 각각 관리자, 고객, 구독권에 대한 정보가 담겨져 있었죠?
# RoleType에서 필요한 정보가 있는 것 같군요. 한 번 살펴보도록 하겠습니다.
from kakao_account.entity.role_type import RoleType


# AccountRoleType (계정 역할 타입?유형?)
# 아마도 우리가 RoleType에서 생성해주었던 객체들(관리자, 고객, 구독권)을 유형별로 나누어 
# 추후에 관리자 별, 고객 별, 구독권 별로 필요한 정보를 매핑할 것 같습니다.
class AccountRoleType(models.Model):
    roleType = models.CharField(max_length=64, choices=RoleType.choices, default=RoleType.NORMAL)

    # __str__은  그 반환값이 문자열이라고 했었죠?
    # roleType을 문자열로 반환해줍니다.
    def __str__(self):
        return self.roleType
    
    class Meta:
        db_table = 'account_role_type'
        app_label = 'account'