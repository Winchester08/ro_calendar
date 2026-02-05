from django.db import models

class usuarios(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Nombre Usuario')
    apellidos = models.CharField(max_length=80, verbose_name='Apellido Usuario')
    tipo = models.CharField(max_length=30, verbose_name='Tipo Usuario')
    usuario = models.CharField(max_length=20, verbose_name='Usuario')
    clave = models.CharField(max_length=20, verbose_name='Clave Usuario')
