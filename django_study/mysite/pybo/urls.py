from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    # int:는 question_id에 숫자가 매핑되어 있음을 의미한다.
    path('<int:question_id>/', views.detail),
]

""" * /pybo/2/ 페이지가 호출되면 장고에서 벌어지는 일

(1) localhost:8000/pybo/2를 입력한다.
(2) config/urls.py에서 pybo/를 매핑한다.
(3) pybo/urls.py에서 2/를 매핑한다(<int:question_id>에 2를 매핑)
(4) pybo/views.py의 detail 함수의 매개변수 question_id로 2가 전달됨
"""
