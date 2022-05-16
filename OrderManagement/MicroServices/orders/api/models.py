from django.db import models

# Create your models here.


class Orders(models.Model):
    productName = models.CharField(max_length=100)
    productId = models.IntegerField()
    productQuantity = models.IntegerField(default=0)
    productPrice = models.FloatField(default=0.00)
    Amount = models.FloatField(default=0.00)



