from django.shortcuts import render
from django.http import HttpResponse
from .models import login
import uuid

# Create your views here.
def login_web(request): #Registro de user y password
     if request.method == 'POST':
        usern=request.POST['username']
        passw=request.POST['password']

        try:
            search=login.objects.get(username=usern)
            if search.username==passw:
                return HttpResponse('Contraseña Correcta') ##Cambiamos despues por la pagina de inicio en vez del mesaje
        except login.DoesNotExist:
            return HttpResponse('Usuario No existe')##Falta estilizar, para despues preguntar si desea registrarse
        return HttpResponse('Contraseña Incorrecta') ##Redireccionar a recuperacion de cuenta
     return render(request, 'login.html', {})



def register(request):
    if request.method == 'POST':
        usern=request.POST['username']
        passw=request.POST['password']
        try:
            log=login(id=uuid.uuid4(), username=usern, password=passw)
            log.save()
        except Exception as e:
            return HttpResponse(e)
        return HttpResponse('Ingresado')
    else:
        return render(request, 'login.html', {})
    


def recovery(request):
    return HttpResponse('Recovery')