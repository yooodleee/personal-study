# django에서 모델은 데이터에 대한 하나의 정보 소스입니다.
# 모델은 저장하고 있는 데이터의 필수적인 필드와 동작(메서드)을 포함하고 있습니다.
# 일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 Mapping 됩니다.
from django.db import models

# 우선, bookmark(일종의 즐겨찾기?) 테이블을 만들기위해서 Account(사용자 계정에 대한)에 대한 테이블 정보를 가져올게요. 
from kakao_account.entity.account import Account
# Books(책에 대한 정보) 테이블 정보도 가져올게요~
from books.entity.books import Books


# BookMark 테이블을 만들어줍니다(우선 BookMark 테이블에 필요한(북마크 기능에 필요한) 정보와 기능들에 대해 생각해보죠.)
class BookMark(models.Model):
    # 우선 Id-> Django에서는 테이블을 생성과 동시에 자동적으로 Id가 생성됩니다. 그래서 굳이 Id를 생성해주지 않아도 되지만,
    # 일단 가독성(팀 협업)을 위해 명시하도록 할게요.
    bookmarkId = models.AutoField(primary_key=True)
    # account(사용자 계정)은 Account 테이블에 있던 정보죠? 이 정보를 BookMark 테이블에서 다시 생성하기보다
    # 이미 생성했었던 정보이므로 참조(ForeignKey)하도록 할게요. 아래 정보들도 생성되었던 정보들이므로 모두 
    # 참조해줍니다.
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='bookmarks')
    bookName = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='bookmarks')
    bookImage = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='bookmarks')
    # serializer에 필요한 Date(날짜)를 생성하고 업데이트해줍니다(이 설명은 일단 추후에 하도록 할게요...)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    # __str__ 메서드는 문자열을 출력합니다.
    # 여기서는 "" 안의 문자열을 출력하는데, 각각 위의 테이블에서 생성했었던 bookmarkId와 account를 출력해줍니다.
    def __str__(self):
        return f"Bookmark -> id: {self.bookmarkId}, account: {self.account.id}"
    
    # 파이썬에선 클래스도 객체입니다.
    # 클래스도 객체라면 클래스를 만드는 또 다른 클래스가 있는데, 이를 "메타 클래스"라고 부릅니다.
    # 이는, 클래스로 객체를 만들 듯 메타 클래스로 클래스를 만들 수 있다는 의미입니다.
    # 자세한 내용은 -> https://wikidocs.net/21056 를 참조하세요~
    class Meta:
        db_table = 'bookmark'
        app_label = 'bookmark'
    
    # 대부분의 메서드(def)는 동사를 사용합니다. 즉, 이름에서 대략 그 메서드의 기능을 생각해볼 수 있음을 의미합니다.
    # 메서드의 구조가 너무 복잡할 때, 그 메서드의 흐름만 알고 싶다면 메서드의 이름을 생각해보면서 흐름을 읽으면 좋을 것 같네요~
    # 이 메서드는 getAccount인 것으로 보아, 사용자 정보를 가져오는 기능을 수행하는 것으로 보이네요.
    def getAccount(self):
        # BookMark 테이블에서 선언했던 account에 대한 정보를 가져옵니다.
        return self.account