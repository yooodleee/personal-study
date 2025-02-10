from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bookmark.controller.bookmark_controller import BookmarkController

router = DefaultRouter()
router.register(
    r"bookmark",
    BookmarkController,
    basename='bookmark',
)

urlpatterns = [
    path('', include(router.urls)),
    path('create',
         BookmarkController.as_view({ 'post': 'requestCreateBookmark'}),
         name='북마크 생성 및 추가'),
    path('list',
         BookmarkController.as_view({ 'post': 'requestListBookmark'}),
         name='북마크 리스트'),
    path('remove',
         BookmarkController.as_view({ 'poist': 'requestRemoveBookmark'}),
         name='북마크 제거'),
]