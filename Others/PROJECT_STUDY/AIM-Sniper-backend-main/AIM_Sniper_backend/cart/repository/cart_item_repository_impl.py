from cart.entity.cart import Cart
from cart.entity.cart_item import CartItem
from cart.repository.cart_item_repository import CartItemRepository


class CartItemRepositoryImpl(CartItemRepository):
    __instance = None   # singleton 선언

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def register(self, cartData, cart, companyReport):
        # CartData에서 companyReportPrice(회사 보고 가격) 가져옴.
        companyReportPrice = cartData.get('companyReportPrice')

        # CartItem에 cart, product, quantity, price를 생성
        CartItem.objects.create(
            cart=cart,
            product=companyReport,
            quantity=1,
            price=companyReportPrice
        )

    def findByCart(self, cart):
        # cart로 filtering한 CartItem 객체를 리스트로 반환
        return list(CartItem.objects.filter(cart=cart))

    def findByProductId(self, companyReportId):
        try:    # companyReportId인 CartItem 객체를 반환
            return CartItem.objects.get(product_id=companyReportId)
        
        # 해당되는 객체가 없다면 None 반환
        except CartItem.DoesNotExist:
            return None

    def findAllByProductId(self, companyReportId):
        # compantyReortId로 filtering한 CartItem의 객체를 반환
        return CartItem.objects.filter(product_id=companyReportId)

    def findById(self, id):
        return CartItem.objects.get(cartItemId=id)


    def deleteByCartItemId(self, cartItemIdList):
        # cartItemIdList에 cartItemId가 있다면 cartItemId인 CartItem 객체들을 delete
        for cartItemId in cartItemIdList:
            cartItem = CartItem.objects.get(cartItemId=cartItemId)
            cartItem.delete()

    def checkDuplication(self, cartItemList, companyReportId):
        for cartItem in cartItemList:
            # cartItem의 product에서 companyReportId가 유일한 값이라면 True
            if str(cartItem.product.companyReportId) == str(companyReportId):
                return True
            
        # 중복된 companyReportId가 있다면 False
        return False



