from payment.entity.payment import Payment
from payment.repository.payment_repository import PaymentRepository


class PaymentRepositoryImpl(PaymentRepository):
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
    
    def register(self, account):
        return Payment.objects.create(account=account)
    
    def findByAccount(self, account):
        try:
            return Payment.objects.get(account=account)
        except Payment.DoesNotExist:
            return None