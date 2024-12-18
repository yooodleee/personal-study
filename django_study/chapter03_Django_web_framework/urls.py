"""
URLconf = URL 정의

클라이언트로부터 요청을 받으면 장고는 가장 먼저 요청에 들어있는 URL을 분석한다.
즉, 요청에 들어있는 URL이 urls.py 파일에 정의된 URL 패턴과 매칭되는지를 분석한다.

파이썬의 URL 정의 방식은 전통적인 자바나 PHP 계열의 URL보다 직관적이고 이해하기가 쉽다.
그래서 이런 방식을 우아한 URL이라고 부른다. URL을 정의하기 위해서 다음처럼 urls.py에 URL과 처리 함수(view)를 매핑하는 파이썬 코드를 작성한다.
이러한 URL/view 매핑을 URLconf라고 한다.
"""
from django.urls import path

from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>', views.articles_detail),
]

'''
위 예시에서 articles/2003/ 부분이 URL이고, views.special_2003 부분이 처리함수(view)이다.

이와 같이 URL과 처리 함수를 별도로 정의하고, 이 둘을 매핑하는 방법은 개발자에게 많은 유연성을 제공한다.
URL 자체에 처리 함수나 처리용 스크립트 파일 이름이 들어가면 변경이 어려워지기 때문이다.
반면 URLconf를 사용하면 URL과 뷰 함수를 서로 자유롭게 연결할 수 있어서 규모가 큰 프로젝트를 개발할 때처럼 URL과 뷰 함수 이름이 자주
바뀌는 경우에도 URLconf에서 매핑한 부분만 수정하면 되므로 변경이 쉬워진다.

웹 클라이언트가 웹 서버에 페이지 요청 시, 장고에서 URL을 분석하는 순서를 간단히 요약하면 다음과 같다.

* setting.py 파일의 ROOT_URLCONF 항목을 읽어 최상위 URLconf(urls.py)의 위치를 알아낸다.
* URLconf를 로딩하여 urlpatterns 변수에 지정되어 있는 URL 리스트를 검사한다.
* 위에서부터 순서대로 URL 리스트의 내용을 검사하면서 URL 패턴이 매치되면 검사를 종료한다.
* 매치된 URL 뷰를 호출한다. 여기서 뷰는 함수 또는 클래스의 메서드이다. 호출 시 HttpRequest 객체와 그리고, 매칭할 때 추출된 단어들을 뷰에 인자로 넘겨준다.
* URL 리스트 끝까지 검사했는데도 매칭에 실패하면 에러를 처리하는 뷰를 호출한다.

위의 예제를 보면 URL 패턴을 정의할 때 <int:year>처럼 꺽쇠를 사용하는 부분이 있다.
이는 URL 패턴의 일부 문자열을 추출하기 위한 것이며, <type:name> 형식으로 사용한다.
예를 들어 다음 라인의 의미는, 요청 URL이 /articles/2018/처럼 <> 부분이 정수이면 매치되고 /articles/post/처럼 정수가 아니면 매치되지 않는다.
또한 매치된 경우에는 매치된 문자열 2018을 인자명 year에 할당한다.
즉, 요청 URL이 /articles/2018/이면 뷰 함수를 views.year_archive(request, year=2018)처럼 호출한다.
'''
path('articles/<int:year>/', views.year_archive),

'''
<> 부분을 장고에서는 Path Converter라고 부르는데, 여기에 사용되는 타입은 다음과 같다.
물론 개발자가 추가로 타입을 등록할 수도 있다.

* str: /(슬래시)를 제외한 모든 문자열과 매치된다. 타입이 지정되지 않았다면 디폴트로 str 타입을 사용한다.
* int: 0 또는 양의 정수와 매치된다. 매치된 정수는 파이썬의 int 타입으로 변환된다.
* slug: slug 형식의 문자열(ASCII, 숫자, 하이픈, 밑줄로만 구성됨)과 매치된다.
* uuid: UUID 형식의 문자열과 매치된다. 매치된 문자열은 파이썬의 UUID 타입으로 변환된다.
* path: /(슬래시)를 포함한 모든 문자열과 매치된다. 이는 URL 패턴의 일부가 아니라 전체를 추출하고자 할 때 많이 사용한다.

URL 패턴에 정규표현식(Regular Expression)을 사용하면 URL을 좀 더 세밀하게 표현하거나, 복잡한 URL도 표현할 수 있다.
예컨대, 정규표현식을 사용하여 앞서의 예시와 동일한 URL 패턴을 작성하면 다음과 같다.
'''
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    re_path(r'^articles/(?P<year>[0-9]{4})$', views.year_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.articles_detail),
]