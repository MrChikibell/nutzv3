from django.db import models
from cuentas.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Paciente(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paciente')
    #Información personal - a llenar despues
    id_paciente = models.CharField(max_length=10)
    ocupacion = models.CharField(max_length=255)
    nacionalidad = models.CharField(max_length=100)
    observacion = models.TextField(max_length=5000)
    ultima_atencion = models.DateTimeField(null=True, blank=True)
    
    #informacion nutricional
    peso = models.IntegerField(default=0)

    #información bioquímica
    glicemia_mgdl = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.id_paciente

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Paciente.objects.create(user=instance)
        print("PACIENTE CREADO")

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.paciente.get(pk=instance.pk).save()
    # instance.paciente.all()[0].save()

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.paciente.observacion = 'Objservacion desde modelo'
    user.save()