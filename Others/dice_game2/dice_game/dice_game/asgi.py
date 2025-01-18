# Django 프로젝트를 ASGI(Asynchronous Server Gateway Interface) 서버에 연결
# 비동기 작업이 필요한 경우 필요

import os
from django.core.asgi import get_asgi_application

# Django 설정 모듈 지정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dice_game.settings')

# ASGI 애플리케이션 가져오기
application=get_asgi_application()