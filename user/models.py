from django.db import models

# Create your models here.
class User(models.Model):
    login = models.CharField(max_length = 16)
    password = models.CharField(max_length = 8)
    sex = models.CharField(max_length = 5)