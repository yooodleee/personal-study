from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse


from deep_learning.controller.request_form.ai_command_request_form import AICommandRequestForm
from deep_learning.service.deep_learning_service_impl import DeepLearningServiceImpl
from system_queue.repository.system_queue_repository_impl import SystemQueueRepositoryImpl


deepLearningRouter = APIRouter()




async def injectDeepLearningService() -> DeepLearningServiceImpl:
    """
    async def (비동기 함수 선언)
    
    Return
    --------------
        DeepLearningServiceImpl:
            SystemQueueRepositoryImpl의 객체 정보를 담습니다.
    """
    return DeepLearningServiceImpl(
        SystemQueueRepositoryImpl.getInstance()
    )


# 데코레이션: deepLearningRouter에서 /request-ai-command 정보를 가져옵니다.
@deepLearningRouter.post("/request-ai-command")
async def requestAiCommand(
    aiCommandRequestForm: AICommandRequestForm,
    deepLearningService: DeepLearningServiceImpl = Depends(injectDeepLearningService)
):
    """
    Decoration
    -----------------
        deepLearningRouter:
            get "/request-ai-command"

    Params
    -------------------
        aiCommandRequestForm:
            AICommandRequestForm
        deepLearningService:
            DeepLearningServiceImpl에서 injectDeepLearningService에 종속된 객체 정보를
            가져옵니다.

    Return
    --------------------
        JSONResponse:
            content: (bool)
                True
            status_code:
                HTTP_200_OK(정상 실행)
    """

    deepLearningService.requestAICommand(aiCommandRequestForm.toAICommandRequest())

    return JSONResponse(
        content=True, 
        status_code=status.HTTP_200_OK
    )
