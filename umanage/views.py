from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist#, RelatedObjectDoesNotExist
from .models import login, user, credentials_user
from .forms import loginForm, userForm, credentials_userForm
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
                    url=reverse('cred', args=[lo.pk])
                    return redirect(url)
                else:
                    return HttpResponse('Contraseña Incorrecta')
            except ObjectDoesNotExist:
                return HttpResponse('No existe User-Login')
    return render(request, 'login.html',{'form':form, 'title':'Login Page'})

def credentials(request):
    form=credentials_userForm()
    if request.method=='POST':
        form=credentials_userForm(request.POST)
        if form.is_valid():

            tipo=form.cleaned_data['tipo']
            name_cred=form.cleaned_data['name_credential']
            pass_cred=form.cleaned_data['pass_credential']
            usr=form.cleaned_data['user_master']
            credentials_user.objects.create(id=uuid.uuid4(), tipo=tipo,name_credential=name_cred, pass_credential=pass_cred, user_master=usr)
            
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
