from django.urls import path, include
from rest_framework.routers import DefaultRouter

from regression.controller.regression_controller import RegressionController

router = DefaultRouter()
router.register(
    r"regression",
    RegressionController,
    basename='regression',
)

urlpatterns = [
    path('', include(router.urls)),
    path('request-logistic-regression',
    RegressionController.as_view({ 'get': 'requestLogisticRegression'}),
    name='로지스틱 회귀 테스트'),
]