from django.db import models


class Subscription(models.Model):
    subscriptionId = models.AutoField(primary_key=True)
    subscriptionName = models.CharField(max_length=128, null=False)
    subscriptionDescription = models.TextField()
    subscriptionPrice = models.DecimalField(max_digits=10, decimal_places=0)
    subscriptionImage = models.CharField(max_length=100, null=True)

    # 추후 이미지 관련 필드 추가
    registeredDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def getId(self):
        return self.subscriptionId
    
    class Meta:
        db_table = 'subscription'
        app_label = 'subscription'