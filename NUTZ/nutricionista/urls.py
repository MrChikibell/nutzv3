
from django.conf.urls import url
from nutricionista import views


urlpatterns = [
    url(r'^$', views.index, name='index-nutricionista'),
    url(r'^dashboard/$', views.dashboard, name='nutricionista-dashboard'),
    url(r'^calculadora/$', views.calculadora, name='nutricionista-calculadora'),
]
