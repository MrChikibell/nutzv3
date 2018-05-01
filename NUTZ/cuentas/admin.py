from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminActualizarForm, UserAdminCrearForm
from .models import User

class UserAdmin(BaseUserAdmin):
    # Los forms para añadir y cambiar isntancias de usuarios
    form = UserAdminActualizarForm
    add_form = UserAdminCrearForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin','rut')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Información personal', {'fields': ('rut', 'nombres','apellidos', 'nacimiento', 'genero')}),
        #, 'ocupacion', 'nacionalidad',
        # ('Ficha Paciente', {'fields': ('observacion','ultima_atencion')}),
        # ('Información Nutricional', {'fields': ('peso',)}),
        # ('Información Bioquimica', {'fields': ('glicemia_mgdl',)}),
        ('Permisos', {'fields': ('admin','staff', 'nutri', 'active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('rut','email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', )
    ordering = ('email', )
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


