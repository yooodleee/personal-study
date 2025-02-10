from abc import ABC, abstractmethod
import pandas as pd


class SubscriptionRepository(ABC):

    @abstractmethod
    def create(self, subscriptionData):
        pass

    @abstractmethod
    def findAll(self)-> pd.DataFrame:
        pass

    @abstractmethod
    def save(self, subscriptionData):
        pass