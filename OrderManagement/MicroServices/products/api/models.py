from django.db import models

# Create your models here.


class Products(models.Model):
    productName = models.CharField(max_length=100)
    productCategory = models.CharField(max_length=100)
    productQuantity = models.IntegerField(default=0)
    productPrice = models.FloatField(default=0.00)
    productDesc = models.CharField(max_length=200)


