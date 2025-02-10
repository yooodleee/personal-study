# controller를 살펴보기 전에 먼저 확인하고 넘어갈 부분이 있습니다.
# controller의 역할은 무엇일까요? -> controller는 쉽게 말해 요청을 처리해주는 역할을 합니다.
# 요청을 처리하는 순간에는 다양한 동작이 있을 겁니다(요청을 처리하기 위한)
# 그 요청을 처리해주는 로직을 쓰려면 무엇이 필요할지 생각해보면서 코드를 구성하면 좋을 것 같습니다.
# 우선 이 controller는 books에 대한 요청을 처리하는 부분입니다.
# 요청이라는 것은 결국 무엇이 필요하다는 의미이므로 아마 추측해보기로 책에 대한 정보를 등록하기 위한 요청을 처리해주는 것 같네요.
# 자세한 것은 코드를 읽어보면서 살펴보도록 할게요.

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from books.entity.books import Books
from books.serializers import BookSerizlier
from books.service.books_service_impl import BookServiceImpl

# viewsets를 사용하려면 rest_framework가 설정되어야 합니다.
# pip install djangorestframework
class BooksView(viewsets.ViewSet):
    queryset = Books.objects.all()
    booksService = BookServiceImpl.getInstance()

    # 인자로 보면 알수있듯이 request(요청하다)가 있습니다-> controller의 역할은 요청을 처리한다고 했었죠?
    def list(self, request):
        # bookList가 필요한 것 같네요-> Books 테이블의 모든 객체들을 가져와줍니다.
        booksList = Books.objects.all()
        # serializer-> 이 친구는 우리가 Django Rest Framework를 사용하면 등장하는 개념입니다.
        # 직렬화를 의미하는데 쉽게 말해, django에 저장되어 있는 모델 객체를 REST API에서
        # 사용하는 JSON 형태로 바꿔주는 것을 말합니다.
        # 우선 자세한 것은 BookSerizlier 테이블을 살펴봐야할 것 같고 그럼 계속해서 설명으로 넘어갈게요.
        serializer = BookSerizlier(booksList, many=True)
        # 렌더링되지 않은 객체를 불러와 클라이언트(우리)에게 리턴할 컨텐츠 형태(JSON)로 변환해줍니다.
        # render: 지정한 template(화면에 보여줄 UI?)을 띄움과 동시에 template에서 매핑한 변수를 사용할 수 있는 함수입니다.
        return Response(serializer.data)
    
    def register(self, request):
        # 책에 대한 정보들을 등록(register)하고 있네요.
        try:
            data = request.data

            bookImage = request.FILES.get('bookImage')
            bookName = data.get('bookName')
            bookPrice = data.get('bookPrice')
            bookDescription = data.get('bookDescription')

            # 만약 책에 대한 정보들 중에 하나라도 없다면-> 오류를 발생시키고, 책을 등록해줘야 합니다.
            # all() 메서드는 구조 내의 모든 요소가 참일 때만 True를 반환해주는 함수입니다.
            if not all([bookImage, bookName, bookPrice, bookDescription]):
                return Response({ 'error': '책을 등록해주세요!'}, status=status.HTTP_400_BAD_REQUEST)
            
            # 책 정보들을 등록해주어 새로 등록(저장된)책으로 처리합니다.
            savedBook = self.booksService.createBook(bookName, bookPrice, bookDescription, bookImage)

            # 저장된 책들을 JSON 형태로 처리해줍니다.
            serializer = BookSerizlier(savedBook)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            print({ 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    # 책 정보가 JSON 형태로 저장되있는 상태입니다.
    # 이 JSON을 읽어와줍니다.
    # 일단 이 정도만 알고 넘어갈게요(pass)
    def readBook(self, request, pk=None):
        book = self.booksService.readBook(pk)
        serilizer = BookSerizlier(book)
        return Response(serilizer.data)