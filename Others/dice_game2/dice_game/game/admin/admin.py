# 관리자 패널 설정
# 관리자 패널에서 데이터를 관리할 수 있도록 설정

from django.contrib import admin
from entity.models import Player, GameRecord

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display=("name", "score")

@admin.register(GameRecord)
class GameRecordAdmin(admin.ModelAdmin):
    list_display=("player1_score", "player2_score", "winner", "create_at")
    list_filter=("winner", "create_at")
    ordering=("-created_at")