from django.db import models

# Create your models here.


class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDesc = models.CharField(max_length=200)