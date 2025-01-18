# Service layer(비즈니스 로직)
# 게임의 비즈니스 로직을 담당, 저장소 계층을 통해 데이터를 관리

from repository.repository import GameRepository
from random import randint


class DiceRoll:
    """주사위 결과 기록, 값 객체"""
    def __init__(self, roll1, roll2):
        self.roll1=roll1
        self.roll2=roll2
    
    @property
    def total(self):
        return self.roll1 + self.roll2
    
    @staticmethod
    def roll():
        """주사위 2개를 굴리고 결과 반환"""
        return DiceRoll(randint(1, 6), randint(1, 6))


class GameService:
    """게임 비즈니스 로직"""
    def __init__(self):
        self.repository=GameRepository()
        self.player1, self.player2=self.repository.get_all_records()
    
    def play_round(self):
        """단일 라운드 실행"""
        roll1=DiceRoll.roll()
        roll2=DiceRoll.roll()

        if roll1.total > roll2.total:
            winner="Player 1"
            self.player1.increment_score()
        elif roll1.total < roll2.total:
            winner="Player 2"
            self.player2.increment_score()
        else:
            winner="Draw"
        
        # Game Result Store
        self.repository.save_game_record(roll1.total, roll2.total, winner)
    
    def get_results(self):
        """마지막 결과 반환"""
        records=self.repository.get_all_records()
        scores={
            "Player 1": self.player1.score,
            "Player 2": self.player2.score
        }
        return {"scores": scores, "records": records}