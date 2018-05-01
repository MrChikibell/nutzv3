from django.db import models
from cuentas.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Paciente(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paciente')
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    #Información personal - a llenar despues
    ocupacion = models.CharField(max_length=255)
    nacionalidad = models.CharField(max_length=100)
    observacion = models.TextField(max_length=5000)
    ultima_atencion = models.DateTimeField(null=True, blank=True)
    
    #informacion nutricional
    peso = models.IntegerField(default=0)

    #información bioquímica
    glicemia_mgdl = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.user.email

@receiver(post_save, sender=User)
def crear_paciente(sender, instance, created, **kwargs):
    if created:
        Paciente.objects.create(user=instance)
        

@receiver(post_save, sender=User)
def guardar_paciente(sender, instance, **kwargs):
    instance.paciente.save()


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.paciente.observacion = 'Observacion desde modelo'
    user.save()