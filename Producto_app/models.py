from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    precio=models.CharField(max_length=100)
    tipoprod=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    lote=models.CharField(max_length=100)
    marca=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre