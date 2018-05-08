from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.contrib import messages

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