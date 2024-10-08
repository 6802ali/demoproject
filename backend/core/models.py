from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    price = models.IntegerField(default=10)
