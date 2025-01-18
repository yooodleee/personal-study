# 프로젝트의 URL 라우팅을 정의

from django.contrib import admin
from django.urls import path, include

urlpatterns=[
    path('admin/', admin.site.urls),    # 관리자 페이지 URL
    path('game/', include('game.urls')),   # 게임 앱의 URL
]