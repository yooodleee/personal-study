from abc import ABC, abstractmethod


class PaymentRepository(ABC):

    @abstractmethod
    def request(self, paymentRequestData):
        pass

    @abstractmethod
    def create(self, payment):
        pass