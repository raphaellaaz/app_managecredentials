from django.shortcuts import render, redirect
from .forms import loginFormulario, registerForm, recoverForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
#from .models import Ulogin



# Create your views here.
@never_cache
def login_web(request): #Registro de user y password
    form=loginFormulario()
    if request.method=='POST':
        usern=request.POST.get('username')
        request.session['user']=usern
        password=request.POST.get('password')

        user=authenticate(request, username=usern, password=password)

        if user is not None:
            login(request, user)
            return redirect('credentials')
        else: ##Añadir mensaje emergente de Error
            return HttpResponse('Credendiales Incorrectas')

    return render(request, 'base_form.html',{'title_form': 'Login', 'form':form, 'title':'Login Page'})


def register(request):
    form=registerForm()
    if request.method=='POST':
        usern=request.POST.get('username')
        if request.POST.get('password1') == request.POST.get('password2'):
            passw=request.POST.get('password1')
        else:
            return HttpResponse('Contraseñas no coinciden')

    
    return render(request, 'base_form.html', {'form': form, 'title_form':'Register', 'title':'Register Page'})

def recover(request):##Enviar Correo de Recuperacion, SOLO si se encuentra ya registrado.
    form=recoverForm()
    
    return render(request, 'base_form.html', {'form': form, 'title_form':'Recover', 'title':'Recover Page'})

def userlogout(request):
    logout(request)
    return login_web(request)

