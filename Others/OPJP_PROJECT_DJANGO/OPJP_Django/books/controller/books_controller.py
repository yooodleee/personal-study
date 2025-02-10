from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status

from books.service.books_service_impl import BooksServiceImpl


# Create your views here.
class BooksController(viewsets.ViewSet):
    __bookService = BooksServiceImpl.getInstance()

    def requestBookList(self, request):
        try:
            bookListDataFrame = self.__bookService.bookList()
            print(
                f"bookListDataFrame: {bookListDataFrame}"
            )

            return JsonResponse(
                bookListDataFrame.to_dict(orient='records'),
                safe=False
            )
        
        except Exception as e:
            return JsonResponse(
                {"error": str(e)},
                status = status.HTTP_400_BAD_REQUEST,
            )
    
    def requestModiftBookDescription(self, request):
        isSuccess = self.__bookService.requestModifyBookDescription()

        if isSuccess:
            return JsonResponse({"success": True})
        else:
            return JsonResponse(
                {"success": False, "error": "Failed to modify book description"},
                status = status.HTTP_400_BAD_REQUEST,
            )