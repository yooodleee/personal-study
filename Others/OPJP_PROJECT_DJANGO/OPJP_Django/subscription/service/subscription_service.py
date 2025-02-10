from abc import ABC, abstractmethod


class SubscriptionService(ABC):

    @abstractmethod
    def subscriptionList(self):
        pass

    @abstractmethod
    def requestModifySubscriptionDescription(self):
        pass