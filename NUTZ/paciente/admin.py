from django.contrib import admin
from .models import Paciente
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import PacienteAdminActualizarForm, PacienteAdminCrearForm
class PacienteAdmin(BaseUserAdmin):
    
    list_display = ('user', )
    list_filter = ('user',)
    form = PacienteAdminActualizarForm
    add_form = PacienteAdminCrearForm

    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Información personal', {'fields': ('rut', 'nombres','apellidos', 'nacimiento',  'ocupacion', 'nacionalidad','genero')}),
        ('Ficha Paciente', {'fields': ('observacion','ultima_atencion')}),
        ('Información Nutricional', {'fields': ('peso',)}),
        ('Información Bioquimica', {'fields': ('glicemia_mgdl',)}),
        ('Permisos', {'fields': ('admin','staff', 'nutri', 'active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('rut','email', 'password1', 'password2')}
        ),
    )
    search_fields = ('rut', )
    ordering = ('user', )
    filter_horizontal = ()
#     pass
admin.site.register(Paciente)