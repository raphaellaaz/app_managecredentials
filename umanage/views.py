from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist#, RelatedObjectDoesNotExist
from .models import login, user
from .forms import loginForm, userForm
import uuid

# Create your views here.
def login_web(request): #Registro de user y password
    form=loginForm()

    if request.method=='POST':
        form=loginForm(request.POST)
        if form.is_valid():
            usern=form.cleaned_data['username']
            passw=form.cleaned_data['password']
            try:
                lo=login.objects.get(username=usern)
                if lo.password==passw:
                    return render(request, 'login.html', {'form':'esto esuna prueba'})
                else:
                    return HttpResponse('Contraseña Incorrecta')
            except ObjectDoesNotExist:
                return HttpResponse('No existe Usuario')
    return render(request, 'login.html',{'form':form, 'title':'Login Page'})

def register(request):
    form1=userForm()
    form=loginForm()

    if request.method =='POST':
        form1=userForm(request.POST)
        form=loginForm(request.POST)
        if form.is_valid() & form1.is_valid():

            usern=form.cleaned_data['username']
            passw=form.cleaned_data['password']
            uname=form1.cleaned_data['u_name']
            ulast=form1.cleaned_data['u_lastname']
            uemail=form1.cleaned_data['u_email']
            uborn=form1.cleaned_data['u_borndate']
            uphone=form1.cleaned_data['u_phone']
            #ulogin=form.cleaned_data['u_lastlogin']

            
            if not login.objects.filter(username=usern):
                log=login.objects.create(id=uuid.uuid4(),username=usern,password=passw)
                log.save()
                user.objects.create(id=uuid.uuid4(),username=log,u_name=uname, u_lastname=ulast, u_email=uemail, u_borndate=uborn, u_phone=uphone, u_lastlogin=uborn)
            else:
                log=login.objects.get(username=usern)
    
                user.objects.create(
                    id=uuid.uuid4(),
                    username=log,
                    u_name=uname, 
                    u_lastname=ulast, 
                    u_email=uemail, 
                    u_borndate=uborn, 
                    u_phone=uphone, 
                    u_lastlogin=uborn
                    )

    return render(request, 'login.html', {'form': form, 'form1':form1, 'title':'Register Page'})

def recovery(request):
    return HttpResponse('Recovery: Se le envio un enlace de recuperacion a su correo registrado')