from django.db import models

# Create your models here.

class Clients (models.Model):
    type_CHOICES = (
        ('Premium','Premium'),
        ('Normal','Normal')
    )

    nombre = models.CharField(max_length=100)
    detalle = models.CharField(max_length=500,unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    tipo = models.CharField(choices = type_CHOICES, max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} - {self.email} - {self.tipo}'