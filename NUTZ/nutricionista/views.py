from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request,template_name='nutricionista/index.html')

def dashboard(request):
    return render(request,template_name='nutricionista/dashboard.html')

def calculadora(request):
    return render(request,template_name='nutricionista/calculadora.html')