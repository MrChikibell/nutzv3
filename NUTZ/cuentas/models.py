from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)
# Create your models here.


class UsuarioManager(BaseUserManager):
    def crear_usuario(self, email, password=None):
        """
        Crea y guarda el usuario con email y contraseña
        """
        if not email:
            raise ValueError('Los usuarios deben tener su email y contraseña')

        usuario = self.model(
            email=self.normalize_email(email),
        )

        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def crear_usuario_nutri(self, email, password):
        """
        Crea y guarda un usuario nutricionista con email y contraseña, utiliza la funcion de arriba
        """
        usuario = self.crear_usuario(
            email,
            password=password,
        )
        usuario.nutri = True
        usuario.save(using=self._db)
        return usuario

    def crear_usuario_admin(self, email, password):
        """
        Crea y guarda un super usuario dado email y contraseña
        """
        usuario = self.create_user(
            email,
            password=password,
        )
        usuario.nutri = True
        usuario.admin = True
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser):
    #Información personal - obligatiorios
    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=2)
    nacimiento = models.DateField()

    #Información personal - a llenar despues
    ocupacion = models.CharField(max_length=255)
    nacionalidad = models.CharField(max_length=100)
    observacion = models.TextField(max_length=5000)
    ultima_atencion = models.DateTimeField()

    # EDAD = calcular_edad(nacimiento)
    # GRUPO_ETARIO = calcular_etario(EDAD)

    # def calcular_edad(fecha_nacimiento):
    #     """
    #     Devuelve la edad en entero del usuario segun su fecha de nacimiento
    #     """
    #     pass
    # def calcular_etario(fecha_nacimiento):
    #     """
    #     Devuelve el grupo etario basado en la cantidad de dias hasta la fecha 
    #     """
    #     pass


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

    #informacion nutricional
    peso = models.IntegerField(default=0)

    #información bioquímica
    glicemia_mgdl = models.FloatField()

    #Permisos y accesos
    activo = models.BooleanField(default=True)
    admin = models.BooleanField(default=True)
    nutri = models.BooleanField(default=True)

    @property
    def esta_activo(self):
        return self.activo

    @property
    def es_nutri(self):
        return self.nutri
    
    @property
    def es_admin(self):
        return self.admin

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rut','nombres','apellidos']

    #Funciones de utilidad
    
    def get_nombre(self):
        return self.email

    def get_nombre_completo(self):
        return self.nombres + self.apellidos

    def __str__(self):
        return self.email
    
    objects = UsuarioManager()