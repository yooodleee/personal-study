# Models 정의-> Django ORM을 사용하여 게임 관련 데이터를 모델로 정의

from django.db import models

class Player(models.Model):
    """플레이어 모델"""
    name=models.CharField(max_length=100)  # 최대 글자 길이를 제한
    score=models.IntegerField(default=0)    # Raises a ValidationError

    def increment_score(self):
        """점수 증가"""
        self.score += 1
        self.save()

    def __str__(self):
        return self.name

class GameRecord(models.Model):
    """게임 결과 기록"""
    player1_score=models.IntegerField()
    player2_score=models.IntegerField()
    winner=models.CharField(max_length=100) # 'player 1', 'player2' or 'Draw'
    created_at=models.DateTimeField(auto_now_add=100)   

    def __str__(self):
        return f"Player 1: {self.player1_score}, Player 2: {self.player2_score}"