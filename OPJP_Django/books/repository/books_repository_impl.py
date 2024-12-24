# 혹시 OS에 대해 알고 계신가요? 쉽게 말해 OS는 operating system(운영체제)입니다.
# os 모듈은 운영 체제의 종속 기능을 사용하게 해줍니다.
# 종종 파일을 읽고 쓰고 싶을 경우에는 open()을, 경로를 조작하려면 os.path() 모듈을 사용할 수 있게 해주죠.
# 이 외에도 다양한 모듈을 지원해줍니다.
# 자세한 내용은 -> https://docs.python.org/ko/3.10/library/os.html
import os

# 루트 디렉토리(OPJP_Django)에 있는 settings에서 무언가 필요한 게 있나보네요.
# 일단 자세한 건 아래 로직 흐름을 읽어보면서 무엇이 필요해서 settings를 가져온건지
# 생각해보아요.
from OPJP_Django import settings
# 책 정보를 가져와줍니다.
from books.entity.books import Books
# BooksRepository에서 abstractmethod(추상 메서드)으로 정의된 메서드들을
# 이번에는 자세하게 로직을 쓰기 위해 임포트해줄게요.
from books.repository.books_repository import BooksRepository


class BookRepositoryImpl(BooksRepository):
    # 싱글턴을 선언해줍니다-> 싱글턴의 장점도 생각해보면 좋을 것 같네요(ex. 재사용성)
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance
    
    # 싱글턴을 사용하기 위해서는?-> @classmethod
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    # list(책 정보를 담을)
    # 반환하는 값을 살펴보니 Books 테이블의 모든 객체들을 가져오는데
    # 'registerDate' 등록된 날 순으로 정렬된 정보들을 리스트에 담아주고 있군요.
    def list(self):
        return Books.objects.all().order_by('registerDate')
    
    # 책 정보를 만들어주는 메서드네요. 아래로 가면서 자세하게 살펴볼게요.
    def create(self, bookName, bookPrice, bookDescription, bookImage):
        # 책 정보가 업로드(갱신)되는 경로를 지정해주는 것 같아요.
        # 책 정보가 어디로 업로드되는지 지정해주어야 겠죠?
        # os.path.join은 쉽게 말해 settings에서 정의했던 BASE_DIR(원래 경로)와 # 무엇을 넣어야 할까요?
        # 부분을 조인(결합)함으로써 경로를 임의로 지정해주는 것 같아요.
        # 이 부분에 대한 이해는 일단 아~이렇구나!라는 느낌만 남기고 넘어가셔도 좋을것 같네요.
        uploadDirectory = os.path.join(
            settings.BASE_DIR,
            # 무엇을 넣어야 할까요?
        )
        # 만약 업로드될 경로가 존재하지 않는다면 새로 만들어줍니다.
        if not os.path.exists(uploadDirectory):
            os.makedirs(uploadDirectory)
        
        # 책 이미지를 저장해줄 경로도 지정해줍니다.
        imagePath = os.path.join(uploadDirectory, bookImage.name)
        # 책 이미지 파일을 destination이란 이름으로 open하는데
        # 이때 우리는 파일을 열때 모드를 지정해줄 수 있습니다(여기서는 'wb+'모드로 열어주었네요.)
        # 모드에 대한 자세한 내용은 -> https://kimdoky.github.io/python/2017/11/28/python-file_object/
        with open(imagePath, 'wb+') as destination:
            # chunk는 쉽게 말해 작은 단위로 나누어주는 개념입니다.
            # 여기서는 bookImage가 한 두개가 아니다보니 나누어준 것 같아요.
            for chunk in bookImage.chunks():
                # 우리가 열었던 파일들에 chunk(작은 단위로 쪼갠)한 bookImage들을 등록해줍니다.
                # 한 번에 너무 많은 bookImage들을 등록한다면 무슨 일이 벌어질까요?
                # 아마도 뒤죽박죽될 것 같네요.
                destination.write(chunk)
            
            # flush()는 파일 쓰기 작업(write) 도중 쓰여지는 내용을 확인해주는 메서드입니다.
            # bookImage가 잘 등록되고 있는지 확인해주는 것이죠~
            destination.flush()
            # fsync는 쉽게 말해 우리가 작업한(write) 파일들을 디스크에 기록해주는 메서드입니다.
            # fileno()는 스트림 파일 설명자를 숫자로 반환해줍니다.
            # 자세한 설명은-> https://homzzang.com/b/py-253
            os.fsync(destination.fileno())
        
        # 책 정보들을 등록하고 있는 것 같네요.
        book = Books(
            bookName=bookName,
            bookDescription=bookDescription,
            bookPrice=bookPrice,
            bookImage=bookImage.name
        )
        # 등록된 책 정보들을 저장해줍니다.
        book.save()

        # 저장된 책 정보들이 필요할 때 bookId(고유한 식별되는 값)로 참조합니다.
        savedBook = Books.objects.get(bookId=book.bookId)
        print(f"savedBook: {savedBook.bookImage}")
        return savedBook
    
    # findByBookId는 어떤 기능을 할지 생각해봅시다.
    def findByBookId(self, bookId):
        try:
            return Books.objects.get(bookId=bookId)
        except Books.DoesNotExist:
            return None