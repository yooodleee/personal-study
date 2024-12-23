# 파일들을 잘 살펴보면 예컨대, bookmark_repository.py와 bookmark_repository_impl.py 이 있는 것을 알 수 있습니다.
# 첫 번째 파일에서는 단순히 메서드를 명시해주고(생성만!) 메서드에 대한 자세한 기능들은 두 번째 파일에서 기술합니다.
# abstractmethod 기능을 사용하기 위해서는 abc라는 모듈을 가져옵니다(abc=Abstract Base Class).
from abc import ABC, abstractmethod


# BookmarkRepository(클래스명)을 보면 알 수 있듯이 대부분 해당 파일의 이름과 동일하게 이름을 사용합니다.
class BookmarkRepository(ABC):
    # abstractmethod(추상 클래스)는 메서드의 목록만 가진 클래스이며, 상속빋는 클래스에서 메서드 구현을 강제하기 위해 사용합니다.
    # 위에서 말했듯이, 이 파일은 메서드만 생성해주는 파일입니다. 자세한 로직은 생략하죠. 그래서 자세한 로직 기술은 pass(패스!)합니다.
    @abstractmethod
    # register라는 이름을 생각해봅시다.
    def register(cls, account):
        pass

    @abstractmethod
    # findByAccount라는 이름을 생각해봅시다.
    # account를 왜 사용할까요? 어디에 쓰이는 걸까요?
    # 이렇게 생각해보면서 impl 파일을 읽으시면 더욱 좋을 것 같아요.
    def findByAccount(self, account):
        pass