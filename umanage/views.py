from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist#, RelatedObjectDoesNotExist
#from .forms import  userForm, credentials_userForm
import uuid
from .import views
from login.models import Ulogin
from .models import credentials_user

# Create your views here.
#TODO --> @Ulogin_required
def credentials(request):
    log=Ulogin.objects.get(email='user@a.com')
    cre=credentials_user.objects.filter(user_master=log)
    return render(request, 'base.html',{'credenciales':cre})


