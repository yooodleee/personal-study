from django.urls import path, include
from rest_framework.routers import DefaultRouter

from payment.controller.views import PaymentView

router = DefaultRouter()
router.register(r'payment', PaymentView, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
    path('list', PaymentView.as_view({'post': 'paymentItemList'}), name='payment-list'),
    path('register', PaymentView.as_view({'post': 'paymentRegister'}), name='payment-register'),
    path('remove', PaymentView.as_view({'delete': 'removePaymentItem'}), name='payment-remove'),
]