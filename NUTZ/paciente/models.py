from django.db import models
from cuentas.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='paciente')
    #Información personal - a llenar despues
    ocupacion = models.CharField(max_length=255)
    nacionalidad = models.CharField(max_length=100)
    observacion = models.TextField(max_length=5000)
    #.
    #.
    #.
    ultima_atencion = models.DateTimeField(null=True, blank=True)
    #informacion nutricional
    #.
    #.
    #.
    peso = models.IntegerField(default=0)
    #información bioquímica
    #.
    #.
    #.
    glicemia_mgdl = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.user.rut + " - " +self.user.email

        
@receiver(post_save, sender=User)
def crear_paciente(sender, instance, created, **kwargs):
    if created:
        if instance.es_paciente:
            Paciente.objects.create(user=instance)
            print("EL USUARIO ES PACIENTE, CREANDO PERFIL PACIENTE")
        else:
            print("EL USUARIO NO ES PCIENTE")
        

        


