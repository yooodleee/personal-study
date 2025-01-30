from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response

from interview.service.interview_service_impl import InterviewServiceImpl


class InterviewView(viewsets.ViewSet):
    interviewService = InterviewServiceImpl.getInstance()

    def insertSession(self, request):
        # session을 interviewSerivce에 추가.
        isSaved = self.interviewService.insertSession()
        return Response(
            isSaved, 
            status=status.HTTP_200_OK
        )

    def insertFirstQuestion(self, request):
        # firstQuestion을 interviewService에 추가.
        isSaved = self.interviewService.insertFirstQuestion()
        print("첫 번째 질문 Insert 완료")
        return Response(
            isSaved, 
            status=status.HTTP_200_OK
        )

    def insertTechQuestion(self, request):
        # TechQuestion을 interviewService에 추가.
        isSaved = self.interviewService.insertTechQuestion()
        print("기술적 역량 질문 Insert 완료")
        return Response(
            isSaved, 
            status=status.HTTP_200_OK
        )

    def getSession(self, request):
        # sessionId 필드를 가져옴.
        sessionId = request.data.get('sessionId')
        print('데이터를 잘 불러왔나?:', sessionId)
        # sessionId 필드를 interviewService에서 가져옴.
        questionList = self.interviewService.getSession(sessionId)
        return Response(
            {'questionList': questionList}, 
            status=status.HTTP_200_OK
        )

    def getFirstQuestion(self, request):
        # 'questionId' 필드를 가져옴.
        questionId = request.data.get('questionId')
        print('questionId:', questionId)
        # questionId 필드를 interviewService에서 가져옴.
        firstQuestion = self.interviewService.getFirstQuestion(questionId)
        return Response(
            {'firstQuestion': firstQuestion}, 
            status=status.HTTP_200_OK
        )

    def getTechQuestion(self, request):
        # 'job' 필드의 '_value'를 가져옴.
        job = request.data.get('job').get('_value')

        print('job:', job)
        # job 필드를 interviewService에서 가져옴.
        techQuestion = self.interviewService.getTechQuestion(job=job)
        return JsonResponse(
            techQuestion, 
            safe=False, 
            status=status.HTTP_200_OK
        )
