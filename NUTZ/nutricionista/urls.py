
from django.conf.urls import url
from nutricionista import views


urlpatterns = [
    url(r'^$', views.inicio_nutri, name='nutricionista-index'),
    url(r'^dashboard/$', views.dashboard, name='nutricionista-dashboard'),
    url(r'^calculadora/$', views.calculadora, name='nutricionista-calculadora'),
]
