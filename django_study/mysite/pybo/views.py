from django.http import HttpResponse
# 모델 데이터를 템플릿 파일을 사용해 화면에 출력함-> render
from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.
def index(request):
    """pybo 목록 출력"""

    # Question 모델 데이터 작성일시 역순으로 조회하기(-create_date)
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    
    # render로 화면 출력하기기
    return render(request, 'pybo/question_list.html', context)
    # return HttpResponse("안녕하세요 pybo에 오신 것을 환영합니다.")

""" *render()

context에 있는 Question 모델 데이터 question_list를 pybo/question_list.html 파일에 적용해 
HTML 코드로 변환함.
장고에서는 이런 파일(pybo/question_list.html)을 템플릿이라 부름.
장고의 태그를 추가로 사용할 수 있는 HTML 파일이라고 생각하면 됨.
"""

def detail(request, question_id):
    """pybo 내용 출력"""

    # 존재하지 않는 페이지에 접속하면 오류 대신 404 페이지 출력
    # 모델의 기본키를 이용하여 모델 객체 한 건을 반환함
    # pk에 해당하는 건이 없으면 오류 대신 404 페이지를 반환(Not Found)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)