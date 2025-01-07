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
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm


def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'POST':
        form = AnswerForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()

            return redirect(
                'pybo:detail', question_id=question_id
            )
    else:
        form = AnswerForm()
    context = {
        'question': question,
        'form': form,
    }
    return render(
        request, 'pybo/question_detail.html', context
    )


def question_create(request):
    """
    pybo 질문 등록
    """

    # form = QuestionForm()
    # return render(
    #     request,
    #     'pybo/question_form.html',
    #     {'form': form},
    # )

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(
        request, 'pybo/question_form.html',
        context,
    )