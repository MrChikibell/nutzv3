from django.db import models
from django.apps import apps
from cuentas.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Nutricionista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='nutricionista')
    info_nutri = models.CharField(max_length=254)
    def __str__(self):
        return self.user.rut + " - " +self.user.email

    def crear_paciente(self):
        # paciente.nutricionista = self
        Paciente = apps.get_model('paciente', 'Paciente')
        paciente = Paciente.objects.create(user=self.user, nutricionista = self)
        # paciente = paciente.save()
        print("Paciente Creado")
        return paciente


        
@receiver(post_save, sender=User)
def crear_usuario_nutricionista(sender, instance, created, **kwargs):
    if created:
        if instance.es_nutri:
            Nutricionista.objects.create(user=instance)
            print("EL USUARIO ES NUTRICIONISTA, CREANDO PERFIL NUTRICIONISTA")
        else:
            print("EL USUARIO NO ES NUTRICIONISTA")
            
        


