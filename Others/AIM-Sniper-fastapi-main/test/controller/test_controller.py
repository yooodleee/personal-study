import os
import sys


from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse


from test.service.test_service_impl import TestServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl
from template.include.socket_server.utility.color_print import ColorPrinter # type: ignore


# .., template 디렉터리에서 필요한 기능 가져옴.
sys.path.append(os.path.join(
    os.path.dirname(__file__), 
    '..', 
    'template')
)

# .., template, include, socket_server 디렉터리에서 필요한 기능을 가져옴.
sys.path.append(os.path.join(
    os.path.dirname(__file__), 
    '..', 
    'template', 
    'include', 
    'socket_server')
)


testRouter = APIRouter()



def injectTestService() -> TestServiceImpl:
    """
    Return
    ---------------
        TestServiceImpl에 UserDefinedQueueRepository의 객체 정보를 가져와 저장함.
    """

    return TestServiceImpl(
        UserDefinedQueueRepositoryImpl.getInstance()
    )


# 데코레이터(decorator): 함수에 추가하고 싶은 내용이나 기능
# testRouter에서 /test-result를 가져와서 requestOpenaiApiResult에 추가함.
@testRouter.get('/test-result')
def requestOpenaiApiResult(
    testService: TestServiceImpl = Depends(injectTestService)
):
    """
    Params
    -------------
        testService: 
            TestServiceImpl에서 injectTestService에 종속된 정보를 가져옴.
        testResult:
            testService에서 요청한 test result를 가져옴.

    Return
    -------------
        JSONResponse:
            content: testResult
            status_code: HTTP_200_OK(정상 실행)
    """

    ColorPrinter.print_important_message("requestTestResult()")

    testResult = testService.requestTestResult()

    return JSONResponse(
        content=testResult, 
        status_code=status.HTTP_200_OK
    )
