from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account_profile.controller.account_profile_controller import AccountProfileController

router = DefaultRouter()
router.register(
    r'account_profile', AccountProfileController, basename='account_profile'
)

urlpatterns = [
    path('', include(router.urls)),
]