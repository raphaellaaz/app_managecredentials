from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist#, RelatedObjectDoesNotExist
from .models import login, user, credentials_user
from .forms import loginForm, userForm, credentials_userForm
import uuid
from .import views
import json

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
                    request.session['usernow']=str(lo.id)
                    return redirect('credentials')
                else:
                    return HttpResponse('Contraseña Incorrecta')
            except ObjectDoesNotExist:
                return HttpResponse('No existe User-Login') 
    return render(request, 'login.html',{'log': 'Login', 'form':form, 'title':'Login Page'})

def credentials(request):##No deberia estar aqui, la movere despues a la app de loginuser
    form=credentials_userForm()
    if request.method=='POST':
        form=credentials_userForm(request.POST)
        if form.is_valid():
            lid=request.session.get('usernow', None)
            userm=user.objects.get(username=lid)
            tipo=form.cleaned_data['tipo']
            name_cred=form.cleaned_data['name_credential']
            pass_cred=form.cleaned_data['pass_credential']
            credentials_user.objects.create(id=uuid.uuid4(), tipo=tipo, name_credential=name_cred, pass_credential=pass_cred,user_master=userm)
            return HttpResponse(userm)
            
    return render(request, 'base.html', {'content': form})

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
