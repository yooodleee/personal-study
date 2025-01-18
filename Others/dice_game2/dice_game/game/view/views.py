# View 정의
# 사용자 요청을 처리하고 결과를 반환

from django.http import JsonResponse
from service.services import GameService

def play_game(request, rounds):
    """게임 실행"""
    if rounds <= 0:
        return JsonResponse({"error": "Rounds must be a positive integer."}, status=400)
    
    service=GameService()

    for _ in range(rounds):
        service.play_round()

    results=service.get_results()
    return JsonResponse({
        "scores": results["scores"],
        "records": [
            {
                "player1_score": record.player1_score,
                "player2_score": record.player2_score,
                "winner": record.winner,
                "created_at": record.create_at
            }
            for record in results["records"]
        ]
    })