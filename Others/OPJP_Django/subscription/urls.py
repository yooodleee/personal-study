from django.urls import path, include
from rest_framework.routers import DefaultRouter

from subscription.controller.views import SubscriptionView

router = DefaultRouter()
router.register(r'subscription', SubscriptionView)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', SubscriptionView.as_view({'get': 'list'}), name='subscription-list'),
    path('register/', SubscriptionView.as_view({'post': 'register'}), name='subscription-register'),
    path('read/<int:pk', SubscriptionView.as_view({'get': 'readSubscription'}), name='subscription-read'),
]