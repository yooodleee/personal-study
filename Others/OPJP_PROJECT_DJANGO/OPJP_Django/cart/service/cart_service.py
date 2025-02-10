from abc import ABC, abstractmethod


class CartService(ABC):

    @abstractmethod
    def createCart(self, accountId, cart):
        pass

    @abstractmethod
    def listcart(self, accountId, page, pageSize):
        pass

    @abstractmethod
    def removeCart(self, accountId, cartId):
        pass