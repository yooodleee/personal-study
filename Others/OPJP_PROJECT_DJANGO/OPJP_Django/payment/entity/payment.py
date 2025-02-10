from django.db import models

from account.entity.account import Account


# Create your models here.
class Payment(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='payment'
    )
    paymentKey = models.CharField(max_length=255)   # 결제 키
    orderId = models.CharField(max_length=255)  # 주문 ID
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # 결제 금액
    provider = models.CharField(max_length=100) # 결제 제공자
    method = models.CharField(max_length=100)   # 결제 방법
    paid_at = models.DateTimeField()    # 결제 승인 시간
    reciept_url = models.URLField() # 영수증 URL

    create_at = models.DateTimeField(auto_now_add=True) # 결제 생성 시간
    update_at = models.DateTimeField(auto_now=True) # 결제 정보 수정 시간

    def __str__(self):
        return f"Payment {self.paymentKey} for Order {self.orderId}"
    
    class Meta:
        db_table = 'payment'
        app_label = 'payment'