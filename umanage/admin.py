from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import login, user, credentials_user

admin.site.register(login)
admin.site.register(user)
admin.site.register(credentials_user)
