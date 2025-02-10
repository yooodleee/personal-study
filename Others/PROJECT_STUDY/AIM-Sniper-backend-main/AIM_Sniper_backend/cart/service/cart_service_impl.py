from account.repository.account_repository_impl import AccountRepositoryImpl
from cart.repository.cart_item_repository_impl import CartItemRepositoryImpl
from cart.repository.cart_repository_impl import CartRepositoryImpl
from cart.service.cart_service import CartService
from company_report.repository.companyReport_repository_impl import CompanyReportRepositoryImpl


class CartServiceImpl(CartService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__cartRepository = \
                CartRepositoryImpl.getInstance()
            
            cls.__instance.__productRepository = \
                CompanyReportRepositoryImpl.getInstance()
            
            cls.__instance.__accountRepository = \
                AccountRepositoryImpl.getInstance()
            
            cls.__instance.__cartItemRepository = \
                CartItemRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def cartRegister(self, cartData, accountId):
        # account와 cart를 각각 accountRepository, cartRepository에서 가져옴.
        account = self.__accountRepository.findById(accountId)
        cart = self.__cartRepository.findByAccount(account)
        if cart is None:
            print("장바구니 새롭게 생성")
            # cartRepository에 account에 해당하는 새로운 cart 등록
            cart = self.__cartRepository.register(account)

        print("기존 장바구니 사용")

        # companyReportId와 cartItemList를 가져옴.
        companyReportId = cartData.get('companyReportId')
        cartItemList = self.__cartItemRepository.findAllByProductId(
            companyReportId
        )

        cartItem = None
        for item in cartItemList:
            # item의 cart를 가져옴.
            cartFromCartItem = item.cart
            # cartFromCartItem의 account를 가져옴.
            accountFromCart = cartFromCartItem.account
            # accountFromCart(카트에 해당하는 account의 id)와 account의 id가 동일하다면
            if accountFromCart.id == account.id:
                # cart에 담긴 Item은 item이 맞습니다.
                cartItem = item
                break

        if cartItem is None:
            print("신규 상품 추가")
            product = self.__productRepository.findByCompanyReportId(
                companyReportId
            )
            # cartdata, cart, product를 cartItemRepository에 새로 등록
            self.__cartItemRepository.register(cartData, cart, product)

    def cartList(self, accountId):
        # account와 cart를 각각 accountRepository와 cartRepository에서 가져옴.
        account = self.__accountRepository.findById(accountId)
        cart = self.__cartRepository.findByAccount(account)
        # print(f"cartList -> cart: {cart}")
        cartItemList = self.__cartItemRepository.findByCart(cart)
        # print(f"cartList -> cartItemList: {cartItemList}")

        cartItemListResponseForm = []

        for cartItem in cartItemList:
            # 출력할 cartItemResponseForm을 지정합니다(출력될 정보들 지정)
            cartItemResponseForm = {
                'cartItemId': cartItem.cartItemId,  # 카트 아이템의 id
                'companyReportName': cartItem.product.companyReportName,
                'companyReportPrice': cartItem.product.companyReportPrice,
                'companyReportTitleImage': cartItem.product.companyReportTitleImage,
                'companyReportId': cartItem.product.companyReportId,
                'quantity': cartItem.quantity,
            }
            cartItemListResponseForm.append(cartItemResponseForm)

        return cartItemListResponseForm

    def removeCartItem(self, cartItemId):
        # cartItemRepository에서 삭제하고자 하는 CartItemId에 해당하는 item을 지정.
        self.__cartItemRepository.deleteByCartItemId(cartItemId)