from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books.controller.books_controller import BooksController

router = DefaultRouter()
router.register(
    r'books', BooksController, basename='books'
)

urlpatterns = [
    path('', include(router.urls)),
    path('request-book-list',
         BooksController.as_view({ 'get': 'requestBookList'}),
         name='도서 정보 리스트 획득'),
    path('request-modify-book-description',
         BooksController.as_view({ 'get': 'requestModifyBookDescription'}),
         name='도서 이름 변경'),
]