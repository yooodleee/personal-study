import os
import sys


from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse


from openai_api.service.openai_api_service_impl import OpenaiApiServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl
from template.include.socket_server.utility.color_print import ColorPrinter


sys.path.append(os.path.join(
    os.path.dirname(__file__), 
    '..', 
    'template')
)
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


# async 비동기 함수 / type hint(OpenaiApiServiceImpl)
async def injectOpenaiApiService() -> OpenaiApiServiceImpl:

    return OpenaiApiServiceImpl(
        UserDefinedQueueRepositoryImpl.getInstance()
    )



@openaiApiRouter.get('/openai-api-result')
async def requestOpenaiApiResult(
    oepnaiApiService: OpenaiApiServiceImpl = Depends(injectOpenaiApiService)):

    ColorPrinter.print_important_message("requestOpenaiApiResult()")

    generatedOpenaiApiResult = oepnaiApiService.requestOpenaiApiResult()


    return JSONResponse(
        content=generatedOpenaiApiResult, 
        status_code=status.HTTP_200_OK
    )
