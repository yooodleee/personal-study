from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bookmark.controller.views import BookmarkViews

router = DefaultRouter()
router.register(r'cart', BookmarkViews, basename='bookmark')

urlpatterns = [
    path('', include(router.urls)),
    path('list', BookmarkViews.as_view({'post': 'bookmarkItemList'}), name='bookmark-list'),
    path('register', BookmarkViews.as_view({'post': 'bookmarkRegister'}), name='bookmark-register'),
    path("remove", BookmarkViews.as_view({'delete': 'removeBookmarkItem'}), name='bookmark-remove'),
]