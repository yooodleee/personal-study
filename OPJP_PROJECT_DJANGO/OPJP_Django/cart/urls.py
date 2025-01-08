from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cart.controller.cart_controller import CartController

router = DefaultRouter()
router.register(r"cart", CartController, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    path('create',
        CartController.as_view({ 'post': 'requestCreateCart'}),
        name='카트 생성 및 추가'),
    path('list',
         CartController.as_view({ 'post': 'requestListCart'}),
         name='카트 리스트'),
    path('remove',
         CartController.as_view({ 'post': 'requestRemoveCart'}),
         name='카트 제거'),
]