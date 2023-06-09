from django.db import models
from django.conf import settings

# Create your models here.

class Equipo(models.Model):
    nombre = models.TextField(default='', blank=False)
    fundacion = models.IntegerField(default=0)
    continente = models.TextField(default='', blank=False)
    trofeos = models.IntegerField(default=0)
    presidente = models.TextField(default='', blank=False)
    pais = models.TextField(default='', blank=False)
    liga = models.TextField(default='', blank=False)
    trofeosinte = models.IntegerField(default=0)
    trofeosloca = models.IntegerField(default=0)
    numerojuga = models.IntegerField(default=0)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    equipo = models.ForeignKey('equipos.Equipo', related_name='votes', on_delete=models.CASCADE)

