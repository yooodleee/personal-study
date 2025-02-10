# Django REST Framework(DRF)는 Django의 내장 URL 추적 시스템과 유사한 
# 강력하고 유연한 URL 라우팅 시스템을 제공합니다.
# Router는 RESTful API를 구축하기 위한 자동 URL 라우팅과 뷰셋(viewset)과 연결하는 과정을 
# 단순화하여 제공된 뷰셋을 기반으로 필요한 URL을 자동으로 생성해줍니다.
# 쉽게 말해 URL과 viewset을 연결해주는 것이죠.
# Router를 사용하면 URL 패턴을 쉽게 생성할 수 있다는 장점이 있습니다.
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books.controller.views import BooksView

# 먼저 DefaultRouter의 객체를 생성합니다.
router = DefaultRouter()
# router.register() 메서드를 사용해 BookView를 라우터에 등록합니다.
# 이때 첫 번째 인자는 URL접두사(books)이고, 두 번째는 뷰셋 클래스입니다.
router.register(r'books', BooksView)

# 라우터를 사용하기 위해 먼저 라우터의 객체를 생성해야 합니다.
# 그런 다음, 뷰셋을 라우터에 등록하고 Django 프로젝트의 URL 구성에 
# 라우터의 URL을 포함시킵니다.
urlpatterns = [
    path('', include(router.urls)),
    path('list/', BooksView.as_view({'get': 'list'}), name='books-list'),
    path('register/', BooksView.as_view({'post': 'register'}), name='books-register'),
    path('read/<int:pk>', BooksView.as_view({'get': 'readBook'}), name='books-read'),
]