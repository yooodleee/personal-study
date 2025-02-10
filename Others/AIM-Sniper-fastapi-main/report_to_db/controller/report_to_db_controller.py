import os
import sys

# .., template 디렉터리에서 기능을 가져옴.
sys.path.append(os.path.join(
    os.path.dirname(__file__), 
    '..', 
    'template')
)


from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse


from report_to_db.service.report_to_db_service_impl import ReportToDbServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl


from template.include.socket_server.utility.color_print import ColorPrinter # type: ignore
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse


reportToDbRouter = APIRouter()


async def injectReportToDbService() -> ReportToDbServiceImpl:
    """
    async 비동기 함수 선언이며, type hint(ReportToDbServiceImpl) 사용.

    Return
    -------------
        ReportToDbServiceImpl
            : UserDefinedQueueRepository의 객체 정보를 가져옴.
    """
    return ReportToDbServiceImpl(
        UserDefinedQueueRepositoryImpl.getInstance()
    )


@reportToDbRouter.post('/update')
async def requestReportToDb(
    reportToDbService: ReportToDbServiceImpl = Depends(injectReportToDbService)
):
    """
    Params
    --------------
        reportToDbService:
            ReportToDbServiceImpl에서 injectReportToDbService에 종속된 정보 가져옴.
        success: (await)
            reportToDbService에서 Ai에 요청한 응답을 가져옴.

    Return
    ---------------
        JSONResponse:
            content: success
            status_code: HTTP_200_OK(정상 실행)
    """

    ColorPrinter.print_important_message("requestReportToDbPoint()")

    success = await reportToDbService.requestReportToAi()

    return JSONResponse(
        content=success, 
        status_code=status.HTTP_200_OK
    )