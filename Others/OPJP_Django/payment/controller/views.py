from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from payment.service.payment_service_impl import PaymentServiceImpl

from kakao_authentication.service.kakao_oauth_service_impl import KakaoOauthServiceImpl


class PaymentView(viewsets.ViewSet):
    paymentService = PaymentServiceImpl.getInstance()
    redisService = KakaoOauthServiceImpl.getInstance()

    def paymentItemList(self, request):
        data = request.data
        userToken = data.get('userToken')

        if not userToken:
            return Response({'error': 'User token is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        accountId = self.redisService.getValueByKey(userToken)
        if not accountId:
            return Response({'error': 'Invalid user token'}, status=status.HTTP_400_BAD_REQUEST)
        
        paymentItemListResponseForm = self.paymentService.paymentList(accountId)
        return Response(paymentItemListResponseForm, status=status.HTTP_200_OK)
    
    def paymentRegister(self, request):
        try:
            data = request.data
            print('data:', data)

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            self.paymentService.paymentRegister(data, accountId)
            return Response(status=status.HTTP_200_OK)
        
        except Exception as e:
            print('결제 내역 등록 중 문제 발생:', e)
            return Response({ 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def removePaymentItem(self, requset):
        try:
            data = requset.data
            if list(data.keys())[0] == 'PaymentItemId':
                paymentItemId = data['PaymentItemId']
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print("결제 내역 정리 중 에러 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)