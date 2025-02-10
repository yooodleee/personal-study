from django.db import models

from kakao_account.entity.account import Account
from subscription.entity.subscription import Subscription


class Payment(models.Model):
    paymentId = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='payments')
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='payments')

    def __str__(self):
        return f"Payment -> id: {self.paymentId}, account: {self.account.id}"
    
    class Meta:
        db_table = 'payment'
        app_label = 'payment'
    
    def getAccount(self):
        return self.account