from django.shortcuts import render, redirect
from .forms import loginFormulario, registerForm, recoverForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Ulogin



# Create your views here.
def login_web(request): #Registro de user y password
    form=loginFormulario()
    email=request.POST.get('email')
    password=request.POST.get('password')
    if request.method=='POST':
        lg=Ulogin.objects.get(email=email)
        if lg is not None:
            if Ulogin.objects.get(password=password):
                print(str(lg.is_superuser))
                return HttpResponse('hola matinero')
    return render(request, 'base_form.html',{'title_form': 'Login', 'form':form, 'title':'Login Page'})


def register(request):
    form=registerForm()
    
    return render(request, 'base_form.html', {'form': form, 'title_form':'Register', 'title':'Register Page'})

def recover(request):
    form=recoverForm()
    
    return render(request, 'base_form.html', {'form': form, 'title_form':'Recover', 'title':'Recover Page'})
