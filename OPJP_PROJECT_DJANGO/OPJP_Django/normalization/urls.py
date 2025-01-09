from django.urls import path, include
from rest_framework.routers import DefaultRouter

from normalization.controller.normalization_controller import NormalizationController


router = DefaultRouter()
router.register(
    r'normalize',
    NormalizationController,
    basename='normalize',
)

urlpatterns = [
    path('', include(router.urls)),
    path('request-normalize',
         NormalizationController.as_view({ 'get': 'requestNormalize'}),
         name='데이터 표준화 테스트'),
]