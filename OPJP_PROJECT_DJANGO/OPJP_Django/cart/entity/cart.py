from django.db import models

from account.entity.account import Account
from books.entity.books import Books


# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    books = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'cart'
        app_label = 'cart'

    def __str__(self):
        return f"Cart(id={self.id}, account={self.account})"
    
    def getId(self):
        return self.id
    
    def getAccount(self):
        return self.account