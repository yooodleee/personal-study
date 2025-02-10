from subscription.repository.subscription_repository_impl import SubscriptionRepositoryImpl
from subscription.service.subscription_service import SubscriptionService


class SubscriptionServiceImpl(SubscriptionService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__subscriptionRepository = SubscriptionRepositoryImpl.getInstance()
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    def list(self):
        return self.__subscriptionRepository.list()
    
    def createSubscription(self, subscriptionName, subscriptionPrice, subscriptionDescription, subscriptionImage):
        return self.__subscriptionRepository.create(
            subscriptionName, subscriptionPrice, subscriptionDescription, subscriptionImage)
    
    def readSubscription(self, subscriptionId):
        return self.__subscriptionRepository.findBySubscription(subscriptionId)