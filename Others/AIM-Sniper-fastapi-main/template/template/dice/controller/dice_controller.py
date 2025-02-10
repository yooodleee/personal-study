from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse


from dice.service.dice_service_impl import DiceServiceImpl
from include.socket_server.socket_server.utility.color_print import ColorPrinter
from system_queue.repository.system_queue_repository_impl import SystemQueueRepositoryImpl


diceResultRouter = APIRouter()



async def injectDiceService() -> DiceServiceImpl:
    """
    async def (비동기 함수 선언)

    Return
    ---------------
        DiceServiceImpl:
            SystemQueueRepository의 객체 정보를 담는다.
    """
    return DiceServiceImpl(
        SystemQueueRepositoryImpl.getInstance())



@diceResultRouter.post("/dice-result")
async def requestDiceResult(
    diceService: DiceServiceImpl = Depends(injectDiceService)
):
    """
    Decoration
    ------------------
    diceResultRouter:
        post "/dice-result"

    Params
    --------------------
        diceService:
            DiceServiceImpl에서 injectDiceService에 의존된 객체 정보를 가져옴.
        diceListResult:
            diceService에서 요청한 List 결과에 대한 응답을 가져옴.
    
    Return
    ---------------------
        JSONResponse:
            content:
                diceListResult
            status_code:
                HTTP_200_OK(정상 실행)
    """

    diceListResult = diceService.requestListResult()
    ColorPrinter.print_important_data("requestDiceResult", diceListResult)

    return JSONResponse(
        content=diceListResult, 
        status_code=status.HTTP_200_OK
    )
