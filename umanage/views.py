from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist#, RelatedObjectDoesNotExist
#from .forms import  userForm, credentials_userForm
import uuid
from .import views
from django.contrib.auth.models import User
from .models import credentials_user
from django.contrib.auth.decorators import login_required

# Create your views here.
#Falta el control de acceso, he aqui hardcode con el motivo de testing
@login_required
def credentials(request):
    #log=User.objects.get(email=request.POST.get('email'))
    use=request.session['user']
    cre=credentials_user.objects.all()
    if cre.exists():
        return render(request, 'base.html',{'user_info':use,'credenciales':cre})
    else:
        return redirect('homelog')

    


