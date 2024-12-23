from django.urls import path, include
from rest_framework.routers import DefaultRouter
from kakao_account.controller.account_controller import AccountController

router = DefaultRouter()
router.register(r"game", AccountController, basename='game')

urlpatterns = [
    path('', include(router.urls)),
]