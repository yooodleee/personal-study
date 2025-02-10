from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status

from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl


# Create your views here.
class OrderController(viewsets.ViewSet):
    redisCacheService = RedisCacheServiceImpl.getInstance()

    def requestCreateOrder(self, request):
        postRequest = request.data
        cart = postRequest.get("cart")
        userToken = postRequest.get("userToken")

        if not userToken:
            return JsonResponse(
                {"error": "userToken이 필요합니다.", "success": False},
                status = status.HTTP_400_BAD_REQUEST,
            )
        
        try:
            accountId = self.redisCacheService.getValueByKey(userToken)
        
        except Exception as e:
            print(f"주문 처리 중 오류 발생: {e}")
            return JsonResponse(
                {"error": "서버 내부 오류", "success": False},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR,
            )