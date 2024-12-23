from rest_framework import serializers

from books.entity.books import Books


# 실제 사용할 데이터의 형식이 무엇인지를 알려줍니다.
class BookSerizlier(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['bookId', 'bookName', 'bookPrice', 'bookDescription', 'bookImage', 'registeredDate', 'updatedDate']
        read_only_fields = ['registeredDate', 'updatedDate']