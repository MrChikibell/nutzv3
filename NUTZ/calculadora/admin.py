from django.contrib import admin

from .models import Alimento, GrupoAlimento, Calculadora

# Register your models here.

admin.site.register(Alimento)
admin.site.register(GrupoAlimento)
admin.site.register(Calculadora)