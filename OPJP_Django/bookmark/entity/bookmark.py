from django.db import models

from kakao_account.entity.account import Account
from books.entity.books import Books


class BookMark(models.Model):
    bookmarkId = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='bookmarks')
    bookName = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='bookmarks')
    bookImage = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='bookmarks')
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bookmark -> id: {self.bookmarkId}, account: {self.account.id}"
    
    class Meta:
        db_table = 'bookmark'
        app_label = 'bookmark'
    
    def getAccount(self):
        return self.account