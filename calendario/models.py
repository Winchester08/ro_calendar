from django.db import models

# Create your models here.
class evento(models.Model):
    fecha = models.CharField(max_length=30, verbose_name='Fecha Evento')
    hora = models.CharField(max_length=10, verbose_name='Hora Evento')
    descripcion = models.TextField(max_length=150, verbose_name='Descripcion')
    estado = models.CharField(max_length=20, verbose_name='Esatus')