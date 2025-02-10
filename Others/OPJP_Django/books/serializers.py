from rest_framework import serializers

from books.entity.books import Books


# 실제 사용할 데이터의 형식이 무엇인지를 알려줍니다.
class BookSerizlier(serializers.ModelSerializer):
    class Meta:
        # Books 테이블
        model = Books  
        # 필드 값(책을 등록하기 위해 필요한 정보들)
        fields = ['bookId', 'bookName', 'bookPrice', 'bookDescription', 'bookImage', 'registeredDate', 'updatedDate']
        # 이 부분은 일단 pass할게요.
        read_only_fields = ['registeredDate', 'updatedDate']