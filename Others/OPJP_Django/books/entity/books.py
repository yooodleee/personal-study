from django.db import models


# Books 테이블을 생성해줄게요. bookmark에서와 마찬가지로 책에 대한 정보를 등록하고자 할 때 필요한 정보는 무엇일지 생각해보아요.
class Books(models.Model):
    # 장고(Django)에서는 우선 모델을 생성과 동시에 Id를 자동적으로 생성해주지만 일단 적어볼게요.
    bookId = models.AutoField(primary_key=True)
    # 책 이름(max_length는 최대 길이를 지정해주고, null=False로 빈 값이 아니게 해줍니다-> 빈 값이라면 오류가 발생하겠죠?책 정보인데 책 이름이 없으니...)
    bookName = models.CharField(max_length=128, null=False)
    # 책에 대한 묘사? 기술? 소개글? 정도라고 할게요.
    bookDescription = models.TextField()
    # 책 이미지도 넣어주도록 하겠습니다.
    bookImage = models.CharField(max_length=100, null=True)

    # 추후 이미지 관련 필드 추가(일단 이 2개는 pass하도록 할게요.)
    registeredDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    # 책 Id를 가져와줍니다.
    def getId(self):
        return self.bookId
    
    # 익숙한 클래스가 등장했네요. 만약 기억이 나지 않으시다면 bookmark/entity에서도 언급되었던 메타 클래스를 참고해보세요!
    class Meta:
        db_table = 'books'
        app_label = 'books'
        