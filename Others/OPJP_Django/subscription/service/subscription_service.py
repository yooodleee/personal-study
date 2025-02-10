from abc import ABC, abstractmethod


class SubscriptionService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createSubscription(self, subscriptionName, subscriptionPrice, subscriptionDescription, subscriptionImage):
        pass

    @abstractmethod
    def readSubscription(self, subscriptionId):
        pass