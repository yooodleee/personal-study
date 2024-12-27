from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    # Question 모델 데이저 조회 결과에 속성값 보여 주기
    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

"""
>>> python manage.py shell

in [1]: from pybo.models import Question, Answer

in [2]: from django.utils import timezone

in [3]: q = Question(
                subject='pybo가 무엇인가요?',
                content='pybo에 대해서 알고 싶습니다.',
                create_date=timezone.now())

in [4]: q.save()

>>> q.id
1

>>> q = Question(
            subject='장고 모델 질문입니다.',
            content='id는 자동으로 생성되나요?',
            create_date=timezone.now())

>>> q.save()
>>> q.id
2

>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>, <Question: Question object (2)>]>
"""

