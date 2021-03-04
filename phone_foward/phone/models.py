from django.db import models

# Create your models here.
class Func(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    alias = models.CharField(max_length=40)
