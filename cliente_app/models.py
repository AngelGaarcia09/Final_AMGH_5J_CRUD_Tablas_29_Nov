from django.db import models

# Create your models here.
class Cliente(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    apellidom=models.CharField(max_length=100)
    cuenta=models.CharField(max_length=100)
    apellidop=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre