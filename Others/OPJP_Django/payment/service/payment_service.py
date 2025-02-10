from abc import ABC, abstractmethod


class PaymentService(ABC):
    @abstractmethod
    def paymentRegister(self, paymentData, accountId):
        pass

    @abstractmethod
    def paymentList(self, accountId):
        pass

    @abstractmethod
    def removePaymentItem(self, paymentItemId):
        pass