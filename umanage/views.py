from django.shortcuts import render
from django.http import HttpResponse
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
            lo=login.objects.get(username=usern)
            if lo.password==passw:
                return render(request, 'base.html', {'form':'esto esuna prueba'})
    return render(request, 'login.html',{'form':form, 'title':'Login Page'})

def profile_set(request):
    form=userForm()
    return render(request, 'base.html', {'form': form, 'title':'Profile Page'})

def register(request):
    form=userForm()
    form1=loginForm()
    if request.method=='POST':
        form=userForm(request.POST)
        form1=loginForm(request.POST)
        if form.is_valid() & form1.is_valid():

            usern=form1.cleaned_data['username']
            passw=form1.cleaned_data['password']
            uname=form.cleaned_data['u_name']
            ulast=form.cleaned_data['u_lastname']
            uemail=form.cleaned_data['u_email']
            uborn=form.cleaned_data['u_borndate']
            uphone=form.cleaned_data['u_phone']
            #ulogin=form.cleaned_data['u_lastlogin']
            
            if not login.objects.filter(username=usern):
                log=login.objects.create(id=uuid.uuid4(),username=usern,password=passw)
                userl=log.usuario.create(id=uuid.uuid4(),u_name=uname, u_lastname=ulast, u_email=uemail, u_borndate=uborn, u_phone=uphone, u_lastlogin=uborn)

            ##Alertar sobre que el usuario ya existe

    return render(request, 'base.html', {'form': form, 'form1':form1, 'title':'Register Page'})

def recovery(request):
    return HttpResponse('Recovery')