from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book_registration.controller.book_registration_controller import BookRegistrationController

router = DefaultRouter()
router.register(
    r"book-registration",
    BookRegistrationController,
    basename='books'
)

urlpatterns = [
    path('', include(router.urls)),
    path('request-create-book-registration-data',
         BookRegistrationController.as_view({ 'get': 'requestCreateBookRegistrationData' }),
         name='도서 등록 정보 생성'),
    path('request-book-registration-list',
         BookRegistrationController.as_view({ 'get': 'requestBookRegistrationList' }),
         name='도서 등록 정보 리스트 획득'),
]