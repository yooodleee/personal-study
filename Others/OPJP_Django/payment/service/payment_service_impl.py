from kakao_account.repository.account_repository_impl import AccountRepositoryImpl
from payment.repository.payment_repository_impl import PaymentRepositoryImpl
from payment.service.payment_service import PaymentService
from subscription.repository.subscription_repository_impl import SubscriptionRepositoryImpl


class PaymentServiceImpl(PaymentService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__paymentRepository = PaymentRepositoryImpl.getInstance()
            cls.__instance.__subscriptionRepository = SubscriptionRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    def paymentRegister(self, paymentData, accountId):
        account = self.__accountRepository.findById(accountId)
        paymentData = self.__paymentRepository.findById(account)
        if paymentData is None:
            print("구독권 새로 구입")
            paymentData = self.__paymentRepository.register(account)
        else:
            print("기존 구독권 사용")
        
        paymentId = paymentData.get('paymentId')
        print(f"paymentId:", {paymentId})

        accountId = paymentData.get('accountId')
        print(f"accountId:", {accountId})

        subscriptionId = paymentData.get('subscriptionId')
        print(f"subscriptionId:", {subscriptionId})

        paymentItemList = self.__paymentRepository.findAllByPaymentId(paymentId)
        print(f"paymentItemList:", {paymentItemList})

        paymentItem = None
        for item in paymentItemList:
            paymentFromSubscriptionItem = item.payment
            accountFromPayment = paymentFromSubscriptionItem.account
            if accountFromPayment.id == account.id:
                paymentItem = item
                break
        
        if paymentItem is None:
            print("신규 구독권 신청")
            subscription = self.__subscriptionRepository.findBySubscriptionId(subscriptionId)
            self.__paymentRepository.register(paymentData, subscription)
        else:
            print("기존 구독권 사용")
            self.__paymentItemRepository.update(paymentItem)
    
    def paymentList(self, accountId):
        account = self.accountRepository.findById(accountId)
        subscription = self.__subscriptionRepository.findByAccount(account)
        print(f"paymentList -> subscription: {subscription}")
        subscriptionItemList = self.__subscriptionItemRepository.findByPayment(subscription)
        print(f"paymentList -> paymentItemList: {subscriptionItemList}")
        paymentItemListResponseForm = []

        for paymentItem in paymentItemList:
            paymentItemResponseForm = {
                'paymentId': paymentItem.paymentId,
                'account': paymentItem.account,
                'subscription': paymentItem.subscription,
            }
            paymentItemListResponseForm.append(paymentItemResponseForm)
        
        return paymentItemListResponseForm
    
    def removePaymentItem(self, paymentItemId):
        return self.__paymentItemRepository.deleteByPaymentItemId(paymentItemId)