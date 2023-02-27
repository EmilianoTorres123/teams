from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.TextField(default='', blank=False)
    fundacion = models.IntegerField(default='', blank=False)
    continente = models.TextField(default='', blank=False)
    trofeos = models.IntegerField(default=0)
    presidente = models.TextField(default='', blank=False)
    pais = models.TextField(default='', blank=False)
    liga = models.TextField(default='', blank=False)
    trofeosinte = models.IntegerField(default=0)
    trofeosloca = models.IntegerField(default=0)
    numerojuga = models.IntegerField(default=0)

