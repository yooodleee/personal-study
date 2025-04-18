from django.db import models

# Create your models here.
class InterviewQuestion(models.Model):
    question = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.question[:50]