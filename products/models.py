from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    detalle = models.CharField(max_length=500)
    price = models.FloatField()
    stock = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    
   
    


