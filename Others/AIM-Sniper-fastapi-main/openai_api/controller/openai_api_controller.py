import os
import sys


from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse


from openai_api.service.openai_api_service_impl import OpenaiApiServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl
from template.include.socket_server.utility.color_print import ColorPrinter # type: ignore



# .., template 디렉터리를 가져와서 사용
sys.path.append(os.path.join(
    os.path.dirname(__file__), 
    '..', 
    'template')
)

# .., template, include, socket_servder 디렉터리를 가져와서 사용
sys.path.append(os.path.join(
    os.path.dirname(__file__), 
    '..', 
    'template', 
    'include', 
    'socket_server')
)


# FastAPI에서 라우터(router)는 하나의 파일을 통해 모든 것을 구성하는 것이 아니라,
# 각 특성에 맞는 코드와 파일을 분리하고 이를 조합해 더 큰 application을 만들게 도와주는 구조이다.
openaiApiRouter = APIRouter()


async def injectOpenaiApiService() -> OpenaiApiServiceImpl:
    """
    Return
    -------------
        OpenaiApiServiceImpl:
            UserDefinedQueueRepositoryImpl(사용자 정의 큐 저장소)의 객체를 가져옴.
    """

    return OpenaiApiServiceImpl(
        UserDefinedQueueRepositoryImpl.getInstance()
    )



@openaiApiRouter.get('/openai-api-result')
async def requestOpenaiApiResult(
    oepnaiApiService: OpenaiApiServiceImpl = Depends(injectOpenaiApiService)):
    """
    Params
    ------------------
        openaiApiService(OpenaiApiService)
        generatedOpenaiApiResult:
            openaiApiService의 API에 요청한 응답을 가져옴.

    Return
    ---------------
        JSONResponse:
            HTTP_200_OK(정상 출력)
    """

    ColorPrinter.print_important_message("requestOpenaiApiResult()")

    generatedOpenaiApiResult = oepnaiApiService.requestOpenaiApiResult()


    return JSONResponse(
        content=generatedOpenaiApiResult, 
        status_code=status.HTTP_200_OK
    )
