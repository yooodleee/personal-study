from abc import ABC, abstractmethod


class PaymentRepository(ABC):
    @abstractmethod
    def register(self, account):
        pass

    @abstractmethod
    def findByAccount(self, account):
        pass