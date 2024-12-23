# BookMark 테이블에 생성했었던 정보들을 사용해봅시다.
from bookmark.entity.bookmark import BookMark
# bookmark_repository에서는 메서드들을 단순히 '정의(생성)'만 했기 때문에 이 파일에서 그 메서드들에 대한 
# 자세한 기능들을 구현해봅시다.
from bookmark.repository.bookmark_repository import BookmarkRepository


class BookmarkRepositoryImpl(BookmarkRepository):
    # 보통 _(언더바)는 개수(1개, 2개)에 따라 의미가 다릅니다.
    # 우선 한개인 경우, 해당 클래스를 상속받은 클래스에서만 접근이 가능하도록 하지만 이를 강제하지는 않습니다.
    # 두개인 경우, 외부에서 클래스 속성값에 접근할 수 없게 할 때(private), 그리고 오버라이딩을 제한합니다.
    # 우리의 경우, 두개를 지정해주었는데, BookmarkRepositoryImpl 클래스 내에서만 사용하므로 언더바 2개를 지정해줍니다.
    __instance = None

    # __new__는 클래스 자기 자신을 인자로 받습니다. 주로 cls라고 선언하죠.
    # 자세한 내용은 -> https://reo91004.tistory.com/232
    def __new__(cls):
        # 만약, 객체의 인스턴스가 없다면 새로운 인스턴스를 생성해줍니다.
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance
    
    # 위에서 생성해준 __instance는 싱글턴 패턴입니다.
    # BookmarkRepositoryImpl이라는 클래스에서만 사용할 예정입니다.
    # 만약 이 싱글턴을 아래 메서드에서 재사용하고 싶다면 getInstance라는 메서드를 생성과 동시에
    # 위에 @classmethod라는 것을 적어줍니다(쉽게 말해 싱글턴을 재사용한다는 의미이죠.) 
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    # BookMark 테이블의 account(사용자 계정)에 대한 객체를 생성해줍니다.
    def register(cls, account):
        return BookMark.objects.create(account=account)
    
    def findByAccount(self, account):
        # try에서 BookMark 테이블에서 account(사용자 계정) 객체를 생성해주려고 합니다.
        try:
            return BookMark.objects.get(account=account)
        # 만약 BookMark라는 테이블이 존재하지 않다면(있어야 할 테이블이 없으므로 오류가 발생한 경우라고 할 수 있죠)
        # None(아무것도 없음, 무)을 반환합니다.
        except BookMark.DoesNotExist:
            return None