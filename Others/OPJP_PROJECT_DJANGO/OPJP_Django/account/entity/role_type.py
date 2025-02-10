from django.db import models


# Create your models here.
class RoleType(models.TextChoices):
    ADMIN = 'ADMIN'
    NORMAL = 'NORMAL'
    SUBSCRIBE = 'SUBSCRIBE'