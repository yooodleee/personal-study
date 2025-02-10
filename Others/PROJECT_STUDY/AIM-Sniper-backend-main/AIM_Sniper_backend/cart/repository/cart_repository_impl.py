from cart.entity.cart import Cart
from cart.repository.cart_repository import CartRepository


class CartRepositoryImpl(CartRepository):
    __instance = None   # singletom 선언

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def register(self, account):
        # Cart에 account라는 새로운 객체를 등록(생성).
        return Cart.objects.create(account=account)

    def findByAccount(self, account):
        try:
            # account에 해당하는 Cart의 객체가 있다면 반환
            return Cart.objects.get(account=account)
        
        # 해당되는 경우가 없다면 None 반환
        except Cart.DoesNotExist:
            return None

