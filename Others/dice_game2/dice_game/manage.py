# Django 관리 스크립트

import os
from game.services import GameService

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dice_game.settings')

service=GameService()
service.play_round()    # 단일 라운드 실행
print(service.get_results())    # 결과 확인