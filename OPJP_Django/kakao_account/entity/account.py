from django.db import models
from kakao_account.entity.accout_role_type import AccountRoleType


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=32)
    roleType = models.ForeignKey(AccountRoleType, on_delete=models.CASCADE)

    class Meta:
        db_table = 'account'
        app_label = 'account'
    
    def getId(self):
        return self.id