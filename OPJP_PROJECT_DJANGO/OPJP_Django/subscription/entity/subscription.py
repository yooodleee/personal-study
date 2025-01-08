from django.db import models


# Create your models here.
class Subscription(models.Model):
    subscriptionId = models.AutoField(primary_key=True)
    subscriptionName = models.CharField(max_length=128, name=False)
    subscriptionDescription = models.TextField()
    subscriptionImage = models.CharField(max_length=100, null=True)

    # 추후 이미지 관련 필드 추가
    registeredDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Subscription {self.subscriptionName} ({self.subscriptionDescription})"
    
    def getId(self):
        return self.subscriptionId
    
    class Meta:
        db_table = 'subscription'
        app_label = 'subscription'