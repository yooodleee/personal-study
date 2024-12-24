from abc import abstractmethod, ABC


class BooksRepository(ABC):
    # 책에 대한 정보를 저장하는 리스트입니다.
    @abstractmethod
    def list(self):
        pass
    
    # 만들어줍니다(create)/ 무엇을 만들지는 아직 자세히 모르겠지만 일단 인자를 살펴보아요.
    # bookName(책이름), bookPrice(책가격), bookDescription(책 묘사), bookImage(책 이미지)
    # 위 4개의 인자로 보아 아마 책에 대한 정보(책 이름이 무엇이고, 가격은 어떻고, 책에 대한 소개글과 이미지 등등)를 생성해주는 메서드인 것 같아요.
    # 이런 느낌을 가지고 자세한 로직은 impl에서 살펴보도록 할게요.
    @abstractmethod
    def create(self, bookName, bookPrice, bookDescription, bookIamge):
        pass

    # BookId로 특정 정보를 찾는 것 같아요.
    # 우선 왜 특정 정보를 찾을 때 BookId를 기준으로 찾는 걸까요?
    # 테이블에서 Id는 고유한 값입니다.
    # 고유하다는 것은 서로 식별되므로 구별된다는 것이죠.
    # 이러한 특성때문에 Id를 기준으로 특정 정보를 구분짓는다면 쉽게 우리에게 필요한 정보를 구분짓고 찾을 수 있을 것 같습니다.
    @abstractmethod
    def findByBookId(self, bookId):
        pass