from subscription.entity.subscription import Subscription
from subscription.repository.subscription_repositry import SubscriptionRepository

import pandas as pd


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
    
    def create(self, subscriptionData):
        subscription = Subscription(**subscriptionData)
        subscription.save()
        return subscription
    
    def createMany(self, subscriptionDataList):
        subscriptions = []
        for subscriptionData in subscriptionDataList:
            subscription = Subscription(**subscriptionData)
            subscription.save()
            subscriptions.append(subscription)
        
        return subscriptions
    
    def findAll(self)-> pd.DataFrame:
        subscriptions = Subscription.objects.all().values()
        return pd.DataFrame(subscriptions)
    
    def save(self, subscriptionData):
        try:
            # 데이터베이스에서 ID로 기존 레코드 검색
            subscription = Subscription.objects.get(
                id = subscriptionData['subscriptionId']
            )

            # 업데이트할 필드 설정
            subscription.subscriptionDescription = subscriptionData['subscriptionDescription']

            # 저장
            subscription.save()
            print(
                f"Subscription with ID {subscription.subscriptionId} successfully updated."
            )
        except Subscription.DoesNotExist:
            print(
                f"Subscription with ID {subscriptionData['subscriptionId']} does not exist in the database."
            )
        except Exception as e:
            print(
                f"An error occurred while saving the subscription data: {e}"
            )