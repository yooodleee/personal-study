# Django 프로젝트를 WSGI(Web Server Gateway Interface) 서버에 연결
# 배포 환경에서 필요

import os
from django.core.wsgi import get_wsgi_application

# Django 설정 모듈 지정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dice_game.settings')

# WSGI 애플리케이션 가져오기
application=get_wsgi_application()