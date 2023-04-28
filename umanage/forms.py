from django import forms
from .models import login, user, credentials_user

class loginForm(forms.ModelForm):
    class Meta:
        model=login
        fields=['username','password',]

class userForm(forms.ModelForm):
    class Meta:
        model=user
        fields=['u_name','u_lastname','u_email','u_borndate','u_phone',]

class credentials_userForm(forms.ModelForm):
    class Meta:
        model=credentials_user
        exclude=('id',)