from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre Cliente')
    direccion = models.CharField(
        max_length=50, verbose_name='Direccion Cliente')
    email = models.EmailField(blank=True, null=True,
                              verbose_name='Email Cliente')
    telefono = models.CharField(max_length=7, verbose_name='Telefono Cliente')


class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return (self.nombre, self.seccion, self.precio)


class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
