from django.db import models
from cuentas.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Paciente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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
        return self.user.rut

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Paciente.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()