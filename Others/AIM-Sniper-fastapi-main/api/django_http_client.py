"""
HTTPX는 Python의 최신 비동기 HTTP 클라이언트 라이브러리다.
`requests` 라이브러리의 사용 편의성을 유지하면서 비동기 기능을 제공한다.
이 라이브러리는 동기 및 비동기 요청 모두를 지원하여 개발자가 더욱 효율적으로 네트워크 작업을
    수행할 수 있도록 돕는다.

    * 주요 기능:

        1) 동기 및 비동기 지원:
            동기적으로도 사용할 수 있고, `asyncio`와 같은 비동기 프레임워크와 함께 사용할 수도 있다.
        2) HTTP /1.1 및 HTTP /2 지원:
            두 가지 프로토콜 모두에 대한 지원을 통해 향상된 성능과 호환성을 제공한다.
        3) 완전한 기능의 요청과 응답 객체:
            `requests`의 사용자 친화적인 인터페이스를 유지하며, 요청 및 응답에 대한 완전한 제어를 제공한다.
        4) 표준 기반:
            요청과 응답에 대한 표준 Python 타입을 사용하며, 표준 HTTP 기능을 지원한다.

"""

import httpx
import os
from dotenv import load_dotenv

load_dotenv()

class DjangoHttpClient:
    """
    Http 클라이언트를 사용해서 직접 클라이언트의 입장이 된다.
    백엔드가 프론트의 서버가 직접 API를 호출하여 요청할 수 있도록 한다.

        * 서버에 대한 요청
        * Django Appilication을 통해 요청을 분석(URLconf)
        * 요청을 처리하는 기술(View) 실행을 통해 DB와 커뮤니케이션(Model)
        * 서버 작업을 수행하고 요청에 맞는 응답을 보낼 수 있는 Backend API를 구현
    
        
    Params
    -----------------
        djangoHttpxInstace:
            base_url: DJANGO_URL
            timeout: 2500 초를 할당해, 시간이 초과되면 TimeoutException
    """
    djangoHttpxInstance = httpx.AsyncClient(
        base_url=os.getenv("DJANGO_URL"),
        timeout=2500    
    )

    @classmethod
    async def post(
        cls, 
        endpoint: str, 
        data: dict) -> bool: # 타입 힌트(fastapi-> typehint를 적극 장려)
        
        """
        def 에 async 키워드를 붙이면 비동기 처리 -> 코루틴(coroutine)
            일반 동기 함수가 호출하듯이 호출하면 coroutine 객체가 리턴된다.

            비동기 함수는 일반적으로 `async`로 선언된 다른 비동기 함수 내에서 
            `await` 키워드를 붙여서 호출해야 한다(`await`는 비동기 함수나 코루틴
            의 실행을 일시 중단하고 다른 작업을 처리할 수 있도록 한다).

        * `async`로 선언되지 않은 일반 동기 함수(def) 내에서 비동기 함수를 호출하려면
            --> `asyncio.run`을 이용

        * coroutine ?
            1) 일반적으로 메인 함수는 서브 루틴을 호출한 뒤 서브 루틴의 작업이 끝날 때까지 기다린다.
                만약 서브 루틴이 파일 I/O 내지 대용량 파일 다운로드와 같은 작업을 수행한다면
                서브 루틴이 작업을 마칠 때까지 기다려야 한다.
            2) 이 기다림을 코루틴(Coroutine: Cooperative routine)이 보완해준다. 메인 루틴과 서브 루틴처럼
                종속된 관계가 아니라 서로 대등한 관계이며 특정 시점에 상대방의 코드를 실행하낟.
            3) 코루틴은 함수가 종료되지 않은 상태에서 메인 루틴의 코드를 실행한 뒤 다시 돌아와서 코루틴의
                코드를 실행한다. 따라서 코루틴이 종료되지 않았으므로 코루틴의 내용도 계속 유지된다. 일반 함수를
                호출하면 코드를 한 번만 실행할 수 있지만, 코루틴은 코드를 여러 번 실행할 수 있다.
        """
        url = f"{endpoint}"

        try:
            response = await cls.djangoHttpxInstance.post(url, json=data)

            if response.status_code == 200:
                return True
            else:
                print(f"Failed to send to Django: {response.status_code}")
                return False

        except httpx.RequestError as exc:
            print(f"An error occurred while sending to Django: {str(exc)}")
            return False