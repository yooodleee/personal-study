from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status

from book_registration.service.book_registration_service_impl import BookRegistrationServiceImpl


# Create your views here.
class BookRegistrationController(viewsets.ViewSet):
    __bookRegistrationService = BookRegistrationServiceImpl.getInstance()

    def requestCreateBookRegistrationData(self, request):
        isSuccess = self.__bookRegistrationService.createBookRegistration()

        return JsonResponse({ 'success': isSuccess})
    
    def requestBookRegistrationList(self, request):
        try:
            bookRegistrationDataFrame = self.__bookRegistrationService.bookRegistrationList()
            print(
                f"bookRegistrationDataFrame: {bookRegistrationDataFrame}"
            )
            return JsonResponse(
                bookRegistrationDataFrame.to_dict(orient='records'),
                safe=False,
            )
        
        except Exception as e:
            return JsonResponse(
                {"error": str(e)},
                status = status.HTTP_400_BAD_REQUEST,
            )