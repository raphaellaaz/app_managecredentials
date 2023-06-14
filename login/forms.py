from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
#from .models import Ulogin#, user, credentials_user

class loginFormulario(forms.Form): ##Formulario de Incio de Sesion

    username = forms.CharField(max_length=60, label='Username')
    password = forms.CharField(max_length=60, label='Password')
    
    class Meta:

        widgets={
            'username': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Username'
            }),
            'password': forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'Contraseña'
            }),
        }
        labels={
            'Username': 'Usuario',
            'Password': 'Contraseña',
        }

class registerForm(UserCreationForm): ##Formulario de Registro
    class Meta:
        model=User
        fields=('username','email','password1','password2')

class recoverForm(forms.Form): ##Formulario de Recuperación, solo se pide el correo
    email=forms.EmailField(label='Email', max_length=60)
    