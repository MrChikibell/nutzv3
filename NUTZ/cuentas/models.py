from django.db import models
import datetime

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)
# Create your models here.

#LOS SIGUIENTES METODOS ESTAN ESCRITOS EN INGLES PORQUE SOBREESCRIBEN FUNCIONALIDAD DE LA CLASE QUEHEREDAN
class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None):
        """
        Crea y guarda un usuario segun su email y contraseña
        """
        if not email:
            raise ValueError('Debes ingresar un email correcto.')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Crea y guarda un usuario staff con email, contraseña.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Crea y guarda un superusuario con email y contraseña
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

    def create_nutricionista(self, email, password):
        """
        Crea un usuario nutricionista
        """
        user = self.create_user(
            email,
            password=password
        )
        user.staff = True
        user.nutri = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    #Información personal - obligatiorios
    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)
    nacimiento = models.DateField(null=True, blank=True)

    M = 'M'
    F = 'F'
    GENEROS = (
        (M, 'Masculino'),
        (F, 'Femenino')
    )
    genero = models.CharField(max_length=2, choices=GENEROS, default=F)

    email = models.EmailField(
        verbose_name = 'Correo electrónico',
        max_length=100,
        unique=True
    )

    #Permisos y accesos
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    nutri = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #'rut','nombres','apellidos','nacimiento'
    objects = UserManager()
    #PROPIEDADES
    @property
    def is_staff(self):
        "¿Es el usuario staff?"
        return self.staff

    @property
    def is_admin(self):
        "¿Es el usuario administrador?"
        return self.admin

    @property
    def is_active(self):
        "Esta el usuario activo?"
        return self.active

    @property
    def es_nutri(self):
        "¿Es el usuario nutricionista?"
        return self.nutri
    
    def has_perm(self, perm, obj=None):
        """
        Tiene permisos ?
        """
        return True

    def has_module_perms(self, app_label):
        """
        Aca vamos a restringir accesos a ciertos modulos
        """
       
        return True

    def get_nombre(self):
        """
        Devuelve un string email
        """
        return self.email

    def get_nombre_completo(self):
        """
        Devuelve nombre y apellidos
        """
        return self.nombres + self.apellidos
    
    def __str__(self):
        """
        Al imprimir el objeto
        """
        string = "{} - {}".format(self.rut, self.email) 
        return string
    
    