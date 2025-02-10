from django.urls import path, include
from rest_framework.routers import DefaultRouter

from payment.controller.payment_controller import PaymentController

router = DefaultRouter()
router.register(
    r'payment',
    PaymentController,
    basename='payment',
)

urlpatterns = [
    path('', include(router.urls)),
    path('process',
         PaymentController.as_view({ 'post': 'requestProcessPayment'}),
         name='결제 진행'),
]