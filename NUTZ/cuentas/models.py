from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)
# Create your models here.

#LOS SIGUIENTES METODOS ESTAN ESCRITOS EN INGLES PORQUE SOBREESCRIBEN FUNCIONALIDAD DE LA CLASE QUEHEREDAN
class UsuarioManager(BaseUserManager):
    
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
    apellidos = models.CharField(max_length=2)
    nacimiento = models.DateField()

    #Información personal - a llenar despues
    ocupacion = models.CharField(max_length=255)
    nacionalidad = models.CharField(max_length=100)
    observacion = models.TextField(max_length=5000)
    ultima_atencion = models.DateTimeField()

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
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    nutri = models.BooleanField(default=False)

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
    # #CACHAÑA

    # def calcular_edad(fecha_nacimiento):
    #     """
    #     Devuelve la edad en entero del usuario segun su fecha de nacimiento
    #     """
    #     GRUPO_ETARIO = "Lactante"
    #     return ((0,1,15),GRUPO_ETARIO)

    # @property
    # def edad(self):
    #     GRUPO_ETARIOS = ("Lactante")
    #     return ((0,1,15),GRUPO_ETARIO)

    # EDAD = calcular_edad(nacimiento)
    # GRUPO_ETARIO = calcular_etario(EDAD)

 
    # def calcular_etario(fecha_nacimiento):
    #     """
    #     Devuelve el grupo etario basado en la cantidad de dias hasta la fecha 
    #     """
    #     pass
   
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rut','nombres','apellidos','nacimiento']

    #Funciones de utilidad
    
    def get_nombre(self):
        return self.email

    def get_nombre_completo(self):
        return self.nombres + self.apellidos

    def __str__(self):
        return self.email
    
    objects = UsuarioManager()