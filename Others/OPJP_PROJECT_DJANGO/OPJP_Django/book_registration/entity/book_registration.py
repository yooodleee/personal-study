from django.db import models

from books.entity.books import Books


# Create your models here.
class BookRegistration(models.Model):
    bookregistrationId = models.AutoField(primary_key=True)
    bookName = models.ForeignKey(
        Books, on_delete=models.CASCADE, related_name='book_registration'
    )
    bookCount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.bookName} - {self.bookCount}"
    
    class Meta:
        db_table = 'book_registration'
        app_label = 'book_registration'