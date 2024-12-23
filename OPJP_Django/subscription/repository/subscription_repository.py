from abc import ABC, abstractmethod


class SubscriptionRepository(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, subsciptionName, subscriptionPrice, subscriptionDescription, subscriptionImage):
        pass

    @abstractmethod
    def findBySubscriptionId(self, subscriptionId):
        pass