
from django.conf.urls import url
from nutricionista import views


urlpatterns = [
    url(r'^$', views.inicio_nutri, name='nutricionista-index'),
    url(r'^dashboard/$', views.PacienteListView.as_view(), name='nutricionista-dashboard'),
    url(r'^calculadora/$', views.calculadora, name='nutricionista-calculadora'),
    # url(r'^pacientes/$', views.paciente, name='nutricionista-calculadora'),
    url(r'^alimentos/$', views.AlimentoCreate, name='alimentos'),
    url(r'^tipo-alimentos/$', views.TipoAlimentoCreate, name='tipo-alimento'),
]
