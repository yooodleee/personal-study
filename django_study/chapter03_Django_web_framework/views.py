"""
View = 로직 정의

장고는 웹 요청에 있는 URL을 분석하고, 그 결과로 해당 URL에 매팽된 뷰를 호출한다.

일반적으로 뷰는 웹 요청을 받아 데이터베이스 접속 등 해당 애플리케이션의 로직에 맞는 처리를 하고,
그 결과 데이터를 HTML로 변환하기 위해 탬플릿 처리를 한 후에, 최종 HTML로 된 응답 데이터를 웹 클라이언트로 반환하는 역할을 한다.

장고에서의 뷰는 함수 또는 클래스의 메서드로 작성되며, 웹 요청을 받고 응답을 반환해준다.
여기서 응답은 HTML 데이터일 수도 있고, 리다이렉션 명령일 수도 있고, 404 에러 메시지일 수도 있다.
다양한 형태의 응답 데이터를 만들어내기 위한 로직을 뷰에 작성하는 것이다.
이러한 뷰는 보통 views.py 파일에 작성하지만, 원한다면 다른 파일에 작성해도 무방하다.
다만 파이썬 경로에 있는 파일이어야 장고가 찾을 수 있다.

간단한 예로 현재의 날짜와 시간을 HTML로 반환해주는 뷰를 작성해보겠다.
"""
from django.http import HttpResponse, HttpResponseNotFound
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

'''
이 경우는 클래스가 아니라 함수로 뷰를 작성한 예시이다. 뷰 함수는 첫 번째 인자로 HttpResponse 객체(위에서는 request)를 받는다.
그리고 필요한 처리를 한 후에 최종적으로 HttpResponse 객체를 반환한다.

만일 에러를 반환하고 싶다면 아래처럼 HttpResponseNotFound와 같은 에러 응답 객체를 반환하면 된다.
에러 응답 클래스는 모두 HttpResponse 클래스의 하위 클래스로 정의되어 있다.

return HttpResponseNotFound('<h1>Page not found</h1>')
'''

'''
앞서의 예시는 HTML 코드를 뷰 함수내에 직접 사용했지만, 보통은 별도의 탬플릿 파일에 HTML 코드를 작성한다.
즉 뷰는 별도로 작성된 템플릿 파일을 해석해서 HTML 코드를 생성히고 이를 HttpResponse 객체에 담아서 클라이언트에게 응답한다.
MVT 방식의 마지막 요소인 템플릿(또는 템플릿 파일)에 대해서는 다음 절에서 설명한다.
'''