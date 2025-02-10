from django.db import models


# Create your models here.
class Books(models.Model):
    bookId = models.AutoField(primary_key=True)
    bookName = models.CharField(max_length=128, null=False)
    bookDescription = models.TextField()
    bookImage = models.CharField(max_length=100, null=True)
    bookPrice = models.IntegerField(null=True, blank=True)

    # 추후 이미지 관련 필드 추가
    registeredDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"BookData {self.bookName} ({self.bookDescription})"
    
    def getId(self):
        return self.bookId
    
    class Meta:
        db_table = 'books'
        app_label = 'books'