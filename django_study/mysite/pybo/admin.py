from django.contrib import admin
from .models import Question, Answer

# Register your models here.

# 장고 admin에 데이터 검색 기능 추가하기
class QuestionAdmin(admin.ModelAdmin):
    serach_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)