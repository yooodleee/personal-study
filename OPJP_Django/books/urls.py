from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books.controller.views import BooksView

router = DefaultRouter()
router.register(r'books', BooksView)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', BooksView.as_view({'get': 'list'}), name='books-list'),
    path('register/', BooksView.as_view({'post': 'register'}), name='books-register'),
    path('read/<int:pk>', BooksView.as_view({'get': 'readBook'}), name='books-read'),
]