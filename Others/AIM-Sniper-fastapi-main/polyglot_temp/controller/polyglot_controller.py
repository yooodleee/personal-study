import os
import sys


from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse


from polyglot_temp.service.polyglot_service_impl import PolyglotServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl
from template.include.socket_server.utility.color_print import ColorPrinter # type: ignore


# .., template 디렉터리 기능을 가져옴.
sys.path.append(os.path.join(
    os.path.dirname(__file__), 
    '..', 
    'template')
)

# .., template, include, socket_server 디렉터리 기능을 가져옴.
sys.path.append(os.path.join(
    os.path.dirname(__file__), 
    '..', 
    'template', 
    'include', 
    'socket_server')
)


polyglotRouter = APIRouter()



def injectPolyglotService() -> PolyglotServiceImpl:
    """
    injectPolyglotService -> PolyglotServiceImpl(type hint)


    Return
    --------------
        PolyglotServiceImpl:
            UserDefinedQueueRepository의 객체 정보를 가져옴.
    """
    return PolyglotServiceImpl(
        UserDefinedQueueRepositoryImpl.getInstance()
    )



@polyglotRouter.get('/polyglot-result')
def requestNextQuestion(
    polyglotService: PolyglotServiceImpl=Depends(injectPolyglotService)
):
    """
    Params
    --------------
        polyglotService:
            PolyglotServiceImpl에서 injectPolyglotSerivce에 종속되어 있는
            정보를 가져옴.

    Return
    -------------
        JSONReponse:
            content: polyglotService의 요청한 NextQuestion의 응답답
            HTTP_200_OK(정상 실행)
    """

    ColorPrinter.print_important_message("requestNextQuestion()")

    nextQuestion = polyglotService.requestNextQuestion()

    return JSONResponse(
        content=nextQuestion, 
        status_code=status.HTTP_200_OK
    )



@polyglotRouter.get('/polyglot-score-result')
def requestScore(
    polyglotService: PolyglotServiceImpl = Depends(injectPolyglotService)
):
    """
    Params
    -------------
        polyglotService:
            polyglotServiceImpl에서 injectPolyglotService에 종속된 정보를 가져옴.
        scoreResult:
            polyglotService에서 요청한 score.

    Return
    -------------
        JSONResponse:
            content: scoreResult
            status_code: HTTP_200_OK(정상 실행)
    """
    
    ColorPrinter.print_important_message("requestScore()")
    scoreResult = polyglotService.requestScore()

    return JSONResponse(
        content=scoreResult, 
        status_code=status.HTTP_200_OK
    )
