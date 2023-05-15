from django import forms
from .models import Ulogin#, user, credentials_user

class loginFormulario(forms.ModelForm):
    class Meta:
        model=Ulogin
        fields=['email','password']
        widgets={
            
            'password': forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'Contraseña'
            }),
            'email': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Correo Electronico'
            })
        }
        labels={
            'username': 'Usuario',
            'password': 'Contraseña',
            'email':'Email',
        }

class registerForm(forms.ModelForm):
    class Meta:
        model=Ulogin
        fields=[
            'first_name',
            'last_name',
            'username',
            'password',
            'email',
        ]

class recoverForm(forms.Form):
    email=forms.EmailField(label='Email', max_length=60)
    