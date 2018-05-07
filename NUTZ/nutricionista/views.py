from django.shortcuts import render
from nutricionista.models import Nutricionista
from django.apps import apps
from .forms import (
    FormAddPaciente,

)
from django.shortcuts import get_object_or_404
# Create your views here.



def index(request):
    return render(request,template_name='nutricionista/index.html')

def dashboard(request):
    return render(request,template_name='nutricionista/dashboard.html')

def calculadora(request):
    return render(request,template_name='nutricionista/calculadora.html')

#La nutricionista en el inicio, va a poder ver un formulario para
#agregar paciente y listarlos.
#INGRESA PACIENTE FORMULARIO -> SE VALIDA EN LA F.B.V. -> SE DEVUELVE UNA LISTA ACTUALIZADA

def inicio_nutri(request):

    if request.method == "POST":
        form_add_paciente = FormAddPaciente(request.POST)
        if form_add_paciente.is_valid():
            #Quien es el nutricionista?
            #author = get_object_or_404(User, username=slug)
            #IF USER.is logged()
            # user = get_auth_user()
            # nutricionista = user.nutricionista 
            nutricionista = get_object_or_404(Nutricionista, pk=5)
            paciente = nutricionista.crear_paciente() #rut, email, law e
            print("Paciente creado desde el form")

    else:
        form_add_paciente = FormAddPaciente()

    context = dict()
    context['form'] = form_add_paciente

    return render(request,'nutricionista/index.html', context)