from django.db import models
from kakao_account.entity.account import Account

# 프로필에 필요한 정보들은 무엇이 있을까요? 
# 생각해보면서 밑에 생성해준 테이블의 구성을 살펴보도록 하겠습니다.
class AccountProfile(models.Model):
    # 우선 차례대로 id, nickname(별명), account로 구성되어 있네요.
    # account는 Kakao_account 도메인에서 참조하는 방법도 있을 것 같습니다(이건 나중에 한 번 다같이 생각해보면 좋을 것 같네요).
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=32, unique=True)
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    class Meta:
        db_table = "account_profile"
        app_label = "account_profile"