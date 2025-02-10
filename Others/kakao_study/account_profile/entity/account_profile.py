from django.db import models

from accout.entity.account import  Account


class AccountProfile(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=32, unique=True)
    account = models.oneToOneField(
        Account,
        on_delete = models.CASCADE,
        related_name = "profile"
    )

    class Meta:
        db_table = 'account_profile'
        app_label = 'account_profile'