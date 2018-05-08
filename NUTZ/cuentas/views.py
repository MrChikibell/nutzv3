from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.contrib import messages
from cuentas.models import UserManager
from .forms import (
    FormRegistar,
    FormRegNutri,
)

# Create your views here.

def login(request):
    
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email)
        print(password)
        user = authenticate(email=email, password=password)
        if user is None:
            messages.add_message(request, messages.INFO, 'Email o contraseña incorrectos')
        else:
            return HttpResponseRedirect("/nutricionista")
    return render(request,template_name='login.html')

def iniciar_registro(request):
    form_add_user = FormRegNutri()
    context = dict()
    context['form'] = form_add_user
    return render(request,template_name='registro_usuario.html', context=context)

######Revisar con HUGO MAÑANA#########

def registro(request):  
    if request.method == "POST":
            email = request.POST["email"]
            rut = request.POST["rut"]
            password = request.POST["password2"]
            es_nutri = True
            es_paciente = False
            usuario = UserManager.create_user(rut,email,es_paciente,es_nutri,password)
    else:
        messages.add_message(request, messages.INFO, 'Email o contraseña incorrectos')
    form_add_user = FormRegNutri()
    context = dict()
    context['form'] = form_add_user    
    return render(request,template_name='registro_usuario.html', context=context)
