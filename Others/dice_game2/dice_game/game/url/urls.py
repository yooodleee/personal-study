# URL 라우팅
# 게임의 URL을 정의함

from django.urls import path
from . import views

urlpatterns=[
    path('play/<int:rounds>/', views.play_game, name='play_game'),
]