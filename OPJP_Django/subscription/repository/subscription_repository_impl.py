import os

from OPJP_Django import settings
from subscription.entity.subscription import Subscription
from subscription.repository.subscription_repository import SubscriptionRepository


class SubscriptionRepositoryImpl(SubscriptionRepository):
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
    
    def list(self):
        return Subscription.objects.all().order_by('registeredDate')
    
    def create(self, subscriptionName, subscriptionPrice, subscriptionDescription, subscriptionImage):
        uploadDirectory = os.path.join(
            settings.BASE_DIR,
            # 무엇을 넣어야 할까?
        )
        if not os.path.exists(uploadDirectory):
            os.makedirs(uploadDirectory)
        
        imagePath = os.path.join(uploadDirectory, subscriptionImage.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in subscriptionImage.chunks():
                destination.write(chunk)
            
            destination.flush()
            os.fsync(destination.fileno())
        
        subscription = Subscription(
            subscriptionName=subscriptionName,
            subscriptionDescription=subscriptionDescription,
            subscriptionPrice=subscriptionPrice,
            subscriptionImage=subscriptionImage.name
        )
        subscription.save()

        savedSubscription = Subscription.objects.get(subscriptionId=subscription.subscriptionId)
        print(f'savedSubscription: {savedSubscription.subscriptionImage}')
        return savedSubscription
    
    def findBySubscriptionId(self, subscriptionId):
        try:
            return Subscription.objects.get(subscriptionId=subscriptionId)
        except Subscription.DoesNotExist:
            return None