# Repository 계층(저장소)
# Django 모델을 통해 데이터를 저장하고 조회하는 저장소 계층 구현

from entity.models import Player, GameRecord

class GameRepository:
    """게임 데이터 저장"""

    @staticmethod
    def get_or_create_players():
        """플레이어 가져오기 혹은 생성"""
        player1, _=Player.objects.get_or_create(name="Player 1")
        player2, _=Player.objects.get_or_create(name="Player 2")
        return player1, player2
    @staticmethod
    def save_game_record(player1_score, player2_score, winner):
        """게임 기록 저장"""
        GameRecord.objects.create(
            player1_score=player1_score,
            player2_score=player2_score,
            winner=winner
        )
    
    @staticmethod
    def get_all_records():
        """전체 게임 기록 가져오기"""
        return GameRecord.objects.all()