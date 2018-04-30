from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Paciente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    peso = models.IntegerField(default=0)

    def __str__(self):
        return self.rut