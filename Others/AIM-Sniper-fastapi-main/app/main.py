"""
Python FastAPI에서 CORS 적용하기


* CORS(Cross Origin Resource Sharing)란?
    1) CORS는 한 도메인의 웹 페이지가 다른 도메인의 리소스를 요청 및 상호 작용하는 방식을
        제어하기 위해 웹 브라우저에 구현된 '보안' 기능이다.
    2) 한 출처에서 실행 중인 웹 애플리케이션이 다른 출처의 자원에 접근할 수 있는 권한을
        부여하도록 브라우저에게 알려주는 것.
    3) CORS가 필요한 이유는 Same - Origin 정책(Same - Origin policy, SOP)은 매우 중요하지만,
        웹 페이지가 다른 도메인의 리소스에 엑세스하는데에는 또 다른 합법적이고 정당한 이유가 
        있기 때문이다. 이때 CORS는 Origin domain이 다른 도메인의 API를 호출하도록 허용하는 
        '안전한 방법'을 제공해준다.

* Origin이란?
    1) Origin은 프로토콜(Http, Https), 도메인(yoodleee.com, localhost, localhost.yooodleee.com)
        및 포트(80, 443, 8080)의 조합이다.
    2) 예컨대 아래는 서로 다른 오리진(Origin)이다.
        * http://localhost
        * https://localhost
        * http://localhost:8080
    3) 즉, 모두 localhost일지라도 서로 다른 프로토콜이나 포트를 사용하므로 서로 다른 Origin이 된다.
    4) CORS는 이러한 Cross origin을 지원해주는 안전 장치라고 볼 수 있다.
"""

"""
Uvicorn vs Hypercorn


* Uvicorn
    1) 사이썬 기반의 ASGI 서버이며, 비동기 코드를 지원한다.
    2) 성능이 빠르며 대규모 응용 프로그램에 적합하다.
    3) 주로 FastAPI와 함께 사용되도록 설계됐다.
    4) 비동기 처리 방식에 있어 유비콘은 파이썬의 uvloop 라이브러리를 사용해
        이벤트 루프를 빠르게 처리한다.

* Hypercorn
    1) 비동기 코드를 지원하는 ASGI 서버이지만, 유비콘보다는 약간 느릴 수 있다.
    2) 하지만 높은 처리량이나 낮은 지연시간을 필요로 하는 작업에는 하이퍼콘이 적합하다.
    3) 여러 프레임워크와 호환되는 플러그인 시스템을 지원해 다양한 설정 및 확장 기능을
        제공한다.
    4) 멀티 프로세스와 워커를 지원해 멀티 코어 시스템에서의 병렬처리를 쉽게 할 수 있다.


* 사이썬 기반(Cython-based)
    1) 가능하다면 `uvloop(이벤트 루프)`를 설치해 사용하낟.
    2) 가능하다면 `httptools`를 이용해 HTTP 프로토콜을 처리한다.
"""

import os.path
import sys
from fastapi.middleware.cors import CORSMiddleware


import colorama # print문의 색상과 음영 변경 지원원


import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI


from openai_api.controller.openai_api_controller import openaiApiRouter
from polyglot_temp.controller.polyglot_controller import polyglotRouter
from report_to_db.controller.report_to_db_controller import reportToDbRouter
from test.controller.test_controller import testRouter
from user_defined_initializer.init import UserDefinedInitializer


sys.path.append(
    os.path.join(os.path.dirname(__file__), '..', 'template')
)
sys.path.append(os.path.join(
    os.path.dirname(__file__), 
    '..', 
    'template', 
    'include', 
    'socket_server')
)


from template.template.deep_learning.controller.deep_learning_controller import deepLearningRouter
from template.template.dice.controller.dice_controller import diceResultRouter
from template.template.system_initializer.init import SystemInitializer
from template.template.task_manager.manager import TaskManager
from template.template.include.socket_server.initializer.init_domain import DomainInitializer # type: ignore


DomainInitializer.initEachDomain()
SystemInitializer.initSystemDomain()
UserDefinedInitializer.initUserDefinedDomain()



app = FastAPI()

load_dotenv()

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(deepLearningRouter)
app.include_router(diceResultRouter)

app.include_router(openaiApiRouter)
app.include_router(testRouter)
app.include_router(polyglotRouter)
app.include_router(reportToDbRouter)



if __name__ == "__main__":
    colorama.init(autoreset=True)

    TaskManager.createSocketServer()
    uvicorn.run(
        app, 
        host=os.getenv('HOST'), 
        port=int(os.getenv('FASTAPI_PORT'))
    )
